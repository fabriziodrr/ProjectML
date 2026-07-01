# resnet18_exnovo_v5_20260701-1033

## Ipotesi
La v5 riprende la configurazione vincente di v3 (0.9725 BA con WeightedRandomSampler + label smoothing + ReduceLROnPlateau) e la potenzia con warmup LR per maggiore stabilita in fase iniziale e TTA per migliorare le predizioni in inference. Tutte le tecniche sono riconducibili al corso.

## Cosa ha funzionato (da analisi v2, v3, v3.2, v4)
- **WeightedRandomSampler**: +1.34% BA rispetto a v2. Bilanciamento classi nei batch.
- **Label smoothing 0.1**: calibrazione migliorata, meno overconfidence.
- **ReduceLROnPlateau**: decadimento adattivo superiore a CosineAnnealingLR.
- **AdamW con LR differenziati**: backbone=1e-4, head=5e-4. Convergenza rapida e stabile.
- **ResNet18**: 11M parametri, bilanciamento ottimale capacita/overfitting per ~12K immagini.

## Cosa NON ha funzionato
- **ResNet34** (v4): 21M parametri, overfitting su dataset piccolo (0.9626 BA).
- **SGD+momentum** (v3.2): convergenza troppo lenta, 0.9576 BA nonostante piu epoche.
- **Dropout 0.40+ e weight_decay 5e-4**: troppa regolarizzazione, degrada performance.
- **CosineAnnealingLR**: schedule cieco, non adattivo; ReduceLROnPlateau migliore.

## Novita v5 rispetto a v3
1. **Warmup LR (3 epoche)**: aumento lineare del learning rate da 0 al target. Stabilizza ReduceLROnPlateau nelle prime epoche. Tecnica standard di LR scheduling (S:09).
2. **Patience 8->10**: sfrutta meglio ReduceLROnPlateau, riducendo il rischio di early stopping prematuro.
3. **TTA**: 5 viste mediate in inference (identico a v3.3). Aggiunge robustezza senza costi in training (S:05).

## Differenze rispetto al notebook del collega
- WeightedRandomSampler per bilanciare le classi nel training.
- Label smoothing 0.1 per ridurre overconfidence.
- ReduceLROnPlateau con warmup LR.
- TTA in inference.
- Niente augmentation per-classe, niente training in due fasi, niente affine/shear/zoom aggressivi.

## Tecniche del corso usate
- Transfer learning (S:12): ResNet18 pretrained ImageNet
- Discriminative LRs (S:12): backbone piu conservativo
- WeightedRandomSampler (S:05): class balancing
- Label smoothing (S:09): calibrazione
- ReduceLROnPlateau (S:09): adaptive LR decay
- Warmup LR (S:09): learning rate scheduling
- Dropout 0.25 (S:13, L:07A): regolarizzazione
- L2/weight_decay 1e-4 (S:09): regolarizzazione
- Data augmentation (S:05, L:04): flip, rotazione, ColorJitter, RandomErasing
- TTA (S:05): 5 viste in inference
- Early stopping (S:09, L:04): patience=10
- CrossEntropyLoss con class weights (S:09, L:04)
- Balanced accuracy (S:05): metrica primaria
- StratifiedShuffleSplit (L:01): split 80/20

## Target vs v3 (0.9725 BA, gap 2.66%)
- Standard: BA >= 0.97 (warmup + patience maggiore stabilizzano il training)
- TTA: ulteriore +0.2-0.5% atteso

## Risultato
Best epoch: 14
Best validation balanced accuracy: 0.9684
TTA validation accuracy: 0.9694
TTA validation balanced accuracy: 0.9679
Branch run: exp-resnet18-exnovo-v5-20260701-1033
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v5_20260701-1033
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v5_20260701-1033/resnet18_exnovo_v5_best.pth

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
