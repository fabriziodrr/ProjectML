# **Machine Learning Neural Networks p.02 Prof. Mario Vento Prof. Diego Gragnaniello** 

## Other architectures 

## ◆ Recurrent networks 

   - The output of a layer goes back as input of the same layer (or of a precedent layer) 

- Lateral connections 

   - The neurons in the same layer are connected to each other 

Neural network with lateral connections 

## Connections 

- Fully connected: every node of a layer is connected to every node of the successive layer 

- Sparse connections: only a subset of the connections are present 

## Multi-Layer Perceptron (MLP) 

- Feed forward network with 3 or more layers (at least one hidden layer) 

- Nodes are perceptrons with a non-linear activation function 

- ▪ The activation function must be derivable (we will see why when we discuss the learning algorithm) 

## Multi-Layer Perceptron (MLP) 

**==> picture [657 x 438] intentionally omitted <==**

**----- Start of picture text -----**<br>
Neuron Neuron<br>𝑥<br>1<br>1 1 𝑦1<br>𝑥<br>2<br>Neuron Neuron<br>𝑦2<br>2 2<br>𝑥<br>𝑑<br>Neuron Neuron<br>𝑁2 𝑁𝑚 𝑦𝑁𝑚<br>Layer 1 Layer 2 Layer  𝑚 Final result<br>(Input Layer) (Hidden Layer) (Output Layer)<br>**----- End of picture text -----**<br>


## Multi-Layer Perceptron (MLP) 

