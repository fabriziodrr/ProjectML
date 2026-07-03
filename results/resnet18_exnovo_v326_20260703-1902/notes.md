# resnet18_exnovo_v326_20260703-1902

## Ipotesi
La two-phase training (S:12) protegge il backbone pre-addestrato durante le prime epoche, permettendo al classificatore di convergere senza degradare i pesi ImageNet. Poi l'unfreeze completa il fine-tuning con learning rate differenziati. La Reject Option corregge gli errori residui.

## Modifiche v3.2.4 rispetto a v3.1
- AGGIUNTA Two-Phase Training (S:12): freeze backbone 5 epoche, poi unfreeze e fine-tuning completo
- AGGIUNTA Reject Option (Vento et al., S:11, L:reject_option)
- AGGIUNTO split val in val_cal (50% calibrazione) e val_eval (50% valutazione)
- AUMENTATE epoche da 35 a 40 per compensare le 5 epoche di sola testa

## Tecniche del corso
- Transfer learning / Two-Phase Training: S:12 (teoria) + L:08 (AlexNet fine-tuning)
- ResNet18 / Skip connections: S:14 (Residual Learning)
- StratifiedShuffleSplit: L:01 (KNN validation)
- Data augmentation (flip, rotazione, ColorJitter, RandomErasing): S:05 + L:04
- AdamW optimizer: S:09 (Adam) + L:04
- CrossEntropyLoss con class weights: S:09 + L:04
- Label smoothing: S:09 (regolarizzazione loss)
- WeightedRandomSampler: S:04-05 (class imbalance)
- ReduceLROnPlateau: S:09 (learning rate decay)
- Early stopping: S:09 + L:04
- Dropout: S:13 + L:07A
- L2 regularization (weight_decay): S:09
- Balanced accuracy: S:05
- Discriminative learning rates: S:12
- ImageNet normalization: L:07A
- Reject Option (Vento et al.): S:11 + L:reject_option

## Cosa NON c'e in v3.2.4
- Niente Focal Loss (non nel corso)
- Niente AMP (FP32 puro)
- Niente TTA (non richiesto per reject option)
- Niente torch.backends.cudnn.benchmark
- Niente non_blocking=True

## Risultato
Best epoch: 16
Best validation BA (val_cal): 0.9625
Val_eval BA (no reject): 0.9651
Branch run: exp-resnet18-exnovo-v326-20260703-1902
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v326_20260703-1902
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v326_20260703-1902/resnet18_exnovo_v324_best.pth

## File prodotti in repo
- `split.csv`
- `config.json`
- `class_weights.csv`
- `history.csv`
- `summary.json`
- `classification_report.txt`
- `confusion_matrix.csv`
- `confusion_matrix.png`
- `confusion_matrix_norm.png`
- `training_curves.png`
- `reject_standard.json`
