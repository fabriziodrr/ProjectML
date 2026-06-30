import argparse
import datetime
import json
import os
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from PIL import Image
from sklearn.metrics import balanced_accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import StratifiedShuffleSplit
from torch.utils.data import DataLoader, Dataset, WeightedRandomSampler
from torchvision import models, transforms


CLASS_NAMES = [
    "Battery",
    "Clothing",
    "Glass",
    "Metal",
    "Organic",
    "Papery",
    "Plastic",
    "Undifferentiated",
]

LABEL_MAP = {
    "battery": 0,
    "clothes": 1,
    "clothing": 1,
    "shoes": 1,
    "brown": 2,
    "green": 2,
    "transparent": 2,
    "glass": 2,
    "metal": 3,
    "organic": 4,
    "cardboard": 5,
    "paper": 5,
    "papery": 5,
    "plastic": 6,
    "undifferentiated": 7,
}

IMG_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")

VARIANTS = {
    "v31": {
        "exp_name": "resnet18_exnovo_v31_local_rtx2060",
        "epochs": 35,
        "patience": 8,
        "batch_size": 16,
        "backbone_lr": 1e-4,
        "head_lr": 5e-4,
        "dropout_p": 0.25,
        "weight_decay": 1e-4,
        "label_smoothing": 0.1,
        "optimizer": "adamw",
        "checkpoint_name": "resnet18_exnovo_v31_best.pth",
    },
    "v32": {
        "exp_name": "resnet18_exnovo_v32_local_rtx2060",
        "epochs": 50,
        "patience": 8,
        "batch_size": 16,
        "backbone_lr": 1e-4,
        "head_lr": 1e-3,
        "dropout_p": 0.40,
        "weight_decay": 5e-4,
        "label_smoothing": 0.1,
        "optimizer": "sgd",
        "sgd_momentum": 0.9,
        "checkpoint_name": "resnet18_exnovo_v32_best.pth",
    },
}


class WasteDataset(Dataset):
    def __init__(self, frame, transform=None):
        self.frame = frame.reset_index(drop=True)
        self.transform = transform

    def __len__(self):
        return len(self.frame)

    def __getitem__(self, idx):
        row = self.frame.iloc[idx]
        image = Image.open(row["path"]).convert("RGB")
        if self.transform is not None:
            image = self.transform(image)
        return image, int(row["label"])


def find_repo_root():
    current = Path.cwd().resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "local_rtx2060").exists():
            return candidate
    return current


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def scan_dataset(dataset_dir):
    samples = []
    skipped_folders = set()
    for dirpath, _, filenames in os.walk(dataset_dir, followlinks=False):
        if not filenames:
            continue
        folder = Path(dirpath).name.lower()
        if folder not in LABEL_MAP:
            skipped_folders.add(folder)
            continue
        label = LABEL_MAP[folder]
        for fname in filenames:
            if fname.lower().endswith(IMG_EXTENSIONS):
                path = Path(dirpath) / fname
                samples.append(
                    {
                        "path": str(path),
                        "relative_path": str(path.relative_to(dataset_dir)),
                        "folder": folder,
                        "label": label,
                        "class_name": CLASS_NAMES[label],
                    }
                )

    if skipped_folders:
        print(f"WARNING: cartelle ignorate perche non in LABEL_MAP: {sorted(skipped_folders)}")

    frame = pd.DataFrame(samples).sort_values("relative_path").reset_index(drop=True)
    if frame.empty:
        raise RuntimeError(f"Nessuna immagine trovata in {dataset_dir}")
    return frame


