# **Machine Learning Neural Networks p.01 Prof. Mario Vento Prof. Diego Gragnaniello** 

## The biological neuron 

## The biological neuron 

- The operation of a biological neuron is relatively simple: 

   - the neuron receives ions through the input synapses 

   - ▪ if the total received electrical charge is over a threshold, the output is "fired" 

- Complex operations in our nervous system (including our brain) are implemented by a very large number of interconnected neurons (human brain: about 86*10[9] neurons) 

- Learning is performed by adding new synapses or by changing their "intensity" 

## Artificial Neural Networks 

◆ Computing systems inspired by (biological) neural networks: ▪ Complex computations are performed by a large number of simple units (artificial neurons) suitably interconnected 

- Usually able to _learn_ their function 

## McCulloch & Pitts neuron 

**==> picture [367 x 168] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑥<br>1<br>∙𝑤<br>1<br>𝑛𝑒𝑡 𝑜𝑢𝑡<br>Σ 𝑓<br>𝑥<br>𝑑<br>∙𝑤<br>𝑑<br>𝑤<br>0<br>**----- End of picture text -----**<br>


**==> picture [249 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑑<br>𝑥 ∙𝑤 + 𝑤<br>𝑖 𝑖 0<br>𝑛𝑒𝑡= ෍<br>𝑖=1<br>𝑜𝑢𝑡= 𝑓 𝑛𝑒𝑡<br>**----- End of picture text -----**<br>


## ◆ Proposed in 1943 

- 𝑛𝑒𝑡 is the internal " _excitation level_ " of the neuron 

- 𝑓( ) is the **activation function** that transforms the internal excitation into the neuron output 

   - As in biological neurons, the activation is "all-or-nothing" (step function) 

- 𝑤𝑖 are the **weights** of the neuron (the _parameters_ ) 

- No learning algorithm was proposed 

## McCulloch & Pitts neuron 

# ◆ A McCulloch & Pitts neuron works as a **binary classifier** ▪ 𝑥 𝑥 Given the inputs (the features) 1 ,…, 𝑑 the output is: 

𝑐𝑙𝑎𝑠𝑠= 

𝑑 +1 if 𝑤 ∙𝑥 + 𝑤 ≥0 𝑖 𝑖 0 ෍ 𝑖=1 𝑑 −1 if 𝑤 ∙𝑥 + 𝑤 < 0 𝑖 𝑖 0 ෍ 𝑖=1 

▪ Thus, the decision depends on the sign of 𝑑 𝑤 ∙𝑥 + 𝑤 σ𝑖=1 𝑖 𝑖 0 

What is the shape of the decision regions? 

## McCulloch & Pitts neuron 

# ◆ The two decision regions are separated by a **hyperplane** ▪ In 2D space (d=2), it is a straight line; in 3D space (d=3), it is a plane; etc. 

**==> picture [577 x 243] intentionally omitted <==**

**----- Start of picture text -----**<br>
x<br>2 Region attributed to<br>+<br>class +1<br>+ +<br>+<br>+<br>- + +<br>-<br>+<br>- Hyperplane with equation:<br>𝑑<br>-<br>𝑤 ∙𝑥 + 𝑤 = 0<br>𝑖 𝑖 0<br>- ෍𝑖=1<br>-<br>-<br>Region attributed to<br>class -1<br>**----- End of picture text -----**<br>


**==> picture [17 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
x<br>1<br>**----- End of picture text -----**<br>


**-** 

## Rosenblatt's Perceptron 

- Proposed in 1956 

- Same architecture as McCulloch-Pitts neuron, BUT a **learning algorithm** was defined for supervised learning of the weights 

- Perceptron learning is _on-line_ : the perceptron sees **one training sample at a time** , and changes slightly its weights 

## Rosenblatt's Perceptron 

- Learning algorithm: 

   - 𝑥 

   - Given a random sample (feature vector) from the training set: 𝑗 

      - 𝑤 

      - For each weigth 𝑖 in the perceptron: 

         - 𝑤 ←𝑤 𝑖 𝑖 + 𝑟∙(𝑡 −𝑦 ) ∙𝑥 𝑗 𝑗 𝑗𝑖 

## where: 

   - 𝑡 𝑥 𝑗 ∈{−1, +1} is the desired output for sample 𝑗 

   - 𝑥 

   - 𝑦 ∈{−1, +1} is the perceptron actual output for sample 𝑗 𝑗 

   - • 𝑥 𝑥 the i-th feature of sample 

   - 𝑗𝑖 𝑗 

   - 𝑟 is a _learning rate_ ( 0 < 𝑟< 1 ); it is a hyper-parameter of the algorithm 

- Note: if 𝑥 is correctly classified ( 𝑦 = 𝑡 ) , the algorithm does not change the 𝑗 𝑗 𝑗 

- weights; only on errors the weights are changed 

## Rosenblatt's Perceptron 

## ◆ The effect of the learning algorithm 

## Rosenblatt's Perceptron 

◆ Q: We said that a learning algorithm chooses the weights that minimize some loss function. What is the loss function in this case? 

## Rosenblatt's Perceptron 

- Q: We said that a learning algorithm chooses the weights that minimize some loss function. What is the loss function in this case? 

- A: It can be demonstrated (but we will not do it) that, for a 𝑟 

- sufficiently small , the Rosenblatt's learning algorithm will minimize the loss: 

**==> picture [550 x 213] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>𝐿 𝑤, 𝑋= max 0, −𝑡 ∙𝑛𝑒𝑡<br>𝑗 𝑗<br>𝑁 [∙෍]<br>𝑥𝑗∈𝑋<br>training set 𝑑<br>=<br>𝑛𝑒𝑡𝑗  σ𝑖=1 𝑤𝑖 ∙𝑥𝑗𝑖 + 𝑤0<br>size of the<br>is the excitation level of the<br>training set 𝑥<br>neuron for input  𝑗<br>**----- End of picture text -----**<br>


## Rosenblatt's Perceptron 

◆ A: It can be demonstrated (but we will not do it) that, for a 𝑟 sufficiently small , the Rosenblatt's learning algorithm will minimize the loss: 

1 𝐿 𝑤, 𝑋= max 0, −𝑡 ∙𝑛𝑒𝑡 𝑗 𝑗 𝑁[∙෍] 𝑥𝑗∈𝑋 If 𝑡 and 𝑛𝑒𝑡 have the same 𝑗 𝑗 sign, the max is 0, and this term does not contribute to the loss. 

## Rosenblatt's Perceptron 

◆ A: It can be demonstrated (but we will not do it) that, for a 𝑟 sufficiently small , the Rosenblatt's learning algorithm will minimize the loss: 

**==> picture [636 x 230] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>𝐿 𝑤, 𝑋= max 0, −𝑡 ∙𝑛𝑒𝑡<br>𝑗 𝑗<br>𝑁 [∙෍]<br>𝑥𝑗∈𝑋<br>If  𝑡𝑗 and  𝑛𝑒𝑡𝑗 have opposite signs, this term is positive; the algorithm<br>will try to reduce the loss by changing the weights to make  𝑛𝑒𝑡𝑗<br>closer to 0.<br>**----- End of picture text -----**<br>


## Rosenblatt's Perceptron 

◆ A: It can be demonstrated (but we will not do it) that, for a 𝑟 sufficiently small , the Rosenblatt's learning algorithm will minimize the loss: 

**==> picture [601 x 214] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>𝐿 𝑤, 𝑋= max 0, −𝑡 ∙𝑛𝑒𝑡<br>𝑗 𝑗<br>𝑁 [∙෍]<br>𝑥𝑗∈𝑋<br>If  𝑡𝑗 and  𝑛𝑒𝑡𝑗 have opposite signs, this term is positive; the algorithm<br>will try to reduce the loss by changing the weights to make  𝑛𝑒𝑡𝑗<br>closer to 0.<br>**----- End of picture text -----**<br>


This means that the decision hyperplane is moved to be closer to 𝑥 . 𝑗 

## Rosenblatt's Perceptron 

## ◆ Example: 

**==> picture [577 x 253] intentionally omitted <==**

**----- Start of picture text -----**<br>
x<br>2 Region attributed to<br>+<br>class +1<br>+ +<br>+<br>+<br>- + +<br>-<br>+<br>- Hyperplane with equation:<br>𝑑<br>-<br>𝑤 ∙𝑥 + 𝑤 = 0<br>𝑖 𝑖 0<br>- ෍𝑖=1<br>-<br>-<br>Region attributed to<br>class −1<br>**----- End of picture text -----**<br>


x 1 

**-** 

## Rosenblatt's Perceptron 

## ◆ Example: 

**==> picture [441 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
We add a new<br>example here; the<br>algorithm does not<br>change its weights<br>x<br>2 +<br>+<br>+ +<br>+<br>+<br>- + +<br>-<br>+<br>-<br>-<br>-<br>-<br>-<br>**----- End of picture text -----**<br>


x 1 

**-** 

## Rosenblatt's Perceptron 

## ◆ Example: 

**==> picture [532 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
We add a new<br>example here; the<br>algorithm change the<br>x<br>2 + weights moving the<br>+<br>hyperplane a little<br>+ + towards the point<br>+<br>+<br>- + +<br>-<br>+ -<br>-<br>-<br>-<br>-<br>-<br>**----- End of picture text -----**<br>


x 1 

**-** 

## Rosenblatt's Perceptron 

# ◆ A demo online of the operation of a perceptron: ▪ https://codepen.io/bagrounds/full/wdqypY/ 

## Rosenblatt's Perceptron 

# ◆ Question: what happens if the samples of the two classes are distributed as in the figure below? 

## Rosenblatt's Perceptron 

- Minsky and Papert demonstrated in 1969 that perceptrons can only learn how to solve _linearly separable_ classification problems 

   - A simple function like XOR was not representable with a single perceptron; of course it can be realized by a network of perceptrons, but no learning algorithm was available for such a network 

   - This caused the research in Artificial Intelligence to move away from neural networks in the '70s and the early '80s 

## Using multiple neurons 

- Combining several perceptron-like neurons, it is possible to make more complex decision regions 

   - Example: with two perceptrons processing the inputs 

**==> picture [364 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
-<br>+<br>Hyperplane of<br>neuron 1<br>- +<br>Hyperplane of<br>neuron 2<br>**----- End of picture text -----**<br>


## Using multiple neurons 

- Combining several perceptron-like neurons, it is possible to make more complex decision regions 

   - Example: with two perceptrons processing the inputs 

**==> picture [478 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Region attributed to<br>Region attributed to<br>class +1<br>+ - class −1<br>Hyperplane of<br>neuron 1<br>Region attributed to<br>class −1<br>- +<br>Region attributed to<br>class +1<br>Hyperplane of<br>neuron 2<br>**----- End of picture text -----**<br>


## Using multiple neurons 

- Combining several perceptron-like neurons, it is possible to make more complex decision regions 

   - Example: with two perceptrons processing the inputs (plus one processing their partial result) 

**==> picture [563 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Neuron<br>x<br>1<br>1<br>Neuron final<br>3<br>result<br>x<br>2<br>Neuron<br>2 Question : we cannot use Rosenblatt<br>algorithm to train neuron 1 and 2.<br>Why?<br>**----- End of picture text -----**<br>


## Using multiple neurons 

- Combining several perceptron-like neurons, it is possible to make more complex decision regions 

   - Example: with two perceptrons processing the inputs (plus one processing their partial result) 

**==> picture [600 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
Neuron<br>x<br>1<br>1<br>???<br>Neuron final<br>3<br>result<br>???<br>x<br>2<br>Neuron<br>Answer : we cannot use Rosenblatt<br>2<br>algorithm to train neuron 1 and 2 because<br>we don't know what their result should be!<br>Training set only includes the final result…<br>**----- End of picture text -----**<br>


## Using multiple neurons 

# ◆ So, if we want to solve more complex problem, we need _networks_ of neurons (neural networks) 

- In order to do this, we will need to understand: 

   - How the neurons can be interconnected in a network 

   - How we can learn the weights of _all_ the neurons in a network 

## Neural network architectures 

- Neural Network: the output is not computed by a single neuron, but by a combination of neurons 

- A Neural Network **Architecture** is an answer to the question: how the neurons are interconnected to each others? 

## Feed-forward networks 

- Neurons are divided into _layers_ 

- ◆ A neuron in layer 𝑖 takes its inputs from layer 𝑖−1 and gives its outputs to layer 𝑖+ 1 

- ◆ An initial input layer collects the inputs (with no processing) ◆ Hidden layers: intermediate processing layers not connected directly to the output 

(layer 1) 

(layer 2) 

(layer 3) 