**==> picture [61 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
Layer  𝑘<br>**----- End of picture text -----**<br>


**==> picture [827 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
Layer  𝑘−1<br>[𝑘]<br>Neuron 𝑦𝑖<br>[𝑘−1] [𝑘] 𝑖<br>𝑦  ∙𝑤<br>𝑗 𝑖,𝑗<br>Neuron<br>𝑗<br>◆ The computation of generic neuron  𝑖 in layer  𝑘 (for simplicity we<br>call  𝑛 the number of neurons in the previous level,  𝑛= 𝑁𝑘−1 )<br>**----- End of picture text -----**<br>


**==> picture [572 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑛<br>[𝑘] [𝑘] [𝑘−1] [𝑘]<br>𝑛𝑒𝑡 𝑤  ∙𝑦  + 𝑤<br>𝑖 𝑖,𝑗 𝑗 𝑖,𝑛+1<br>= ෍<br>𝑗=1<br>[𝑘] [𝑘]<br>[𝑘]<br>This is called "bias" weight<br>𝑦 = 𝑓 (𝑛𝑒𝑡 )<br>𝑖 𝑖<br>**----- End of picture text -----**<br>


**==> picture [147 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Activation function<br>**----- End of picture text -----**<br>


## Multi-Layer Perceptron (MLP) 

## ◆ We can slightly simplify the equations if we add a "fictitious" bias [∗] neuron to each layer that, always has fixed output: 𝑦𝑛+1 = 1 

**==> picture [295 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑛+1<br>[𝑘] [𝑘] [𝑘−1]<br>=<br>𝑛𝑒𝑡 𝑤  ∙𝑦<br>𝑖 𝑖,𝑗 𝑗<br>෍<br>𝑗=1<br>[𝑘] [𝑘]<br>[𝑘]<br>𝑦 = 𝑓 (𝑛𝑒𝑡 )<br>𝑖 𝑖<br>**----- End of picture text -----**<br>


The single neuron has the same behavior as the Rosenblatt perceptron, except that the activation function is more general 

## Multi-Layer Perceptron (MLP) 

## ◆ This can be expressed much more compactly in matrix notation: 

**==> picture [721 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
Vector function<br>∙<br>𝑤 [[𝑘]]<br>𝑦 [[𝑘]] = 𝑓 [[𝑘]] ( 𝑦 [[𝑘−1]] )<br>Vector,  𝑁𝑘 + 1 Matrix,  Vector,  𝑁𝑘−1 + 1<br>elements (𝑁𝑘 + 1) × (𝑁𝑘−1 + 1) elements<br>elements<br>**----- End of picture text -----**<br>


Vectors have underline Matrixes have double underline 

**==> picture [195 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
"row by column" product<br>**----- End of picture text -----**<br>


## Multi-Layer Perceptron (MLP) 

## ◆ This can be expressed much more compactly in matrix notation: 

**==> picture [476 x 336] intentionally omitted <==**

**----- Start of picture text -----**<br>
∙<br>𝑤 [[𝑘]]<br>𝑦 [[𝑘]] = 𝑓 [[𝑘]] ( 𝑦 [[𝑘−1]] )<br>𝑤 [[𝑘]] 𝑤 [[𝑘]] ∙<br>𝑦 [[𝑘−1]] 𝑦 [[𝑘−1]]<br>𝑘 𝑘<br>𝑓 ( ) 𝑓 ( )<br>"row by column" product<br>**----- End of picture text -----**<br>


Vectors have underline Matrixes have double underline 

## Multi-Layer Perceptron (MLP) 

# ◆ Question 1: Which kind of functions can we represent with a multi-layer perceptron? 

- Question 2: How do we learn the weights of a MLP? 

## Universal Approximation Theorem 

- Any _continuous function_ defined on a _compact domain_ can be approximated to an arbitrary precision ε by a MLP with one hidden layer and a non-polynomial, continuous activation function for the hidden layer (Cybenko, 1989) 

- Thus, MLP are "universal" function approximators 

- Warning: the fact that one hidden layer is theorically sufficient, does not mean that it is the most efficient solution 

## Decision regions of MLP 

- If we use a MLP with (at least) one hidden layer for classification, the decision regions can have complex shapes 

- The more neurons we have in the hidden layer, the more the decision regions can get "complicated" 

## Decision regions of MLP 

- Example: for a 2D binary classification problem, using 1 hidden layer 

## Decision regions of MLP 

- Example: for a 2D binary classification problem, using 1 hidden layer 

## Decision regions of MLP 

- Example: for a 2D binary classification problem, using 1 hidden layer 

## Decision regions of MLP 

- Example: for a 2D binary classification problem, at varying of the number of layers 

## How do we train a MLP? 

- Back Propagation Algorithm, introduced by Rumelhart, Hinton and Williams in 1986 

- In this way the limitations of single perceptrons (linearly separable problems) can be overcome! 

   - This gave rise to the second wave of popularity of neural networks in Artificial Intelligence 

## How do we train a MLP? 

- We want to find the weights (parameters) that minimize the _**loss function**_ on the **training set** 

   - Remember? 

## 𝜃[∗] = arg min𝜃 𝐿(𝜃, 𝑇𝑟𝑎𝑖𝑛) 

   - In this case, 𝜃 are the weights of all the neurons in the network, while the loss function 𝐿 is a measure of the error (e.g. a distance between the actual output of the network and the desired output) 

- Problem: in general, we do not have a closed-form solution for this minimization! 

What can we do? 

## An old friend: the gradient 

- Given a **differentiable** scalar function 𝑓 𝑃= 𝑓 𝑥1, … , 𝑥𝑛 : ℝ[𝑛] → ℝ 

its **gradient** is the vector function: 

**==> picture [525 x 143] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝑓 Partial derivatives<br>ൗ<br>𝜕𝑓 𝜕𝑥1 of  𝑓 with respect to<br>= = 𝑥1, … , 𝑥𝑛<br>𝛻𝑓 ⋮<br>𝜕𝑥<br>1 … 𝑥𝑛<br>𝜕𝑓<br>ൗ<br>𝜕𝑥<br>𝑛<br>**----- End of picture text -----**<br>


- Linear approximation of a function around a point 𝑃0 : ∙ 

- 𝑓 𝑃 ~~0~~ + ∆𝑃 ≈𝑓 𝑃 ~~0~~ + 𝛻𝑓 𝑃 ~~0~~ ∆𝑃 

"Dot" product returns a scalar 

## An old friend: the gradient 

𝑃 𝑃 + ∇ 𝑃 ∙∆𝑃 𝑓 0 + ∆𝑃≈𝑓 0 𝑓 0 

◆ For a given, fixed length of vector ∆𝑃 , the term ∇ 𝑃 ∙∆𝑃has: 𝑓 0 ▪ the largest positive value when ∆𝑃 is aligned with ∇ 𝑃 𝑓 0 ▪ the smallest (i.e. most negative) negative value when ∆𝑃 is in the opposite direction of ∇𝑓 𝑃0 ◆ _P_ Thus, for small movements around a point _0_ **,** −∇ 𝑃 the opposite of the gradient, 𝑓 0 , gives the direction in which 𝑓 𝑃 diminishes more quickly! 

## Gradient Descent 

## ◆ A general technique for finding the minimum of a **differentiable function** : 

1. 𝑤= 𝑤 Start with an initial value of the weights 0 

2. Compute the gradient of the loss function 𝐿 **with respect to the weights** 3. Update the weights by adding a small vector in the _opposite_ direction of the gradient: 𝑤′ = 𝑤 −𝜂∙ ∇𝐿(𝑤) 

4. Repeat from step 2 until the gradient is 0 (or sufficiently close to 0 ) 

## Gradient Descent 

- Gradient Descent is easy to understand in the 1-D case: 

**==> picture [429 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐿(𝑤)<br>W, Global cast<br>min 𝐿(𝑤)<br>𝑤<br>**----- End of picture text -----**<br>


- The coefficient 𝜂 (called **learning** rate) is needed to ensure that small steps are performed, to avoid “overshooting” 

## Gradient Descent 

# ◆ An example in 2-D: 

## Gradient Descent 

# ◆ An example in 2-D at varying of the stating point: 

## Gradient Descent 

- Gradient Descent ensures to find a global optimum if the loss 

- function is **convex** 

- ◆ Otherwise, the algorithm may get stuck in a local minimum: 

## Back Propagation 

- The basic idea is to apply Gradient Descent to find the weights that minimize the loss function 

   - How to change each neuron’s weights to correct the whole network decisions? 

   - How changing a hidden neuron affects the output of next layer? 

- We need an automatic optimization tool to consistently update all network’s weights (all model’s parameters) 

## Back Propagation 

- are couples 

## 

   - Handwritten digit (28x28 grayscale image) 

   - ▪ The correct digit (integer 0,…,9) 

- Adopted notation in the video: 

   - 𝑤 

   - Neuron weights: 𝑖 

   - Neuron bias weights: 𝑏𝑖 

   - Output of the hidden layer: 𝑎[𝐿−1] 

   - Output of the output layer L: 𝑎[𝐿] _(a vector of length 10)_ 

   - ▪ Target (true label): 𝑦 _(one-hot encoded)_ 

   - ▪ Loss function for each output: 𝐶(𝑎[𝐿] −𝑦) 

## Back Propagation 

- Video example math notation: 

   - Neuron weights 𝑤𝑖 and bias 𝑏𝑖 in layer notation: 𝑤[(𝐿)] , 𝑏[(𝐿)] 

   - ▪ Excitation level of output layer L: 𝑧[(𝐿)] ▪ Activation function: 𝜎 

𝜎 𝑎[(𝐿)] = 𝜎(𝑧[(𝐿)] ) 𝑦 𝐶 𝑜 = (𝑎[(𝐿)] −𝑦)[2] 

- Output of the output layer L (10-d vector): 

- ▪ Target (true label, one-hot encoded): 

- ▪ Loss function: 

https://www.youtube.com/watch?v=Ilg3gGewQ5U ◆ https://www.youtube.com/watch?v=Ilg3gGewQ5U 

## Back Propagation 

- Consider a network with one hidden layer; if we call 𝒙 the input vector, 𝒛 the output vector of the hidden layer, and 𝒚 the final output vector, then: 

▪ 𝒘 ∙𝒙 𝒛= 𝑓ℎ ℎ ▪ 𝒘 ∙𝒛 𝒚= 𝑓𝑜 𝑜 

where fh and fo are the activation functions of the hidden and output layers, and 𝒘ℎ and 𝒘𝑜 are the weight **matrices** of those layers. 

## Back Propagation 

- We know the desired output 𝒕 and the loss function 𝐿 𝒚, 𝒕 

▪ : As an example, we can use _mean square error_ 

𝐿 𝒚, 𝒕= 𝒚−𝒕[2] ◆ Thus, we can minimize 𝐿 by update the weights in the opposite direction to the gradient: 

𝜕𝐿(𝒚, 𝒕) 𝒘 ←𝒘 𝑜 𝑜 −𝜂∙ 𝜕𝒘 𝑜 𝜕𝐿(𝒚, 𝒕) 𝒘 ←𝒘 ℎ ℎ −𝜂∙ 𝜕𝒘 ℎ 

## Back Propagation 

## 𝜕𝐿 𝑦,𝑡 ◆ The first partial gradient is easy to compute: 

## 𝜕𝑤 𝑜 

**A single component of the gradient** 𝜕𝐿 𝜕𝐿 𝑦, 𝑡 𝑦, 𝑡 𝜕𝑦𝑖 **The output layer has all** = ∙ **the information needed** 𝑖𝑗 𝑖𝑗 𝜕𝑤 𝜕𝑦𝑖 𝜕𝑤 **to compute this** 𝑜 𝑜 **Element** 𝒊𝒋 **of the matrix** 𝒘𝒐 **Here we consider only** 𝒚𝒊 **because the other** 𝒊𝒋 𝒘 **outputs do not depend on** 𝒐 

Back Propagation 𝜕𝐿 𝑦,𝑡 ◆ For the second gradient 𝜕𝑤 ℎ[we can apply the "chain rule" for ] derivation: 

The hidden layer computes z during the forward step. The value must be stored to be used during the backward step. 

𝜕𝐿 𝜕𝐿 𝜕𝑧 𝑦, 𝑡 𝑦, 𝑡 𝑗 = ∙ 𝑗𝑘 𝜕𝑧 𝑗𝑘 𝜕𝑤 𝜕𝑤 𝑗 ℎ ℎ step. **The hidden layer has the information to compute every piece EXCEPT THIS!** 

**Since y is computed by the OUTPUT LAYER** 

## Back Propagation (doing the math) 

- Let’s do all the math… 

## Back Propagation (doing the math) 

## ◆ The first partial gradient 

## 𝜕𝐿 𝑦,𝑡 is easy to compute: 𝜕𝑤 𝑜 

**==> picture [653 x 306] intentionally omitted <==**

**----- Start of picture text -----**<br>
A single component<br>of the gradient<br>𝜕𝐿 𝜕𝐿 𝜕𝐿<br>𝑦, 𝑡 𝑦, 𝑡 𝜕𝑦𝑖 𝑦, 𝑡<br>= ∙<br>∙𝑓 [′]<br>𝑜 [(𝑤][𝑜𝑖] [∙𝑧) ∙𝑧][𝑗]<br>𝑖𝑗 𝑖𝑗 [=]<br>𝜕𝑤 𝜕𝑦𝑖 𝜕𝑤 𝜕𝑦𝑖<br>𝑜 𝑜<br>Row  𝒊 of the<br>matrix  𝒘<br>Element  𝒊𝒋 of the  𝒐<br>matrix  𝒘<br>𝒐<br>because the other<br>Here we consider only  𝒚𝒊<br>𝒊𝒋<br>𝒘<br>outputs do not depend on  𝒐<br>**----- End of picture text -----**<br>


## Back Propagation (doing the math) 

## ◆ The first partial gradient 

## 𝜕𝐿 𝑦,𝑡 is easy to compute: 𝜕𝑤 𝑜 

**==> picture [628 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿 𝜕𝐿 𝜕𝐿<br>𝑦, 𝑡 𝑦, 𝑡 𝜕𝑦𝑖 𝑦, 𝑡<br>= ∙<br>∙𝑓 [′]<br>𝑜 [(𝑤][𝑜𝑖] [∙𝑧) ∙𝑧][𝑗]<br>𝑖𝑗 𝑖𝑗 [=]<br>𝜕𝑤 𝜕𝑦𝑖 𝜕𝑤 𝜕𝑦𝑖<br>𝑜 𝑜<br>The output layer has all the information<br>needed to compute this<br>**----- End of picture text -----**<br>


Back Propagation (doing the math) 𝜕𝐿 𝑦,𝑡 ◆ For the second gradient 𝜕𝑤 ℎ[we can apply the "chain rule" for ] derivation: 

**==> picture [636 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿 𝜕𝐿 𝜕𝑧 𝜕𝐿<br>𝑦, 𝑡 𝑦, 𝑡 𝑗 𝑦, 𝑡 𝑗<br>= ∙<br>∙𝑓 [′] ℎ [(𝑤] ℎ ∙𝑥) ∙𝑥𝑘<br>𝑗𝑘 𝑗𝑘 [=]<br>𝜕𝑧 𝜕𝑧<br>𝜕𝑤 𝜕𝑤<br>𝑗 𝑗<br>ℎ ℎ<br>**----- End of picture text -----**<br>


**The hidden layer has the information to compute every piece EXCEPT THIS!** 

## Back Propagation (doing the math) 

𝜕𝐿 𝑦,𝑡 ◆ For the second gradient 𝜕𝑤 ℎ[we can apply the "chain rule" for ] derivation: 

**==> picture [620 x 327] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿 𝑦, 𝑡 𝜕𝐿 𝑦, 𝑡 𝜕𝑧𝑗 𝜕𝐿 𝑦, 𝑡 𝑗<br>= ∙ 𝑤 ∙𝑥∙𝑥<br>𝑗𝑘 𝑗𝑘 [=] ∙𝑓 [′] ℎ ℎ 𝑘<br>𝜕𝑧 𝜕𝑧<br>𝜕𝑤 𝑗 𝜕𝑤 𝑗<br>ℎ ℎ<br>𝜕𝐿 𝑦, 𝑡 𝜕𝐿 𝑦, 𝑡 𝜕𝑦𝑖 𝜕𝐿 𝑦, 𝑡<br>𝑖𝑗<br>∙<br>∙𝑓 [′]<br>𝑜 [(𝑤][𝑜𝑖] [∙𝑧) ∙𝑤][𝑜]<br>𝜕𝑧 = ෍ 𝜕𝑧 = ෍<br>𝑖 𝜕𝑦𝑖 𝑖 𝜕𝑦𝑖<br>𝑗 𝑗<br>Here we have to consider all the components of  𝑦 ,<br>𝑧<br>because each of them depends on  𝑗<br>**----- End of picture text -----**<br>


## Back Propagation (doing the math) 

𝜕𝐿 𝑦,𝑡 ◆ For the second gradient 𝜕𝑤 ℎ[we can apply the "chain rule" for ] derivation: 

**==> picture [643 x 270] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿 𝑦, 𝑡 𝜕𝐿 𝑦, 𝑡 𝜕𝑧𝑗 𝜕𝐿 𝑦, 𝑡 𝑗<br>= ∙ 𝑤 ∙𝑥∙𝑥<br>𝑗𝑘 𝑗𝑘 [=] ∙𝑓 [′] ℎ ℎ 𝑘<br>𝜕𝑧 𝜕𝑧<br>𝜕𝑤 𝑗 𝜕𝑤 𝑗<br>ℎ ℎ<br>𝜕𝐿 𝑦, 𝑡 𝜕𝐿 𝑦, 𝑡 𝜕𝑦𝑖 𝜕𝐿 𝑦, 𝑡<br>𝑖𝑗<br>∙<br>∙𝑓 [′]<br>𝑜 [(𝑤][𝑜𝑖] [∙𝑧) ∙𝑤][𝑜]<br>𝜕𝑧 = ෍ 𝜕𝑧 = ෍<br>𝑖 𝜕𝑦𝑖 𝑖 𝜕𝑦𝑖<br>𝑗 𝑗<br>**----- End of picture text -----**<br>


**THIS PIECE CAN BE COMPUTED BY THE OUTPUT LAYER AND THEN PASSED TO THE HIDDEN LAYER!** 

## Back Propagation 

◆ In general, if we have more hidden layers, we can compute the gradient of 𝐿(𝒚, 𝒕) with respect to the **weights** or to the **inputs** of layer 𝑘 GIVEN the gradient with respect to the **output** of layer 𝑘 ▪ The **output** of layer 𝑘 is actually the **input** of layer 𝑘+ 1 ! ▪ Thus, the gradient with respect to it can be computed by layer 𝑘+ 1 and passed back to layer 𝑘 . 

- In this way, we start from the last layer of the network, and propagate the **gradient** of the loss function back to the first layer (this is why the name _Back Propagation_ ) 

## Back Propagation 

## Data propagation direction 

Loss **gradient** propagation direction 

(It is the loss **gradient** that is back-propagated, not the loss!) 

