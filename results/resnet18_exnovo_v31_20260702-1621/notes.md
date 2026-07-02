# resnet18_exnovo_v31_20260702-1621

## Ipotesi
ResNet18 pretrained puo dare una baseline forte con costo computazionale contenuto. Questa variante (v3.1) utilizza ESCLUSIVAMENTE tecniche ML riconducibili agli argomenti del corso: transfer learning, learning rate differenziati, regolarizzazione L2, dropout, data augmentation moderata, learning rate decrescente ed early stopping.

## Modifiche v3.1 rispetto a v3 (rimozione tecniche non corso)
- RIMOSSO AMP (Automatic Mixed Precision): training in FP32 puro come da corso (S:07-08 Back Propagation, L:03-04 PyTorch base).
- RIMOSSO torch.backends.cudnn.benchmark: nessun riferimento nel corso.
- RIMOSSO non_blocking=True nei trasferimenti GPU: tecnica di ottimizzazione CUDA non trattata.
- RIMOSSO set_to_none=True in zero_grad(): micro-ottimizzazione non trattata.
- CORRETTO ordinamento RandomErasing: ora prima di Normalize (posizione standard).
- Training loop semplificato: loss.backward() + optimizer.step() diretti, senza scaler.

## Tecniche del corso mantenute in v3.1
- Transfer learning / Fine-tuning: S:12 (teoria) + L:08 (AlexNet fine-tuning)
- ResNet18 / Skip connections: S:14 (Residual Learning)
- StratifiedShuffleSplit: L:01 (KNN validation)
- Data augmentation (flip, rotazione, ColorJitter, RandomErasing): S:05 (teoria) + L:04 (pratica)
- AdamW optimizer: da S:09 (Adam) + L:04 (Adam pratica)
- CrossEntropyLoss con class weights: S:09 (CCE) + L:04 (pratica)
- Label smoothing: S:09 (regolarizzazione loss)
- WeightedRandomSampler: S:04-05 (class imbalance)
- ReduceLROnPlateau: S:09 (learning rate decay)
- Early stopping: S:09 (teoria) + L:04 (pratica)
- Dropout: S:13 (teoria) + L:07A (AlexNet classifier)
- L2 regularization (weight_decay): S:09 (teoria)
- Balanced accuracy: da S:05 (recall per classe)
- Discriminative learning rates: da S:12 (transfer learning)
- ImageNet normalization: L:07A (AlexNet preprocessing)

## Differenze rispetto al notebook del collega
- Niente augmentation per-classe.
- WeightedRandomSampler per bilanciare le classi nel training.
- Label smoothing 0.1 per ridurre overconfidence.
- Niente training in due fasi frozen/unfrozen.
- Niente affine/shear/zoom aggressivi.
- Training in FP32 puro (no AMP).

## Risultato
Best epoch: 15
Best validation balanced accuracy: 0.9732
Branch run: exp-resnet18-exnovo-v31-20260702-1621
Cartella risultati: /content/ProjectML/results/resnet18_exnovo_v31_20260702-1621
Checkpoint Drive: /content/drive/MyDrive/ProjectML_checkpoints/resnet18_exnovo_v31_20260702-1621/resnet18_exnovo_v31_best.pth

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
