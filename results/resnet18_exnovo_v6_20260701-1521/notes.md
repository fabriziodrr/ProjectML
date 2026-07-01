# resnet18_exnovo_v6_20260701-1521

## Ipotesi
La v6 corregge i problemi della v5 (0.9684 BA) analizzando le cause del degrado rispetto a v3 (0.9725 BA):
- Il warmup LR consumava 3 epoche a LR ridotto senza beneficio
- La patience 10 prolungava inutilmente il training oltre il best epoch
- La TTA con flip/rotate era ridondante rispetto alle training augmentations
- L'overfitting (gap train/val ~3%) richiedeva regolarizzazione piu forte

## Modifiche v6 vs v5
1. **Rimosso warmup LR**: v3 senza warmup ha performato meglio; con 3 epoche a LR ridotto il modello converge piu lentamente al picco.
2. **Patience 8** (tornata al valore v3): 10 era inutile, dopo epoch 14 il modello overfittava senza recuperare.
3. **ReduceLROnPlateau patience 3** (anziche 5): trigger LR decay piu aggressivo per uscire da plateau di overfitting.
4. **Regolarizzazione rafforzata**:
   - Dropout 0.25 -> 0.30 (S:13, L:07A): piu neuroni disattivati, meno co-adattamento.
   - Label smoothing 0.1 -> 0.15 (S:09): soft target piu forti contro overconfidence.
   - Weight decay 1e-4 -> 2e-4 (S:09): penalizzazione L2 piu forte.
5. **Augmentation rafforzata**:
   - RandomResizedCrop scale (0.70-1.0) anziche (0.80-1.0): piu zoom diversity
   - RandomRotation 15deg anziche 10deg
   - RandomAffine con translate=0.05 e shear=5: traslazioni e distorsioni geometriche
   - ColorJitter: brightness 0.30, contrast 0.25, saturation 0.20, hue 0.05
   - RandomErasing p=0.25 (anziche 0.15) con scale (0.02-0.10)
6. **TTA 10-crop**: FiveCrop (4 angoli + centro) x HorizontalFlip = 10 viste. Viste piu diverse e non sovrapposte alle training augmentations (flip/rotate).

## Cosa ha funzionato (da analisi v2, v3, v3.2, v4)
- **WeightedRandomSampler**: +1.34% BA rispetto a v2
- **Label smoothing 0.1**: calibrazione migliorata
- **ReduceLROnPlateau**: decadimento adattivo superiore a CosineAnnealingLR
- **AdamW con LR differenziati**: convergenza rapida e stabile
- **ResNet18**: bilanciamento ottimale capacita/overfitting

## Tecniche del corso usate
- Transfer learning (S:12): ResNet18 pretrained ImageNet
- Discriminative LRs (S:12): backbone piu conservativo
- WeightedRandomSampler (S:05): class balancing
- Label smoothing (S:09): calibrazione
- ReduceLROnPlateau (S:09): adaptive LR decay
- Dropout 0.30 (S:13, L:07A): regolarizzazione
- L2/weight_decay 2e-4 (S:09): regolarizzazione
- Data augmentation (S:05, L:04): flip, rotazione, Affine, ColorJitter, RandomErasing
- TTA 10-crop (S:05): 10 viste in inference
- Early stopping (S:09, L:04): patience=8
- CrossEntropyLoss con class weights (S:09, L:04)
- Balanced accuracy (S:05): metrica primaria
- StratifiedShuffleSplit (L:01): split 80/20

## Target
- Standard BA >= 0.975 (superare v3 0.9725)
- TTA 10-crop: ulteriore +0.2-0.5% atteso

## Risultato
Best epoch: 17
Best validation balanced accuracy: 0.9701
TTA validation accuracy: 0.9794
TTA validation balanced accuracy: 0.9739
Branch run: exp-resnet18-exnovo-v6-20260701-1521
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v6_20260701-1521
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v6_20260701-1521/resnet18_exnovo_v6_best.pth

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
