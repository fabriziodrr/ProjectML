# **Machine Learning Neural Networks p.03 Prof. Mario Vento Prof. Diego Gragnaniello** 

## Back Propagation 

◆ In general, if we have more hidden layers, we can compute the gradient of 𝐿(𝒚, 𝒕) with respect to the **weights** or to the **inputs** of layer 𝑘 GIVEN the gradient with respect to the **output** of layer 𝑘 ▪ The **output** of layer 𝑘 is actually the **input** of layer 𝑘+ 1 ! ▪ Thus, the gradient with respect to it can be computed by layer 𝑘+ 1 and passed back to layer 𝑘 . 

- In this way, we start from the last layer of the network, and propagate the **gradient** of the loss function back to the first layer (this is why the name _Back Propagation_ ) 

## Back Propagation 

## Data propagation direction 

Loss **gradient** propagation direction 

(It is the loss **gradient** that is back-propagated, not the loss!) 

## Back Propagation 

# ◆ What else do we need to make this work? 

## Back Propagation 

# ◆ What else do we need to make this work? 

Answer: the activation functions must be derivable 

- So, we cannot use the step function of the original perceptron 

## Back Propagation 

- What else do we need to make this work? 

- Answer: the activation functions must be derivable 

- So, we cannot use the step function of the original perceptron 

   - For hidden layers, we have an additional constraint… 

## Back Propagation 

# ◆ What happens if, for a hidden layer, we use a _linear_ activation 𝑛𝑒𝑡= 𝑛𝑒𝑡 function (e.g. 𝑓ℎ )? 

## Back Propagation 

◆ What happens if, for a hidden layer, we use a _linear_ activation 𝑛𝑒𝑡= 𝑛𝑒𝑡 function (e.g. 𝑓ℎ )? 

- 𝒘 𝒘 𝒘 ∙𝒙 

- 𝒚= 𝑓𝑜 𝑜 ∙𝒛= 𝑓𝑜 𝑜 ∙𝑓ℎ ℎ 

we have replaced z with its expression 

## Back Propagation 

◆ What happens if, for a hidden layer, we use a _linear_ activation 𝑛𝑒𝑡= 𝑛𝑒𝑡 function (e.g. 𝑓ℎ )? 

◆ 𝒘 𝒘 𝒘 ∙𝒙 = 𝒚= 𝑓𝑜 𝑜 ∙𝒛= 𝑓𝑜 𝑜 ∙𝑓ℎ ℎ ∙ 𝒘 𝒘 ∙𝒙 𝑓𝑜 𝑜 ℎ 

**==> picture [36 x 55] intentionally omitted <==**

since 𝑛𝑒𝑡= 𝑛𝑒𝑡 𝑓ℎ 

## Back Propagation 

◆ What happens if, for a hidden layer, we use a _linear_ activation 𝑛𝑒𝑡= 𝑛𝑒𝑡 function (e.g. 𝑓ℎ )? 

- 𝒘 𝒘 𝒘 ∙𝒙 = 

- 𝒚= 𝑓𝑜 𝑜 ∙𝒛= 𝑓𝑜 𝑜 ∙𝑓ℎ ℎ ∙ 

- 𝒘 𝒘 ∙𝒙 = ∙𝒘 

- 𝑓𝑜 𝑜 ℎ 𝑓𝑜 (𝒘𝑜 ℎ) ∙𝒙 

**==> picture [36 x 55] intentionally omitted <==**

Dot product is associative 

## Back Propagation 

- What happens if, for a hidden layer, we use a _linear_ activation 𝑛𝑒𝑡= 𝑛𝑒𝑡 

- function (e.g. 𝑓ℎ )? 

- 𝒘 𝒘 𝒘 ∙𝒙 = 

- 𝒚= 𝑓𝑜 𝑜 ∙𝒛= 𝑓𝑜 𝑜 ∙𝑓ℎ ℎ 𝒘 ∙ 𝒘 ∙𝒙 = ∙𝒘 = 

- 𝑓𝑜 𝑜 ℎ 𝑓𝑜 (𝒘𝑜 ℎ) ∙𝒙 𝒘 ∙𝒙 

