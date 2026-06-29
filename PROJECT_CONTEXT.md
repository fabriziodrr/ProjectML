# ProjectML - Context rapido

Questo file raccoglie le informazioni principali del progetto universitario di Machine Learning, in modo da dare contesto rapidamente nelle prossime sessioni.

## Obiettivo del progetto

Il project work riguarda la classificazione di immagini di rifiuti: il sistema deve riconoscere il tipo di rifiuto in immagini acquisite in condizioni molto diverse.

Le immagini possono avere risoluzioni diverse, sfondi naturali o preprocessati, piu oggetti della stessa classe nella stessa foto e oggetti non perfettamente rappresentati nel training set.

## Classi e label

Il mapping delle label e fisso e non va cambiato:

| Label | Classe |
| --- | --- |
| 0 | Battery |
| 1 | Clothing |
| 2 | Glass |
| 3 | Metal |
| 4 | Organic |
| 5 | Papery |
| 6 | Plastic |
| 7 | Undifferentiated |

Macro-classi presenti nella traccia:

- `Clothing`: clothes, shoes
- `Glass`: brown, green, transparent
- `Papery`: paper, cardboard
- `Undifferentiated`: classe other

## Vincoli

- Non si puo estendere il training set fornito.
- Si puo scegliere liberamente train/validation split o cross-validation.
- Si possono usare data augmentation e preprocessing.
- Sono ammessi algoritmi PyTorch, anche non necessariamente reti neurali, purche siano spiegabili.
- Il codice deve essere eseguibile in Google Colab.
- Limite memoria GPU in test: meno di 4 GB.
- Limite memoria GPU in training: meno di 5 GB.

## Metrica e valutazione

La metrica principale e la balanced accuracy, cioe la media dei recall/TPR delle 8 classi:

```text
Balanced accuracy = mean(TPR_battery, TPR_clothing, TPR_glass, TPR_metal,
                         TPR_organic, TPR_papery, TPR_plastic, TPR_undifferentiated)
```

Conseguenza pratica: non basta massimizzare l'accuracy globale. Ogni classe pesa allo stesso modo, quindi classi rare o difficili devono essere monitorate con metriche per classe e confusion matrix.

La valutazione considera anche il trade-off tra:

- balanced accuracy, piu alta e meglio;
- memoria GPU richiesta in test, piu bassa e meglio;
- frame rate/velocita di processamento, piu alto e meglio.

## Requisiti di consegna

La consegna richiede una cartella Google Drive, non Shared Drive, rinominata con il team name e accessibile a tutti senza richiesta di autorizzazione.

La cartella deve contenere:

- notebook Python per il training;
- protocollo train/validation split, come CSV o lista campioni, senza includere il dataset;
- file dei modelli/pesi salvati dopo il training;
- codice o notebook di test;
- report completo di circa 10 pagine;
- slide per presentazione di circa 5 minuti;
- file con i nomi dei membri del team.

## Specifica del notebook di test

Il notebook di test deve caricare il modello e definire una funzione di predizione compatibile con la valutazione privata.

Input di `predict`:

```text
X shape: (batch_size, rows, cols, 3)
X dtype: uint8
```

Output richiesto:

```text
shape: (batch_size, 1)
dtype: uint8
valori: label intere da 0 a 7
```

La funzione deve funzionare con batch size variabile, non deve assumere una dimensione fissa del batch e deve includere internamente preprocessing, forward del modello e postprocessing.

Schema tipico:

```python
def load_model():
    # creare modello
    # caricare pesi da path relativo
    # model.eval()
    return model

def predict(model, X):
    # X: NumPy uint8 NHWC
    # convertire a torch float NCHW
    # resize/normalize come in training
    # forward con torch.no_grad()
    # argmax e ritorno NumPy uint8 (batch_size, 1)
    return y
```

## Strategia sperimentale consigliata

- Definire subito uno split riproducibile e salvarlo in CSV.
- Impostare seed per Python, NumPy e PyTorch.
- Partire da una baseline semplice e tracciabile.
- Salvare il best checkpoint in base alla balanced accuracy su validation.
- Registrare per ogni esperimento: ipotesi, modifica introdotta, metriche, confusion matrix, classi migliorate/peggiorate e conclusione.
- Dopo ogni validazione, guardare gli errori per classe e alcune immagini misclassificate.
- Non rigenerare lo split tra esperimenti confrontabili.

## Modelli e training utili

Materiale del corso/laboratorio rilevante:

- train/validation/test split e cross-validation;
- metriche di classificazione, soprattutto recall per classe e balanced accuracy;
- gestione dataset sbilanciati;
- data augmentation;
- regolarizzazione, early stopping, dropout, batch normalization;
- CNN e transfer learning;
- PyTorch training loop, `model.train()`, `model.eval()`, `torch.no_grad()`;
- fine-tuning tipo AlexNet/ResNet/MobileNet;
- reject option come concetto teorico, se utile per analisi ma non necessariamente per la submission finale.

Per Colab e limiti RAM e sensato partire da modelli compatti di `torchvision.models`, ad esempio ResNet18, MobileNetV2/V3 o EfficientNet small, con testa a 8 classi.

Preprocessing tipico se si usa un modello pretrained ImageNet:

- resize/crop a 224x224;
- conversione `uint8 -> float` in `[0, 1]`;
- normalization ImageNet;
- augmentation moderata in training: crop, flip orizzontale se semanticamente sensato, rotazioni leggere, color jitter leggero.

Per la balanced accuracy valutare:

- `CrossEntropyLoss(weight=class_weights)`;
- `WeightedRandomSampler`;
- augmentation piu forte sulle classi deboli;
- analisi mirata delle classi con recall basso.

## Colab e GitHub

La repo remota corrente e:

```text
https://github.com/fabriziodrr/ProjectML
```

Il notebook `colab_runner.ipynb` serve a montare Google Drive, clonare o aggiornare la repo su Colab, preparare il dataset locale, eseguire eventuali notebook di esperimento e fare commit/push automatico dei risultati.

Quando si usa il runner in Colab, verificare sempre:

- path dello zip del dataset su Google Drive;
- nome della cartella prodotta dall'estrazione dello zip;
- lista dei notebook di esperimento da eseguire;
- nome/email git da usare nei commit;
- presenza di un token GitHub con permesso di scrittura sulla repo.

## File sorgente del contesto

Informazioni principali ricavate da:

- `project_work_Computer_Engineering.md`
- `test_Computer_Engineering.md`
- `Slides/*.md`
- `Laboratorio/*.md`
- `colab_runner.ipynb`
