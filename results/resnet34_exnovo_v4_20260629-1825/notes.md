# resnet34_exnovo_v4_20260629-1825

## Ipotesi
ResNet34 pretrained aumenta la capacita rispetto a ResNet18 mantenendo un costo computazionale ancora contenuto. Questa v4 prova a migliorare sia val_acc sia val_bal_acc partendo dai punti deboli della v2: Metal e Plastic. Usa transfer learning, learning rate differenziati, regolarizzazione L2, dropout, data augmentation moderata, learning rate decrescente ed early stopping.

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- Niente WeightedRandomSampler.
- Niente label smoothing.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi: scelta conservativa per non distorcere classi con poche immagini, in particolare Plastic.

## Differenze rispetto a v2
- Backbone ResNet34 invece di ResNet18, per aumentare capacita senza uscire da un profilo GPU leggero.
- Learning rate del backbone piu conservativo e head LR leggermente piu basso, per ridurre oscillazioni su validation.
- Dropout 0.30 e weight decay 8e-5 per regolarizzare il modello piu grande.
- Pesi di classe piu morbidi con esponente 0.45 e piccolo boost mirato per Metal e Plastic.
- Augmentation simile ma leggermente meno distruttiva su rotazione/ColorJitter/RandomErasing.
- Piu epoche e patience maggiore, mantenendo early stopping su balanced accuracy.

## Risultato
Best epoch: 20
Validation accuracy at best BA: 0.9752
Best validation balanced accuracy: 0.9626
Branch run: exp-resnet18-exnovo-v4-20260629-1825
Cartella risultati: /content/ProjectML/results/resnet34_exnovo_v4_20260629-1825
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet34_exnovo_v4_20260629-1825/resnet34_exnovo_v4_best.pth

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
