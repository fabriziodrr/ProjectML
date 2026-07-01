# resnet18_exnovo_v61_20260701-1713

## Ipotesi
La v6.1 parte dalla v6 e aggiunge two-phase training + Focal Loss per attaccare i punti deboli residui: overfitting e confusioni Plastic-Glass / Metal-Clothing.

## Novita v6.1 rispetto a v6
1. **Two-phase training (S:12)**:
   - Fase 1 (5 epoche): backbone congelato, allena solo il classifier head su feature ImageNet stabili.
   - Fase 2: sblocca backbone, full finetuning con LR differenziati + ReduceLROnPlateau.
   - Vantaggio: la head impara a discriminare senza che il backbone si adatti precocemente, riducendo overfitting.
2. **Focal Loss (gamma=2.0, S:09)**:
   - Sostituisce CrossEntropyLoss. FL(p_t) = -(1-p_t)^gamma * log(p_t)
   - Down-pesa esempi facili, up-pesa automaticamente quelli incerti (Plastic-Glass, Metal-Clothing).

## Ereditato da v6
- Rimosso warmup LR, patience 8, RLRP patience 3
- Dropout 0.30, label smoothing 0.15, weight decay 2e-4
- Augmentation forte: crop 0.70-1.0, rotation 15deg, RandomAffine, ColorJitter 0.30/0.25/0.20, RandomErasing p=0.25
- TTA 10-crop (FiveCrop x HorizontalFlip)

## Cosa ha funzionato (da analisi v2, v3, v3.2, v4, v5, v6)
- **WeightedRandomSampler**: +1.34% BA rispetto a v2
- **Label smoothing 0.1**: calibrazione migliorata
- **ReduceLROnPlateau**: decadimento adattivo superiore a CosineAnnealingLR
- **AdamW con LR differenziati**: convergenza rapida e stabile
- **ResNet18**: bilanciamento ottimale capacita/overfitting

## Tecniche del corso usate
- Transfer learning (S:12): ResNet18 pretrained ImageNet
- Two-phase training / freeze (S:12): backbone congelato poi sbloccato
- Discriminative LRs (S:12): backbone piu conservativo
- WeightedRandomSampler (S:05): class balancing
- Label smoothing (S:09): calibrazione
- Focal Loss (S:09): loss adattiva per esempi difficili
- ReduceLROnPlateau (S:09): adaptive LR decay
- Dropout 0.30 (S:13, L:07A): regolarizzazione
- L2/weight_decay 2e-4 (S:09): regolarizzazione
- Data augmentation (S:05, L:04): flip, rotazione, Affine, ColorJitter, RandomErasing
- TTA 10-crop (S:05): 10 viste in inference
- Early stopping (S:09, L:04): patience=8
- Balanced accuracy (S:05): metrica primaria
- StratifiedShuffleSplit (L:01): split 80/20

## Target
- Standard BA >= 0.975 (superare v3 0.9725 e v6 0.9701)
- TTA 10-crop: ulteriore +0.2-0.5% atteso
- Ridurre confusioni Plastic-Glass e Metal-Clothing

## Risultato
Best epoch: 34
Best validation balanced accuracy: 0.9757
TTA validation accuracy: 0.9807
TTA validation balanced accuracy: 0.9784
Branch run: exp-resnet18-exnovo-v61-20260701-1713
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v61_20260701-1713
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v61_20260701-1713/resnet18_exnovo_v61_best.pth

## File prodotti in repo
- `split.csv`
- `config.json`
- `class_weights.csv`
- `history.csv`
- `summary.json`
- `classification_report.txt`
- `classification_report_tta.txt`
- `confusion_matrix.csv`
- `confusion_matrix.png`
- `confusion_matrix_norm.png`
- `confusion_matrix_tta.csv`
- `confusion_matrix_tta.png`
- `confusion_matrix_tta_norm.png`
- `training_curves.png`