def build_loaders(df, cfg, results_dir):
    splitter = StratifiedShuffleSplit(n_splits=1, test_size=0.20, random_state=42)
    train_idx, val_idx = next(splitter.split(df["relative_path"], df["label"]))
    df = df.copy()
    df["split"] = "train"
    df.loc[val_idx, "split"] = "val"
    df[["relative_path", "folder", "label", "class_name", "split"]].to_csv(results_dir / "split.csv", index=False)

    train_df = df[df["split"] == "train"].reset_index(drop=True)
    val_df = df[df["split"] == "val"].reset_index(drop=True)

    train_transform = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.RandomResizedCrop(224, scale=(0.80, 1.0), ratio=(0.9, 1.1)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomRotation(degrees=10),
            transforms.ColorJitter(brightness=0.20, contrast=0.20, saturation=0.15, hue=0.03),
            transforms.ToTensor(),
            transforms.RandomErasing(p=0.15, scale=(0.02, 0.08), ratio=(0.3, 3.3)),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    val_transform = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    sample_counts = train_df["label"].value_counts().sort_index().to_numpy()
    sample_inv_weights = 1.0 / np.maximum(sample_counts, 1.0)
    train_sample_weights = sample_inv_weights[train_df["label"].values]
    train_sampler = WeightedRandomSampler(train_sample_weights, num_samples=len(train_sample_weights), replacement=True)

    train_loader = DataLoader(
        WasteDataset(train_df, train_transform),
        batch_size=cfg["batch_size"],
        sampler=train_sampler,
        num_workers=0,
        pin_memory=torch.cuda.is_available(),
    )
    val_loader = DataLoader(
        WasteDataset(val_df, val_transform),
        batch_size=cfg["batch_size"],
        shuffle=False,
        num_workers=0,
        pin_memory=torch.cuda.is_available(),
    )

    train_counts = train_df["label"].value_counts().reindex(range(len(CLASS_NAMES)), fill_value=0).sort_index().to_numpy(dtype=np.float32)
    class_weights = np.sqrt(train_counts.max() / np.maximum(train_counts, 1.0))
    class_weights = class_weights / class_weights.mean()
    weights_df = pd.DataFrame(
        {"label": range(len(CLASS_NAMES)), "class_name": CLASS_NAMES, "train_count": train_counts.astype(int), "loss_weight": class_weights}
    )
    weights_df.to_csv(results_dir / "class_weights.csv", index=False)
    return train_loader, val_loader, class_weights


def build_model(cfg, device, class_weights):
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    num_features = model.fc.in_features
    model.fc = nn.Sequential(nn.Dropout(p=cfg["dropout_p"]), nn.Linear(num_features, len(CLASS_NAMES)))
    model = model.to(device)

    criterion = nn.CrossEntropyLoss(
        weight=torch.tensor(class_weights, dtype=torch.float32, device=device),
        label_smoothing=cfg["label_smoothing"],
    )
    backbone_params = [p for name, p in model.named_parameters() if not name.startswith("fc.")]
    head_params = list(model.fc.parameters())
    param_groups = [
        {"params": backbone_params, "lr": cfg["backbone_lr"]},
        {"params": head_params, "lr": cfg["head_lr"]},
    ]

    if cfg["optimizer"] == "sgd":
        optimizer = torch.optim.SGD(param_groups, momentum=cfg["sgd_momentum"], weight_decay=cfg["weight_decay"])
    else:
        optimizer = torch.optim.AdamW(param_groups, weight_decay=cfg["weight_decay"])
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode="max", factor=0.5, patience=5, min_lr=1e-6)
    return model, criterion, optimizer, scheduler


def run_epoch(model, loader, criterion, optimizer, device, train):
    model.train(train)
    total_loss = 0.0
    all_preds = []
    all_targets = []
    context = torch.enable_grad() if train else torch.no_grad()
    with context:
        for images, targets in loader:
            images = images.to(device)
            targets = targets.to(device)
            if train:
                optimizer.zero_grad()
            logits = model(images)
            loss = criterion(logits, targets)
            if train:
                loss.backward()
                optimizer.step()
            total_loss += loss.item() * images.size(0)
            all_preds.append(logits.argmax(dim=1).detach().cpu())
            all_targets.append(targets.detach().cpu())

    y_pred = torch.cat(all_preds).numpy()
    y_true = torch.cat(all_targets).numpy()
    loss = total_loss / len(loader.dataset)
    acc = float((y_pred == y_true).mean())
    bal_acc = float(balanced_accuracy_score(y_true, y_pred))
    return loss, acc, bal_acc, y_true, y_pred


