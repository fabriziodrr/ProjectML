---
jupyter:
  colab:
    authorship_tag: ABX9TyOQHFUsQb7YpOmJW4rUMKLR
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":21537,\"status\":\"ok\",\"timestamp\":1744118920743,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="Cyoxe1h3W7Wt" outputId="390529a3-d0a8-4bc3-ba57-04685628e10b"}
``` python
! pip install ucimlrepo &
from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir('/content/drive/MyDrive/Didattica/ML/Exercises/Exercise_Reject_option')
import numpy as np
import torch

%matplotlib inline
import matplotlib.pyplot as plt
```

::: {.output .stream .stdout}
    Requirement already satisfied: ucimlrepo in /usr/local/lib/python3.11/dist-packages (0.0.7)
    Requirement already satisfied: pandas>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from ucimlrepo) (2.2.2)
    Requirement already satisfied: certifi>=2020.12.5 in /usr/local/lib/python3.11/dist-packages (from ucimlrepo) (2025.1.31)
    Requirement already satisfied: numpy>=1.23.2 in /usr/local/lib/python3.11/dist-packages (from pandas>=1.0.0->ucimlrepo) (2.0.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas>=1.0.0->ucimlrepo) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas>=1.0.0->ucimlrepo) (2025.2)
    Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas>=1.0.0->ucimlrepo) (2025.2)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas>=1.0.0->ucimlrepo) (1.17.0)
    Mounted at /content/drive
:::
::::

::: {.cell .markdown id="ZLihVHSSFsqa"}
\#Dataset
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":1231,\"status\":\"ok\",\"timestamp\":1744118921979,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="pBtwj_ROWbVL" outputId="15806d44-37f0-436f-8124-2481c43a8aee"}
``` python
from ucimlrepo import fetch_ucirepo
from torch.utils.data import TensorDataset, Subset, DataLoader

# fetch dataset
banknote_authentication = fetch_ucirepo(id=267)

# metadata
print(banknote_authentication.metadata)

# variable information
print(banknote_authentication.variables)

# data (as pandas dataframes)

X = banknote_authentication.data.features.to_numpy()
y = banknote_authentication.data.targets.to_numpy()

num_samples, num_features = X.shape
num_classes = len(np.unique(y))

dataset = TensorDataset(torch.from_numpy(X).float(), torch.from_numpy(y).float())
```

::: {.output .stream .stdout}
    {'uci_id': 267, 'name': 'Banknote Authentication', 'repository_url': 'https://archive.ics.uci.edu/dataset/267/banknote+authentication', 'data_url': 'https://archive.ics.uci.edu/static/public/267/data.csv', 'abstract': 'Data were extracted from images that were taken for the evaluation of an authentication procedure for banknotes.', 'area': 'Computer Science', 'tasks': ['Classification'], 'characteristics': ['Multivariate'], 'num_instances': 1372, 'num_features': 4, 'feature_types': ['Real'], 'demographics': [], 'target_col': ['class'], 'index_col': None, 'has_missing_values': 'no', 'missing_values_symbol': None, 'year_of_dataset_creation': 2012, 'last_updated': 'Fri Feb 16 2024', 'dataset_doi': '10.24432/C55P57', 'creators': ['Volker Lohweg'], 'intro_paper': None, 'additional_info': {'summary': 'Data were extracted from images that were taken from genuine and forged banknote-like specimens.  For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.  ', 'purpose': None, 'funded_by': None, 'instances_represent': None, 'recommended_data_splits': None, 'sensitive_data': None, 'preprocessing_description': None, 'variable_info': '       1. variance of Wavelet Transformed image (continuous) \r\n       2. skewness of Wavelet Transformed image (continuous)\r\n       3. curtosis of Wavelet Transformed image (continuous)\r\n       4. entropy of image (continuous)\r\n       5. class (integer) \r\n', 'citation': None}}
           name     role        type demographic  \
    0  variance  Feature  Continuous        None   
    1  skewness  Feature  Continuous        None   
    2  curtosis  Feature  Continuous        None   
    3   entropy  Feature  Continuous        None   
    4     class   Target     Integer        None   

                                 description units missing_values  
    0  variance of Wavelet Transformed image  None             no  
    1  skewness of Wavelet Transformed image  None             no  
    2  curtosis of Wavelet Transformed image  None             no  
    3                       entropy of image  None             no  
    4                                   None  None             no  
:::
::::

