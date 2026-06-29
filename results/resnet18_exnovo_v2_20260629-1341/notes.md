# resnet18_exnovo_v2_20260629-1341

## Ipotesi
ResNet18 pretrained puo dare una baseline forte con costo computazionale contenuto. Questa variante prova a migliorare la generalizzazione usando argomenti del corso: transfer learning, learning rate differenziati, regolarizzazione L2, dropout, data augmentation moderata, learning rate decrescente ed early stopping.

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- Niente WeightedRandomSampler.
- Niente label smoothing.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi: scelta conservativa per non distorcere classi con poche immagini, in particolare Plastic.

## Differenze rispetto al baseline ResNet18 exnovo
- Learning rate differenziati: backbone pre-addestrato piu conservativo, classificatore nuovo piu rapido.
- Dropout prima del layer finale per ridurre overfitting.
- Augmentation leggermente piu robusta: crop moderato, piccola rotazione, ColorJitter leggero e RandomErasing.
- Piu epoche e patience maggiore, mantenendo early stopping su balanced accuracy.

## Risultato
Best epoch: 14
Best validation balanced accuracy: 0.9591
Branch run: exp-resnet18-exnovo-v2-20260629-1341
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v2_20260629-1341
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v2_20260629-1341/resnet18_exnovo_v2_best.pth

## File prodotti in repo
- `split.csv`
- `config.json`
- `class_weights.csv`
- `history.csv`
- `summary.json`
- `classification_report.txt`
- `confusion_matrix.csv`
- `confusion_matrix.png`
- `training_curves.png`
