# **Machine Learning Convolutional Neural Networks Prof. Mario Vento Prof. Diego Gragnaniello** 

## Convolutional Neural Networks 

- Proposed by LeCun, 1998 

**==> picture [506 x 371] intentionally omitted <==**

## Convolutional Neural Networks 

- Proposed by LeCun, 1998 

- Inspired by the working of the visual cortex of mammals 

- Effective on signals characterized by a strong spatial/temporal continuity (e.g. images) 

- In the following presentation we will usually assume a 2D input signal, but the network can be generalized to other dimensions 

## Convolution 

- Several signal processing tasks can be modeled as a convolution with a suitably defined “kernel” 

In the discrete case, for one-dimensional signal with a kernel of finite length (a.k.a. **F** inite **I** npulse **R** esponse filter, FIR): 

**==> picture [435 x 210] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑀<br>2<br>= 𝑤 ∙𝑥<br>𝑦𝑘 𝑖 𝑘−𝑖<br>෍<br>𝑖=−𝑀<br>1<br>Output signal<br>Input signal<br>Element of the<br>convolution<br>kernel<br>**----- End of picture text -----**<br>


## Convolution 

## ◆ Example: convolution with a kernel of length 3: 

**==> picture [409 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
xk-1 xk xk+1 xk+2<br>… -2 0 1.5 4 …<br>* * *<br>w1 w0 w-1<br>Kernel<br>0.5 1 0.2<br>(reversed)<br>-1 0 0.3<br>+<br>… … -0.7 …<br>**----- End of picture text -----**<br>


**==> picture [93 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
Input signal<br>**----- End of picture text -----**<br>


Output signal 

yk-1 

yk 

yk+1 

yk+2 

## Convolution 

## ◆ Example: convolution with a kernel of size 3: 

**==> picture [580 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
xk-1 xk xk+1 xk+2<br>… -2 0 1.5 4 …<br>Input signal<br>* * *<br>w1 w0 w-1<br>Kernel<br>0.5 1 0.2<br>(reversed)<br>0 1.5 0.8<br>+<br>… … -0.7 2.3  …<br>Output signal<br>**----- End of picture text -----**<br>


Output signal 

yk-1 

yk 

yk+1 

yk+2 

## Convolution 

- This can be extended to 2 or more dimensions 

**==> picture [259 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
Multiply the<br>corresponding<br>elements Add together to<br>obtain the<br>element of the<br>result<br>**----- End of picture text -----**<br>


## Convolution 

## Input signal 

## Kernel matrix 

## Output signal 

## Convolutional layers 

- Reproduce the convolution operation 

- The kernel is represented by the weights of the neurons 

   - Thus, the kernel is **learned** during the training 

- In the following, we will refer to the case of 2D input, like an image (but this can be generalized to other dimensions) 

## Layer organization 

- Each layer is organized as a 3D volume (tensor) 

   - Two dimensions (Width and Height) correspond to the spatial dimensions of the signal being processed; the third one ( **Depth** ) to the number of features computed in the layer 

   - A “slice” in the Depth direction is called a **Feature Map** 

- The input layer too is a 3D volume 

- ▪ For images, the input layer depth corresponds to the number of image channels (e.g. Red/Green/Blue for color images) 

## Layer organization 

- Each neuron is connected to a “ **receptive field** ”, that is a 

   - subvolume of the previous layer 

   - ▪ The receptive field include (usually) all the depth of the previous layer 

   - ▪ The width and height of the receptive field are small, and correspond to the size of the desired convolution kernels (e.g. 3x3, 5x5) [locality of connections] 

- All the neurons in the same feature map **share their weights** 

## Layer organization 

receptive field of a neuron 

The **first layer** has: Width=32 Height=32 Depth=3 Neurons=32x32x3=3072 **3 feature maps** (each containing 32x32=1024 neurons) 

## Layer organization 

receptive field of a neuron 

The **second layer** has: Width=28 Height=28 Depth=6 Neurons=28x28x6=4704 **6 feature maps** (each containing 28x28=784 neurons) 

## Layer organization 

receptive field of a neuron 

Each neuron in the second layer has a **receptive field** with: Width=5 Height=5 Depth=3 Kernel size=5x5 Each neuron in the second layer requires: Weights=5x5x3+1=76 (the +1 is for an optional "bias" weight added) 

## Layer organization 

receptive field of a neuron 

Each neuron in the second layer has a **receptive field** with: Width=5 Height=5 Depth=3 Kernel size=5x5 Each neuron in the second layer requires: Weights=5x5x3+1=76 (the +1 is for an optional "bias" weight added) **Q: How many weights has the second layer?** 

## Layer organization 

**Q: How many** receptive field of a **weights has the** neuron **second layer? A: (wrong) 28x28x6x76=35704** 

## Layer organization 

**Q: How many** receptive field of a **weights has the** neuron **second layer? A: (wrong) 28x28x6x76=35704** 

As we said, neurons in the same feature map **share** their weights **A: (correct) 6x76=456** 

## Layer organization 

- Note that we have greatly reduced the number of weights with 

- respect to a traditional **fully connected** layer 

- Part of the reduction because each neuron has a small receptive field (not 

- connected to all neurons in previous layer) 

- Part of the reduction because neurons in the same feature map share their 

- weights 

## Layer organization 

# ◆ For the second layer in our previous example: 

- We used only **456** weights 

- If the layer were fully connected: 

(3072+1)x4704= **14 455 392** 

**==> picture [46 x 86] intentionally omitted <==**

Neurons in previous layer 

Neurons in the considered layer 

## Layer organization 

- Each neuron in a convolutional layer perform a linear combination between the values in its receptive field and its weights 

- The result of this linear combination is then passed to the **ReLU activation function** 

   - You can use other activation functions, but ReLU is strongly 

   - suggested 

- The way the receptive fields are organized ensures that the layer as a whole performs a convolution (before the ReLU) 

## Layer organization: stride 

# ◆ Usually, moving from one neuron to an adjacent one, the receptive field is moved by one step in the same direction 

- To reduce the size of the layer, it is possible to change the “ **stride** ” (number of steps) 

- This does not reduce the number of weights (weights are shared) but does reduce the number of computations! 

## Layer organization: stride 

**==> picture [68 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
receptive<br>field<br>receptive<br>field<br>Stride=1<br>**----- End of picture text -----**<br>


## In this example: 3x3 kernel 

The receptive field of the second neuron (green) is translated by 1 position w.r.t. the receptive field of the first neuron (red). 

In this case: 

- Output width = Input width – kernel width + 1 

- Output height = Input height – kernel height + 1 

## Layer organization: stride 

**==> picture [68 x 15] intentionally omitted <==**

**----- Start of picture text -----**<br>
Stride=1<br>**----- End of picture text -----**<br>


**==> picture [102 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
receptive<br>field<br>receptive<br>field<br>receptive<br>field<br>Stride=2<br>**----- End of picture text -----**<br>


## Layer organization: stride 

With stride=2, the receptive field of the second neuron (green) is translated by 2 positions w.r.t. the receptive field of the first neuron (red). 

## In this case: 

- Output width = ⎣ (Input width – kernel width)/stride ⎦ + 1 

   - Output height = ⎣ (Input height – kernel height)/stride ⎦ + 1 

- 

⎣ x ⎦ means floor(x) (the largest integer ≤x) 

**==> picture [102 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
receptive<br>field<br>receptive<br>field<br>receptive<br>field<br>Stride=2<br>**----- End of picture text -----**<br>


## Layer organization: padding 

- You cannot apply the kernel on pixels close to the borders of the input 

- For this reason, the output is always smaller than the input 

**==> picture [128 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
You cannot<br>apply the kernel<br>here…<br>… or here…<br>**----- End of picture text -----**<br>


… or here… 

## Layer organization: padding 

◆ In order to have receptive fields covering also the parts of the volume close to the spatial borders, dummy “padding” units may be added around the volume (their value is always 0) 

Left Padding=2 Right Padding=2 Horizontal Padding = 2+2 = 4 Top Padding=2 Bottom Padding=2 Vertical Padding = 2+2 = 4 

## Layer organization: padding 

◆ With padding (assuming stride=1 for simplicity): ◆ Output width = Input width – kernel width + horiz. padding + 1 ◆ Output height = Input height – kernel height + vert. padding + 1 

- Thus, if we use: 

   - Horizontal Padding = Kernel Width – 1 

   - ◆ Vertical Padding = Kernel Height – 1 

then the output of the layer will have the same spatial size as the input. 

## Pooling layers 

- In a Convolutional Neural Network, not all the layers are Convolutional Layers 

- Another type of layers commonly found are the **pooling layers** that are used for two purposes: 

   - Reducing the spatial size (e.g. width and height) of the data 

   - Ensure a certain degree of **translation invariance** 

      - a small change in the position of a detected feature should not affect the final result of the network 

## Pooling layers 

- Each neuron has a receptive field with depth=1 

   - The depth of the layer is the same as the depth of the 

   - previous one 

- The neuron performs an **aggregation** of the data in its receptive field 

   - Common aggregation functions: **Max** (most used), **Average** 

- These neurons have **no weights** , and so are **not trained** 

   - But they pass back the gradient to the previous layer 

- Usually, the stride is > 1 

## Pooling layers 

## **Input feature map** 

**Output feature map** 

Receptive field: 2x2 Stride=2 [0 2.2sr, Bl . BY / Receptive field This is the Max of {37, 4, 25, 12} 

## Dropout layers 

- A **dropout layer** has the same shape (width, height, depth) as the previous layer 

   - Each neuron is connected to exactly one neuron of the previous layer 

- During the training of the network, a dropout neuron will: 

- ◆ Pass its input unaltered to its output, with probability 𝒑 

- ◆ Or else, pass 0 to its output (with probability 1 −𝑝 ) 

- This is equivalent to temporarily "shutting down" the neurons of a layer with probability 1 −𝑝 

## Dropout layers 

- The probability 𝒑 is a hyperparameter for the whole layer 

- Outside of the training phase (when the network is being tested/used), a dropout neuron passes always its input to its output, but multiplies it by 𝒑 

   - In this way, the average value of the output does not change between 

   - training and testing 

- A dropout neuron has **no weights** , and thus it is **not trained** 

- ◆ But it passes back the gradient to the previous layer during backtracking 

## Dropout layers 

## **Training time** 

**==> picture [55 x 55] intentionally omitted <==**

**==> picture [54 x 229] intentionally omitted <==**

**==> picture [450 x 320] intentionally omitted <==**

**----- Start of picture text -----**<br>
y1<br>y1<br>(with probability 𝒑 )<br>y2 0<br>(with probability  𝟏−𝒑 )<br>yk<br>yk<br>(with probability 𝒑 )<br>**----- End of picture text -----**<br>


## **Previous layer** 

## **Dropout layer** 

## Dropout layers 

## **Testing/usage time** 

**==> picture [55 x 55] intentionally omitted <==**

**==> picture [54 x 229] intentionally omitted <==**

**==> picture [450 x 320] intentionally omitted <==**

**----- Start of picture text -----**<br>
y1<br>p*y1<br>y2<br>p*y2<br>yk<br>p*yk<br>**----- End of picture text -----**<br>


## **Previous layer** 

## **Dropout layer** 

## Dropout layers 

## ◆ Why should we use a dropout layer? 

- It seems we are just sabotaging our neural network… 

## Dropout layers 

◆ The effect of a dropout layer is roughly equivalent to training many smaller networks (each having a fraction 𝒑 of the original nodes), and then combining their output by averaging at test/usage time 

## Dropout layers 

- The result is (in most cases) a **reduction of the variance error** 

   - (i.e. a **reduction of overfitting** ) 

- Training convergence becomes slower, but the overall time is still smaller than that required by a true "multi-expert approach" (i.e. really training many smaller networks) 

## Output layers 

- The final layers are typically “ **fully connected** ”, i.e. they are traditional MLP layers (a.k.a. **dense** layers) 

- Activation function is usually ReLU except for the last layer, which typically has (for the reasons previously explained): 

- ◆ **linear** activation if the task is **regression** ◆ **sigmoid** if the task is **binary classification** ◆ **softmax** if the task is **multiclass classification** 

## Example 

- AlexNet: developed in 2012 for the ImageNet Large Scale Visual Recognition Challenge (a 1000-classes image recognition task) 

   - Its victory ignited the popularity of Deep Neural Networks 

**==> picture [102 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
Drop Drop<br>out out<br>**----- End of picture text -----**<br>


## Example 

- 5 convolutional layers (11x11, 5x5, 3x3) 

◆ 3 max pooling layers (3x3, stride=2) ◆ 2 dropout layers (with p=0.5) ◆ 3 dense layers 

**==> picture [102 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
Drop Drop<br>out out<br>**----- End of picture text -----**<br>


## Feature maps 

Video Demo 

# ◆ The higher the level, the more compact the representation 

## Feature maps 

Video Demo 

# ◆ The higher the level, the more compact the representation 

## Feature maps 

**==> picture [105 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Video Demo<br>**----- End of picture text -----**<br>


- The higher the level, the more compact the representation 

## Feature maps 

## ◆ Patterns activating each feature map 

