Connect the Notebook to a Google Drive account

`python
from google.colab import drive
drive.mount('/content/drive')
`

Now go to the appropriate folder on your google drive. Note: you may need to change the folder name, depending on where on your drive you have the data files.

`python
import os
os.chdir('/content/drive/MyDrive/Didattica/ML/Exercises/Exercise05_Pytorch_network_training_and_validation')
`

#Introduction
![image.png](data:image/png;base64,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)

Documentation for [PyTorch](https://pytorch.org/docs/stable/index.html) and [TorchVision](https://pytorch.org/vision/stable/index.html)


`python
import torch
print('PyTorch version:', torch.__version__)
`

`python
import matplotlib.pyplot as plt
def plot_digit(data):
    img, label = data
    img = img.squeeze()   # remove the trailing dimensions for visualization purpose only
    plt.imshow(img, cmap=plt.cm.gray_r)
    plt.title(label)
`

`python
# download and read the training and the test data sets
from torchvision.datasets import MNIST
import torchvision.transforms as T

train_dataset = MNIST(root='./dataset/train/', train=True, download=True, transform=T.Compose([T.RandomApply([T.RandomRotation(10)], p=.5),
                                                                                               T.ToTensor()]))
val_dataset   = MNIST(root='./dataset/train/', train=True, download=False, transform=T.ToTensor())

test_dataset = MNIST(root='./dataset/test/', train=False, download=True, transform=T.ToTensor())

# input image dimensions
train_imgs, img_rows, img_cols = train_dataset.data.shape
test_imgs = len(test_dataset)
num_classes = 10
`

`python
K = 10
indexes = torch.randperm(len(train_dataset)) % K
torch.save(indexes, "cross-val-indexes.pt")
`

`python
indexes
`

`python
(indexes==0).nonzero().shape
`

`python
(indexes==0).nonzero().squeeze()
`

`python
from torch.utils.data import Subset, DataLoader

dataloader_params = {"batch_size": 32, "num_workers": 4, "pin_memory": True}

train_folds, val_folds = [], []
for k in range(K):

    val_fold   = Subset(val_dataset,   (indexes==k).nonzero().squeeze())
    train_fold = Subset(train_dataset, (indexes[:100]!=k).nonzero().squeeze())

    val_fold   = DataLoader(val_fold,   shuffle=False, **dataloader_params)
    train_fold = DataLoader(train_fold, shuffle=True,  **dataloader_params)

    val_folds.append(val_fold)
    train_folds.append(train_fold)
`

#PyTorch Network models
Now let us build a Multilayer Perceptron.
To do this, we:

1.   instantiate an empty feed-forward ([sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html)) network
2.   add two fully-connected ([a.k.a. linear](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)) layers to the network (i.e. one hidden layer and the output layer)

Other [PyTorch layers and functions for Neural Networks](https://pytorch.org/docs/stable/nn.html)

##General model

`python
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

        x = self.flatten(x)                    # apply the flatten to the input

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
`

`python
model = MultiLayerPerceptron()         # model
print("Model:\n", model)
`

### Model parameters

`python
def print_parameters(model):
    for name, param in model.named_parameters():
      print(name)
      print("- requires_grad:", param.requires_grad)
      print("- shape:", param.shape)
      print("- is on GPU?", param.is_cuda,"\n")

print_parameters(model)
`

##From CPU to GPU and back

`python
model = model.cuda()
print_parameters(model)
`

`python
model = model.cpu()
print_parameters(model)
`

#One training iteration

##Loss function and optimizer
Now we select the cross-entropy as the loss and the Stochastic Gradient Descent as the optimizer.

##Forward pass

`python
model = model.cuda()
`

###Data and model on different devices

`python
batch_x, batch_y = next(iter(train_folds[0]))
print("x shape:", batch_x.shape)
print("y shape:", batch_y.shape)

output = model(batch_x)
print("Output:", output, output.shape)
`

###Move data on the GPU and execute the forward pass

`python
batch_x = batch_x.cuda()
batch_y = batch_y.cuda()
print("Data is CUDA?", batch_x.is_cuda)

output = model(batch_x)
print("Output:", output, output.shape)
`

`python
lossFunction = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),   #   <-- SELECT WHICH PARAMETERS TO OPTIMIZE
                            weight_decay=0,       #   <-- REGULARIZATION DEACTIVATED IN THIS EXAMPLE
                            lr=0.1)               #   <-- HIGH LEARNING RATE ONLY TO OBSERVE THE WEIGHT UPDATE
`

##Backward pass

`python
param = model.layer2.bias
print(param)
print("Gradient of the param:", param.grad)
`

###Backpropagation and gradient computation

`python
loss = lossFunction(output, batch_y)
loss.backward()
`

`python
batch_y
`

`python
loss
`

`python
print(param)
print("Gradient of the param:", param.grad)
`

###Weights update and gradient reset

`python
optimizer.step()
optimizer.zero_grad()
`

`python
print(param)
print("Gradient of the param:", param.grad)
`

#Train for one epoch

Now we train the model for one *epoch*

`python
optimizer = torch.optim.SGD(model.parameters(),   #   <-- SELECT WHICH PARAMETERS TO OPTIMIZE
                            lr=0.001, weight_decay=0)
`

`python
k=0
train_loader, val_loader = train_folds[k], val_folds[k]
val_losses, val_accuracies = [], []
`

`python
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
`

#Validate results on a validation set

`python
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
`

`python
print("Validation losses per epoch:", val_losses)
print("Validation accuracies per epoch:", val_accuracies)
`

Run the training-validation cells multiple time, then run this cell to plot the validation metrics

`python
plt.plot(val_losses)
plt.plot(val_accuracies)
plt.legend(["Loss", "Accuracy"])
plt.xlabel("epoch")
plt.show()
`

#Save the trained model

`python
torch.save(model.state_dict(), 'saved_model.pth')
`

#Load a previously trained model

`python
model.load_state_dict(torch.load('saved_model.pth'))
`

#Exercise: put together the code
Perform a K-fold cross validation. For each fold:
1. train the model for 20 epochs;
2. save the validation loss and accuracy after each epoch;
3. save the best model only, i.e. the one reaching the lowest validation loss.

Thus, compute the average accuracy among the best model trained at each fold.

Eventually implement an early stopping criterion, i.e. stop the training if the validation loss does not increase for 5 consecutive epochs. Likely, to activate the early stopping, more than 20 training epochs would be necessary.

`python
def one_epoch(model, lossFunction, optimizer, train_loader, val_loader):
  for X, y in train_loader:
    X = X.cuda()
    y = y.cuda()

    optimizer.zero_grad()

    o = model(X)
    l = lossFunction(o, y)

    l.backward()
    optimizer.step()

    acc = (o.detach().argmax(-1) == y.detach()).float().mean()
    print("- batch loss and accuracy : {:.7f}\t{:.4f}".format(l.detach().item(), acc))

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

    print("Validation loss and accuracy : {:.7f}\t{:.4f}".format(val_loss, val_accuracy))
  return val_loss, val_accuracy
`

`python
# learning parameters
lossFunction = torch.nn.CrossEntropyLoss()
lr = .01
momentum = .9
lambda_reg = 0

epochs = 20
early_stopping_patience = 5

# dataset and network parameters
K_cross_val = 10
num_hidden_neurons = 72

# create output directory and logger
experiment_name = "my_first_MLP_temp"
import os
os.makedirs(experiment_name)
torch.save(indexes, os.path.join(experiment_name, "cross-val-indexes.pt"))
`

`python
val_losses = torch.zeros(epochs, K_cross_val)
val_accuracies = torch.zeros(epochs, K_cross_val)

for k in range(K_cross_val):
  train_loader, val_loader = train_folds[k], val_folds[k]
  model = MultiLayerPerceptron(hidden_size=num_hidden_neurons).cuda()
  optimizer = torch.optim.SGD(model.parameters(),
                              lr=lr,
                              weight_decay=lambda_reg,
                              momentum=momentum)

  early_stopping_counter = early_stopping_patience
  min_val_loss = 1e10

  for e in range(epochs):
    print("FOLD {} - EPOCH {}".format(k, e))
    val_loss, val_accuracy = one_epoch(model, lossFunction, optimizer, train_loader, val_loader)

    # store the validation metrics
    val_losses[e, k] = val_loss
    val_accuracies[e, k] = val_accuracy
    torch.save(val_losses, os.path.join(experiment_name,'val_losses.pth'))
    torch.save(val_accuracies, os.path.join(experiment_name,'val_accuracies.pth'))

    # save the best model and check the early stopping criteria
    if val_loss < min_val_loss: # save the best model
      min_val_loss = val_loss
      early_stopping_counter = early_stopping_patience # reset early stopping counter
      torch.save(model.state_dict(), os.path.join(experiment_name,'fold_{}_best_model.pth'.format(k)))
      print("- saved best model")

    if e>0: # early stopping counter update
      if val_losses[e, k] > val_losses[e-1, k]:
          early_stopping_counter -= 1 # update early stopping counter
      else:
          early_stopping_counter = early_stopping_patience # reset early stopping counter
    if early_stopping_counter == 0: # early stopping
        break
`

`python
import matplotlib.pyplot as plt
plt.plot(val_losses)
plt.legend(range(K_cross_val))
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()
`

`python
plt.plot(val_accuracies)
plt.legend(range(K_cross_val))
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.show()
`

`python
best_acc = []
for k in range(K_cross_val):
  i = val_losses[:, k].argmin()
  best_acc.append(val_accuracies[i, k])

print("Best accuracies:", best_acc)
print(torch.tensor(best_acc).mean(), torch.tensor(best_acc).std())
`