- 𝑓𝑜 𝑜ℎ 

**==> picture [36 x 55] intentionally omitted <==**

where 𝒘 = 𝒘 ∙𝒘 𝑜ℎ 𝑜 ℎ 

## Back Propagation 

- What happens if, for a hidden layer, we use a _linear_ activation 𝑛𝑒𝑡= 𝑛𝑒𝑡 

- function (e.g. 𝑓ℎ )? 

- 𝒘 𝒘 𝒘 ∙𝒙 = 

- 𝒚= 𝑓𝑜 𝑜 ∙𝒛= 𝑓𝑜 𝑜 ∙𝑓ℎ ℎ 𝒘 ∙ 𝒘 ∙𝒙 = ∙𝒘 = 

- 𝑓𝑜 𝑜 ℎ 𝑓𝑜 (𝒘𝑜 ℎ) ∙𝒙 𝒘 ∙𝒙 

- 𝑓𝑜 𝑜ℎ 

- Thus the network becomes like a network **without** a hidden layer!!! 

   - For this reason, hidden layers **must** have a non-linear activation function 

## MLP online graphical demonstration 

# ◆ The Tensorflow Neural Network Playground: 

http://playground.tensorflow.org/ 

## Stochastic Gradient Descent 

◆ In order to apply the gradient descent algorithm, we should compute the gradient of the loss function on **all** the samples in the training set: 

𝜕𝐿(𝒚,𝒕) 𝒘←𝒘−𝜂∙ 𝜕𝒘 

This is the loss computed on the entire training set! 

𝐿 𝒚, 𝒕= 𝐿(𝑦𝑖, 𝑡𝑖) ෍ 𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑖 

## Stochastic Gradient Descent 

- Computing the gradient wrt the whole training set before each update of the weights would be computationally expensive, except for very small sets 

- Here, we can use again the Law of Large Numbers to make the problem tractable 

## Stochastic Gradient Descent 

◆ From: 

𝐿 𝒚, 𝒕= 𝐿(𝑦𝑖, 𝑡𝑖) ෍ 𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑖 

## We can conclude that: 

𝜕𝐿 𝜕𝐿 (𝒚, 𝒕) (𝑦𝑖, 𝑡𝑖) 𝜂 = 𝜂 𝜕𝒘 ෍ 𝜕𝒘 𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑖 

## Stochastic Gradient Descent 

# ◆ Now, if the training set has 𝑁 elements, by changing the constant we can obtain: 𝜂 

