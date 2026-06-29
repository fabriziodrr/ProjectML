# ProjectML

Repository condivisa per il project work universitario di Machine Learning: classificazione di immagini di rifiuti (*Waste Type Identification*) con 8 classi finali.

## File principali

- `PROJECT_CONTEXT.md`: riassunto operativo del progetto, vincoli, label, metrica e consegna.
- `colab_runner.ipynb`: notebook Colab della nostra repo, configurato per `fabriziodrr/ProjectML`, con clone/pull, preparazione dataset, lancio esperimenti e commit/push.
- `project_work_Computer_Engineering.md`: traccia del project work.
- `test_Computer_Engineering.md`: specifica del notebook/funzione di test richiesta.
- `Slides/` e `Laboratorio/`: materiale del corso e dei laboratori.

## Classi

Il mapping delle label e fisso:

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

La metrica principale e la balanced accuracy, quindi ogni esperimento deve monitorare anche recall per classe e confusion matrix.

## Uso su Google Colab

1. Aprire `colab_runner.ipynb` in Google Colab.
2. Eseguire il mount di Google Drive.
3. Nella cella di configurazione controllare:
   - `DRIVE_ZIP_PATH`, cioe il path dello zip del dataset sul proprio Drive;
   - `DATASET_DIR_NAME`, cioe il nome della cartella prodotta dall'estrazione;
   - `GIT_USER_NAME` e `GIT_USER_EMAIL`;
   - `EXPERIMENT_NOTEBOOKS`, cioe i notebook da eseguire in ordine.
4. Inserire un GitHub token personale quando richiesto. Il token deve avere permessi di scrittura sulla repo.
5. Eseguire le celle fino al commit/push finale.

Il dataset non va committato nella repo. Il runner crea un symlink locale `dataset/` dentro Colab, ma `.gitignore` impedisce di versionarlo.

## Workflow consigliato

- Tenere `main` come versione stabile condivisa.
- Sviluppare gli esperimenti su branch dedicati, per esempio `exp/resnet18-baseline` o `exp/mobilenet-augmentation`.
- Non cambiare split tra esperimenti confrontabili.
- Salvare il protocollo di split in CSV, ma non salvare le immagini del dataset.
- Documentare ogni esperimento con ipotesi, configurazione, metriche e conclusione.
- Evitare di pushare checkpoint intermedi pesanti. Per modelli finali molto grandi, usare Google Drive e documentare il path/link.

## Cosa non pushare

- dataset e zip del dataset;
- token o credenziali;
- checkpoint intermedi pesanti;
- output temporanei di training;
- cartelle `eval/`, `runs/`, `wandb/`, `.ipynb_checkpoints/`.
