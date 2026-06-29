# **Machine Learning Deep Learning Prof. Mario Vento Prof. Diego Gragnaniello** 

## Neural network popularity 

- First wave: Cybernetics: 1940s-1960s 

- ▪ Study of biological neurons, Hebbian learning, Perceptron 

- ◆ Second wave: Connectionism: 1980s-1990s 

   - MLP with Back Propagation, Kohonen networks 

◆ Third wave: Deep Learning: 2000s-today ▪ Unsupervised Deep NN (e.g. Restricted Boltzmann Machines) ▪ Supervised Deep NN (e.g. Convolutional Neural Networks) ▪ Breakthrough results on several complex tasks (e.g. image recognition) 

## Second wave NNs: shallow networks 

- Second wave NNs were shallow: typically 1-2 hidden layers 

   - The Universal Approximation Theorem ensures that one hidden layer is enough! 

   - Computational power limited the number of neurons 

   - Often, only small datasets were available 

   - Belief that layers had to be fully connected 

   - Numerical problems with gradient descent on many layers (vanishing gradient) 

## Vanishing gradient 

# ◆ Second wave networks typically used the _sigmoid_ (or its relative, _tanh_ ) as activation function 

# ◆ The sigmoid has some nice formal properties 

- Continuous and infinitely differentiable 

- Has a well established probabilistic interpretation (see Logistic regression) 

## Vanishing gradient 

- Unfortunately, the derivative of the sigmoid is almost 0 for most of its domain 

**==> picture [588 x 346] intentionally omitted <==**

**----- Start of picture text -----**<br>
Y<br>1<br>f '(x)=0.105<br>0.75<br>f '(x)=0.002<br>f '(x)=0.018<br>0.5<br>f '(x)=0.018<br>f '(x)=0.002<br>0.25<br>f '(x)=0.105<br>0<br>-6 -4 -2 0 2 4 6<br>**----- End of picture text -----**<br>


## Vanishing gradient 

◆ The problem gets worse if you chain several layers For the chain rule: 

**==> picture [635 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐽 𝜕𝐽<br>[𝑘] [𝑘−1] [𝑘−1]<br>[𝑘−1] [= ෍] [𝑘] [∙𝑓][[𝑘]′][(෍] 𝑤𝑖𝑚  ∙𝑦𝑚 ) ∙𝑤𝑖𝑗<br>𝑖 𝑚<br>𝜕𝑦 𝜕𝑦<br>𝑗 𝑖<br>**----- End of picture text -----**<br>


Gradient backpropagated from layer [k+1] 

Gradient backpropagated from layer [k] 

## Vanishing gradient 

- The problem gets worse if you chain several layers: 

- In fact, for the chain rule: 

**==> picture [635 x 279] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐽 𝜕𝐽<br>[𝑘] [𝑘−1] [𝑘−1]<br>[𝑘−1] [= ෍] [𝑘] [∙𝑓][[𝑘]′][(෍] 𝑤𝑖𝑚  ∙𝑦𝑚 ) ∙𝑤𝑖𝑗<br>𝑖 𝑚<br>𝜕𝑦 𝜕𝑦<br>𝑗 𝑖<br>If this is small…<br>… and this is<br>small…<br>**----- End of picture text -----**<br>


- … then, that will be 

even smaller! 

## Vanishing gradient 

◆ If the derivative of the activation function is ~0, the gradient will become smaller and smaller as it is back-propagated across several layers 

**Why is this a problem?** 

## Vanishing gradient 

- If the derivative of the activation function is ~0, the gradient will become smaller and smaller as it is back-propagated across several layers 

- This is a problem because small gradient ⇒ small changes of the ⇒ 

- weights slow learning 

   - ⇒ 

   - For numeric underflow, it may even become 0 no learning at all! 

- For this reason, using the sigmoid (or the tanh) does not allow the use of many hidden layers 

## What changed in the 2000's? 

- Better understanding of biological neural networks 

- Larger datasets available 

- Larger computational resources 

- Better understanding of the vanishing gradient (and solutions to it) 

- Architectural innovations (weight sharing, local connections, heterogeneous layers) 

## Biological NNs: deep networks! 

Schematic structure of the visual cortex of a primate 

## Biological NNs: deep networks! 

## Schematic structure of the visual cortex of a primate 

Many layers 

## Biological NNs: deep networks! 

## Schematic structure of the visual cortex of a primate 

**==> picture [199 x 200] intentionally omitted <==**

**----- Start of picture text -----**<br>
Several types<br>of layers<br>Each type of layer has a<br>different organization of<br>the neurons and of their<br>receptive fields<br>**----- End of picture text -----**<br>


## Third wave: large training sets 

## ◆ Availability of huge quanties of data (“Big Data”) 

## Third wave: Large NNs 

◆ Increase of computational power and memory + GPU massively parallel processing = Feasibility of large numbers of neurons 

## Third wave innovations: ReLU activation 

- Rectified Linear Unit (ReLU): a different activation function (introduced in the ‘80s but popularized in the ’90s) 

## Third wave innovations: ReLU activation 

- Rectified Linear Unit (ReLU): 

**==> picture [761 x 302] intentionally omitted <==**

**----- Start of picture text -----**<br>
f (net) = max(0, net) 𝑓′(𝑛𝑒𝑡)<br>1<br>:Lo net ne 𝑛𝑒𝑡<br>3 𝑓 [′] a)<br>1 if 𝑛𝑒𝑡> 0<br>𝑛𝑒𝑡= ቊ [0 if 𝑛𝑒𝑡≤0]<br>◆ Solves the vanishing gradient problem!<br>**----- End of picture text -----**<br>


