# resnet18_exnovo

## Ipotesi
ResNet18 pretrained puo dare una baseline forte con costo computazionale contenuto. Si usa fine-tuning singola fase di tutti i layer per adattare le feature al dominio dei rifiuti senza pipeline troppo complessa.

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- Niente WeightedRandomSampler.
- Niente label smoothing.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi: scelta conservativa per non distorcere classi con poche immagini, in particolare Plastic.

## Risultato
Best epoch: 24
Best validation balanced accuracy: 0.9487
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo/resnet18_exnovo_best.pth

## File prodotti in repo
- `config.json`
- `class_weights.csv`
- `history.csv`
- `summary.json`
- `classification_report.txt`
- `confusion_matrix.csv`
- `confusion_matrix.png`
- `training_curves.png`