**==> picture [513 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿(𝑦𝑖, 𝑡𝑖) 1 𝜕𝐿(𝑦𝑖, 𝑡𝑖)<br>𝜂 = 𝜂′<br>෍ 𝜕𝒘 ෍ 𝑁 𝜕𝒘<br>𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑥 ∈𝑇𝑟𝑎𝑖𝑛<br>𝑖 𝑖<br>**----- End of picture text -----**<br>


## Stochastic Gradient Descent 

◆ Now, if the training set has 𝑁 elements, by changing the constant we can obtain: 𝜂 

**==> picture [535 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿(𝑦𝑖, 𝑡𝑖) 1 𝜕𝐿(𝑦𝑖, 𝑡𝑖)<br>𝜂 = 𝜂′<br>෍ 𝜕𝒘 ෍ 𝑁 𝜕𝒘<br>𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑥 ∈𝑇𝑟𝑎𝑖𝑛<br>𝑖 𝑖<br>Question :<br>what is this?<br>**----- End of picture text -----**<br>


## Stochastic Gradient Descent 

## ◆ Now, if the training set has 𝑁 elements, by changing the constant we can obtain: 𝜂 

**==> picture [543 x 356] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜕𝐿(𝑦𝑖, 𝑡𝑖) 1 𝜕𝐿(𝑦𝑖, 𝑡𝑖)<br>𝜂 = 𝜂′<br>෍ 𝜕𝒘 ෍ 𝑁 𝜕𝒘<br>𝑖𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑥 ∈𝑇𝑟𝑎𝑖𝑛<br>𝑖 𝑖<br>This is the  expected value  of the<br>gradient of the loss on the training set<br>(assuming that each sample of the<br>training set is equiprobable, with<br>probability =  1/𝑁 )<br>**----- End of picture text -----**<br>


## Stochastic Gradient Descent 

# ◆ Thus, we can approximate this with an average computed on a few random samples from the training set: 

1 𝜕𝐿(𝑦𝑖, 𝑡𝑖) 1 𝜕𝐿(𝑦𝑗, 𝑡𝑗) 𝜂′ ≈𝜂′ ෍ 𝑁 𝜕𝒘 𝑚 ෍ 𝜕𝒘 𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑥 ~𝑇𝑟𝑎𝑖𝑛 𝑖 𝑗 

We take 𝑚 random samples from the training set. If 𝑚 is small, this is easier to compute than the left side 

## Stochastic Gradient Descent 

# ◆ Thus, we can approximate this with an average computed on a few random samples from the training set: 

**==> picture [553 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 𝜕𝐿(𝑦𝑖, 𝑡𝑖) 1 𝜕𝐿(𝑦𝑗, 𝑡𝑗)<br>𝜂′ ≈𝜂′<br>෍ 𝑁 𝜕𝒘 𝑚 ෍ 𝜕𝒘<br>𝑥 ∈𝑇𝑟𝑎𝑖𝑛 𝑥 ~𝑇𝑟𝑎𝑖𝑛<br>𝑖 𝑗<br>**----- End of picture text -----**<br>


We can actually get rid of the constant 1/𝑚 by incorporating it inside the constant 𝜂′ 

## Stochastic Gradient Descent 

- With this approximation, our update rule becomes: 

𝜕𝐿(𝑦 , 𝑡 ) 𝑗 𝑗 𝒘←𝒘−𝜂 ෍ 𝜕𝒘 𝑥 ~𝑇𝑟𝑎𝑖𝑛 𝑗 

▪ As a special case, we may use **a single sample** of the training set for each update ( 𝑚= 1 ) 

## Stochastic Gradient Descent 

◆ With this approximation, our update rule becomes: 

𝜕𝐿(𝑦 , 𝑡 ) 𝑗 𝑗 𝒘←𝒘−𝜂 ෍ 𝜕𝒘 𝑥 ~𝑇𝑟𝑎𝑖𝑛 𝑗 

This term is a crude approximation of the gradient wrt the whole training set (especially if 𝑚= 1 ). However, if we repeat the update many times, the "approximation errors" will compensate (even if 𝑚= 1 ). 

## Stochastic Gradient Descent 

# ◆ With this approximation, our update rule becomes: 

𝜕𝐿(𝑦 , 𝑡 ) 𝑗 𝑗 𝒘←𝒘−𝜂 ෍ 𝜕𝒘 𝑥 ~𝑇𝑟𝑎𝑖𝑛 𝑗 

- This is called **Stochastic Gradient Descent (SGD)** , because we have replaced the computation of the gradient on the whole training set with the computation of the gradient over a few random samples 

## Stochastic Gradient Descent 

◆ The convergence of the SGD can be _guaranteed_ for simple loss functions (which are _not_ the ones corresponding to MLP) if: ▪ The learning rate 𝜂 is gradually decreased, tending to 0 ▪ … but it is not decreased too fast! 

Mathematically, if we indicate with 𝜂𝑘 the learning rate used at iteration _k_ , it must be: 

∞ ∞ 2 = ∞ < ∞ 𝜂𝑘 𝜂𝑘 ෍ ෍ 𝑘=1 𝑘=1 For example, having 𝜂𝑘 ∝1/𝑘 satisfies the conditions above. 

**==> picture [42 x 53] intentionally omitted <==**

∝ means "proportional to" 

## Stochastic Gradient Descent 

◆ **Question** : the smaller the value of 𝑚 , the smaller the computational cost of the weight update. So, should you choose a value of 𝑚> 1 ? And why? 

## Stochastic Gradient Descent 

- **Question** : the smaller the value of 𝑚 , the smaller the computational cost of the weight update. So, should you choose a value of 𝑚> 1 ? And why? 

- **Answer** : with 𝑚> 1 , the stochastic approximation of the gradient becomes more accurate, and thus the algorithm should converge faster to the (local) minimum 

