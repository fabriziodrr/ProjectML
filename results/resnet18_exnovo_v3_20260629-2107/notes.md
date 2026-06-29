# resnet18_exnovo_v3_20260629-2107

## Ipotesi
ResNet18 pretrained puo dare una baseline forte con costo computazionale contenuto. Questa variante prova a migliorare la generalizzazione usando argomenti del corso: transfer learning, learning rate differenziati, regolarizzazione L2, dropout, data augmentation moderata, learning rate decrescente ed early stopping.

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- WeightedRandomSampler per bilanciare le classi nel training.
- Label smoothing 0.1 per ridurre overconfidence.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi: scelta conservativa per non distorcere classi con poche immagini, in particolare Plastic.

## Miglioramenti v3 rispetto a v2
- Introdotti WeightedRandomSampler e label smoothing 0.1 per affrontare le classi deboli (Metal 91.6%, Plastic 91.9% in v2).
- Sostituito CosineAnnealingLR con ReduceLROnPlateau per un decadimento del LR piu adattivo.
- Logging corretto del learning rate: ora registra il LR effettivamente usato dall'epoca, non quello futuro.
- Il scheduler non viene piu avanzato quando scatta early stopping.
- CSV history scritto solo alla fine del training (non piu ad ogni epoca).
- os.walk con followlinks=False per evitare loop su symlink di Drive.
- Warning esplicito sulle cartelle dataset ignorate durante lo scan.
- torch.load con weights_only=False esplicito (compatibilita PyTorch 2.6+).
- Matplotlib backend Agg configurato per ambienti non interattivi.
- Matrice di confusione aggiuntiva normalizzata per riga.

## Differenze rispetto al baseline ResNet18 exnovo
- Learning rate differenziati: backbone pre-addestrato piu conservativo, classificatore nuovo piu rapido.
- Dropout prima del layer finale per ridurre overfitting.
- Augmentation leggermente piu robusta: crop moderato, piccola rotazione, ColorJitter leggero e RandomErasing.
- Piu epoche e patience maggiore, con ReduceLROnPlateau su balanced accuracy al posto del CosineAnnealing.

## Risultato
Best epoch: 19
Best validation balanced accuracy: 0.9725
Branch run: exp-resnet18-exnovo-v3-20260629-2107
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v3_20260629-2107
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v3_20260629-2107/resnet18_exnovo_v3_best.pth

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
