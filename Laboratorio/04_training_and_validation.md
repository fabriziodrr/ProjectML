---
jupyter:
  accelerator: GPU
  colab:
    provenance:
    - file_id: 1wnxmk-Mza9uy-H7cfPAcRuaXIKOr9swz
      timestamp: 1641824449258
  kernelspec:
    display_name: Python 3
    name: python3
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="8YZmd1F-4QO7"}
Connect the Notebook to a Google Drive account
:::

::: {.cell .code execution_count="1" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":54174,\"status\":\"ok\",\"timestamp\":1776334000877,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="QaUyCscL4LV8" outputId="52ac96a5-ce40-424a-b18b-d7a8486fa24c"}
``` python
from google.colab import drive
drive.mount('/content/drive')
```

::: {.output .stream .stdout}
    Mounted at /content/drive
:::
:::

::: {.cell .markdown id="v9UsnNBi4cHV"}
Now go to the appropriate folder on your google drive. Note: you may
need to change the folder name, depending on where on your drive you
have the data files.
:::

::: {.cell .code execution_count="2" executionInfo="{\"elapsed\":2435,\"status\":\"ok\",\"timestamp\":1776334003315,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="5js9PSBo4m2j"}
``` python
import os
os.chdir('/content/drive/MyDrive/Didattica/ML/Exercises/Exercise05_Pytorch_network_training_and_validation')
```
:::

::: {.cell .markdown id="8MF8NHzcHB8a"}
#Introduction
![image.png](data:image/png;base64,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)

Documentation for [PyTorch](https://pytorch.org/docs/stable/index.html)
and [TorchVision](https://pytorch.org/vision/stable/index.html)
:::

::: {.cell .code execution_count="3" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":5244,\"status\":\"ok\",\"timestamp\":1776334008561,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="O9pmRGx_wwhA" outputId="65bc020c-223a-410a-9323-018837cb529d"}
``` python
import torch
print('PyTorch version:', torch.__version__)
```

::: {.output .stream .stdout}
    PyTorch version: 2.10.0+cu128
:::
:::

::: {.cell .code execution_count="4" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1776334008566,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="lM6ZKKb1vG7q"}
``` python
import matplotlib.pyplot as plt
def plot_digit(data):
    img, label = data
    img = img.squeeze()   # remove the trailing dimensions for visualization purpose only
    plt.imshow(img, cmap=plt.cm.gray_r)
    plt.title(label)
```
:::

::: {.cell .code execution_count="5" executionInfo="{\"elapsed\":28178,\"status\":\"ok\",\"timestamp\":1776334036742,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="omieiCj8vG7s"}
``` python
# download and read the training and the test data sets
from torchvision.datasets import MNIST
import torchvision.transforms as T

train_dataset = MNIST(root='./dataset/train/', train=True, download=True, transform=T.ToTensor())
val_dataset   = MNIST(root='./dataset/train/', train=True, download=False,transform=T.ToTensor())
test_dataset = MNIST(root='./dataset/test/', train=False, download=True, transform=T.ToTensor())

# input image dimensions
train_imgs, img_rows, img_cols = train_dataset.data.shape
test_imgs = len(test_dataset)
num_classes = 10
```
:::

::: {.cell .markdown id="OXDpZiJiUg00"}
#3-fold cross validation indexes
:::

::: {.cell .code execution_count="6" executionInfo="{\"elapsed\":2236,\"status\":\"ok\",\"timestamp\":1776334038979,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="iZBK_Jh3vG7u"}
``` python
K = 3
indexes = torch.randperm(len(train_dataset)) % K
torch.save(indexes, "cross-val-indexes.pt")
```
:::

::: {.cell .code execution_count="7" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":28,\"status\":\"ok\",\"timestamp\":1776334039009,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="83-eb9rUvG7v" outputId="2453dc67-7b66-4224-de96-a4e472d1d722"}
``` python
indexes
```

::: {.output .execute_result execution_count="7"}
    tensor([0, 2, 2,  ..., 2, 0, 2])
:::
:::

::: {.cell .code execution_count="8" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":14,\"status\":\"ok\",\"timestamp\":1776334039025,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="KmGDcXJKP-a_" outputId="eb6571b5-2952-46cf-9210-3f75a8bb4741"}
``` python
(indexes==0)
```

::: {.output .execute_result execution_count="8"}
    tensor([ True, False, False,  ..., False,  True, False])
:::
:::

::: {.cell .code execution_count="9" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":51,\"status\":\"ok\",\"timestamp\":1776334039077,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="V5AOB6z2QBeZ" outputId="edab71c5-8b8f-4716-b4e1-2318e8cb548e"}
``` python
(indexes==0).nonzero()
```

::: {.output .execute_result execution_count="9"}
    tensor([[    0],
            [    3],
            [    7],
            ...,
            [59987],
            [59988],
            [59998]])
:::
:::

::: {.cell .code execution_count="10" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":1,\"status\":\"ok\",\"timestamp\":1776334039079,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="UDsELtCHJTZg" outputId="61b7047f-ef93-456c-baba-83095d548789"}
``` python
(indexes==0).nonzero().shape
```

::: {.output .execute_result execution_count="10"}
    torch.Size([20000, 1])
:::
:::

::: {.cell .code execution_count="11" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":3,\"status\":\"ok\",\"timestamp\":1776334039083,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="YABxeeCOvG7w" outputId="908c3e30-c899-4771-baab-0c2839fd696d"}
``` python
(indexes==0).nonzero().squeeze()
```

::: {.output .execute_result execution_count="11"}
    tensor([    0,     3,     7,  ..., 59987, 59988, 59998])
:::
:::

::: {.cell .code execution_count="12" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":8,\"status\":\"ok\",\"timestamp\":1776334039091,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="lyAzO1HUvG7x" outputId="24a81d66-7e60-4493-cae3-9adbbae3dafa"}
``` python
from torch.utils.data import Subset, DataLoader

dataloader_params = {"batch_size": 32, "num_workers": 4, "pin_memory": True}

train_folds, val_folds = [], []
for k in range(K):

    val_fold   = Subset(val_dataset,   (indexes==k).nonzero().squeeze())
    train_fold = Subset(train_dataset, (indexes!=k).nonzero().squeeze())

    val_fold   = DataLoader(val_fold,   shuffle=False, **dataloader_params)
    train_fold = DataLoader(train_fold, shuffle=True,  **dataloader_params)
    # train_fold = DataLoader(train_fold, shuffle=True, batch_size=32, num_workers=4, pin_memory=True)

    val_folds.append(val_fold)
    train_folds.append(train_fold)
```

::: {.output .stream .stderr}
    /usr/local/lib/python3.12/dist-packages/torch/utils/data/dataloader.py:424: UserWarning: This DataLoader will create 4 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
      self.check_worker_number_rationality()
:::
:::

::: {.cell .markdown id="RpAP4sQ9rCO8"}
#PyTorch Network models Now let us build a Multilayer Perceptron. To do
this, we:

1.  instantiate an empty feed-forward
    ([sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html))
    network
2.  add two fully-connected ([a.k.a.
    linear](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html))
    layers to the network (i.e. one hidden layer and the output layer)

Other [PyTorch layers and functions for Neural
Networks](https://pytorch.org/docs/stable/nn.html)
:::

::: {.cell .code execution_count="14" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":11,\"status\":\"ok\",\"timestamp\":1776334074212,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="N4fpPHExKUNd" outputId="76fffe71-ff2e-4bca-ef2d-3a30a8089a35"}
``` python
import torch.nn as nn
hidden_size = 72
model2 = nn.Sequential(
    nn.Flatten(),
    nn.Linear(img_rows*img_cols, hidden_size),
    nn.Sigmoid(),
    nn.Linear(hidden_size, num_classes),
    nn.Softmax(dim=-1)
)
print("Model 2:\n", model2)
```

::: {.output .stream .stdout}
    Model 2:
     Sequential(
      (0): Flatten(start_dim=1, end_dim=-1)
      (1): Linear(in_features=784, out_features=72, bias=True)
      (2): Sigmoid()
      (3): Linear(in_features=72, out_features=10, bias=True)
      (4): Softmax(dim=-1)
    )
:::
:::

::: {.cell .markdown id="XpQ5Kkv08IWV"}
##General model
:::

::: {.cell .code execution_count="15" executionInfo="{\"elapsed\":9,\"status\":\"ok\",\"timestamp\":1776334077546,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="BTqkKBQH5bxx"}
``` python
from torch import nn
class MultiLayerPerceptron(nn.Module):
    def __init__(self, input_size=img_rows*img_cols, hidden_size=72, output_size=num_classes):
        # init function executed once when the nn is instantiated
        super().__init__() # execute the nn.Module init function

        # layers with trainable parameters
        self.layer1 = nn.Linear(input_size, hidden_size)    # fully-connected layer
        self.layer2 = nn.Linear(hidden_size, output_size)   # fully-connected layer

        # layers without trainable parameters
        self.flatten = nn.Flatten()               # reshape from (a, b) to (a*b, 1)
        self.sigmoid = nn.Sigmoid()               # sigmoid activation layer
        self.softmax = nn.Softmax(dim=-1)         # softmax activation layer

    def forward(self, x, verbose=False):
        # forward function executed when an input is passed to the nn
        if verbose:
          print("Input shape", x.shape)  # 32 x 1 x 28 x 28

        x = self.flatten(x)                    # apply the flatten to the input 32 x (28**2)

        if verbose:
          print("Flattened shape", x.shape)

        x = self.layer1(x)                        # apply the first fully-connected layer
        x = self.sigmoid(x)                       # apply the sigmoid activation layer

        if verbose:
          print("1st layer features shape", x.shape) # 32 x 72

        logits = self.layer2(x)                   # apply the second fully-connected layer
        probs = self.softmax(logits)              # apply the softmax activation layer

        if verbose:
          print("2nd (output) layer features shape", probs.shape) # 32 x 10

        return probs                              # model output
```
:::

::: {.cell .code execution_count="16" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":12,\"status\":\"ok\",\"timestamp\":1776334081297,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="sEuniwOHvG71" outputId="fabbfb08-b4a7-4274-e37a-d07dc68cfa01"}
``` python
model = MultiLayerPerceptron()         # model
print("Model:\n", model)
```

::: {.output .stream .stdout}
    Model:
     MultiLayerPerceptron(
      (layer1): Linear(in_features=784, out_features=72, bias=True)
      (layer2): Linear(in_features=72, out_features=10, bias=True)
      (flatten): Flatten(start_dim=1, end_dim=-1)
      (sigmoid): Sigmoid()
      (softmax): Softmax(dim=-1)
    )
:::
:::

::: {.cell .markdown id="2gt0Ipcexs_Q"}
### Model parameters
:::

::: {.cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1776334084421,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="AHnY3AWW_0ff" outputId="8921cffd-b00e-40b2-89ce-115d88e446d5"}
``` python
def print_parameters(model):
    for name, param in model.named_parameters():
      print(name)
      print("- requires_grad:", param.requires_grad)
      print("- shape:", param.shape)
      print("- is on GPU?", param.is_cuda,"\n")

print_parameters(model)
```

::: {.output .stream .stdout}
    layer1.weight
    - requires_grad: True
    - shape: torch.Size([72, 784])
    - is on GPU? False 

    layer1.bias
    - requires_grad: True
    - shape: torch.Size([72])
    - is on GPU? False 

    layer2.weight
    - requires_grad: True
    - shape: torch.Size([10, 72])
    - is on GPU? False 

    layer2.bias
    - requires_grad: True
    - shape: torch.Size([10])
    - is on GPU? False 
:::
:::

::: {.cell .markdown id="SHwuz6hlyjAP"}
##From CPU to GPU and back
:::

::: {.cell .code execution_count="18" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":248,\"status\":\"ok\",\"timestamp\":1776334088043,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="ghSIQ5Oa-a5Y" outputId="3dc49f8d-082a-4623-97b0-2ec5bffda0d0"}
``` python
model = model.cuda()
print_parameters(model)
```

::: {.output .stream .stdout}
    layer1.weight
    - requires_grad: True
    - shape: torch.Size([72, 784])
    - is on GPU? True 

    layer1.bias
    - requires_grad: True
    - shape: torch.Size([72])
    - is on GPU? True 

    layer2.weight
    - requires_grad: True
    - shape: torch.Size([10, 72])
    - is on GPU? True 

    layer2.bias
    - requires_grad: True
    - shape: torch.Size([10])
    - is on GPU? True 
:::
:::

::: {.cell .code execution_count="19" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":3,\"status\":\"ok\",\"timestamp\":1776334093680,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="UEWKyx2pyojK" outputId="7829052c-3191-4b15-8350-23d2e8fdbf10"}
``` python
model = model.cpu()
print_parameters(model)
```

::: {.output .stream .stdout}
    layer1.weight
    - requires_grad: True
    - shape: torch.Size([72, 784])
    - is on GPU? False 

    layer1.bias
    - requires_grad: True
    - shape: torch.Size([72])
    - is on GPU? False 

    layer2.weight
    - requires_grad: True
    - shape: torch.Size([10, 72])
    - is on GPU? False 

    layer2.bias
    - requires_grad: True
    - shape: torch.Size([10])
    - is on GPU? False 
:::
:::

::: {.cell .markdown collapsed="false" id="BWdYTuqQvG75"}
#One training iteration
:::

::: {.cell .markdown collapsed="false" id="5_-v1homvG75"}
##Loss function and optimizer Now we select the cross-entropy as the
loss and the Stochastic Gradient Descent as the optimizer.
:::

::: {.cell .markdown collapsed="false" id="W8IH4aRTvG76"}
##Forward pass
:::

::: {.cell .code execution_count="20" executionInfo="{\"elapsed\":40,\"status\":\"ok\",\"timestamp\":1776334097705,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="IbcCsLEJvG76"}
``` python
model = model.cuda()
```
:::

::: {.cell .markdown collapsed="false" id="IfO9qHtcvG77"}
###Data and model on different devices
:::

::: {.cell .code execution_count="21" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":723}" executionInfo="{\"elapsed\":263,\"status\":\"error\",\"timestamp\":1776334099204,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="cOmXWaEnvG77" outputId="4cf07f0f-ed5b-4781-8d2d-c260fa80142a"}
``` python
batch_x, batch_y = next(iter(train_folds[0]))
print("x shape:", batch_x.shape)
print("y shape:", batch_y.shape)

output = model(batch_x)
print("Output:", output, output.shape)
```

::: {.output .stream .stderr}
    /usr/local/lib/python3.12/dist-packages/torch/utils/data/dataloader.py:432: UserWarning: This DataLoader will create 4 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
      self.check_worker_number_rationality()
:::

::: {.output .stream .stdout}
    x shape: torch.Size([32, 1, 28, 28])
    y shape: torch.Size([32])
:::

::: {.output .error ename="RuntimeError" evalue="Expected all tensors to be on the same device, but got mat1 is on cpu, different from other tensors on cuda:0 (when checking argument in method wrapper_CUDA_addmm)"}
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    /tmp/ipykernel_2605/3039069088.py in <cell line: 0>()
          3 print("y shape:", batch_y.shape)
          4 
    ----> 5 output = model(batch_x)
          6 print("Output:", output, output.shape)

    /usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1774             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1775         else:
    -> 1776             return self._call_impl(*args, **kwargs)
       1777 
       1778     # torchrec tests the code consistency with the following code

    /usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1785                 or _global_backward_pre_hooks or _global_backward_hooks
       1786                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1787             return forward_call(*args, **kwargs)
       1788 
       1789         result = None

    /tmp/ipykernel_2605/2253404292.py in forward(self, x, verbose)
         24           print("Flattened shape", x.shape)
         25 
    ---> 26         x = self.layer1(x)                        # apply the first fully-connected layer
         27         x = self.sigmoid(x)                       # apply the sigmoid activation layer
         28 

    /usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py in _wrapped_call_impl(self, *args, **kwargs)
       1774             return self._compiled_call_impl(*args, **kwargs)  # type: ignore[misc]
       1775         else:
    -> 1776             return self._call_impl(*args, **kwargs)
       1777 
       1778     # torchrec tests the code consistency with the following code

    /usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py in _call_impl(self, *args, **kwargs)
       1785                 or _global_backward_pre_hooks or _global_backward_hooks
       1786                 or _global_forward_hooks or _global_forward_pre_hooks):
    -> 1787             return forward_call(*args, **kwargs)
       1788 
       1789         result = None

    /usr/local/lib/python3.12/dist-packages/torch/nn/modules/linear.py in forward(self, input)
        132         Runs the forward pass.
        133         """
    --> 134         return F.linear(input, self.weight, self.bias)
        135 
        136     def extra_repr(self) -> str:

    RuntimeError: Expected all tensors to be on the same device, but got mat1 is on cpu, different from other tensors on cuda:0 (when checking argument in method wrapper_CUDA_addmm)
:::
:::

::: {.cell .code execution_count="22" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":10,\"status\":\"ok\",\"timestamp\":1776334109028,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="YW43-OeszTyl" outputId="829e6fe7-7730-4450-e01d-e2bda1a007a8"}
``` python
batch_y
```

::: {.output .execute_result execution_count="22"}
    tensor([1, 9, 2, 8, 9, 2, 5, 0, 4, 5, 2, 9, 4, 5, 8, 3, 1, 8, 7, 8, 7, 7, 0, 4,
            9, 9, 1, 4, 2, 4, 6, 9])
:::
:::

::: {.cell .code execution_count="23" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":351}" executionInfo="{\"elapsed\":222,\"status\":\"ok\",\"timestamp\":1776334114259,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="sm6Ply3fzXnG" outputId="ed46ddd2-1e95-4b4b-9380-adeb178926df"}
``` python
plot_digit((batch_x[0], batch_y[0]))
```

::: {.output .display_data}
![](4fbf3be1c5ae9e916dea076256d8943841837a1d.png)
:::
:::

::: {.cell .markdown collapsed="false" id="g9CMQfBfvG78"}
###Move data on the GPU and execute the forward pass
:::

::: {.cell .code execution_count="24" colab="{\"base_uri\":\"https://localhost:8080/\"}" collapsed="true" executionInfo="{\"elapsed\":534,\"status\":\"ok\",\"timestamp\":1776334118251,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="P-dz8QmrvG78" outputId="422b9eae-431b-4914-9d91-fe0e7c5e4b21"}
``` python
batch_x = batch_x.cuda()
batch_y = batch_y.cuda()
print("Data is CUDA?", batch_x.is_cuda)

output = model(batch_x)  # model.forward(batch_x)
print("Output:", output, output.shape)
```

::: {.output .stream .stdout}
    Data is CUDA? True
    Output: tensor([[0.1178, 0.1674, 0.0363, 0.0740, 0.1213, 0.1240, 0.1196, 0.0739, 0.0770,
             0.0887],
            [0.1180, 0.1619, 0.0372, 0.0789, 0.1194, 0.1266, 0.1182, 0.0744, 0.0778,
             0.0877],
            [0.1177, 0.1657, 0.0371, 0.0779, 0.1213, 0.1272, 0.1212, 0.0729, 0.0734,
             0.0856],
            [0.1148, 0.1601, 0.0373, 0.0777, 0.1226, 0.1235, 0.1228, 0.0742, 0.0788,
             0.0883],
            [0.1192, 0.1643, 0.0365, 0.0774, 0.1240, 0.1234, 0.1213, 0.0742, 0.0743,
             0.0853],
            [0.1182, 0.1657, 0.0362, 0.0787, 0.1236, 0.1262, 0.1207, 0.0714, 0.0750,
             0.0842],
            [0.1156, 0.1642, 0.0360, 0.0765, 0.1190, 0.1255, 0.1224, 0.0743, 0.0793,
             0.0872],
            [0.1152, 0.1644, 0.0366, 0.0762, 0.1217, 0.1229, 0.1216, 0.0742, 0.0788,
             0.0885],
            [0.1191, 0.1649, 0.0353, 0.0759, 0.1235, 0.1241, 0.1212, 0.0721, 0.0776,
             0.0864],
            [0.1175, 0.1625, 0.0367, 0.0753, 0.1214, 0.1254, 0.1212, 0.0745, 0.0774,
             0.0879],
            [0.1172, 0.1647, 0.0355, 0.0743, 0.1207, 0.1315, 0.1279, 0.0709, 0.0750,
             0.0823],
            [0.1181, 0.1638, 0.0365, 0.0778, 0.1237, 0.1217, 0.1203, 0.0762, 0.0744,
             0.0874],
            [0.1159, 0.1648, 0.0365, 0.0769, 0.1237, 0.1241, 0.1204, 0.0739, 0.0774,
             0.0864],
            [0.1175, 0.1629, 0.0359, 0.0764, 0.1238, 0.1218, 0.1211, 0.0739, 0.0770,
             0.0898],
            [0.1148, 0.1598, 0.0371, 0.0783, 0.1240, 0.1267, 0.1213, 0.0746, 0.0760,
             0.0875],
            [0.1168, 0.1654, 0.0361, 0.0768, 0.1217, 0.1279, 0.1215, 0.0712, 0.0759,
             0.0866],
            [0.1198, 0.1636, 0.0363, 0.0738, 0.1194, 0.1265, 0.1217, 0.0741, 0.0760,
             0.0889],
            [0.1160, 0.1604, 0.0369, 0.0791, 0.1238, 0.1261, 0.1239, 0.0710, 0.0766,
             0.0860],
            [0.1240, 0.1617, 0.0358, 0.0770, 0.1188, 0.1248, 0.1225, 0.0726, 0.0767,
             0.0862],
            [0.1154, 0.1632, 0.0367, 0.0786, 0.1155, 0.1246, 0.1239, 0.0751, 0.0781,
             0.0889],
            [0.1198, 0.1628, 0.0366, 0.0758, 0.1187, 0.1242, 0.1185, 0.0756, 0.0785,
             0.0895],
            [0.1188, 0.1658, 0.0365, 0.0780, 0.1257, 0.1234, 0.1204, 0.0715, 0.0749,
             0.0850],
            [0.1155, 0.1651, 0.0364, 0.0733, 0.1194, 0.1265, 0.1270, 0.0723, 0.0777,
             0.0868],
            [0.1167, 0.1666, 0.0364, 0.0752, 0.1224, 0.1237, 0.1188, 0.0743, 0.0785,
             0.0876],
            [0.1156, 0.1634, 0.0355, 0.0785, 0.1210, 0.1220, 0.1243, 0.0741, 0.0779,
             0.0876],
            [0.1200, 0.1627, 0.0352, 0.0771, 0.1218, 0.1265, 0.1196, 0.0740, 0.0768,
             0.0863],
            [0.1207, 0.1675, 0.0357, 0.0753, 0.1205, 0.1234, 0.1195, 0.0733, 0.0767,
             0.0874],
            [0.1155, 0.1658, 0.0363, 0.0809, 0.1287, 0.1238, 0.1166, 0.0720, 0.0771,
             0.0834],
            [0.1151, 0.1675, 0.0356, 0.0752, 0.1178, 0.1251, 0.1281, 0.0719, 0.0756,
             0.0880],
            [0.1227, 0.1645, 0.0362, 0.0803, 0.1214, 0.1229, 0.1173, 0.0720, 0.0767,
             0.0861],
            [0.1172, 0.1663, 0.0361, 0.0749, 0.1202, 0.1222, 0.1254, 0.0746, 0.0761,
             0.0871],
            [0.1213, 0.1597, 0.0363, 0.0784, 0.1205, 0.1253, 0.1208, 0.0731, 0.0765,
             0.0881]], device='cuda:0', grad_fn=<SoftmaxBackward0>) torch.Size([32, 10])
:::
:::

::: {.cell .code execution_count="25" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":33,\"status\":\"ok\",\"timestamp\":1776334130831,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="UJ60xHu8nIaQ" outputId="08a87915-3e50-415a-a779-7ccabc712d8a"}
``` python
output.detach().argmax(-1)
```

::: {.output .execute_result execution_count="25"}
    tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1], device='cuda:0')
:::
:::

::: {.cell .code execution_count="26" executionInfo="{\"elapsed\":8,\"status\":\"ok\",\"timestamp\":1776334132411,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="mHYtZJ0VvG76"}
``` python
lossFunction = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),   #   <-- SELECT WHICH PARAMETERS TO OPTIMIZE
                            weight_decay=0,       #   <-- REGULARIZATION DEACTIVATED IN THIS EXAMPLE
                            lr=1)               #   <-- HIGH LEARNING RATE ONLY TO OBSERVE THE WEIGHT UPDATE
```
:::

::: {.cell .markdown collapsed="false" id="QV93b02dvG78"}
##Backward pass
:::

::: {.cell .code execution_count="27" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":11,\"status\":\"ok\",\"timestamp\":1776334136962,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="rWHQoJKbvG79" outputId="666d3666-fde7-43ee-d34e-0aad2105b542"}
``` python
param = model.layer2.bias
print(param)
print("Gradient of the param:", param.grad)
```

::: {.output .stream .stdout}
    Parameter containing:
    tensor([ 0.0504,  0.0276, -0.0995, -0.0944, -0.0161,  0.0665, -0.0722, -0.0253,
            -0.1168, -0.0205], device='cuda:0', requires_grad=True)
    Gradient of the param: None
:::
:::

::: {.cell .markdown collapsed="false" id="J6rFt_EvvG79"}
###Backpropagation and gradient computation
:::

::: {.cell .code execution_count="28" collapsed="true" executionInfo="{\"elapsed\":107,\"status\":\"ok\",\"timestamp\":1776334141163,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="ze1SWJbRvG7-"}
``` python
loss = lossFunction(output, batch_y)
loss.backward()
```
:::

::: {.cell .code execution_count="29" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":12,\"status\":\"ok\",\"timestamp\":1776334141778,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="9CepRfg1IXJH" outputId="d2d96b11-65ea-4867-d00e-1958b415e718"}
``` python
batch_y
```

::: {.output .execute_result execution_count="29"}
    tensor([1, 9, 2, 8, 9, 2, 5, 0, 4, 5, 2, 9, 4, 5, 8, 3, 1, 8, 7, 8, 7, 7, 0, 4,
            9, 9, 1, 4, 2, 4, 6, 9], device='cuda:0')
:::
:::

::: {.cell .code execution_count="30" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":9,\"status\":\"ok\",\"timestamp\":1776334143619,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="bwczNMpUIXJH" outputId="d3641997-147f-4bd2-f16b-178c4ff68e54"}
``` python
loss
```

::: {.output .execute_result execution_count="30"}
    tensor(2.3057, device='cuda:0', grad_fn=<NllLossBackward0>)
:::
:::

::: {.cell .code execution_count="31" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":27,\"status\":\"ok\",\"timestamp\":1776334145042,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="Fol2FBlDvG7-" outputId="1cc9424e-836e-4923-b40c-5487382c296f"}
``` python
print(param)
print("Gradient of the param:", param.grad)
```

::: {.output .stream .stdout}
    Parameter containing:
    tensor([ 0.0504,  0.0276, -0.0995, -0.0944, -0.0161,  0.0665, -0.0722, -0.0253,
            -0.1168, -0.0205], device='cuda:0', requires_grad=True)
    Gradient of the param: tensor([ 4.3400e-03,  1.3107e-03, -1.2465e-03,  4.8016e-03, -7.3899e-03,
             6.4456e-04,  8.0135e-03,  1.7079e-05, -2.4441e-03, -8.0470e-03],
           device='cuda:0')
:::
:::

::: {.cell .markdown collapsed="false" id="Fb2HwpyivG7-"}
###Weights update and gradient reset
:::

::: {.cell .code execution_count="32" executionInfo="{\"elapsed\":105,\"status\":\"ok\",\"timestamp\":1776334148735,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="T_5I_BmqvG7_"}
``` python
optimizer.step()
optimizer.zero_grad()
```
:::

::: {.cell .code execution_count="33" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1776334150664,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="yK4tS8dDvG8B" outputId="32a6ac99-d50f-4ef5-998b-443e5505c98f"}
``` python
print(param)
print("Gradient of the param:", param.grad)
```

::: {.output .stream .stdout}
    Parameter containing:
    tensor([-0.9496, -0.9724,  0.9005, -1.0944,  0.9839, -0.9334, -1.0722, -1.0247,
             0.8832,  0.9795], device='cuda:0', requires_grad=True)
    Gradient of the param: None
:::
:::

::: {.cell .markdown collapsed="false" id="G8sDTz1UvG8B"}
#Train for one epoch

Now we train the model for one *epoch*
:::

::: {.cell .code execution_count="35" executionInfo="{\"elapsed\":14,\"status\":\"ok\",\"timestamp\":1776334178715,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="8F8dcs_rvG8B"}
``` python
optimizer = torch.optim.Adam(model.parameters(),   #   <-- SELECT WHICH PARAMETERS TO OPTIMIZE
                            lr=0.001, weight_decay=0)
```
:::

::: {.cell .code execution_count="36" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1776334181978,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="PskIyE2GvG8C"}
``` python
k=0
train_loader, val_loader = train_folds[k], val_folds[k]
val_losses, val_accuracies = [], []
```
:::

::: {.cell .code execution_count="53" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":9809,\"status\":\"ok\",\"timestamp\":1776335746625,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="zXWzN8FmvG8C" outputId="e57d70f2-e442-4482-babe-4dc6ce7471a5"}
``` python
for X, y in train_loader:
  X = X.cuda()
  y = y.cuda()

  optimizer.zero_grad()

  o = model(X)
  l = lossFunction(o, y)


  l.backward()
  optimizer.step()

  acc = (o.detach().argmax(-1) == y.detach()).float().mean()
  print("Training batch loss: {:.4f}  accuracy: {:.2f} %".format(l.detach().item(), acc.item()*100))
```

::: {.output .stream .stderr}
    /usr/local/lib/python3.12/dist-packages/torch/utils/data/dataloader.py:432: UserWarning: This DataLoader will create 4 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
      self.check_worker_number_rationality()
:::

::: {.output .stream .stdout}
    Training batch loss: 1.9517  accuracy: 50.00 %
    Training batch loss: 2.0092  accuracy: 43.75 %
    Training batch loss: 2.0664  accuracy: 37.50 %
    Training batch loss: 2.1279  accuracy: 31.25 %
    Training batch loss: 2.1162  accuracy: 34.38 %
    Training batch loss: 2.1288  accuracy: 31.25 %
    Training batch loss: 2.1937  accuracy: 25.00 %
    Training batch loss: 1.9900  accuracy: 46.88 %
    Training batch loss: 1.9863  accuracy: 46.88 %
    Training batch loss: 2.1230  accuracy: 31.25 %
    Training batch loss: 2.0318  accuracy: 43.75 %
    Training batch loss: 2.1283  accuracy: 31.25 %
    Training batch loss: 2.0779  accuracy: 37.50 %
    Training batch loss: 2.0699  accuracy: 37.50 %
    Training batch loss: 2.0761  accuracy: 37.50 %
    Training batch loss: 1.9813  accuracy: 46.88 %
    Training batch loss: 1.9463  accuracy: 53.12 %
    Training batch loss: 2.2279  accuracy: 21.88 %
    Training batch loss: 2.0136  accuracy: 43.75 %
    Training batch loss: 2.1526  accuracy: 28.12 %
    Training batch loss: 2.2239  accuracy: 21.88 %
    Training batch loss: 2.0174  accuracy: 43.75 %
    Training batch loss: 2.0181  accuracy: 43.75 %
    Training batch loss: 2.0203  accuracy: 43.75 %
    Training batch loss: 2.0704  accuracy: 37.50 %
    Training batch loss: 2.0227  accuracy: 43.75 %
    Training batch loss: 2.1270  accuracy: 31.25 %
    Training batch loss: 2.1371  accuracy: 31.25 %
    Training batch loss: 2.1033  accuracy: 34.38 %
    Training batch loss: 2.0428  accuracy: 40.62 %
    Training batch loss: 2.0106  accuracy: 43.75 %
    Training batch loss: 2.1602  accuracy: 28.12 %
    Training batch loss: 2.1065  accuracy: 34.38 %
    Training batch loss: 2.0232  accuracy: 43.75 %
    Training batch loss: 2.0098  accuracy: 46.88 %
    Training batch loss: 2.0477  accuracy: 40.62 %
    Training batch loss: 1.9822  accuracy: 50.00 %
    Training batch loss: 2.1865  accuracy: 25.00 %
    Training batch loss: 2.1287  accuracy: 31.25 %
    Training batch loss: 2.0960  accuracy: 34.38 %
    Training batch loss: 2.0727  accuracy: 37.50 %
    Training batch loss: 2.1963  accuracy: 25.00 %
    Training batch loss: 2.0956  accuracy: 34.38 %
    Training batch loss: 2.0251  accuracy: 43.75 %
    Training batch loss: 2.1971  accuracy: 25.00 %
    Training batch loss: 2.0118  accuracy: 43.75 %
    Training batch loss: 2.0269  accuracy: 40.62 %
    Training batch loss: 2.1596  accuracy: 28.12 %
    Training batch loss: 1.9790  accuracy: 46.88 %
    Training batch loss: 2.2051  accuracy: 25.00 %
    Training batch loss: 2.0895  accuracy: 37.50 %
    Training batch loss: 2.0701  accuracy: 37.50 %
    Training batch loss: 2.1059  accuracy: 34.38 %
    Training batch loss: 2.0849  accuracy: 37.50 %
    Training batch loss: 1.9758  accuracy: 46.88 %
    Training batch loss: 2.2362  accuracy: 18.75 %
    Training batch loss: 1.9616  accuracy: 50.00 %
    Training batch loss: 1.9805  accuracy: 46.88 %
    Training batch loss: 2.0324  accuracy: 40.62 %
    Training batch loss: 2.0421  accuracy: 40.62 %
    Training batch loss: 2.1065  accuracy: 34.38 %
    Training batch loss: 2.0228  accuracy: 43.75 %
    Training batch loss: 2.1095  accuracy: 31.25 %
    Training batch loss: 2.0800  accuracy: 37.50 %
    Training batch loss: 2.0579  accuracy: 37.50 %
    Training batch loss: 2.0624  accuracy: 37.50 %
    Training batch loss: 2.1048  accuracy: 34.38 %
    Training batch loss: 1.8511  accuracy: 62.50 %
    Training batch loss: 1.9512  accuracy: 50.00 %
    Training batch loss: 1.8910  accuracy: 56.25 %
    Training batch loss: 1.9942  accuracy: 46.88 %
    Training batch loss: 2.1020  accuracy: 34.38 %
    Training batch loss: 2.0266  accuracy: 43.75 %
    Training batch loss: 2.1010  accuracy: 34.38 %
    Training batch loss: 2.0869  accuracy: 34.38 %
    Training batch loss: 2.1389  accuracy: 31.25 %
    Training batch loss: 2.2920  accuracy: 15.62 %
    Training batch loss: 2.0264  accuracy: 40.62 %
    Training batch loss: 2.0111  accuracy: 43.75 %
    Training batch loss: 2.1631  accuracy: 28.12 %
    Training batch loss: 2.0368  accuracy: 40.62 %
    Training batch loss: 2.0674  accuracy: 37.50 %
    Training batch loss: 2.1024  accuracy: 34.38 %
    Training batch loss: 2.0862  accuracy: 37.50 %
    Training batch loss: 2.1874  accuracy: 25.00 %
    Training batch loss: 2.0876  accuracy: 37.50 %
    Training batch loss: 2.1607  accuracy: 28.12 %
    Training batch loss: 2.0787  accuracy: 34.38 %
    Training batch loss: 1.9753  accuracy: 46.88 %
    Training batch loss: 2.1615  accuracy: 28.12 %
    Training batch loss: 2.0988  accuracy: 34.38 %
    Training batch loss: 2.0993  accuracy: 34.38 %
    Training batch loss: 2.0400  accuracy: 43.75 %
    Training batch loss: 2.0633  accuracy: 40.62 %
    Training batch loss: 2.1326  accuracy: 31.25 %
    Training batch loss: 2.2281  accuracy: 21.88 %
    Training batch loss: 2.2398  accuracy: 18.75 %
    Training batch loss: 2.0978  accuracy: 34.38 %
    Training batch loss: 2.1211  accuracy: 31.25 %
    Training batch loss: 2.0744  accuracy: 37.50 %
    Training batch loss: 2.1427  accuracy: 31.25 %
    Training batch loss: 2.0160  accuracy: 43.75 %
    Training batch loss: 2.0214  accuracy: 43.75 %
    Training batch loss: 2.1627  accuracy: 28.12 %
    Training batch loss: 2.0248  accuracy: 43.75 %
    Training batch loss: 2.1046  accuracy: 34.38 %
    Training batch loss: 2.1243  accuracy: 31.25 %
    Training batch loss: 2.0712  accuracy: 37.50 %
    Training batch loss: 2.0987  accuracy: 34.38 %
    Training batch loss: 2.1058  accuracy: 34.38 %
    Training batch loss: 2.0397  accuracy: 40.62 %
    Training batch loss: 2.0741  accuracy: 37.50 %
    Training batch loss: 2.1667  accuracy: 28.12 %
    Training batch loss: 2.1698  accuracy: 28.12 %
    Training batch loss: 2.0659  accuracy: 37.50 %
    Training batch loss: 2.0883  accuracy: 37.50 %
    Training batch loss: 1.9488  accuracy: 50.00 %
    Training batch loss: 2.0527  accuracy: 40.62 %
    Training batch loss: 2.1200  accuracy: 34.38 %
    Training batch loss: 1.9438  accuracy: 50.00 %
    Training batch loss: 2.1079  accuracy: 34.38 %
    Training batch loss: 2.1230  accuracy: 31.25 %
    Training batch loss: 1.9632  accuracy: 50.00 %
    Training batch loss: 2.0413  accuracy: 40.62 %
    Training batch loss: 2.0020  accuracy: 46.88 %
    Training batch loss: 2.1600  accuracy: 28.12 %
    Training batch loss: 2.0533  accuracy: 40.62 %
    Training batch loss: 2.0755  accuracy: 37.50 %
    Training batch loss: 2.0127  accuracy: 43.75 %
    Training batch loss: 2.0154  accuracy: 43.75 %
    Training batch loss: 2.0094  accuracy: 43.75 %
    Training batch loss: 2.1618  accuracy: 31.25 %
    Training batch loss: 1.9801  accuracy: 46.88 %
    Training batch loss: 2.1379  accuracy: 31.25 %
    Training batch loss: 2.0196  accuracy: 43.75 %
    Training batch loss: 2.0497  accuracy: 40.62 %
    Training batch loss: 2.0615  accuracy: 37.50 %
    Training batch loss: 2.1915  accuracy: 25.00 %
    Training batch loss: 1.9649  accuracy: 50.00 %
    Training batch loss: 2.0461  accuracy: 40.62 %
    Training batch loss: 1.9091  accuracy: 53.12 %
    Training batch loss: 2.0742  accuracy: 37.50 %
    Training batch loss: 2.1275  accuracy: 31.25 %
    Training batch loss: 2.0260  accuracy: 43.75 %
    Training batch loss: 2.1124  accuracy: 34.38 %
    Training batch loss: 2.0417  accuracy: 40.62 %
    Training batch loss: 1.9219  accuracy: 53.12 %
    Training batch loss: 2.0987  accuracy: 37.50 %
    Training batch loss: 2.0369  accuracy: 40.62 %
    Training batch loss: 2.1283  accuracy: 31.25 %
    Training batch loss: 2.1406  accuracy: 31.25 %
    Training batch loss: 2.0127  accuracy: 43.75 %
    Training batch loss: 1.9803  accuracy: 46.88 %
    Training batch loss: 2.0777  accuracy: 37.50 %
    Training batch loss: 2.0080  accuracy: 43.75 %
    Training batch loss: 2.1012  accuracy: 34.38 %
    Training batch loss: 1.9724  accuracy: 50.00 %
    Training batch loss: 2.0657  accuracy: 40.62 %
    Training batch loss: 2.1285  accuracy: 31.25 %
    Training batch loss: 2.0765  accuracy: 37.50 %
    Training batch loss: 2.0174  accuracy: 43.75 %
    Training batch loss: 2.0096  accuracy: 43.75 %
    Training batch loss: 2.0070  accuracy: 43.75 %
    Training batch loss: 2.0794  accuracy: 37.50 %
    Training batch loss: 1.9868  accuracy: 46.88 %
    Training batch loss: 2.2201  accuracy: 21.88 %
    Training batch loss: 2.0193  accuracy: 43.75 %
    Training batch loss: 2.2155  accuracy: 21.88 %
    Training batch loss: 2.1085  accuracy: 34.38 %
    Training batch loss: 2.0522  accuracy: 40.62 %
    Training batch loss: 2.0732  accuracy: 37.50 %
    Training batch loss: 2.2198  accuracy: 21.88 %
    Training batch loss: 2.0132  accuracy: 46.88 %
    Training batch loss: 2.0307  accuracy: 43.75 %
    Training batch loss: 1.9451  accuracy: 53.12 %
    Training batch loss: 1.9961  accuracy: 46.88 %
    Training batch loss: 2.1562  accuracy: 28.12 %
    Training batch loss: 1.9857  accuracy: 46.88 %
    Training batch loss: 2.1133  accuracy: 34.38 %
    Training batch loss: 2.0409  accuracy: 43.75 %
    Training batch loss: 2.0827  accuracy: 34.38 %
    Training batch loss: 2.0802  accuracy: 37.50 %
    Training batch loss: 1.9551  accuracy: 50.00 %
    Training batch loss: 2.1378  accuracy: 31.25 %
    Training batch loss: 2.0014  accuracy: 46.88 %
    Training batch loss: 2.1030  accuracy: 34.38 %
    Training batch loss: 2.1387  accuracy: 31.25 %
    Training batch loss: 2.1280  accuracy: 31.25 %
    Training batch loss: 1.9853  accuracy: 46.88 %
    Training batch loss: 2.0788  accuracy: 37.50 %
    Training batch loss: 2.1131  accuracy: 34.38 %
    Training batch loss: 2.1947  accuracy: 25.00 %
    Training batch loss: 2.1805  accuracy: 28.12 %
    Training batch loss: 2.1323  accuracy: 31.25 %
    Training batch loss: 2.1351  accuracy: 31.25 %
    Training batch loss: 2.0776  accuracy: 37.50 %
    Training batch loss: 2.0697  accuracy: 37.50 %
    Training batch loss: 2.1391  accuracy: 31.25 %
    Training batch loss: 2.1285  accuracy: 31.25 %
    Training batch loss: 2.0773  accuracy: 37.50 %
    Training batch loss: 2.0607  accuracy: 40.62 %
    Training batch loss: 2.1036  accuracy: 34.38 %
    Training batch loss: 2.0398  accuracy: 40.62 %
    Training batch loss: 2.1063  accuracy: 34.38 %
    Training batch loss: 2.0690  accuracy: 37.50 %
    Training batch loss: 2.0748  accuracy: 37.50 %
    Training batch loss: 2.1264  accuracy: 31.25 %
    Training batch loss: 1.9835  accuracy: 46.88 %
    Training batch loss: 2.0418  accuracy: 40.62 %
    Training batch loss: 2.1671  accuracy: 28.12 %
    Training batch loss: 2.0795  accuracy: 37.50 %
    Training batch loss: 2.1592  accuracy: 28.12 %
    Training batch loss: 2.0376  accuracy: 40.62 %
    Training batch loss: 2.1047  accuracy: 34.38 %
    Training batch loss: 2.0648  accuracy: 40.62 %
    Training batch loss: 2.2846  accuracy: 15.62 %
    Training batch loss: 2.1245  accuracy: 31.25 %
    Training batch loss: 2.1086  accuracy: 34.38 %
    Training batch loss: 1.9794  accuracy: 46.88 %
    Training batch loss: 2.0722  accuracy: 37.50 %
    Training batch loss: 2.0380  accuracy: 40.62 %
    Training batch loss: 2.0889  accuracy: 40.62 %
    Training batch loss: 2.2013  accuracy: 25.00 %
    Training batch loss: 2.1795  accuracy: 25.00 %
    Training batch loss: 2.1650  accuracy: 28.12 %
    Training batch loss: 2.1040  accuracy: 34.38 %
    Training batch loss: 2.0077  accuracy: 43.75 %
    Training batch loss: 1.9628  accuracy: 50.00 %
    Training batch loss: 2.0978  accuracy: 34.38 %
    Training batch loss: 2.1089  accuracy: 37.50 %
    Training batch loss: 2.0769  accuracy: 37.50 %
    Training batch loss: 2.1022  accuracy: 34.38 %
    Training batch loss: 2.0736  accuracy: 37.50 %
    Training batch loss: 2.1230  accuracy: 31.25 %
    Training batch loss: 2.0473  accuracy: 40.62 %
    Training batch loss: 2.0340  accuracy: 40.62 %
    Training batch loss: 2.0952  accuracy: 34.38 %
    Training batch loss: 2.1987  accuracy: 25.00 %
    Training batch loss: 2.1432  accuracy: 31.25 %
    Training batch loss: 2.0122  accuracy: 43.75 %
    Training batch loss: 2.1114  accuracy: 31.25 %
    Training batch loss: 2.1586  accuracy: 28.12 %
    Training batch loss: 2.1352  accuracy: 31.25 %
    Training batch loss: 2.1053  accuracy: 34.38 %
    Training batch loss: 2.0180  accuracy: 43.75 %
    Training batch loss: 1.9052  accuracy: 56.25 %
    Training batch loss: 2.2362  accuracy: 21.88 %
    Training batch loss: 1.9247  accuracy: 53.12 %
    Training batch loss: 2.0415  accuracy: 40.62 %
    Training batch loss: 2.0781  accuracy: 37.50 %
    Training batch loss: 2.1256  accuracy: 34.38 %
    Training batch loss: 1.9165  accuracy: 53.12 %
    Training batch loss: 2.0680  accuracy: 37.50 %
    Training batch loss: 2.0474  accuracy: 40.62 %
    Training batch loss: 2.1361  accuracy: 31.25 %
    Training batch loss: 2.1552  accuracy: 28.12 %
    Training batch loss: 1.9337  accuracy: 53.12 %
    Training batch loss: 2.0250  accuracy: 43.75 %
    Training batch loss: 2.0413  accuracy: 40.62 %
    Training batch loss: 1.9791  accuracy: 50.00 %
    Training batch loss: 2.0428  accuracy: 40.62 %
    Training batch loss: 2.0953  accuracy: 34.38 %
    Training batch loss: 2.1369  accuracy: 31.25 %
    Training batch loss: 2.0643  accuracy: 40.62 %
    Training batch loss: 2.0729  accuracy: 37.50 %
    Training batch loss: 2.1012  accuracy: 34.38 %
    Training batch loss: 2.0148  accuracy: 43.75 %
    Training batch loss: 1.9742  accuracy: 46.88 %
    Training batch loss: 2.0477  accuracy: 40.62 %
    Training batch loss: 2.2755  accuracy: 15.62 %
    Training batch loss: 1.9221  accuracy: 53.12 %
    Training batch loss: 2.0626  accuracy: 37.50 %
    Training batch loss: 2.1778  accuracy: 25.00 %
    Training batch loss: 1.8485  accuracy: 62.50 %
    Training batch loss: 1.9658  accuracy: 50.00 %
    Training batch loss: 2.0142  accuracy: 43.75 %
    Training batch loss: 2.0726  accuracy: 37.50 %
    Training batch loss: 2.0515  accuracy: 40.62 %
    Training batch loss: 2.0488  accuracy: 40.62 %
    Training batch loss: 2.1341  accuracy: 31.25 %
    Training batch loss: 1.9572  accuracy: 50.00 %
    Training batch loss: 1.9824  accuracy: 46.88 %
    Training batch loss: 2.1590  accuracy: 28.12 %
    Training batch loss: 2.0657  accuracy: 40.62 %
    Training batch loss: 2.0192  accuracy: 43.75 %
    Training batch loss: 1.9770  accuracy: 50.00 %
    Training batch loss: 2.1951  accuracy: 25.00 %
    Training batch loss: 2.1276  accuracy: 34.38 %
    Training batch loss: 1.9866  accuracy: 43.75 %
    Training batch loss: 2.0335  accuracy: 40.62 %
    Training batch loss: 2.1018  accuracy: 34.38 %
    Training batch loss: 2.1520  accuracy: 28.12 %
    Training batch loss: 2.1538  accuracy: 31.25 %
    Training batch loss: 2.0198  accuracy: 43.75 %
    Training batch loss: 2.1039  accuracy: 37.50 %
    Training batch loss: 2.1623  accuracy: 28.12 %
    Training batch loss: 2.1619  accuracy: 28.12 %
    Training batch loss: 2.1533  accuracy: 28.12 %
    Training batch loss: 1.9267  accuracy: 53.12 %
    Training batch loss: 1.9765  accuracy: 46.88 %
    Training batch loss: 2.1764  accuracy: 28.12 %
    Training batch loss: 2.0649  accuracy: 37.50 %
    Training batch loss: 2.1602  accuracy: 28.12 %
    Training batch loss: 2.0082  accuracy: 43.75 %
    Training batch loss: 1.9541  accuracy: 50.00 %
    Training batch loss: 2.0904  accuracy: 34.38 %
    Training batch loss: 2.1369  accuracy: 31.25 %
    Training batch loss: 2.1708  accuracy: 28.12 %
    Training batch loss: 2.0538  accuracy: 40.62 %
    Training batch loss: 2.0124  accuracy: 43.75 %
    Training batch loss: 2.1297  accuracy: 31.25 %
    Training batch loss: 2.0391  accuracy: 40.62 %
    Training batch loss: 2.1703  accuracy: 28.12 %
    Training batch loss: 1.9547  accuracy: 50.00 %
    Training batch loss: 2.1294  accuracy: 31.25 %
    Training batch loss: 2.1037  accuracy: 34.38 %
    Training batch loss: 2.1197  accuracy: 34.38 %
    Training batch loss: 2.0665  accuracy: 37.50 %
    Training batch loss: 2.1899  accuracy: 25.00 %
    Training batch loss: 2.1636  accuracy: 28.12 %
    Training batch loss: 2.1359  accuracy: 31.25 %
    Training batch loss: 1.9528  accuracy: 50.00 %
    Training batch loss: 2.0461  accuracy: 40.62 %
    Training batch loss: 1.9888  accuracy: 46.88 %
    Training batch loss: 2.1036  accuracy: 34.38 %
    Training batch loss: 2.1723  accuracy: 28.12 %
    Training batch loss: 1.9821  accuracy: 46.88 %
    Training batch loss: 2.0597  accuracy: 37.50 %
    Training batch loss: 2.0067  accuracy: 43.75 %
    Training batch loss: 2.0816  accuracy: 37.50 %
    Training batch loss: 2.0962  accuracy: 34.38 %
    Training batch loss: 2.0101  accuracy: 43.75 %
    Training batch loss: 2.0149  accuracy: 43.75 %
    Training batch loss: 2.0958  accuracy: 34.38 %
    Training batch loss: 2.0330  accuracy: 40.62 %
    Training batch loss: 1.9634  accuracy: 50.00 %
    Training batch loss: 2.0375  accuracy: 40.62 %
    Training batch loss: 1.9787  accuracy: 46.88 %
    Training batch loss: 2.1140  accuracy: 34.38 %
    Training batch loss: 2.1857  accuracy: 25.00 %
    Training batch loss: 1.8850  accuracy: 59.38 %
    Training batch loss: 2.0730  accuracy: 37.50 %
    Training batch loss: 2.1043  accuracy: 34.38 %
    Training batch loss: 1.9962  accuracy: 43.75 %
    Training batch loss: 2.0511  accuracy: 40.62 %
    Training batch loss: 2.0393  accuracy: 40.62 %
    Training batch loss: 2.1096  accuracy: 34.38 %
    Training batch loss: 2.0114  accuracy: 43.75 %
    Training batch loss: 2.2005  accuracy: 25.00 %
    Training batch loss: 2.0404  accuracy: 40.62 %
    Training batch loss: 2.1017  accuracy: 34.38 %
    Training batch loss: 2.1008  accuracy: 34.38 %
    Training batch loss: 2.2226  accuracy: 21.88 %
    Training batch loss: 2.0700  accuracy: 37.50 %
    Training batch loss: 2.0827  accuracy: 37.50 %
    Training batch loss: 2.0539  accuracy: 37.50 %
    Training batch loss: 2.0282  accuracy: 40.62 %
    Training batch loss: 1.9891  accuracy: 46.88 %
    Training batch loss: 2.0777  accuracy: 37.50 %
    Training batch loss: 2.1289  accuracy: 31.25 %
    Training batch loss: 2.0998  accuracy: 34.38 %
    Training batch loss: 2.0175  accuracy: 43.75 %
    Training batch loss: 2.0119  accuracy: 43.75 %
    Training batch loss: 2.1270  accuracy: 31.25 %
    Training batch loss: 2.0937  accuracy: 34.38 %
    Training batch loss: 2.2310  accuracy: 21.88 %
    Training batch loss: 2.0416  accuracy: 40.62 %
    Training batch loss: 2.1294  accuracy: 31.25 %
    Training batch loss: 1.9975  accuracy: 43.75 %
    Training batch loss: 2.0876  accuracy: 37.50 %
    Training batch loss: 2.1289  accuracy: 31.25 %
    Training batch loss: 2.0543  accuracy: 37.50 %
    Training batch loss: 2.0126  accuracy: 43.75 %
    Training batch loss: 2.0713  accuracy: 37.50 %
    Training batch loss: 2.0458  accuracy: 40.62 %
    Training batch loss: 2.0260  accuracy: 40.62 %
    Training batch loss: 2.1036  accuracy: 34.38 %
    Training batch loss: 2.2241  accuracy: 21.88 %
    Training batch loss: 1.8853  accuracy: 56.25 %
    Training batch loss: 2.1809  accuracy: 28.12 %
    Training batch loss: 2.1258  accuracy: 31.25 %
    Training batch loss: 1.8782  accuracy: 59.38 %
    Training batch loss: 2.1623  accuracy: 28.12 %
    Training batch loss: 2.1027  accuracy: 34.38 %
    Training batch loss: 2.0263  accuracy: 40.62 %
    Training batch loss: 1.9302  accuracy: 53.12 %
    Training batch loss: 1.9799  accuracy: 50.00 %
    Training batch loss: 1.9462  accuracy: 53.12 %
    Training batch loss: 2.1021  accuracy: 34.38 %
    Training batch loss: 2.0988  accuracy: 34.38 %
    Training batch loss: 2.1766  accuracy: 28.12 %
    Training batch loss: 2.0304  accuracy: 40.62 %
    Training batch loss: 2.0862  accuracy: 37.50 %
    Training batch loss: 2.1056  accuracy: 34.38 %
    Training batch loss: 2.1416  accuracy: 31.25 %
    Training batch loss: 1.9831  accuracy: 46.88 %
    Training batch loss: 2.1543  accuracy: 28.12 %
    Training batch loss: 2.2280  accuracy: 21.88 %
    Training batch loss: 2.0790  accuracy: 37.50 %
    Training batch loss: 2.2317  accuracy: 21.88 %
    Training batch loss: 2.0466  accuracy: 40.62 %
    Training batch loss: 2.1790  accuracy: 28.12 %
    Training batch loss: 2.0161  accuracy: 43.75 %
    Training batch loss: 2.0091  accuracy: 43.75 %
    Training batch loss: 2.0720  accuracy: 37.50 %
    Training batch loss: 1.9664  accuracy: 50.00 %
    Training batch loss: 2.0702  accuracy: 37.50 %
    Training batch loss: 2.0193  accuracy: 43.75 %
    Training batch loss: 2.0637  accuracy: 40.62 %
    Training batch loss: 2.0837  accuracy: 37.50 %
    Training batch loss: 1.9497  accuracy: 53.12 %
    Training batch loss: 2.1731  accuracy: 28.12 %
    Training batch loss: 2.0995  accuracy: 34.38 %
    Training batch loss: 2.0413  accuracy: 40.62 %
    Training batch loss: 2.0836  accuracy: 34.38 %
    Training batch loss: 2.1335  accuracy: 31.25 %
    Training batch loss: 2.0724  accuracy: 37.50 %
    Training batch loss: 2.1102  accuracy: 34.38 %
    Training batch loss: 2.1072  accuracy: 34.38 %
    Training batch loss: 2.1236  accuracy: 31.25 %
    Training batch loss: 1.8977  accuracy: 56.25 %
    Training batch loss: 2.0238  accuracy: 43.75 %
    Training batch loss: 2.2031  accuracy: 25.00 %
    Training batch loss: 1.9624  accuracy: 50.00 %
    Training batch loss: 1.9527  accuracy: 50.00 %
    Training batch loss: 1.9751  accuracy: 46.88 %
    Training batch loss: 2.0901  accuracy: 37.50 %
    Training batch loss: 2.0414  accuracy: 40.62 %
    Training batch loss: 2.1578  accuracy: 28.12 %
    Training batch loss: 2.1573  accuracy: 28.12 %
    Training batch loss: 1.9496  accuracy: 50.00 %
    Training batch loss: 1.9552  accuracy: 50.00 %
    Training batch loss: 1.9769  accuracy: 46.88 %
    Training batch loss: 2.1314  accuracy: 31.25 %
    Training batch loss: 2.1365  accuracy: 31.25 %
    Training batch loss: 2.0577  accuracy: 37.50 %
    Training batch loss: 1.9835  accuracy: 46.88 %
    Training batch loss: 2.1192  accuracy: 31.25 %
    Training batch loss: 1.9965  accuracy: 46.88 %
    Training batch loss: 2.2237  accuracy: 21.88 %
    Training batch loss: 2.1136  accuracy: 34.38 %
    Training batch loss: 2.1319  accuracy: 34.38 %
    Training batch loss: 2.1414  accuracy: 28.12 %
    Training batch loss: 2.0344  accuracy: 40.62 %
    Training batch loss: 1.9898  accuracy: 46.88 %
    Training batch loss: 2.0355  accuracy: 40.62 %
    Training batch loss: 2.0089  accuracy: 43.75 %
    Training batch loss: 2.1468  accuracy: 28.12 %
    Training batch loss: 2.0547  accuracy: 40.62 %
    Training batch loss: 2.0433  accuracy: 40.62 %
    Training batch loss: 2.0583  accuracy: 37.50 %
    Training batch loss: 1.9667  accuracy: 50.00 %
    Training batch loss: 2.1023  accuracy: 34.38 %
    Training batch loss: 2.0097  accuracy: 43.75 %
    Training batch loss: 2.0808  accuracy: 37.50 %
    Training batch loss: 1.9938  accuracy: 43.75 %
    Training batch loss: 2.0507  accuracy: 40.62 %
    Training batch loss: 2.0184  accuracy: 43.75 %
    Training batch loss: 2.2246  accuracy: 21.88 %
    Training batch loss: 2.0364  accuracy: 40.62 %
    Training batch loss: 2.1037  accuracy: 34.38 %
    Training batch loss: 2.1705  accuracy: 28.12 %
    Training batch loss: 2.0442  accuracy: 40.62 %
    Training batch loss: 2.1918  accuracy: 25.00 %
    Training batch loss: 2.0410  accuracy: 40.62 %
    Training batch loss: 2.1851  accuracy: 25.00 %
    Training batch loss: 2.0690  accuracy: 37.50 %
    Training batch loss: 2.1959  accuracy: 25.00 %
    Training batch loss: 2.0686  accuracy: 37.50 %
    Training batch loss: 2.2312  accuracy: 18.75 %
    Training batch loss: 2.0189  accuracy: 43.75 %
    Training batch loss: 2.0840  accuracy: 34.38 %
    Training batch loss: 2.1308  accuracy: 31.25 %
    Training batch loss: 1.9490  accuracy: 50.00 %
    Training batch loss: 2.0489  accuracy: 40.62 %
    Training batch loss: 2.1147  accuracy: 34.38 %
    Training batch loss: 2.0271  accuracy: 40.62 %
    Training batch loss: 2.1675  accuracy: 28.12 %
    Training batch loss: 2.0364  accuracy: 40.62 %
    Training batch loss: 2.0569  accuracy: 40.62 %
    Training batch loss: 2.0254  accuracy: 43.75 %
    Training batch loss: 1.9940  accuracy: 46.88 %
    Training batch loss: 2.0638  accuracy: 40.62 %
    Training batch loss: 2.2532  accuracy: 18.75 %
    Training batch loss: 2.0459  accuracy: 40.62 %
    Training batch loss: 1.9969  accuracy: 46.88 %
    Training batch loss: 2.0903  accuracy: 37.50 %
    Training batch loss: 2.0745  accuracy: 37.50 %
    Training batch loss: 2.0916  accuracy: 34.38 %
    Training batch loss: 2.1559  accuracy: 28.12 %
    Training batch loss: 2.0111  accuracy: 43.75 %
    Training batch loss: 2.1640  accuracy: 28.12 %
    Training batch loss: 1.9562  accuracy: 50.00 %
    Training batch loss: 2.0144  accuracy: 43.75 %
    Training batch loss: 2.1253  accuracy: 31.25 %
    Training batch loss: 2.1558  accuracy: 28.12 %
    Training batch loss: 2.0064  accuracy: 43.75 %
    Training batch loss: 2.1702  accuracy: 28.12 %
    Training batch loss: 2.0115  accuracy: 43.75 %
    Training batch loss: 2.0398  accuracy: 40.62 %
    Training batch loss: 2.1302  accuracy: 31.25 %
    Training batch loss: 2.1037  accuracy: 34.38 %
    Training batch loss: 2.1439  accuracy: 31.25 %
    Training batch loss: 2.0506  accuracy: 40.62 %
    Training batch loss: 2.0825  accuracy: 37.50 %
    Training batch loss: 2.1339  accuracy: 31.25 %
    Training batch loss: 2.1979  accuracy: 25.00 %
    Training batch loss: 2.1020  accuracy: 34.38 %
    Training batch loss: 2.1523  accuracy: 28.12 %
    Training batch loss: 2.0825  accuracy: 37.50 %
    Training batch loss: 2.0765  accuracy: 37.50 %
    Training batch loss: 2.0448  accuracy: 40.62 %
    Training batch loss: 1.8851  accuracy: 56.25 %
    Training batch loss: 2.1711  accuracy: 28.12 %
    Training batch loss: 2.0246  accuracy: 43.75 %
    Training batch loss: 2.1291  accuracy: 31.25 %
    Training batch loss: 2.2031  accuracy: 25.00 %
    Training batch loss: 2.0752  accuracy: 37.50 %
    Training batch loss: 2.1673  accuracy: 28.12 %
    Training batch loss: 2.0846  accuracy: 37.50 %
    Training batch loss: 2.0938  accuracy: 34.38 %
    Training batch loss: 2.1364  accuracy: 31.25 %
    Training batch loss: 2.1068  accuracy: 34.38 %
    Training batch loss: 2.0765  accuracy: 37.50 %
    Training batch loss: 2.0080  accuracy: 43.75 %
    Training batch loss: 2.1410  accuracy: 31.25 %
    Training batch loss: 2.1479  accuracy: 28.12 %
    Training batch loss: 1.9508  accuracy: 50.00 %
    Training batch loss: 2.1023  accuracy: 34.38 %
    Training batch loss: 2.1935  accuracy: 25.00 %
    Training batch loss: 1.9950  accuracy: 46.88 %
    Training batch loss: 2.0672  accuracy: 37.50 %
    Training batch loss: 2.1342  accuracy: 31.25 %
    Training batch loss: 2.0761  accuracy: 37.50 %
    Training batch loss: 2.2183  accuracy: 21.88 %
    Training batch loss: 2.0132  accuracy: 43.75 %
    Training batch loss: 2.1448  accuracy: 28.12 %
    Training batch loss: 2.0744  accuracy: 37.50 %
    Training batch loss: 2.0967  accuracy: 34.38 %
    Training batch loss: 2.1014  accuracy: 34.38 %
    Training batch loss: 2.0552  accuracy: 40.62 %
    Training batch loss: 2.0653  accuracy: 37.50 %
    Training batch loss: 2.1540  accuracy: 31.25 %
    Training batch loss: 2.1939  accuracy: 25.00 %
    Training batch loss: 2.1304  accuracy: 31.25 %
    Training batch loss: 1.9839  accuracy: 46.88 %
    Training batch loss: 1.8914  accuracy: 56.25 %
    Training batch loss: 1.9782  accuracy: 46.88 %
    Training batch loss: 2.0508  accuracy: 40.62 %
    Training batch loss: 2.0718  accuracy: 37.50 %
    Training batch loss: 2.0170  accuracy: 43.75 %
    Training batch loss: 2.0085  accuracy: 43.75 %
    Training batch loss: 2.0838  accuracy: 34.38 %
    Training batch loss: 2.0372  accuracy: 40.62 %
    Training batch loss: 2.0713  accuracy: 37.50 %
    Training batch loss: 2.0915  accuracy: 37.50 %
    Training batch loss: 1.9899  accuracy: 46.88 %
    Training batch loss: 2.0430  accuracy: 40.62 %
    Training batch loss: 2.0652  accuracy: 37.50 %
    Training batch loss: 2.1600  accuracy: 28.12 %
    Training batch loss: 2.0714  accuracy: 37.50 %
    Training batch loss: 2.1603  accuracy: 28.12 %
    Training batch loss: 2.0996  accuracy: 34.38 %
    Training batch loss: 2.1181  accuracy: 34.38 %
    Training batch loss: 1.8926  accuracy: 56.25 %
    Training batch loss: 1.9795  accuracy: 46.88 %
    Training batch loss: 2.1321  accuracy: 31.25 %
    Training batch loss: 2.0530  accuracy: 40.62 %
    Training batch loss: 2.0985  accuracy: 34.38 %
    Training batch loss: 1.9462  accuracy: 53.12 %
    Training batch loss: 1.9999  accuracy: 43.75 %
    Training batch loss: 2.0700  accuracy: 37.50 %
    Training batch loss: 2.0088  accuracy: 43.75 %
    Training batch loss: 2.0855  accuracy: 37.50 %
    Training batch loss: 1.9935  accuracy: 43.75 %
    Training batch loss: 2.1943  accuracy: 25.00 %
    Training batch loss: 2.1267  accuracy: 31.25 %
    Training batch loss: 1.9456  accuracy: 50.00 %
    Training batch loss: 2.2233  accuracy: 21.88 %
    Training batch loss: 1.9566  accuracy: 50.00 %
    Training batch loss: 1.9760  accuracy: 50.00 %
    Training batch loss: 1.9798  accuracy: 46.88 %
    Training batch loss: 2.0845  accuracy: 37.50 %
    Training batch loss: 2.0692  accuracy: 37.50 %
    Training batch loss: 2.2387  accuracy: 21.88 %
    Training batch loss: 2.1617  accuracy: 28.12 %
    Training batch loss: 2.2478  accuracy: 18.75 %
    Training batch loss: 2.1269  accuracy: 31.25 %
    Training batch loss: 2.0028  accuracy: 43.75 %
    Training batch loss: 2.2007  accuracy: 25.00 %
    Training batch loss: 1.8662  accuracy: 59.38 %
    Training batch loss: 2.1556  accuracy: 28.12 %
    Training batch loss: 2.1303  accuracy: 31.25 %
    Training batch loss: 1.9548  accuracy: 50.00 %
    Training batch loss: 2.0171  accuracy: 43.75 %
    Training batch loss: 2.0515  accuracy: 40.62 %
    Training batch loss: 2.0981  accuracy: 34.38 %
    Training batch loss: 2.1107  accuracy: 34.38 %
    Training batch loss: 2.1446  accuracy: 28.12 %
    Training batch loss: 2.0417  accuracy: 40.62 %
    Training batch loss: 2.0608  accuracy: 40.62 %
    Training batch loss: 2.0107  accuracy: 43.75 %
    Training batch loss: 2.0840  accuracy: 34.38 %
    Training batch loss: 2.0110  accuracy: 43.75 %
    Training batch loss: 2.1572  accuracy: 31.25 %
    Training batch loss: 2.0108  accuracy: 43.75 %
    Training batch loss: 2.1342  accuracy: 31.25 %
    Training batch loss: 2.0199  accuracy: 43.75 %
    Training batch loss: 1.9785  accuracy: 46.88 %
    Training batch loss: 2.0712  accuracy: 37.50 %
    Training batch loss: 2.1476  accuracy: 31.25 %
    Training batch loss: 1.9600  accuracy: 50.00 %
    Training batch loss: 1.9625  accuracy: 50.00 %
    Training batch loss: 2.0599  accuracy: 40.62 %
    Training batch loss: 1.9409  accuracy: 53.12 %
    Training batch loss: 1.9200  accuracy: 53.12 %
    Training batch loss: 2.1640  accuracy: 28.12 %
    Training batch loss: 2.2021  accuracy: 25.00 %
    Training batch loss: 2.0864  accuracy: 37.50 %
    Training batch loss: 2.1339  accuracy: 31.25 %
    Training batch loss: 2.1875  accuracy: 25.00 %
    Training batch loss: 2.2457  accuracy: 18.75 %
    Training batch loss: 1.9742  accuracy: 46.88 %
    Training batch loss: 2.1799  accuracy: 25.00 %
    Training batch loss: 2.0911  accuracy: 37.50 %
    Training batch loss: 2.1913  accuracy: 25.00 %
    Training batch loss: 2.0122  accuracy: 43.75 %
    Training batch loss: 2.0156  accuracy: 43.75 %
    Training batch loss: 2.0702  accuracy: 37.50 %
    Training batch loss: 2.0753  accuracy: 37.50 %
    Training batch loss: 2.0138  accuracy: 43.75 %
    Training batch loss: 2.0850  accuracy: 37.50 %
    Training batch loss: 1.9779  accuracy: 46.88 %
    Training batch loss: 1.9959  accuracy: 46.88 %
    Training batch loss: 2.1029  accuracy: 34.38 %
    Training batch loss: 2.1350  accuracy: 31.25 %
    Training batch loss: 2.1258  accuracy: 31.25 %
    Training batch loss: 2.0487  accuracy: 40.62 %
    Training batch loss: 2.0094  accuracy: 43.75 %
    Training batch loss: 2.0991  accuracy: 34.38 %
    Training batch loss: 2.0753  accuracy: 37.50 %
    Training batch loss: 2.1792  accuracy: 25.00 %
    Training batch loss: 2.1205  accuracy: 34.38 %
    Training batch loss: 2.0614  accuracy: 37.50 %
    Training batch loss: 2.1461  accuracy: 28.12 %
    Training batch loss: 2.1167  accuracy: 34.38 %
    Training batch loss: 1.9561  accuracy: 50.00 %
    Training batch loss: 2.1739  accuracy: 28.12 %
    Training batch loss: 2.1250  accuracy: 31.25 %
    Training batch loss: 2.0017  accuracy: 46.88 %
    Training batch loss: 2.0526  accuracy: 40.62 %
    Training batch loss: 2.0070  accuracy: 43.75 %
    Training batch loss: 1.9541  accuracy: 50.00 %
    Training batch loss: 2.1755  accuracy: 25.00 %
    Training batch loss: 2.1279  accuracy: 31.25 %
    Training batch loss: 1.8929  accuracy: 56.25 %
    Training batch loss: 2.0835  accuracy: 34.38 %
    Training batch loss: 2.0633  accuracy: 37.50 %
    Training batch loss: 2.1050  accuracy: 34.38 %
    Training batch loss: 2.0086  accuracy: 43.75 %
    Training batch loss: 2.1332  accuracy: 31.25 %
    Training batch loss: 2.2004  accuracy: 25.00 %
    Training batch loss: 2.0797  accuracy: 37.50 %
    Training batch loss: 2.0458  accuracy: 40.62 %
    Training batch loss: 1.9991  accuracy: 43.75 %
    Training batch loss: 2.0769  accuracy: 40.62 %
    Training batch loss: 2.2430  accuracy: 18.75 %
    Training batch loss: 2.0725  accuracy: 37.50 %
    Training batch loss: 2.0428  accuracy: 40.62 %
    Training batch loss: 2.2627  accuracy: 18.75 %
    Training batch loss: 2.0348  accuracy: 40.62 %
    Training batch loss: 2.0579  accuracy: 40.62 %
    Training batch loss: 2.1352  accuracy: 31.25 %
    Training batch loss: 2.0105  accuracy: 43.75 %
    Training batch loss: 2.0954  accuracy: 34.38 %
    Training batch loss: 2.0735  accuracy: 37.50 %
    Training batch loss: 2.1921  accuracy: 25.00 %
    Training batch loss: 2.1302  accuracy: 31.25 %
    Training batch loss: 2.0226  accuracy: 43.75 %
    Training batch loss: 2.0325  accuracy: 40.62 %
    Training batch loss: 2.0379  accuracy: 40.62 %
    Training batch loss: 2.1647  accuracy: 28.12 %
    Training batch loss: 2.0695  accuracy: 37.50 %
    Training batch loss: 2.0149  accuracy: 43.75 %
    Training batch loss: 2.0025  accuracy: 46.88 %
    Training batch loss: 1.9877  accuracy: 46.88 %
    Training batch loss: 2.0014  accuracy: 43.75 %
    Training batch loss: 2.0831  accuracy: 37.50 %
    Training batch loss: 2.1359  accuracy: 31.25 %
    Training batch loss: 1.9650  accuracy: 50.00 %
    Training batch loss: 2.1435  accuracy: 28.12 %
    Training batch loss: 2.1628  accuracy: 28.12 %
    Training batch loss: 2.0508  accuracy: 40.62 %
    Training batch loss: 2.1351  accuracy: 31.25 %
    Training batch loss: 2.0252  accuracy: 43.75 %
    Training batch loss: 1.9677  accuracy: 50.00 %
    Training batch loss: 2.0463  accuracy: 40.62 %
    Training batch loss: 2.0451  accuracy: 40.62 %
    Training batch loss: 2.1013  accuracy: 34.38 %
    Training batch loss: 2.1576  accuracy: 28.12 %
    Training batch loss: 2.1322  accuracy: 31.25 %
    Training batch loss: 2.0479  accuracy: 40.62 %
    Training batch loss: 2.1197  accuracy: 34.38 %
    Training batch loss: 2.0553  accuracy: 40.62 %
    Training batch loss: 2.1297  accuracy: 31.25 %
    Training batch loss: 2.1775  accuracy: 28.12 %
    Training batch loss: 2.1244  accuracy: 34.38 %
    Training batch loss: 2.0353  accuracy: 40.62 %
    Training batch loss: 2.1068  accuracy: 34.38 %
    Training batch loss: 2.1093  accuracy: 34.38 %
    Training batch loss: 2.1467  accuracy: 31.25 %
    Training batch loss: 2.1343  accuracy: 31.25 %
    Training batch loss: 2.0590  accuracy: 37.50 %
    Training batch loss: 2.0444  accuracy: 40.62 %
    Training batch loss: 2.1063  accuracy: 34.38 %
    Training batch loss: 2.1310  accuracy: 31.25 %
    Training batch loss: 2.1172  accuracy: 31.25 %
    Training batch loss: 2.1466  accuracy: 31.25 %
    Training batch loss: 2.1668  accuracy: 28.12 %
    Training batch loss: 2.0453  accuracy: 40.62 %
    Training batch loss: 2.0927  accuracy: 34.38 %
    Training batch loss: 2.0716  accuracy: 40.62 %
    Training batch loss: 1.9341  accuracy: 53.12 %
    Training batch loss: 1.8981  accuracy: 53.12 %
    Training batch loss: 2.1313  accuracy: 31.25 %
    Training batch loss: 2.1056  accuracy: 31.25 %
    Training batch loss: 2.1211  accuracy: 31.25 %
    Training batch loss: 2.0330  accuracy: 43.75 %
    Training batch loss: 2.0882  accuracy: 37.50 %
    Training batch loss: 2.2577  accuracy: 18.75 %
    Training batch loss: 2.0099  accuracy: 43.75 %
    Training batch loss: 2.0472  accuracy: 40.62 %
    Training batch loss: 2.0183  accuracy: 43.75 %
    Training batch loss: 2.0950  accuracy: 34.38 %
    Training batch loss: 1.9987  accuracy: 46.88 %
    Training batch loss: 2.0357  accuracy: 40.62 %
    Training batch loss: 1.9944  accuracy: 46.88 %
    Training batch loss: 2.1036  accuracy: 34.38 %
    Training batch loss: 2.1029  accuracy: 34.38 %
    Training batch loss: 2.0692  accuracy: 37.50 %
    Training batch loss: 2.0131  accuracy: 43.75 %
    Training batch loss: 2.0825  accuracy: 37.50 %
    Training batch loss: 2.1355  accuracy: 31.25 %
    Training batch loss: 2.1211  accuracy: 34.38 %
    Training batch loss: 2.1390  accuracy: 31.25 %
    Training batch loss: 1.9542  accuracy: 50.00 %
    Training batch loss: 2.2363  accuracy: 21.88 %
    Training batch loss: 2.0886  accuracy: 34.38 %
    Training batch loss: 2.1055  accuracy: 34.38 %
    Training batch loss: 2.0095  accuracy: 43.75 %
    Training batch loss: 2.1654  accuracy: 28.12 %
    Training batch loss: 2.1595  accuracy: 28.12 %
    Training batch loss: 2.1651  accuracy: 28.12 %
    Training batch loss: 2.1011  accuracy: 34.38 %
    Training batch loss: 2.1085  accuracy: 34.38 %
    Training batch loss: 2.0665  accuracy: 37.50 %
    Training batch loss: 2.0740  accuracy: 37.50 %
    Training batch loss: 2.0818  accuracy: 37.50 %
    Training batch loss: 2.0667  accuracy: 40.62 %
    Training batch loss: 2.1093  accuracy: 34.38 %
    Training batch loss: 2.1485  accuracy: 31.25 %
    Training batch loss: 2.0081  accuracy: 43.75 %
    Training batch loss: 2.1049  accuracy: 37.50 %
    Training batch loss: 2.0124  accuracy: 43.75 %
    Training batch loss: 2.0398  accuracy: 43.75 %
    Training batch loss: 2.1316  accuracy: 31.25 %
    Training batch loss: 2.0007  accuracy: 43.75 %
    Training batch loss: 2.1927  accuracy: 25.00 %
    Training batch loss: 2.0681  accuracy: 37.50 %
    Training batch loss: 2.0759  accuracy: 37.50 %
    Training batch loss: 2.1075  accuracy: 34.38 %
    Training batch loss: 2.1911  accuracy: 25.00 %
    Training batch loss: 2.1663  accuracy: 28.12 %
    Training batch loss: 2.0303  accuracy: 40.62 %
    Training batch loss: 1.9581  accuracy: 50.00 %
    Training batch loss: 2.0727  accuracy: 37.50 %
    Training batch loss: 2.1351  accuracy: 31.25 %
    Training batch loss: 2.2094  accuracy: 21.88 %
    Training batch loss: 2.1121  accuracy: 34.38 %
    Training batch loss: 1.9167  accuracy: 53.12 %
    Training batch loss: 2.1042  accuracy: 34.38 %
    Training batch loss: 1.9459  accuracy: 50.00 %
    Training batch loss: 2.0321  accuracy: 40.62 %
    Training batch loss: 2.0271  accuracy: 43.75 %
    Training batch loss: 1.9336  accuracy: 53.12 %
    Training batch loss: 2.2535  accuracy: 18.75 %
    Training batch loss: 2.1010  accuracy: 34.38 %
    Training batch loss: 1.9770  accuracy: 46.88 %
    Training batch loss: 2.0366  accuracy: 40.62 %
    Training batch loss: 2.1009  accuracy: 34.38 %
    Training batch loss: 2.0111  accuracy: 43.75 %
    Training batch loss: 2.1683  accuracy: 28.12 %
    Training batch loss: 2.1634  accuracy: 28.12 %
    Training batch loss: 2.0066  accuracy: 43.75 %
    Training batch loss: 2.0293  accuracy: 43.75 %
    Training batch loss: 2.0119  accuracy: 43.75 %
    Training batch loss: 2.0059  accuracy: 43.75 %
    Training batch loss: 2.2306  accuracy: 21.88 %
    Training batch loss: 2.0738  accuracy: 37.50 %
    Training batch loss: 2.0773  accuracy: 37.50 %
    Training batch loss: 2.0224  accuracy: 43.75 %
    Training batch loss: 2.0515  accuracy: 40.62 %
    Training batch loss: 1.9968  accuracy: 46.88 %
    Training batch loss: 2.0100  accuracy: 43.75 %
    Training batch loss: 2.1268  accuracy: 31.25 %
    Training batch loss: 2.0692  accuracy: 37.50 %
    Training batch loss: 2.0441  accuracy: 40.62 %
    Training batch loss: 2.1222  accuracy: 34.38 %
    Training batch loss: 2.0347  accuracy: 40.62 %
    Training batch loss: 2.1335  accuracy: 31.25 %
    Training batch loss: 2.0384  accuracy: 40.62 %
    Training batch loss: 2.1112  accuracy: 34.38 %
    Training batch loss: 2.0776  accuracy: 37.50 %
    Training batch loss: 2.0732  accuracy: 37.50 %
    Training batch loss: 1.9814  accuracy: 46.88 %
    Training batch loss: 2.1967  accuracy: 25.00 %
    Training batch loss: 2.0418  accuracy: 40.62 %
    Training batch loss: 2.0226  accuracy: 43.75 %
    Training batch loss: 2.0149  accuracy: 43.75 %
    Training batch loss: 2.0749  accuracy: 37.50 %
    Training batch loss: 2.1038  accuracy: 34.38 %
    Training batch loss: 2.0157  accuracy: 43.75 %
    Training batch loss: 2.1566  accuracy: 28.12 %
    Training batch loss: 2.0123  accuracy: 43.75 %
    Training batch loss: 1.9809  accuracy: 46.88 %
    Training batch loss: 2.0329  accuracy: 40.62 %
    Training batch loss: 2.0710  accuracy: 37.50 %
    Training batch loss: 1.9175  accuracy: 53.12 %
    Training batch loss: 2.0118  accuracy: 43.75 %
    Training batch loss: 2.0402  accuracy: 40.62 %
    Training batch loss: 2.0212  accuracy: 43.75 %
    Training batch loss: 2.1979  accuracy: 25.00 %
    Training batch loss: 2.1622  accuracy: 28.12 %
    Training batch loss: 2.0078  accuracy: 43.75 %
    Training batch loss: 2.0955  accuracy: 34.38 %
    Training batch loss: 1.9832  accuracy: 46.88 %
    Training batch loss: 1.9644  accuracy: 50.00 %
    Training batch loss: 2.1597  accuracy: 28.12 %
    Training batch loss: 2.0404  accuracy: 40.62 %
    Training batch loss: 2.1114  accuracy: 34.38 %
    Training batch loss: 2.0177  accuracy: 43.75 %
    Training batch loss: 2.1201  accuracy: 31.25 %
    Training batch loss: 2.0179  accuracy: 43.75 %
    Training batch loss: 2.0720  accuracy: 37.50 %
    Training batch loss: 2.1148  accuracy: 34.38 %
    Training batch loss: 2.1338  accuracy: 31.25 %
    Training batch loss: 2.0735  accuracy: 37.50 %
    Training batch loss: 2.1624  accuracy: 28.12 %
    Training batch loss: 2.1009  accuracy: 34.38 %
    Training batch loss: 2.1220  accuracy: 31.25 %
    Training batch loss: 2.1068  accuracy: 34.38 %
    Training batch loss: 2.0107  accuracy: 43.75 %
    Training batch loss: 2.0572  accuracy: 40.62 %
    Training batch loss: 2.1913  accuracy: 25.00 %
    Training batch loss: 2.0804  accuracy: 37.50 %
    Training batch loss: 2.0871  accuracy: 37.50 %
    Training batch loss: 2.0151  accuracy: 43.75 %
    Training batch loss: 2.1806  accuracy: 25.00 %
    Training batch loss: 2.1334  accuracy: 31.25 %
    Training batch loss: 1.9183  accuracy: 53.12 %
    Training batch loss: 2.1352  accuracy: 31.25 %
    Training batch loss: 2.1442  accuracy: 31.25 %
    Training batch loss: 1.9809  accuracy: 46.88 %
    Training batch loss: 2.0144  accuracy: 43.75 %
    Training batch loss: 1.9901  accuracy: 46.88 %
    Training batch loss: 2.1753  accuracy: 28.12 %
    Training batch loss: 2.1395  accuracy: 31.25 %
    Training batch loss: 2.0409  accuracy: 40.62 %
    Training batch loss: 2.0681  accuracy: 37.50 %
    Training batch loss: 1.9581  accuracy: 50.00 %
    Training batch loss: 2.0350  accuracy: 40.62 %
    Training batch loss: 1.8735  accuracy: 59.38 %
    Training batch loss: 2.0368  accuracy: 40.62 %
    Training batch loss: 1.9055  accuracy: 56.25 %
    Training batch loss: 2.1295  accuracy: 31.25 %
    Training batch loss: 2.0661  accuracy: 37.50 %
    Training batch loss: 1.9570  accuracy: 50.00 %
    Training batch loss: 2.0980  accuracy: 34.38 %
    Training batch loss: 2.1936  accuracy: 25.00 %
    Training batch loss: 2.0228  accuracy: 43.75 %
    Training batch loss: 2.1831  accuracy: 25.00 %
    Training batch loss: 2.1022  accuracy: 34.38 %
    Training batch loss: 2.0500  accuracy: 40.62 %
    Training batch loss: 2.0387  accuracy: 40.62 %
    Training batch loss: 2.0278  accuracy: 43.75 %
    Training batch loss: 2.1711  accuracy: 28.12 %
    Training batch loss: 2.0964  accuracy: 34.38 %
    Training batch loss: 2.0363  accuracy: 40.62 %
    Training batch loss: 2.1551  accuracy: 28.12 %
    Training batch loss: 2.2151  accuracy: 21.88 %
    Training batch loss: 2.2248  accuracy: 21.88 %
    Training batch loss: 2.1582  accuracy: 28.12 %
    Training batch loss: 2.0094  accuracy: 43.75 %
    Training batch loss: 2.0576  accuracy: 40.62 %
    Training batch loss: 2.2541  accuracy: 18.75 %
    Training batch loss: 2.0879  accuracy: 37.50 %
    Training batch loss: 2.0146  accuracy: 43.75 %
    Training batch loss: 1.9915  accuracy: 46.88 %
    Training batch loss: 2.0087  accuracy: 43.75 %
    Training batch loss: 2.0313  accuracy: 40.62 %
    Training batch loss: 2.0960  accuracy: 34.38 %
    Training batch loss: 2.0786  accuracy: 37.50 %
    Training batch loss: 2.0527  accuracy: 40.62 %
    Training batch loss: 2.0025  accuracy: 43.75 %
    Training batch loss: 2.0605  accuracy: 40.62 %
    Training batch loss: 2.0484  accuracy: 40.62 %
    Training batch loss: 2.0766  accuracy: 37.50 %
    Training batch loss: 2.0657  accuracy: 37.50 %
    Training batch loss: 2.1009  accuracy: 34.38 %
    Training batch loss: 2.0862  accuracy: 37.50 %
    Training batch loss: 2.1845  accuracy: 28.12 %
    Training batch loss: 2.0527  accuracy: 40.62 %
    Training batch loss: 2.0799  accuracy: 37.50 %
    Training batch loss: 2.2171  accuracy: 21.88 %
    Training batch loss: 1.9216  accuracy: 50.00 %
    Training batch loss: 2.1368  accuracy: 31.25 %
    Training batch loss: 2.0642  accuracy: 37.50 %
    Training batch loss: 1.8953  accuracy: 56.25 %
    Training batch loss: 2.1046  accuracy: 34.38 %
    Training batch loss: 2.1390  accuracy: 31.25 %
    Training batch loss: 2.1612  accuracy: 28.12 %
    Training batch loss: 2.0688  accuracy: 37.50 %
    Training batch loss: 2.0387  accuracy: 43.75 %
    Training batch loss: 2.1424  accuracy: 31.25 %
    Training batch loss: 2.1514  accuracy: 31.25 %
    Training batch loss: 2.0124  accuracy: 43.75 %
    Training batch loss: 2.0209  accuracy: 43.75 %
    Training batch loss: 2.1332  accuracy: 31.25 %
    Training batch loss: 2.1514  accuracy: 31.25 %
    Training batch loss: 2.2033  accuracy: 25.00 %
    Training batch loss: 2.0421  accuracy: 40.62 %
    Training batch loss: 2.0013  accuracy: 43.75 %
    Training batch loss: 2.1461  accuracy: 28.12 %
    Training batch loss: 1.9769  accuracy: 46.88 %
    Training batch loss: 2.1031  accuracy: 34.38 %
    Training batch loss: 2.1356  accuracy: 31.25 %
    Training batch loss: 2.0700  accuracy: 40.62 %
    Training batch loss: 2.0680  accuracy: 37.50 %
    Training batch loss: 2.0690  accuracy: 37.50 %
    Training batch loss: 2.0373  accuracy: 40.62 %
    Training batch loss: 2.1159  accuracy: 34.38 %
    Training batch loss: 2.0902  accuracy: 37.50 %
    Training batch loss: 2.0633  accuracy: 37.50 %
    Training batch loss: 2.0846  accuracy: 37.50 %
    Training batch loss: 2.1429  accuracy: 31.25 %
    Training batch loss: 2.1582  accuracy: 28.12 %
    Training batch loss: 1.9318  accuracy: 53.12 %
    Training batch loss: 2.0995  accuracy: 34.38 %
    Training batch loss: 2.1284  accuracy: 31.25 %
    Training batch loss: 2.0442  accuracy: 40.62 %
    Training batch loss: 2.1135  accuracy: 34.38 %
    Training batch loss: 2.1201  accuracy: 31.25 %
    Training batch loss: 2.1306  accuracy: 31.25 %
    Training batch loss: 2.1835  accuracy: 25.00 %
    Training batch loss: 2.0505  accuracy: 40.62 %
    Training batch loss: 2.1587  accuracy: 28.12 %
    Training batch loss: 2.1196  accuracy: 31.25 %
    Training batch loss: 2.0775  accuracy: 37.50 %
    Training batch loss: 1.9901  accuracy: 46.88 %
    Training batch loss: 2.0407  accuracy: 40.62 %
    Training batch loss: 2.1549  accuracy: 28.12 %
    Training batch loss: 2.1537  accuracy: 31.25 %
    Training batch loss: 2.1087  accuracy: 34.38 %
    Training batch loss: 2.0684  accuracy: 37.50 %
    Training batch loss: 2.0556  accuracy: 37.50 %
    Training batch loss: 2.0162  accuracy: 43.75 %
    Training batch loss: 2.2166  accuracy: 21.88 %
    Training batch loss: 2.1609  accuracy: 28.12 %
    Training batch loss: 2.2166  accuracy: 21.88 %
    Training batch loss: 2.0373  accuracy: 40.62 %
    Training batch loss: 2.0475  accuracy: 40.62 %
    Training batch loss: 2.1721  accuracy: 28.12 %
    Training batch loss: 2.1173  accuracy: 31.25 %
    Training batch loss: 2.0799  accuracy: 37.50 %
    Training batch loss: 2.0007  accuracy: 43.75 %
    Training batch loss: 1.9555  accuracy: 50.00 %
    Training batch loss: 2.1364  accuracy: 31.25 %
    Training batch loss: 2.0728  accuracy: 37.50 %
    Training batch loss: 2.1351  accuracy: 31.25 %
    Training batch loss: 2.1045  accuracy: 34.38 %
    Training batch loss: 2.0725  accuracy: 37.50 %
    Training batch loss: 2.0683  accuracy: 37.50 %
    Training batch loss: 2.0396  accuracy: 43.75 %
    Training batch loss: 2.1540  accuracy: 28.12 %
    Training batch loss: 1.9787  accuracy: 46.88 %
    Training batch loss: 2.0962  accuracy: 34.38 %
    Training batch loss: 2.0294  accuracy: 43.75 %
    Training batch loss: 2.0224  accuracy: 43.75 %
    Training batch loss: 2.0958  accuracy: 37.50 %
    Training batch loss: 1.9514  accuracy: 50.00 %
    Training batch loss: 2.0450  accuracy: 40.62 %
    Training batch loss: 2.0220  accuracy: 43.75 %
    Training batch loss: 1.9647  accuracy: 46.88 %
    Training batch loss: 2.0928  accuracy: 37.50 %
    Training batch loss: 2.1290  accuracy: 34.38 %
    Training batch loss: 2.0989  accuracy: 34.38 %
    Training batch loss: 2.2375  accuracy: 21.88 %
    Training batch loss: 2.1223  accuracy: 31.25 %
    Training batch loss: 2.1641  accuracy: 28.12 %
    Training batch loss: 1.9087  accuracy: 53.12 %
    Training batch loss: 2.2862  accuracy: 15.62 %
    Training batch loss: 2.1926  accuracy: 25.00 %
    Training batch loss: 2.1169  accuracy: 34.38 %
    Training batch loss: 2.0998  accuracy: 34.38 %
    Training batch loss: 2.0558  accuracy: 40.62 %
    Training batch loss: 2.0202  accuracy: 43.75 %
    Training batch loss: 2.0670  accuracy: 37.50 %
    Training batch loss: 2.0439  accuracy: 40.62 %
    Training batch loss: 2.0967  accuracy: 34.38 %
    Training batch loss: 2.1906  accuracy: 25.00 %
    Training batch loss: 2.1278  accuracy: 31.25 %
    Training batch loss: 2.1317  accuracy: 31.25 %
    Training batch loss: 2.2461  accuracy: 18.75 %
    Training batch loss: 2.1004  accuracy: 34.38 %
    Training batch loss: 2.2236  accuracy: 21.88 %
    Training batch loss: 1.9692  accuracy: 50.00 %
    Training batch loss: 2.0770  accuracy: 37.50 %
    Training batch loss: 2.2198  accuracy: 21.88 %
    Training batch loss: 2.0100  accuracy: 43.75 %
    Training batch loss: 2.1442  accuracy: 31.25 %
    Training batch loss: 2.0377  accuracy: 40.62 %
    Training batch loss: 2.0051  accuracy: 43.75 %
    Training batch loss: 2.0715  accuracy: 37.50 %
    Training batch loss: 2.1159  accuracy: 34.38 %
    Training batch loss: 2.0576  accuracy: 40.62 %
    Training batch loss: 2.0720  accuracy: 37.50 %
    Training batch loss: 2.1271  accuracy: 34.38 %
    Training batch loss: 2.0321  accuracy: 43.75 %
    Training batch loss: 2.1991  accuracy: 25.00 %
    Training batch loss: 1.9708  accuracy: 46.88 %
    Training batch loss: 2.0319  accuracy: 40.62 %
    Training batch loss: 2.0774  accuracy: 37.50 %
    Training batch loss: 2.1145  accuracy: 34.38 %
    Training batch loss: 2.0164  accuracy: 43.75 %
    Training batch loss: 2.0388  accuracy: 40.62 %
    Training batch loss: 1.9320  accuracy: 53.12 %
    Training batch loss: 2.1437  accuracy: 28.12 %
    Training batch loss: 2.0725  accuracy: 37.50 %
    Training batch loss: 2.1244  accuracy: 31.25 %
    Training batch loss: 2.1340  accuracy: 31.25 %
    Training batch loss: 2.0037  accuracy: 43.75 %
    Training batch loss: 2.0759  accuracy: 37.50 %
    Training batch loss: 2.0357  accuracy: 40.62 %
    Training batch loss: 2.0320  accuracy: 40.62 %
    Training batch loss: 2.0740  accuracy: 37.50 %
    Training batch loss: 2.0448  accuracy: 40.62 %
    Training batch loss: 2.2488  accuracy: 18.75 %
    Training batch loss: 2.1078  accuracy: 34.38 %
    Training batch loss: 2.2834  accuracy: 15.62 %
    Training batch loss: 2.1092  accuracy: 34.38 %
    Training batch loss: 2.1449  accuracy: 28.12 %
    Training batch loss: 2.0652  accuracy: 37.50 %
    Training batch loss: 2.0980  accuracy: 37.50 %
    Training batch loss: 2.0180  accuracy: 43.75 %
    Training batch loss: 2.1399  accuracy: 31.25 %
    Training batch loss: 2.0479  accuracy: 40.62 %
    Training batch loss: 2.2460  accuracy: 18.75 %
    Training batch loss: 2.0788  accuracy: 37.50 %
    Training batch loss: 1.9978  accuracy: 46.88 %
    Training batch loss: 2.0746  accuracy: 37.50 %
    Training batch loss: 2.0593  accuracy: 40.62 %
    Training batch loss: 2.0434  accuracy: 40.62 %
    Training batch loss: 2.0968  accuracy: 34.38 %
    Training batch loss: 2.1478  accuracy: 28.12 %
    Training batch loss: 2.0410  accuracy: 40.62 %
    Training batch loss: 2.1015  accuracy: 34.38 %
    Training batch loss: 2.0467  accuracy: 40.62 %
    Training batch loss: 2.0485  accuracy: 40.62 %
    Training batch loss: 2.0743  accuracy: 37.50 %
    Training batch loss: 2.0821  accuracy: 37.50 %
    Training batch loss: 2.0629  accuracy: 40.62 %
    Training batch loss: 1.9394  accuracy: 53.12 %
    Training batch loss: 2.1332  accuracy: 31.25 %
    Training batch loss: 2.0737  accuracy: 37.50 %
    Training batch loss: 2.0156  accuracy: 43.75 %
    Training batch loss: 2.0350  accuracy: 40.62 %
    Training batch loss: 2.2202  accuracy: 21.88 %
    Training batch loss: 1.9507  accuracy: 50.00 %
    Training batch loss: 2.1012  accuracy: 34.38 %
    Training batch loss: 2.1437  accuracy: 31.25 %
    Training batch loss: 2.1583  accuracy: 28.12 %
    Training batch loss: 2.1067  accuracy: 34.38 %
    Training batch loss: 2.1310  accuracy: 31.25 %
    Training batch loss: 1.9812  accuracy: 46.88 %
    Training batch loss: 1.8853  accuracy: 59.38 %
    Training batch loss: 1.8415  accuracy: 62.50 %
    Training batch loss: 2.0407  accuracy: 40.62 %
    Training batch loss: 2.1476  accuracy: 31.25 %
    Training batch loss: 2.0315  accuracy: 40.62 %
    Training batch loss: 2.0688  accuracy: 37.50 %
    Training batch loss: 2.1313  accuracy: 34.38 %
    Training batch loss: 2.0811  accuracy: 37.50 %
    Training batch loss: 2.2562  accuracy: 18.75 %
    Training batch loss: 2.2227  accuracy: 21.88 %
    Training batch loss: 1.9867  accuracy: 46.88 %
    Training batch loss: 2.2230  accuracy: 21.88 %
    Training batch loss: 2.0610  accuracy: 40.62 %
    Training batch loss: 1.9608  accuracy: 50.00 %
    Training batch loss: 2.0099  accuracy: 43.75 %
    Training batch loss: 2.1268  accuracy: 31.25 %
    Training batch loss: 1.9842  accuracy: 46.88 %
    Training batch loss: 2.0595  accuracy: 37.50 %
    Training batch loss: 1.9552  accuracy: 50.00 %
    Training batch loss: 2.1240  accuracy: 34.38 %
    Training batch loss: 2.0132  accuracy: 43.75 %
    Training batch loss: 2.0445  accuracy: 40.62 %
    Training batch loss: 1.9467  accuracy: 50.00 %
    Training batch loss: 2.2126  accuracy: 21.88 %
    Training batch loss: 2.0655  accuracy: 37.50 %
    Training batch loss: 2.1521  accuracy: 28.12 %
    Training batch loss: 2.1384  accuracy: 31.25 %
    Training batch loss: 2.0425  accuracy: 40.62 %
    Training batch loss: 2.0795  accuracy: 37.50 %
    Training batch loss: 1.9787  accuracy: 46.88 %
    Training batch loss: 2.1282  accuracy: 31.25 %
    Training batch loss: 1.9231  accuracy: 53.12 %
    Training batch loss: 2.0747  accuracy: 37.50 %
    Training batch loss: 2.0684  accuracy: 37.50 %
    Training batch loss: 2.0983  accuracy: 34.38 %
    Training batch loss: 2.1952  accuracy: 25.00 %
    Training batch loss: 2.1058  accuracy: 31.25 %
    Training batch loss: 2.1039  accuracy: 34.38 %
    Training batch loss: 2.0091  accuracy: 43.75 %
    Training batch loss: 2.0503  accuracy: 40.62 %
    Training batch loss: 2.1361  accuracy: 31.25 %
    Training batch loss: 2.1156  accuracy: 34.38 %
    Training batch loss: 1.9930  accuracy: 46.88 %
    Training batch loss: 2.2080  accuracy: 21.88 %
    Training batch loss: 2.1040  accuracy: 34.38 %
    Training batch loss: 2.0366  accuracy: 40.62 %
    Training batch loss: 2.1728  accuracy: 28.12 %
    Training batch loss: 2.1473  accuracy: 28.12 %
    Training batch loss: 2.2223  accuracy: 21.88 %
    Training batch loss: 1.8663  accuracy: 59.38 %
    Training batch loss: 2.1621  accuracy: 28.12 %
    Training batch loss: 2.1018  accuracy: 34.38 %
    Training batch loss: 1.9827  accuracy: 46.88 %
    Training batch loss: 2.1300  accuracy: 31.25 %
    Training batch loss: 1.9878  accuracy: 46.88 %
    Training batch loss: 2.0008  accuracy: 43.75 %
    Training batch loss: 1.9874  accuracy: 46.88 %
    Training batch loss: 2.0595  accuracy: 37.50 %
    Training batch loss: 2.1266  accuracy: 31.25 %
    Training batch loss: 2.1287  accuracy: 31.25 %
    Training batch loss: 2.0423  accuracy: 40.62 %
    Training batch loss: 2.1770  accuracy: 28.12 %
    Training batch loss: 2.2224  accuracy: 21.88 %
    Training batch loss: 2.0101  accuracy: 43.75 %
    Training batch loss: 2.0858  accuracy: 37.50 %
    Training batch loss: 2.1829  accuracy: 25.00 %
    Training batch loss: 2.1120  accuracy: 34.38 %
    Training batch loss: 1.9812  accuracy: 46.88 %
    Training batch loss: 2.0761  accuracy: 37.50 %
    Training batch loss: 1.9203  accuracy: 53.12 %
    Training batch loss: 2.0808  accuracy: 37.50 %
    Training batch loss: 1.9894  accuracy: 46.88 %
    Training batch loss: 2.0091  accuracy: 43.75 %
    Training batch loss: 2.1303  accuracy: 31.25 %
    Training batch loss: 2.0432  accuracy: 40.62 %
    Training batch loss: 2.0544  accuracy: 40.62 %
    Training batch loss: 2.1239  accuracy: 31.25 %
    Training batch loss: 2.0913  accuracy: 34.38 %
    Training batch loss: 2.0907  accuracy: 34.38 %
    Training batch loss: 1.9971  accuracy: 43.75 %
    Training batch loss: 2.1368  accuracy: 31.25 %
    Training batch loss: 2.0576  accuracy: 37.50 %
    Training batch loss: 2.0471  accuracy: 40.62 %
    Training batch loss: 2.0658  accuracy: 40.62 %
    Training batch loss: 1.9957  accuracy: 46.88 %
    Training batch loss: 2.0113  accuracy: 43.75 %
    Training batch loss: 1.9894  accuracy: 46.88 %
    Training batch loss: 2.1740  accuracy: 25.00 %
    Training batch loss: 1.9555  accuracy: 50.00 %
    Training batch loss: 1.9530  accuracy: 50.00 %
    Training batch loss: 1.9099  accuracy: 53.12 %
    Training batch loss: 2.0140  accuracy: 43.75 %
    Training batch loss: 1.9812  accuracy: 46.88 %
    Training batch loss: 2.1742  accuracy: 28.12 %
    Training batch loss: 2.0693  accuracy: 37.50 %
    Training batch loss: 2.1640  accuracy: 28.12 %
    Training batch loss: 2.0955  accuracy: 34.38 %
    Training batch loss: 2.0717  accuracy: 37.50 %
    Training batch loss: 1.9339  accuracy: 53.12 %
    Training batch loss: 2.0680  accuracy: 37.50 %
    Training batch loss: 2.2217  accuracy: 21.88 %
    Training batch loss: 2.0438  accuracy: 40.62 %
    Training batch loss: 2.0844  accuracy: 37.50 %
    Training batch loss: 2.1670  accuracy: 28.12 %
    Training batch loss: 1.9331  accuracy: 50.00 %
    Training batch loss: 1.9850  accuracy: 46.88 %
    Training batch loss: 2.0509  accuracy: 40.62 %
    Training batch loss: 2.1114  accuracy: 34.38 %
    Training batch loss: 2.1658  accuracy: 28.12 %
    Training batch loss: 2.1806  accuracy: 25.00 %
    Training batch loss: 2.1277  accuracy: 31.25 %
    Training batch loss: 2.0094  accuracy: 43.75 %
    Training batch loss: 2.1329  accuracy: 31.25 %
    Training batch loss: 2.1860  accuracy: 25.00 %
    Training batch loss: 2.1543  accuracy: 28.12 %
    Training batch loss: 2.2494  accuracy: 18.75 %
    Training batch loss: 2.0842  accuracy: 34.38 %
    Training batch loss: 2.1596  accuracy: 28.12 %
    Training batch loss: 2.0361  accuracy: 40.62 %
    Training batch loss: 2.1941  accuracy: 25.00 %
    Training batch loss: 2.1868  accuracy: 25.00 %
    Training batch loss: 2.0285  accuracy: 43.75 %
    Training batch loss: 2.1359  accuracy: 31.25 %
    Training batch loss: 2.0951  accuracy: 34.38 %
    Training batch loss: 2.0731  accuracy: 37.50 %
    Training batch loss: 2.1740  accuracy: 25.00 %
    Training batch loss: 2.1150  accuracy: 34.38 %
    Training batch loss: 2.0636  accuracy: 37.50 %
    Training batch loss: 2.2019  accuracy: 25.00 %
    Training batch loss: 2.0358  accuracy: 40.62 %
    Training batch loss: 2.0297  accuracy: 40.62 %
    Training batch loss: 2.0187  accuracy: 43.75 %
    Training batch loss: 1.9277  accuracy: 53.12 %
    Training batch loss: 2.0457  accuracy: 40.62 %
    Training batch loss: 2.1355  accuracy: 31.25 %
    Training batch loss: 1.9954  accuracy: 46.88 %
    Training batch loss: 2.0999  accuracy: 34.38 %
    Training batch loss: 2.1797  accuracy: 25.00 %
    Training batch loss: 2.1164  accuracy: 34.38 %
    Training batch loss: 1.8614  accuracy: 59.38 %
    Training batch loss: 2.0840  accuracy: 37.50 %
    Training batch loss: 1.9914  accuracy: 46.88 %
    Training batch loss: 1.9768  accuracy: 46.88 %
    Training batch loss: 2.1937  accuracy: 25.00 %
    Training batch loss: 2.0135  accuracy: 43.75 %
    Training batch loss: 2.1351  accuracy: 31.25 %
    Training batch loss: 1.9877  accuracy: 46.88 %
    Training batch loss: 2.0187  accuracy: 43.75 %
    Training batch loss: 2.1004  accuracy: 34.38 %
    Training batch loss: 2.1052  accuracy: 34.38 %
    Training batch loss: 2.0394  accuracy: 40.62 %
    Training batch loss: 2.1329  accuracy: 31.25 %
    Training batch loss: 2.1434  accuracy: 31.25 %
    Training batch loss: 2.0190  accuracy: 40.62 %
    Training batch loss: 1.9908  accuracy: 46.88 %
    Training batch loss: 1.9827  accuracy: 46.88 %
    Training batch loss: 1.9834  accuracy: 46.88 %
    Training batch loss: 2.0714  accuracy: 37.50 %
    Training batch loss: 2.1930  accuracy: 25.00 %
    Training batch loss: 2.0678  accuracy: 37.50 %
    Training batch loss: 2.1367  accuracy: 31.25 %
    Training batch loss: 2.0210  accuracy: 43.75 %
    Training batch loss: 2.1749  accuracy: 25.00 %
    Training batch loss: 2.1381  accuracy: 31.25 %
    Training batch loss: 2.0865  accuracy: 34.38 %
    Training batch loss: 2.1628  accuracy: 28.12 %
:::
:::

::: {.cell .markdown collapsed="false" id="LD7Ls_k6vG8C"}
#Validate results on a validation set
:::

::: {.cell .code execution_count="54" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":3734,\"status\":\"ok\",\"timestamp\":1776335750361,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="YZn7L8asvG8D" outputId="ee23ee27-2c85-4219-e12a-16f7fce2bdf8"}
``` python
with torch.no_grad():
  val_loss = []
  val_corr_pred = []
  for X, y in val_loader:
    X = X.cuda()
    y = y.cuda()

    o = model(X)
    val_loss.append(lossFunction(o, y))
    val_corr_pred.append(o.argmax(-1) == y)

  val_loss = torch.stack(val_loss).mean().item()
  val_accuracy = torch.concatenate(val_corr_pred).float().mean().item()
  print("Validation loss:", val_loss)
  print("Validation accuracy:", val_accuracy)

  val_losses.append(val_loss)
  val_accuracies.append(val_accuracy)
```

::: {.output .stream .stderr}
    /usr/local/lib/python3.12/dist-packages/torch/utils/data/dataloader.py:432: UserWarning: This DataLoader will create 4 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
      self.check_worker_number_rationality()
:::

::: {.output .stream .stdout}
    Validation loss: 2.0781068801879883
    Validation accuracy: 0.36934998631477356
:::
:::

::: {.cell .code execution_count="55" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6,\"status\":\"ok\",\"timestamp\":1776335750378,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="mIDN0SDfvG8D" outputId="8a160487-5760-458d-db21-3db4acad4fdd"}
``` python
print("Validation losses per epoch:", val_losses)
print("Validation accuracies per epoch:", val_accuracies)
```

::: {.output .stream .stdout}
    Validation losses per epoch: [2.0853917598724365, 2.081132650375366, 2.0781068801879883]
    Validation accuracies per epoch: [0.3646000027656555, 0.36739999055862427, 0.36934998631477356]
:::
:::

::: {.cell .markdown collapsed="false" id="cLzGCBfxIXJK"}
Run the training-validation cells multiple time, then run this cell to
plot the validation metrics
:::

::: {.cell .code execution_count="56" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":265}" executionInfo="{\"elapsed\":114,\"status\":\"ok\",\"timestamp\":1776335750492,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="RduvEJBLvG8D" outputId="041f20b0-d12f-418c-c231-b4015941bc52"}
``` python
plt.plot(val_losses)
plt.plot(val_accuracies)
plt.legend(["Loss", "Accuracy"])
plt.xlabel("epoch")
plt.show()
```

::: {.output .display_data}
![](b4f208cc99179e2aff163de7e6c6c63348504c4d.png)
:::
:::

::: {.cell .markdown id="DVhZsg9GXk00"}
#Save the trained model
:::

::: {.cell .code execution_count="51" executionInfo="{\"elapsed\":15,\"status\":\"ok\",\"timestamp\":1776335552077,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="BqgK5ARXoQSU"}
``` python
torch.save(model.state_dict(), 'saved_model.pth')
```
:::

::: {.cell .markdown id="FzqYtZHFovlb"}
#Load a previously trained model
:::

::: {.cell .code execution_count="52" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":32,\"status\":\"ok\",\"timestamp\":1776335552122,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="K4XC27ktXpIz" outputId="d15b0969-c92c-46c9-bb15-459e44188768"}
``` python
model.load_state_dict(torch.load('saved_model.pth'))
```

::: {.output .execute_result execution_count="52"}
    <All keys matched successfully>
:::
:::

::: {.cell .markdown collapsed="false" id="fzZMpE3EvG8G"}
#Exercise 1: put together the code Change the learning rate and the
batch size to ensure a correct loss decrease (not too slow, not too
fast, avoid high learning rate values that make the loss curve noisy).

#Exercise 2: put together the code Perform a K-fold cross validation.
For each fold, implement this algorithm:

1.  train the model for 100 epochs;
2.  save the validation loss and accuracy after each epoch;
3.  save the best model only, i.e. the one reaching the lowest
    validation loss.
4.  stop the training if the loss does not decrease for 5 epochs (early
    stopping)

Thus, compute the average accuracy among the best model trained at each
fold.
:::
