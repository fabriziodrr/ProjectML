---
jupyter:
  colab:
    authorship_tag: ABX9TyNWXAri5HdoWebhXCmPqM9Y
    collapsed_sections:
    - fcROIMDgI9Hn
    - TTAQO9aPBJUZ
    - "-7BM4PXsBFjH"
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="zpv25cFQ7Ury"}
\#Before to start
Put this notebook file in the submitted Google Drive directory.

Edit **Section 1**, i.e., the first part of this notebook file implementing:

1.  **Section 1.1**: the loading of your best model(s):

- a\. Create the network(s)
- b\. Load the best saved model(s) using a relative path (e.g., `"./model.pth"` or `"./model/best.pth"`)

1.  **Section 1.2**: the predict function of your model(s):

- a\. Pre-process the input batch of data
- b\. Perform the forward using the network(s)
- c\. Post-process the output of the network(s)

DO NOT EDIT **Section 2** since it replicates the exact evaluation code we run on the private test set.

To test your model you have to:

- create a directory named `"eval"` containing the test images
- run all cells
:::

::: {.cell .markdown id="fcROIMDgI9Hn"}
\#Section 1: YOUR CODE
:::

::: {.cell .markdown id="TTAQO9aPBJUZ"}
\##Section 1.1: IMPLEMENT HERE THE FUNCTION TO LOAD YOUR MODEL
For example, here we use a simple network.

**IMPORTANT: load the trained weights of your model here!**
:::

::: {.cell .code id="9_xVMtGJ6NgC"}
``` python
# THIS IS AN EXAMPLE! REPLACE THIS WHOLE CELL WITH YOUR CODE

from torch.nn import Sequential, Conv2d, AdaptiveAvgPool2d, Flatten, Linear
NUM_CLASSES = 8

def load_model(): # YOU CAN EDIT THIS IF NECESSARY

  # THIS IS AN EXAMPLE! REPLACE THIS FUNCTION WITH YOUR CODE
  model = Sequential(
      Conv2d(in_channels=3, out_channels=16, kernel_size=1),
      AdaptiveAvgPool2d((1,1)),
      Flatten(),
      Linear(in_features=16, out_features=NUM_CLASSES if NUM_CLASSES>2 else 1)
      )
  # IMPORTANT: load here your best model weights!
  # model.load...

  # NOTE: IF YOU USE MORE THAN ONE NETWORK, LOAD ALL OF THEM HERE

  return model # MODIFY THIS IF YOU USE MULTIPLE NETWORKS
```
:::

::: {.cell .markdown id="-7BM4PXsBFjH"}
\##Section 1.2: IMPLEMENT HERE YOUR PREDICT FUNCTION

Consider that the input is a batch of data with:

    shape = (batch_size, rows, cols, channels=3)
    dtype = uint8

For example, here we implement a simple pre and post processing and we call the model forward.

**IMPORTANT: implement your own pre- and post-processing pipeline here!**

Note that you can use torchvision transformations on a single image of the batch. [Read the documentation](https://docs.pytorch.org/vision/main/transforms.html) for more details.
:::

::: {.cell .code id="TtKO0n6r8JAz"}
``` python
# THIS IS AN EXAMPLE! REPLACE THIS WHOLE CELL WITH YOUR CODE

import torch

def predict(model, X): # MODIFY THIS IF YOU USE MULTIPLE NETWORKS

  '''
  X is a uint8 numpy tensor of size (batch_size, rows, cols, channels=3)
  The output must be a uint8 numpy tensor of size (batch_size, 1)
  '''

  # THIS IS AN EXAMPLE! REPLACE THIS FUNCTION WITH YOUR CODE

  model.eval()
  with torch.no_grad():

    # REPLACE WITH YOUR PRE-PROCESSING
    X = torch.from_numpy(X).transpose(2,3).transpose(1,2).float()
    X /= 255.0

    # REPLACE WITH YOUR FORWARD FUNCTION
    Y = model(X)

    # REPLACE WITH YOUR POST-PROCESSING
    Y = Y.argmax(dim=-1).unsqueeze(1).numpy().astype(np.uint8)
  return Y
```
:::

::: {.cell .markdown id="sOvyzlNKvnr4"}
Run this cell to verify that the produced output is well formatted
:::

::: {.cell .code id="QQ5v71yV4F1o"}
``` python
import numpy as np
model = load_model()
X = np.random.randint(0, 255, size=(2,256,256,3), dtype=np.uint8) # this batch size is used only as an example
y = predict(model,X)
assert (y.shape == (X.shape[0],1) and y.dtype == np.uint8 \
      and (y >= 0).all() and (y < NUM_CLASSES).all()), "Verify your model loading or predict function."
```
:::

::: {.cell .markdown id="2vsV3tE512cd"}
\#Before to run the code

1.  eventually change the current working directory using the `os.chdir` function (DO IT IN THE EMPTY CELL BELOW THIS ONE)
2.  create a directory named `"./eval"` in the current working directory
3.  verify that the `"./eval"` directory contains the image files for the test

Then, run all the cells.
:::

::: {.cell .markdown id="Jdz_Q0lKApMW"}
\#Section 2: Test code (DO NOT MODIFY THE CODE BELOW!)
This is exactly the code we run for the final test.

Just run the code to verify that it works. This is the exact code we run for the final evaluation on the private test set.
:::

::: {.cell .code id="oD9KJ34NBodk"}
``` python
#from google.colab import drive;drive.mount('/content/drive'); import os; os.chdir("/content/drive/My Drive/Didattica/ML/exam_2025_2026/project_work_Ing_Inf/evaluation")
```
:::

::: {.cell .code id="M4xCDBymA7WU"}
``` python
import os
from glob import glob

test_dir = "./eval/" # Do not modify this path, instead create a directory with this name in the same folder of this test.ipynb file
assert os.path.isdir(test_dir), "The evaluation directory does not exist. Create it, put some images in it and run again this cell."

samples = [sample for sample in glob(test_dir + '/**', recursive=True) if os.path.isfile(sample)]
assert len(samples) > 0, "The evaluation directory is empty. Put some images in it and run again this cell."
print(f"Found {len(samples)} samples in {test_dir}")
```
:::

::: {.cell .code id="aqr86jEP54e-"}
``` python
import os
from PIL import Image
import numpy as np
from tqdm import tqdm

# Run YOUR LOAD_MODEL FUNCTION
model = load_model()

# Main loop
verbose = True

PREDICTIONs = np.zeros((len(samples), )) * np.nan
for i, img_path in tqdm(enumerate(samples), desc="Processing samples"):
  try:  # ATTENTION: any error occurring in this try-catch means that the corresponding PREDICTION is evaluated as an ERROR of the neural network
    # Open images
    rgb_image = Image.open(img_path)
    rgb_array = np.asarray(rgb_image)[None, ...]
    if verbose:
      print(f"\n  Loaded {img_path}. The input batch has shape {rgb_array.shape} and dtype {rgb_array.dtype}")

    # Run YOUR PREDICT FUNCTION
    predicted_labels_array = predict(model, rgb_array).squeeze()
    if verbose:
      print(f"  Predicted label {predicted_labels_array}")

    PREDICTIONs[i] = predicted_labels_array

  except FileNotFoundError:
    print(f"  Error: Could not find image file {img_path}")
  except Exception as e:
    print(f"  Error processing image {img_path}: {e}")

PREDICTIONs = PREDICTIONs.astype(np.uint8)
print(f"Predictions: {PREDICTIONs}")
np.save("predictions.npy", PREDICTIONs)
```
:::
