# resnet18_exnovo_v32_20260630-1525

## Ipotesi
La v3 ha mostrato overfitting (train BA 99.9% vs val BA 97.3%) e Plastic resta la classe piu debole (recall 91%), confusa principalmente con Glass. La v3.2 applica quattro modifiche mirate, tutte riconducibili al corso:

## Modifiche v3.2 rispetto a v3.1
1. **Dropout 0.25 -> 0.40**: valore intermedio tra v3 e AlexNet (0.5, S:13). Maggiore regolarizzazione per ridurre overfitting.
2. **Weight decay 1e-4 -> 5e-4**: L2 regularization piu forte (S:09) per penalizzare pesi grandi e migliorare generalizzazione.
3. **AdamW -> SGD con momentum=0.9**: SGD e l'ottimizzatore usato nel corso (L:04). Su task di classificazione immagini con transfer learning, SGD spesso generalizza meglio di Adam.
4. **Augmentation ridotta per Plastic/Glass**: rotazione 10deg -> 5deg, RandomErasing p 0.15 -> 0.10. L'analisi della confusion matrix v3 mostra che Plastic viene confusa con Glass (8 errori). Rotazioni ampie eRandomErasing aggressivo potrebbero danneggiare features discriminative per oggetti trasparenti/riflettenti.
5. **HEAD_LR 5e-4 -> 1e-3**: con SGD serve LR piu alto per il classificatore (non c'e scaling adattivo come in Adam).
6. **EPOCHS 35 -> 50**: SGD converge piu lentamente, serve piu tempo.

## Tecniche del corso usate
- SGD con momentum: L:04 (MNIST training)
- Dropout: S:13 + L:07A (AlexNet)
- L2 regularization (weight_decay): S:09
- Transfer learning + discriminative LR: S:12 + L:08
- Data augmentation (flip, rotazione, ColorJitter, RandomErasing): S:05 + L:04
- CrossEntropyLoss + class weights + label smoothing: S:09 + L:04
- WeightedRandomSampler: S:05 (cost-based, class imbalance)
- ReduceLROnPlateau: S:09 (learning rate decay)
- Early stopping: S:09 + L:04
- StratifiedShuffleSplit: L:01
- Balanced accuracy: S:05 (recall per classe)

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- WeightedRandomSampler per bilanciare le classi nel training.
- Label smoothing 0.1 per ridurre overconfidence.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi.
- Training in FP32 puro (no AMP).
- SGD con momentum al posto di Adam/AdamW.

## Risultato
Best epoch: 29
Best validation balanced accuracy: 0.9576
Branch run: exp-resnet18-exnovo-v32-20260630-1525
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v32_20260630-1525
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v32_20260630-1525/resnet18_exnovo_v32_best.pth

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
