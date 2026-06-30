# resnet18_exnovo_v3_20260630-1907

## Ipotesi
La v3.3 mantiene la configurazione vincente di v3 (AdamW 0.9725 val BA) e aggiunge Test-Time Augmentation (TTA) per migliorare la robustezza senza costi di training aggiuntivi. L'idea e' che mediare le predizioni su piu' viste della stessa immagine riduce la varianza e corregge predizioni borderline, specialmente su classi difficili come Plastic e Glass.

## Modifiche v3.3 rispetto a v3
- **TTA**: 5 trasformazioni applicate in inference (originale, flip orizzontale, rotazione +5deg, rotazione -5deg, crop shift 10px). Le softmax vengono mediate prima dell'argmax.
- Rinominato checkpoint in `resnet18_exnovo_v33_best.pth`.
- Nuovi file di output: `classification_report_tta.txt`, `confusion_matrix_tta.csv`, `confusion_matrix_tta.png`, `confusion_matrix_tta_norm.png`.

## Tecniche del corso usate
- Transfer learning + discriminative LR: S:12 + L:08
- Data augmentation (flip, rotazione, ColorJitter, RandomErasing): S:05 + L:04
- TTA come estensione naturale della data augmentation in fase di test (S:05)
- Dropout: S:13 + L:07A (AlexNet)
- L2 regularization (weight_decay): S:09
- CosineAnnealingLR: S:09 (learning rate decay)
- CrossEntropyLoss + class weights: S:09 + L:04
- Early stopping: S:09 + L:04
- StratifiedShuffleSplit: L:01
- Balanced accuracy: S:05 (recall per classe)

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- Niente WeightedRandomSampler.
- Niente label smoothing.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi.

## Risultato
Best epoch: 13
Best validation balanced accuracy: 0.9543
TTA validation accuracy: 0.9794
TTA validation balanced accuracy: 0.9718
Branch run: exp-resnet18-exnovo-v3-20260630-1907
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v3_20260630-1907
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v3_20260630-1907/resnet18_exnovo_v3_best.pth

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