## Third wave innovations: local connections 

- Better understanding of architectures with a restricted number of connections between each neuron and the previous layer 

- ▪ Connections related to spatial/temporal locality in the input data 

- ▪ Example: Convolutional Neural Networks (LeCun 1998) 

- This reduces the number of weights to be trained, making feasible to use more levels and more neurons 

## Third wave innovations: weight sharing 

- Neurons performing conceptually the same operation on different parts of the input data can share the same weights 

- This dramatically reduces the number of weights to be trained, making feasible to use more levels and more neurons, especially on large dimensionality inputs (e.g. images) 

## Third wave innovations: heterogeneous layers 

◆ In biological NNs, layers performing different functions ▪ Hubel and Wiesel, 1962: The visual cortex of cats contains layers of “simple cells” (feature detectors) alternated with layers of “complex cells” (fusion of information, ensure spatial invariance) 

- In CNN neural networks: 

▪ Convolutional layers (feature detectors) ▪ Pooling layers (spatial/temporal invariance) 

## Deep networks 

◆ The previous innovations have made possible the realization and training of neural networks with a high number of hidden layers ( **deep neural networks** ) 

- Tens or even hundreds of layers are quite common 

## Deep networks: advantages? 

- At each successive layer, the network can learn more **complex patterns** using the **composition** of **simple patterns** recognized in the previous layer 

- Thus, even starting with very low-level input information (e.g. raw image pixels) the network could be able to learn complex structures (e.g. objects in the picture) 

## Representation learning 

## Representation learning 

◆ A deep network **learns** the best **representation** (the features) for solving its task! 

- You don't have to define "by hand" what are the features… 

## Deep networks: advantages? 

## ◆ Better **generalization** performance 