::: {.cell .markdown id="q4G3QgWqFu0a"}
\##Cross-validation
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":1100,\"status\":\"ok\",\"timestamp\":1744118923080,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="YZsvCPuKfzOz" outputId="660413ad-f3f8-4002-a2dd-5fa24c0163f2"}
``` python
K = 3
dataloader_params = {"batch_size": num_samples, "num_workers": 1, "pin_memory": True}

torch.random.manual_seed(0)
cross_val_index = torch.randperm(num_samples) % K
train_folds, val_folds = [], []
for k in range(K):

    val_fold   = Subset(dataset, (cross_val_index==k).nonzero().squeeze())
    train_fold = Subset(dataset, (cross_val_index!=k).nonzero().squeeze())

    val_fold   = DataLoader(val_fold,   shuffle=False, **dataloader_params)
    train_fold = DataLoader(train_fold, shuffle=True,  **dataloader_params)

    val_folds.append(val_fold)
    train_folds.append(train_fold)


for k in range(K):
  for (Xt, yt), (Xv, yv) in zip(train_folds[k], val_folds[k]):
    print('fold', k, ', train - samples:', len(yt), 'class balance:', yt.mean().item())
    print('fold', k, ', val   - samples:', len(yv), 'class balance:', yv.mean().item())
```

::: {.output .stream .stdout}
    fold 0 , train - samples: 914 class balance: 0.4595186114311218
    fold 0 , val   - samples: 458 class balance: 0.41484716534614563
    fold 1 , train - samples: 915 class balance: 0.4382513761520386
    fold 1 , val   - samples: 457 class balance: 0.4573304057121277
    fold 2 , train - samples: 915 class balance: 0.43606558442115784
    fold 2 , val   - samples: 457 class balance: 0.4617067873477936
:::
::::

::: {.cell .markdown id="zB_w0TCquJJa"}
\#Training monitoring
In order to use [TensorBoard](https://pytorch.org/docs/stable/tensorboard.html), we will create a [SummaryWriter](https://pytorch.org/docs/stable/tensorboard.html#torch.utils.tensorboard.writer.SummaryWriter) object:
:::

::: {.cell .code id="PxTz6zLpdyzx"}
``` python
import os
from torch.utils.tensorboard import SummaryWriter
from tensorboard import notebook

def start_tensorboard(log_dir):
  writer = SummaryWriter(os.path.join("runs", log_dir))

  # run tensorboard in background
  ! killall tensorboard
  %reload_ext tensorboard
  %tensorboard --logdir ./runs --reload_interval 1

  notebook.list() # View open TensorBoard instances

  return writer
```
:::

::: {.cell .code id="AsAKyrC21sep"}
``` python
!rm -R runs/log
```
:::

::: {.cell .markdown id="NoK9eYYWe3Ta"}
\#Training the MultiLayer Perceptron network
:::

::: {.cell .markdown id="EyxXsInre0NR"}
\##Network model

Create a network with two fully connected layers and Sigmoid activation.
:::

::: {.cell .markdown id="j5nvUBtiF6HC"}
\##Train and validation loop
:::

::: {.cell .markdown id="XrYK0j9-osf7"}
\#Reject option using the MultiLayer Perceptron
:::

::: {.cell .markdown id="_hW54GaRqy_B"}
\##Inference
Load the best trained model and compute the accuracy.
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":98,\"status\":\"ok\",\"timestamp\":1744118994686,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="JNPDx53Co3SP" outputId="c722989f-7dab-445d-9f74-ae08d5e763be"}
``` python
k = 0

model = reset_model()[0]
model.load_state_dict(torch.load('models/best_fold%02d.pth' % k))

val_loader = val_folds[k]

with torch.no_grad():
  O_val = []
  Y_val = []

  for X_val, y_val in val_loader:
    O_val.append(model(X_val))
    Y_val.append(y_val)
  O_val = torch.concatenate(O_val)
  Y_val = torch.concatenate(Y_val)

  O_val = nn.Sigmoid()(O_val)

  O_val = O_val.numpy().squeeze()
  Y_val = Y_val.numpy().squeeze()
  Corr = (O_val > .5) == Y_val
  Err = np.logical_not(Corr)

print('Accuracy: {:.2f}'.format(Corr.mean()*100))
```

::: {.output .stream .stdout}
    Accuracy: 98.03
:::
::::

::: {.cell .markdown id="DvoJczTpq4sB"}
\##Ψₐ function computation
:::

::: {.cell .markdown id="zIhJeH-yrCxn"}
\##Thresholds computation
:::

::: {.cell .markdown id="MF_1DjugPXKL"}
\#Homework: Apply the reject option to previous exercises, e.g., the MNIST classification problem
:::