def save_plots(history_df, cm, results_dir):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history_df["epoch"], history_df["train_loss"], label="train")
    plt.plot(history_df["epoch"], history_df["val_loss"], label="val")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid(alpha=0.3)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history_df["epoch"], history_df["train_bal_acc"], label="train BA")
    plt.plot(history_df["epoch"], history_df["val_bal_acc"], label="val BA")
    plt.xlabel("Epoch")
    plt.ylabel("Balanced accuracy")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(results_dir / "training_curves.png", dpi=160)
    plt.show()

    plt.figure(figsize=(8, 7))
    plt.imshow(cm, interpolation="nearest", cmap="Blues")
    plt.title("Confusion matrix")
    plt.colorbar()
    ticks = np.arange(len(CLASS_NAMES))
    plt.xticks(ticks, CLASS_NAMES, rotation=45, ha="right")
    plt.yticks(ticks, CLASS_NAMES)
    for i in range(len(CLASS_NAMES)):
        for j in range(len(CLASS_NAMES)):
            plt.text(j, i, cm[i, j], ha="center", va="center", color="white" if cm[i, j] > cm.max() / 2 else "black")
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.tight_layout()
    plt.savefig(results_dir / "confusion_matrix.png", dpi=160)
    plt.show()

    cm_norm = cm.astype("float64") / cm.sum(axis=1, keepdims=True)
    cm_norm = np.nan_to_num(cm_norm)
    plt.figure(figsize=(8, 7))
    plt.imshow(cm_norm, interpolation="nearest", cmap="Greens", vmin=0, vmax=1)
    plt.title("Confusion matrix normalized by row")
    plt.colorbar()
    plt.xticks(ticks, CLASS_NAMES, rotation=45, ha="right")
    plt.yticks(ticks, CLASS_NAMES)
    for i in range(len(CLASS_NAMES)):
        for j in range(len(CLASS_NAMES)):
            plt.text(j, i, f"{cm_norm[i, j]:.2f}", ha="center", va="center", fontsize=8, color="white" if cm_norm[i, j] > 0.5 else "black")
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.tight_layout()
    plt.savefig(results_dir / "confusion_matrix_norm.png", dpi=160)
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=sorted(VARIANTS), required=True)
    args = parser.parse_args()
    cfg = VARIANTS[args.variant].copy()

    repo_root = find_repo_root()
    os.chdir(repo_root)
    dataset_dir = repo_root / "data" / "waste_type_identification"
    if not dataset_dir.exists():
        raise FileNotFoundError(f"Dataset non trovato. Mettilo in: {dataset_dir}")

    run_id = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    run_name = f"{cfg['exp_name']}_{run_id}"
    results_dir = repo_root / "results" / run_name
    checkpoint_dir = repo_root / "checkpoints" / run_name
    results_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    set_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Repo root:", repo_root)
    print("Dataset:", dataset_dir)
    print("Device:", device)
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
    print("Run name:", run_name)

    df = scan_dataset(dataset_dir)
    print("Totale immagini:", len(df))
    print(df["class_name"].value_counts().reindex(CLASS_NAMES, fill_value=0))
    train_loader, val_loader, class_weights = build_loaders(df, cfg, results_dir)
    model, criterion, optimizer, scheduler = build_model(cfg, device, class_weights)

    config = {
        **cfg,
        "variant": args.variant,
        "run_id": run_id,
        "run_name": run_name,
        "dataset_dir": str(dataset_dir),
        "results_dir": str(results_dir),
        "checkpoint_dir": str(checkpoint_dir),
        "device": str(device),
        "class_names": CLASS_NAMES,
    }
    with open(results_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)

    best_bal_acc = -1.0
    best_epoch = -1
    epochs_without_improvement = 0
    history = []
    best_checkpoint_path = checkpoint_dir / cfg["checkpoint_name"]

    for epoch in range(1, cfg["epochs"] + 1):
        train_loss, train_acc, train_bal_acc, _, _ = run_epoch(model, train_loader, criterion, optimizer, device, train=True)
        val_loss, val_acc, val_bal_acc, y_true, y_pred = run_epoch(model, val_loader, criterion, optimizer, device, train=False)
        row = {
            "epoch": epoch,
            "backbone_lr": optimizer.param_groups[0]["lr"],
            "head_lr": optimizer.param_groups[1]["lr"],
            "train_loss": train_loss,
            "train_acc": train_acc,
            "train_bal_acc": train_bal_acc,
            "val_loss": val_loss,
            "val_acc": val_acc,
            "val_bal_acc": val_bal_acc,
        }
        history.append(row)
        print(
            f"Epoch {epoch:02d}: lr=[{row['backbone_lr']:.2e},{row['head_lr']:.2e}] "
            f"train_loss={train_loss:.4f} train_ba={train_bal_acc:.4f} "
            f"val_loss={val_loss:.4f} val_acc={val_acc:.4f} val_ba={val_bal_acc:.4f}",
            flush=True,
        )

        if val_bal_acc > best_bal_acc:
            best_bal_acc = val_bal_acc
            best_epoch = epoch
            epochs_without_improvement = 0
            torch.save(
                {
                    "model_state_dict": model.state_dict(),
                    "class_names": CLASS_NAMES,
                    "config": config,
                    "best_epoch": best_epoch,
                    "best_val_bal_acc": best_bal_acc,
                },
                best_checkpoint_path,
            )
            print("  Saved best checkpoint:", best_checkpoint_path)
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= cfg["patience"]:
                print("Early stopping: balanced accuracy non migliora da", cfg["patience"], "epoche.")
                break
        scheduler.step(val_bal_acc)

    history_df = pd.DataFrame(history)
    history_df.to_csv(results_dir / "history.csv", index=False)
    checkpoint = torch.load(best_checkpoint_path, map_location=device, weights_only=False)
    model.load_state_dict(checkpoint["model_state_dict"])
    val_loss, val_acc, val_bal_acc, y_true, y_pred = run_epoch(model, val_loader, criterion, optimizer, device, train=False)
    report = classification_report(y_true, y_pred, target_names=CLASS_NAMES, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=list(range(len(CLASS_NAMES))))
    with open(results_dir / "classification_report.txt", "w") as f:
        f.write(report)
    pd.DataFrame(cm, index=CLASS_NAMES, columns=CLASS_NAMES).to_csv(results_dir / "confusion_matrix.csv")
    save_plots(history_df, cm, results_dir)

    summary = {
        "run_name": run_name,
        "variant": args.variant,
        "best_epoch": best_epoch,
        "best_val_bal_acc": best_bal_acc,
        "final_val_acc_at_best_checkpoint": val_acc,
        "final_val_bal_acc_at_best_checkpoint": val_bal_acc,
        "checkpoint_path": str(best_checkpoint_path),
        "results_dir": str(results_dir),
    }
    with open(results_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(report)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