**==> picture [93 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
On test set!<br>**----- End of picture text -----**<br>


n. of layers 

Goodfellow et al. 2014: Multi-digit number recognition from StreetView images… 

## Deep networks: advantages? 

## ◆ Better performance w.r.t. the number of parameters 

**==> picture [89 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
n. of layers<br>**----- End of picture text -----**<br>


Goodfellow et al. 2014: Multi-digit number recognition from StreetView images… 

## Deep networks: advantages? 

- This may seem counter-intuitive 

   - We expect more layers = more complexity = more overfitting 

- In a sense, a deep network embodies the **assumption** that the function we want to learn can be obtained by **composition from several smaller functions** 

   - Thus, a deep model works better when this assumption is true (showing 

   - better generalization) 

   - The No free-lunch theorem reminds us that there are problems for which 

      - this assumption must be false… 

## Why do deep networks work? 

# ◆ Another perspective: a **single neuron** (as we already said) can only learn to solve linearly separable problems 

**==> picture [262 x 247] intentionally omitted <==**

**----- Start of picture text -----**<br>
x<br>2<br>1<br>0<br>0 1 x1<br>**----- End of picture text -----**<br>


**Example** : the XOR function cannot be learned using a single neuron Here 𝑦= 𝑓 𝒙 with 𝒙= (𝑥1, 𝑥2) →𝑦= 0 →𝑦= 1 

## Why do deep networks work? 

- Instead of building a "more complex" neuron, we can translate our input space into a different space where the problem becomes linearly separable 

   - We try to learn 𝑓(𝜙 𝒙) , where 𝜙(𝒙) is a vector-to-vector function mapping **x** 

   - our input vector to a different space 

   - 𝜙(𝒙) must be non-linear (otherwise, the composition 𝑓(𝜙 𝒙) will still have 

   - the limitations of a linear function) 

But how do we find 𝜙(𝒙) ? 

## Why do deep networks work? 

- In traditional machine learning approaches, we must define 𝜙(𝒙) 

      - manually 

   - To do so we must be expert of the application domain (e.g. computer 

   - vision or speech recognition) 

- Another option is to use a very generic 𝜙 such as the _Radial Basis Functions_ _**,**_ but this usually does not generalize well on 

- complex tasks 

## Why do deep networks work? 

- Example: for XOR, we can define manually: 𝜙 𝒙= (ℎ1, ℎ2) = (𝑥1 ∙𝑥2, 𝑥1 + 𝑥2) 

**==> picture [557 x 249] intentionally omitted <==**

**----- Start of picture text -----**<br>
x h<br>2 2<br>1 2<br>1<br>0 0<br>0 1 x1 0 1 h1<br>**----- End of picture text -----**<br>


**==> picture [509 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
ℎ= ℎ<br>Now the problem can be solved linearly! 𝑓 2 −2 ∙ℎ1<br>**----- End of picture text -----**<br>


## Why do deep networks work? 

- In deep learning, we **learn** 𝜙(𝒙) instead of defining it manually 

   - The **hidden layers** of the network become our 𝜙 

   - We choose for a hidden layer a parametric structure that is highly generic: 

   - the composition between a linear function and a non-linear activation function 

   - We can represent very complicated 𝜙(𝒙) by just applying more hidden 

   - layers… 

## Why do deep networks work? 

- In our XOR example, we can choose a hidden layer modeled as: 

𝜙 𝒙= 𝑅𝑒𝐿𝑈(𝑾∙𝒙+ 𝒃) Bias vector Weight matrix (other Activation (parameters) parameters) function 

_even_ Note: the learning algorithm will choose W and b to best implement the desired function f, if the training data does not give the desired value of 𝜙 

## Why do deep networks work? 

- In our XOR example, we can choose a hidden layer modeled as: 

# 𝜙 𝒙= 𝑅𝑒𝐿𝑈(𝑾∙𝒙+ 𝒃) 

# ◆ For instance, the algorithm may choose (performing a sufficient number of training cycles): 

**==> picture [148 x 122] intentionally omitted <==**

## Why do deep networks work? 

- With this definition of 𝒉= 𝜙 𝒙 : 

**==> picture [562 x 291] intentionally omitted <==**

**----- Start of picture text -----**<br>
x h<br>2 2<br>1 1<br>0 0<br>0 1 x1 0 1 2 h1<br>𝒉= ℎ<br>The problem can be solved linearly! 𝑓 1 −2 ∙ℎ2<br>**----- End of picture text -----**<br>


## Transfer Learning 

# ◆ The lower layers of a deep network learn an intermediate representation that is helpful for solving the network task 

# ◆ What if we need to solve a different but **similar** problem? 

- Probably, the intermediate features will be useful for the new problem, too 

## Transfer Learning 

- We can exploit this fact re-using those layers (already 

      - trained) for building a new network 

   - The topmost layers of the network are replaced with a new NN 

   - ▪ The resulting net is trained on the new problem ( **Fine Tuning** ) 

- In this way, we **transfer** some knowledge that we have learned for the first task to the solution of the second task 

## Transfer Learning 

- Network trained to solve task 1: 

**==> picture [308 x 400] intentionally omitted <==**

**----- Start of picture text -----**<br>
Solution to<br>task 1<br>Layer N<br>High-level<br>features for<br>task 1 Layer N-1<br>Intermediate-<br>level features<br>Layer 2<br>Low-level<br>features<br>Layer 1<br>Input data<br>**----- End of picture text -----**<br>


## Transfer Learning 

◆ We remove some of the top layers: 

**==> picture [308 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
Intermediate-<br>level features<br>Layer 2<br>Low-level<br>features<br>Layer 1<br>Input data<br>**----- End of picture text -----**<br>


Transfer Learning ◆ We add different top layers: 

Intermediatelevel features Low-level features 

Input data 

**==> picture [163 x 347] intentionally omitted <==**

**----- Start of picture text -----**<br>
Layer N<br>Layer N-1<br>Layer 2<br>Layer 1<br>**----- End of picture text -----**<br>


**==> picture [40 x 41] intentionally omitted <==**

## Transfer Learning 

## ◆ We train the resulting network on task 2: 

**==> picture [308 x 400] intentionally omitted <==**

**----- Start of picture text -----**<br>
Solution to<br>task 2<br>Layer N<br>High-level<br>features for<br>task 2 Layer N-1<br>Intermediate-<br>level features<br>Layer 2<br>Low-level<br>features<br>Layer 1<br>Input data<br>**----- End of picture text -----**<br>


## Transfer Learning: advantages 

- Reuse of knowledge across similar problems 

- Time saving: part of the network is already trained! 

- A smaller dataset can be used for the new problem (since there are less weights to be learned) 

- ▪ Extreme case: **one shot learning** : only one example given for task 2 (the additional part of the network must be very simple!) 

## Breakthrough performance on difficult problems 

**==> picture [161 x 40] intentionally omitted <==**

**----- Start of picture text -----**<br>
AlexNet<br>GoogLeNet<br>**----- End of picture text -----**<br>


## ImageNet Large Scale Visual Recognition Challenge 

## Breakthrough performance on difficult problems 

◆ In the last 10 years, deep networks have consistently and significantly improved the state-of-the-art performance on tasks considered very difficult 

- Image classification 

- Object detection and recognition 

- Speech recognition 

- Natural Language Understanding 

- Language translation 

- Image/video modification 

▪ . . . 

