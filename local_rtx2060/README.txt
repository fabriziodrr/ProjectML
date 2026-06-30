Branch locale RTX 2060 per esperimenti v3.1 e v3.2.

Struttura attesa dopo il clone:

ProjectML/
  data/
    waste_type_identification/
      battery/
      clothes/
      shoes/
      brown/
      green/
      transparent/
      metal/
      organic/
      cardboard/
      paper/
      plastic/
      undifferentiated/
  local_rtx2060/
    v3.1/
    v3.2/

Il dataset va messo in:

data/waste_type_identification/

Non va messo dentro local_rtx2060 e non va pushato su GitHub.

Installazione consigliata su Windows con CUDA 12.1:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements-local-rtx2060.txt

Verifica GPU:

python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"

Per eseguire:

1. Aprire il notebook in local_rtx2060/v3.1 oppure local_rtx2060/v3.2.
2. Eseguire tutte le celle.
3. I risultati vengono salvati in results/<run_name>/.
4. I checkpoint vengono salvati in checkpoints/<run_name>/.

Batch size impostato a 16 per ridurre l'uso di VRAM sulla RTX 2060.
