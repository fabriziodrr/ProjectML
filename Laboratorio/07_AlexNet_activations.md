---
jupyter:
  colab:
    authorship_tag: ABX9TyPZiwRHgy6agzjnrQE5/4w7
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="IIZvxE9w2S5h"}
Import modules
:::

::: {.cell .code execution_count="1" executionInfo="{\"elapsed\":7506,\"status\":\"ok\",\"timestamp\":1683715915569,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="VC1kxjqyIVK0"}
``` python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader

import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.utils as utils

import matplotlib.pyplot as plt
```
:::

::: {.cell .markdown id="W_6dgal9zFfL"}
#Download and import the AlexNet pre-trained model Many pre-trained
models are available in the [Pytorch Hub](https://pytorch.org/hub/).

Note that models including layers that act differently during training
and validation/inference phase (e.g., Dropout layers) must be aware of
the phase we are in.

Use the
[.train()](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.train)
and
[.eval()](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.eval)
functions to set the current phase.
:::

::: {.cell .code execution_count="2" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":9616,\"status\":\"ok\",\"timestamp\":1683715925175,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="fQo_JrMXJDeh" outputId="61c33378-5f39-4740-9e7a-440c390ddf59"}
``` python
model = torch.hub.load('pytorch/vision:v0.10.0', 'alexnet', pretrained=True)
model.eval()
```

::: {.output .stream .stderr}
    Downloading: "https://github.com/pytorch/vision/zipball/v0.10.0" to /root/.cache/torch/hub/v0.10.0.zip
    /usr/local/lib/python3.10/dist-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and may be removed in the future, please use 'weights' instead.
      warnings.warn(
    /usr/local/lib/python3.10/dist-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and may be removed in the future. The current behavior is equivalent to passing `weights=AlexNet_Weights.IMAGENET1K_V1`. You can also use `weights=AlexNet_Weights.DEFAULT` to get the most up-to-date weights.
      warnings.warn(msg)
    Downloading: "https://download.pytorch.org/models/alexnet-owt-7be5be79.pth" to /root/.cache/torch/hub/checkpoints/alexnet-owt-7be5be79.pth
    100%|██████████| 233M/233M [00:05<00:00, 48.2MB/s]
:::

::: {.output .execute_result execution_count="2"}
    AlexNet(
      (features): Sequential(
        (0): Conv2d(3, 64, kernel_size=(11, 11), stride=(4, 4), padding=(2, 2))
        (1): ReLU(inplace=True)
        (2): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
        (3): Conv2d(64, 192, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        (4): ReLU(inplace=True)
        (5): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
        (6): Conv2d(192, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (7): ReLU(inplace=True)
        (8): Conv2d(384, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (9): ReLU(inplace=True)
        (10): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (11): ReLU(inplace=True)
        (12): MaxPool2d(kernel_size=3, stride=2, padding=0, dilation=1, ceil_mode=False)
      )
      (avgpool): AdaptiveAvgPool2d(output_size=(6, 6))
      (classifier): Sequential(
        (0): Dropout(p=0.5, inplace=False)
        (1): Linear(in_features=9216, out_features=4096, bias=True)
        (2): ReLU(inplace=True)
        (3): Dropout(p=0.5, inplace=False)
        (4): Linear(in_features=4096, out_features=4096, bias=True)
        (5): ReLU(inplace=True)
        (6): Linear(in_features=4096, out_features=1000, bias=True)
      )
    )
:::
:::

::: {.cell .markdown id="2Pr8TMoG7OeU"}
**Note**: you need to apply the very same image pre-processing used
during the network training. The PyTorch Hub provides the pre-processing
function to use for each pre-trained model.
:::

::: {.cell .code id="PV5Qa6sK6sYM"}
``` python
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```
:::

::: {.cell .markdown id="_1c7WSj56wBs"}
Download the correspondance between last layer neurons and ImageNet
classes
:::

::: {.cell .code id="kSo8loZ86uxc"}
``` python
# Download ImageNet labels
!wget https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
```
:::

::: {.cell .markdown id="eqlqLerlQOBq"}
#Prepare the input image

##Download an example image from the pytorch website
:::

::: {.cell .code id="DeSQyKvCJISi"}
``` python
import urllib
url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
try: urllib.URLopener().retrieve(url, filename)
except: urllib.request.urlretrieve(url, filename)
```
:::

::: {.cell .markdown id="Gcutx-6XQRHJ"}
##Use the Google Colab snippet to acquire from the camera

This code is provided by Google Colaboratory via the code snippets and
allows to acquire an image from your webcam.
:::

::: {.cell .code execution_count="3" executionInfo="{\"elapsed\":9,\"status\":\"ok\",\"timestamp\":1683715925175,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="3o-UtusmOcyw"}
``` python
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
```
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":515}" executionInfo="{\"elapsed\":47046,\"status\":\"ok\",\"timestamp\":1683664861587,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="dqGhNEk9Ocyy" outputId="f287ab8a-a322-43d3-b9ad-a776c98fcc61"}
``` python
from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))
```

::: {.output .display_data}
    <IPython.core.display.Javascript object>
:::

::: {.output .stream .stdout}
    Saved to photo.jpg
:::

::: {.output .display_data}
![](8ca3a5cf32137443831f8333949f804c6c5cbd32.jpg)
:::
:::

::: {.cell .markdown id="oqdekeGxQano"}
#Run the network forward pass

##Compute the top-5 predicted classes

1.  Apply the pre-processing function
2.  Perform the forward pass
3.  Retrieve the top-5 ImageNet classes
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":721}" executionInfo="{\"elapsed\":1314,\"status\":\"ok\",\"timestamp\":1683664870843,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="dj8WNMmzJVSn" outputId="10d6c29b-43f5-4d0e-838d-34149db2a0a5"}
``` python
# sample execution (requires torchvision)
from PIL import Image
from torchvision import transforms
input_image = Image.open(filename)

plt.imshow(input_image)

input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

# move the input and model to GPU for speed if available
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    model.to('cuda')

with torch.no_grad():
    output = model(input_batch)
# Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
probabilities = torch.nn.functional.softmax(output[0], dim=0)

# Read the categories
with open("imagenet_classes.txt", "r") as f:
    categories = [s.strip() for s in f.readlines()]
# Show top categories per image
top5_prob, top5_catid = torch.topk(probabilities, 5)
for i in range(top5_prob.size(0)):
    print(categories[top5_catid[i]], top5_prob[i].item())
```

::: {.output .stream .stdout}
    --2023-05-09 20:41:09--  https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 10472 (10K) [text/plain]
    Saving to: ‘imagenet_classes.txt.3’

    imagenet_classes.tx   0%[                    ]       0  --.-KB/s               imagenet_classes.tx 100%[===================>]  10.23K  --.-KB/s    in 0s      

    2023-05-09 20:41:09 (96.8 MB/s) - ‘imagenet_classes.txt.3’ saved [10472/10472]

    microwave 0.3167443871498108
    entertainment center 0.27593836188316345
    television 0.13045436143875122
    medicine chest 0.04929434135556221
    stove 0.04319416359066963
:::

::: {.output .display_data}
![](8c21970fa99714587cfbfcff541c651307fce582.png)
:::
:::

::: {.cell .markdown id="GpPVNdfBQkNU"}
##Store the activation maps during the forward pass
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":1000}" executionInfo="{\"elapsed\":3445,\"status\":\"ok\",\"timestamp\":1683664896627,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="N7JCRb6dJqbO" outputId="d2da8477-7ba8-48b9-b474-f104748f638c"}
``` python
import torchvision.utils as utils

# Visualize feature maps
activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook

model.features[0].register_forward_hook(get_activation('features[0]'))
model.features[2].register_forward_hook(get_activation('features[2]'))
model.features[5].register_forward_hook(get_activation('features[5]'))
model.features[12].register_forward_hook(get_activation('features[12]'))

with torch.no_grad():
    output = model(input_batch)

for k in activation:
  act = activation[k].squeeze()
  plt.figure(figsize=(10,10))
  plt.imshow(utils.make_grid(act.unsqueeze(1),
                             normalize=True,
                             scale_each=True).numpy().transpose((1,2,0)),
             cmap='jet')
  plt.title(k)
#  fig, axarr = plt.subplots(act.size(0))
#  for idx in range(act.size(0)):
#      axarr[idx].imshow(act[idx])
```

::: {.output .display_data}
![](a2ec0048051292cb1ad5b2332d98668d531818c5.png)
:::

::: {.output .display_data}
![](161a1f3566b885b6bd7eeaa7026a062c29bb0dc4.png)
:::

::: {.output .display_data}
![](ac989f618f50e8e337bfb00215469830ab6842a6.png)
:::

::: {.output .display_data}
![](32353c95a8f01e899e3c48916cee5dd0dd895531.png)
:::
:::
