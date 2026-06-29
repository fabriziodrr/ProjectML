# ProjectML

Repository condivisa per il project work universitario di Machine Learning: classificazione di immagini di rifiuti (*Waste Type Identification*) con 8 classi finali.

## File principali

- `PROJECT_CONTEXT.md`: riassunto operativo del progetto, vincoli, label, metrica e consegna.
- `colab_runner.ipynb`: notebook Colab della nostra repo, configurato per `fabriziodrr/ProjectML`, con clone/pull, preparazione dataset, lancio esperimenti e commit/push.
- `src/resnet18_exnovo/resnet18_exnovo_colab.ipynb`: esperimento ResNet18 ex novo, standalone per Colab, con salvataggio risultati leggeri su GitHub.
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

## Salvataggio risultati esperimenti

Il runner Colab salva automaticamente su GitHub solo i file generati dentro la cartella della repo in Colab:

```text
/content/ProjectML/
```

L'ultima cella del runner esegue `git add -A`, `git commit` e `git push`. Quindi vengono versionati i risultati leggeri salvati dentro la repo, per esempio:

- `splits/split.csv`
- `splits/class_weights.csv`
- `experiments/e1_baseline/config.json`
- `experiments/e1_baseline/metrics.csv`
- `experiments/e1_baseline/confusion_matrix.png`
- `experiments/e1_baseline/notes.md`
- `reports/report_draft.md`

Non vengono salvati automaticamente i file creati fuori dalla repo, per esempio in `/content/` o in una cartella Google Drive, a meno che vengano copiati dentro `/content/ProjectML/` prima della cella finale di commit/push.

Alcuni file dentro la repo sono comunque esclusi dal `.gitignore`, quindi non vengono pushati anche se sono in `/content/ProjectML/`:

- dataset e zip del dataset;
- checkpoint e modelli pesanti: `.pth`, `.pt`, `.ckpt`, `.onnx`;
- cartelle temporanee come `outputs/`, `logs/`, `runs/`, `wandb/`;
- `predictions.npy` e cartelle di valutazione locali.

Per i checkpoint finali o molto pesanti conviene usare Google Drive e documentare in repo il path o il link, per esempio in `models/README.md`. In repo vanno invece tenuti metriche, configurazioni, split, grafici e note degli esperimenti.

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
