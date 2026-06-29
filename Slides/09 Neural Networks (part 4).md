# **Machine Learning Neural Networks p.04 Prof. Mario Vento Prof. Diego Gragnaniello** 

## Stochastic Gradient Descent 

- The "basic" algorithm for training a MLP 

- Training is divided into "epochs" 

   - One epoch correspond to one complete iteration over the training set 

◆ At each epoch, the training samples are **shuffled** , and divided into _**mini-batches**_ of equal size 𝑚 ▪ If 𝑚= 1 , completely "on line" learning ▪ If 𝑚= _size of the training set_ , completely "batch" learning ▪ Usually 𝑚 is a small value >  1 for performance reasons (e.g. 𝑚= 32 or 64 ) 

## Stochastic Gradient Descent 

- For each mini-batch, the gradients for the samples in the minibatch are computed and accumulated (i.e. added into an accumulator vector) 

- The weights are updated at the end of the mini-batch using the accumulated gradients 

- If a validation set is available, at the end of each epoch, performance on the validation set is computed 

- ▪ This can be used to decide whether to stop the training or not 

## Stochastic Gradient Descent 

## ◆ The pseudo-code: 

**`1. Initialize weights with random values`** 

**`2. REPEAT epoch`** 

**`3.   Shuffle the training samples`** 

**`4.   FOR EACH mini-batch`** 

**`5.     Reset the gradient accumulation variables`** 

**`6.     FOR EACH sample in the mini-batch`** 

**`7.       Forward Pass (Compute the output of each layer)`** 

**`8.       Backward Pass (Compute and propagate the gradients)`** 

**`9.       Accumulate the gradients`** 

**`10.    END FOR`** 

**`11.    Update Weights (using the accumulated gradients) 12.  END FOR`** 

**`13.  Compute performance on Training/Validation set 14.UNTIL MaxEpochs OR StopCriterion(performance)`** 

## Stochastic Gradient Descent 

- Random initialization of weights is **fundamental** (if all the neurons are initially equal, the network cannot learn!) 

▪ Can you explain why? 

- Remember that Gradient Descent ensures only a local optimum 

- ▪ Retrying with different initial weights may yield different results 

## Early Stopping 

◆ Sometimes the network may go into overfitting ▪ Training loss decreases, but validation loss increases ▪ Solution: early stopping based on validation performance 

## Early Stopping 

## ◆ Beware! You may stop too soon! 

▪ No guarantee that the loss function has a single minimum wrt the training epochs! 

07 —_ train you may erroneously val. 0.6 stop here 0.5 you should Loss stop here 

It is safer to go ahead for a while after you find the validation optimal performance, BUT keeping saved the best weights found so far (not just the latest weights). 

Epochs 

## Early Stopping 

## ◆ Why Early Stopping works? 

**==> picture [960 x 540] intentionally omitted <==**

**----- Start of picture text -----**<br>
Early Stopping Initial weights<br>**----- End of picture text -----**<br>


## Early Stopping 

**==> picture [323 x 180] intentionally omitted <==**

**==> picture [122 x 98] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial weights<br>After 1 epoch,<br>weights might<br>be here<br>**----- End of picture text -----**<br>


**==> picture [235 x 35] intentionally omitted <==**

**----- Start of picture text -----**<br>
Early Stopping<br>**----- End of picture text -----**<br>


**==> picture [282 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial weights<br>After 1 epoch,<br>weights might<br>be here<br>After 2 epochs,<br>weights might<br>be here<br>**----- End of picture text -----**<br>


**==> picture [347 x 216] intentionally omitted <==**

**==> picture [960 x 540] intentionally omitted <==**

**----- Start of picture text -----**<br>
Early Stopping Initial weights<br>After 1 epoch,<br>weights might<br>be here<br>After 2 epochs,<br>weights might<br>be here<br>After 3 epochs,<br>weights might<br>be here<br>**----- End of picture text -----**<br>


## Early Stopping 

- So, Early Stopping makes the learning algorithm _prefer_ weights that are not too far from their initial values 

does this reminds you of something? 

## Early Stopping 

- So, Early Stopping makes the learning algorithm _prefer_ weights that are not too far from their initial values 

- In other words, Early Stopping is (implicitly) a form of 

   - **regularization** 

## Momentum 

- SGD may have oscillation problems that may delay the convergence to the (local) minimum 

   - Especially if 𝑚 is too small 

◆ A possible solution is to reduce the changes of direction by simulating a physical momentum (part of the previous "velocity" of change is kept in the next iteration): 

## Momentum 

## ◆ The update rule becomes: 

**==> picture [737 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
Increment computed for current  Increment used for previous step<br>step<br>𝜕𝐿<br>Δ𝑤 ← ∙Δ𝑤<br>𝑘 𝜇 𝑘 −𝜂∙<br>𝜕𝑤<br>𝑘<br>𝑤 ←𝑤 + Δ𝑤<br>𝑘 𝑘 𝑘<br>▪ 𝜇  is a hyper-parameter  ∈[0, 1[<br>**----- End of picture text -----**<br>


## Momentum 

## ◆ The update rule becomes: 

𝜕𝐿 Δ𝑤 ← ∙Δ𝑤 𝑘 𝜇 𝑘 −𝜂∙ 𝜕𝑤 𝑘 

## 𝑤 ←𝑤 + Δ𝑤 𝑘 𝑘 𝑘 

- 𝜕𝐿 

- ▪ If 𝜕𝑤 𝑘[ changes its sign between consecutive steps ("oscillations"), the value ] 

- of Δ𝑤𝑘 is reduced (with respect to the SGD update rule) 

- 𝜕𝐿 

- ▪ Instead, if Δ𝑤𝑘 𝜕𝑤 𝑘[ keeps its sign between consecutive steps, the value of ] 

- is increased 

## Momentum 

## "level" curves of the loss function 

**==> picture [266 x 81] intentionally omitted <==**

**==> picture [264 x 70] intentionally omitted <==**

Steps without the use of momentum 

Steps with the use of momentum; the horizontal component of the steps is increased, and the vertical component is reduced 

- No guarantee that momentum will improve the convergence rate! 

- ▪ Sometimes it may get worse!  (no free lunch) 

## Adaptive learning rate 

- Several algorithms more recent than SGD are based on the idea of dynamically changing the learning rate to speed-up convergence 

▪ NAG 

- Adagrad 

- Adadelta 

- Rmsprop 

- ▪ ADAM 

- Also, these algorithms often use a different learning rate for each component of the 𝒘 vector 

# Adaptive learning rate 

## Regularization 

- Other regularization techniques (besides Early Stopping) can be applied to MLP networks 

   - The loss function is modified adding a regularization term, weighted by a hyperparameter: 

𝐿= 𝐿 𝑤 𝑦, 𝑡+ 𝜆∙𝐿 𝑟𝑒𝑔 

- Common regularization terms: 

   - L[2] regularization (the additional term is the sum of the squares of the 𝑤 

   - weights 𝑖 ) 

   - L[1] regularization (the additional term is the sum of the absolute values of 𝑤 

   - the weights 𝑖 ) 

   - Elastic net regularization (a combination of L[1] and L[2] ) 

## Common activation functions 

- Sigmoid, aka logistic 

◆ Hyperbolic tangent (tanh) f(net) = t(net) = 20(2- net) —1 

## Common activation functions 

- For regression problems, the output layer (only!) typically uses the identity function 

   - This is often called "linear" activation 

𝑓 𝑛𝑒𝑡= 𝑛𝑒𝑡 

## Common activation functions 

# ◆ **Question** : can you compute the derivatives of the three activation functions we have seen? 

## Common activation functions 

**==> picture [648 x 425] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑑 𝑑 1<br>𝑑𝑛𝑒𝑡 [𝜎(𝑛𝑒𝑡) =] 𝑑𝑛𝑒𝑡 1 + 𝑒 [−𝑛𝑒𝑡] [=]<br>1<br>− =<br>−1<br>[∙𝑒][−𝑛𝑒𝑡] [∙]<br>1 + 𝑒 [−𝑛𝑒𝑡2]<br>𝑒 [−𝑛𝑒𝑡]<br>[=]<br>1 + 𝑒 [−𝑛𝑒𝑡2]<br>1 + 𝑒 [−𝑛𝑒𝑡] −1<br>[=]<br>1 + 𝑒 [−𝑛𝑒𝑡2]<br>1 1 + 𝑒 [−𝑛𝑒𝑡] −1<br>=<br>1 + 𝑒 [−𝑛𝑒𝑡] [∙] 1 + 𝑒 [−𝑛𝑒𝑡]<br>1 1<br>1 − = 𝜎(𝑛𝑒𝑡) ∙ 1 −𝜎(𝑛𝑒𝑡)<br>1 + 𝑒 [−𝑛𝑒𝑡] [∙] 1 + 𝑒 [−𝑛𝑒𝑡]<br>**----- End of picture text -----**<br>


## Common activation functions 

**==> picture [656 x 429] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑑<br>1 −𝜎(𝑛𝑒𝑡)<br>𝑑𝑛𝑒𝑡 [𝜎(𝑛𝑒𝑡) = 𝜎(𝑛𝑒𝑡) ∙]<br>sigmoid<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>sigma(net) sigma'(net)<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6<br>**----- End of picture text -----**<br>


## Common activation functions 

𝑑 𝑑 2 ∙𝑛𝑒𝑡−1) = 𝑑𝑛𝑒𝑡[𝑡𝑎𝑛ℎ(𝑛𝑒𝑡) =] 𝑑𝑛𝑒𝑡[(2𝜎] 𝑑 4 𝑛𝑒𝑡= 𝑑𝑛𝑒𝑡[𝜎] 

= 4 ∙𝜎(𝑛𝑒𝑡) ∙ 1 −𝜎(𝑛𝑒𝑡) 1 1 ∙ = 4 ∙ tanh 𝑛𝑒𝑡+ 1 1 − tanh 𝑛𝑒𝑡+ 1 2[∙] 2[∙] tanh 𝑛𝑒𝑡+ 1 ∙(1 −tanh 𝑛𝑒𝑡) 

## Common activation functions 

𝑑 tanh 𝑛𝑒𝑡+ 1 ∙(1 −tanh 𝑛𝑒𝑡) 𝑑𝑛𝑒𝑡[𝑡𝑎ℎ𝑛(𝑛𝑒𝑡) =] 

**==> picture [523 x 349] intentionally omitted <==**

**----- Start of picture text -----**<br>
tanh<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6<br>-0.2<br>-0.4<br>-0.6<br>-0.8<br>-1<br>**----- End of picture text -----**<br>


tanh(net) tanh'(net) 

## Common activation functions 

𝑑 𝑑𝑛𝑒𝑡[𝑙𝑖𝑛𝑒𝑎𝑟(𝑛𝑒𝑡) = 1] 

linear 

**==> picture [472 x 337] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>2.5<br>2<br>1.5<br>1<br>0.5<br>0<br>-3 -2.5 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 2.5 3<br>-0.5<br>-1<br>-1.5<br>-2<br>-2.5<br>-3<br>**----- End of picture text -----**<br>


linear(net) linear'(net) 

## MLP as regressor 

- When the network is used as a regressor, the **linear** function is commonly used for the output layer 

- A common choice for the loss function is the _Mean Squared Error_ (MSE): 

𝑠−1 𝐿 (𝑡 −𝑦 )[2] 𝑗 𝑗 𝑦, 𝑡= ෍ 𝑗=0 

𝑗 -th component of 𝑦 

𝑗 -th component of 𝑡 

## MLP as regressor 

- When the network is used as a regressor, the **linear** function is commonly used for the output layer 

◆ An alternative choice is the _Mean Absolute Error_ (MAE): 𝑠−1 𝐿 𝑡 −𝑦 𝑗 𝑗 𝑦, 𝑡= ෍ 𝑗=0 

𝑗 -th component of 𝑦 

𝑗 -th component of 𝑡 

## MLP as a regressor 

# ◆ Q: What is the difference between MSE and MAE? ▪ Will I obtain a different result if I choose one of the two functions? 

## MLP as a regressor 

- Q: What is the difference between MSE and MAE? 

- ▪ Will I obtain a different result if I choose one of the two functions? 

- To answer the previous question, we will make the following simplifying assumptions: 

   1. 𝑡 and 𝑦 are uni-dimensional (they are real numbers) 

2. 𝑥 𝑡 The relationship between (the network input) and is probabilistic, and represented by a conditional probability density 𝑝 𝑡𝑥 3. The learning algorithm works perfectly (it finds the true global minimum of the expected value of the loss) 

## MLP as a regressor 

- Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MSE loss? 

𝑦[∗] = arg min 𝑡−𝑦[2] 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)] 

Expected value of the MSE loss Optimal 𝑦 

## MLP as a regressor 

- Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MSE loss? 

𝑦[∗] = arg min 𝑡−𝑦[2] 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)] = arg min 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)][ (𝑡][2][ −2 ∙𝑦∙𝑡+ 𝑦][2][)] 

**==> picture [41 x 52] intentionally omitted <==**

**==> picture [37 x 48] intentionally omitted <==**

We can ignore this term because it does not depend on 𝑦 

We can take 2𝑦 and out of the 𝑦[2] expected value 

## MLP as a regressor 

◆ Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MSE loss? 

**==> picture [461 x 143] intentionally omitted <==**

We can minimize this by taking the derivative with respect to 𝑦 and equating it to 0 

## MLP as a regressor 

𝑑 = 0 𝑦[2] −2 ∙𝑦∙𝔼 (𝑡) 𝑡~𝑝(𝑡|𝑥) 𝑑𝑦 2 ∙𝑦−2 ∙𝔼 𝑡𝑥 𝑡= 0 𝑡~𝑝 𝔼 𝑡 𝑦= 𝑡𝑥 𝑡~𝑝 

## MLP as a regressor 

- Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MSE loss? 

**==> picture [461 x 180] intentionally omitted <==**

## MLP as a regressor 

- Thus, using the MSE error, a _perfect_ learning algorithm will produce as its output 𝑦 the _expected value_ of 𝑡 given the input 𝑥 

_What happens if we use MAE?_ 

## MLP as a regressor 

- Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MAE loss? 

𝑦[∗] = arg min 𝑡−𝑦 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)] 

Optimal 𝑦 

Expected value of the MAE loss 

## MLP as a regressor 

◆ Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MAE loss? 

𝑦[∗] = arg min 𝑡−𝑦 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)] 

**==> picture [272 x 62] intentionally omitted <==**

We can replace the expected value with its definition 

## MLP as a regressor 

- Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MAE loss? 

𝑦[∗] = arg min 𝑡−𝑦 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)] 𝑦 +∞ 𝑡𝑥𝑑𝑡 = arg min 𝑦−𝑡𝑝 𝑡−𝑦𝑝 𝑦 න−∞ 𝑡𝑥𝑑𝑡+ න𝑦 

We can minimize this by taking the derivative with respect to 𝑦 and equating it to 0 

## MLP as a regressor 

**==> picture [648 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑑 𝑦 𝑑 +∞<br>𝑡𝑥𝑑𝑡+ 𝑡𝑥𝑑𝑡= 0<br>𝑦−𝑡𝑝 𝑡−𝑦𝑝<br>𝑑𝑦 [න] −∞ 𝑑𝑦 [න] 𝑦<br>We can swap the derivatives and the integrals<br>𝑦 𝑑 +∞ 𝑑<br>𝑡𝑥𝑑𝑡= 0<br>𝑦−𝑡𝑝 𝑡−𝑦𝑝<br>න−∞ 𝑑𝑦 𝑡𝑥𝑑𝑡+ න𝑦 𝑑𝑦<br>+1 -1<br>𝑦 +∞<br>𝑡𝑥𝑑𝑡= 0<br>𝑝 𝑝<br>න−∞ 𝑡𝑥𝑑𝑡−න𝑦<br>**----- End of picture text -----**<br>


## MLP as a regressor 

**==> picture [436 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑦 +∞<br>𝑡𝑥𝑑𝑡= 0<br>𝑝 𝑝<br>න−∞ 𝑡𝑥𝑑𝑡−න𝑦<br>This is  𝑃𝑟𝑜𝑏{𝑡≤𝑦|𝑥} This is  1 −𝑃𝑟𝑜𝑏{𝑡≤𝑦|𝑥}<br>**----- End of picture text -----**<br>


**==> picture [261 x 29] intentionally omitted <==**

𝑃𝑟𝑜𝑏 𝑡≤𝑦|𝑥= 1/2 

1 What is the value of such that 𝑃𝑟𝑜𝑏 𝑦 𝑡≤𝑦= 2[?] 

## MLP as a regressor 

- Under the previous assumptions, what is the optimal value of 𝑦 if the algorithm minimizes the MAE loss? 

𝑦[∗] = arg min 𝑡−𝑦 𝑦[𝔼][𝑡~𝑝(𝑡|𝑥)] 𝑦 +∞ 𝑡𝑥𝑑𝑡 = arg min 𝑦−𝑡𝑝 𝑡−𝑦𝑝 𝑦 න−∞ 𝑡𝑥𝑑𝑡+ න𝑦 = median(𝑡|𝑥) Yes, it's the median! 

## MLP as a regressor 

- Thus, using the MSE error, a _perfect_ learning algorithm will produce as its output 𝑦 the _expected value_ of 𝑡 given the input 𝑥 

- Using the MAE error, a _perfect_ learning algorithm will produce as its output 𝑦 the _median_ of 𝑡 given the input 𝑥 

## MLP as regressor 

- **Question** : What is the derivative wrt 𝑦 of the previous loss functions? 

- **Exercise (homework)** : Can you derive the weight update rule for a network having: 

   - Only an output layer (no hidden layers) 

   - The linear activation function 

   - The Mean Square Error as loss function 

   - Does this weight update rule resemble something we have already encountered? 

## MLP as binary classifier 

◆ **Question** : If 𝑡 can only have the values 1 or 0 with probability masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using MSE and using MAE? 

## MLP as binary classifier 

◆ **Question** : If 𝑡 can only have the values 1 or 0 with probability masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using MSE and using MAE? 

- For MSE: 

𝑦= 𝔼 𝑡= 0 ∙𝑃 𝑡= 0 𝑥+ 1 ∙𝑃 𝑡= 1 𝑥= 𝑃(𝑡= 1|𝑥) 𝑡∼𝑃(𝑡|𝑥) 

◆ For MAE: 0 if 𝑃 𝑡= 0 𝑥> 𝑃(𝑡= 1|𝑥) 1 if 𝑃 𝑡= 0 𝑥< 𝑃(𝑡= 1|𝑥) 1/2 if 𝑃 𝑡= 0 𝑥= 𝑃(𝑡= 1|𝑥) 𝑦= 𝑚𝑒𝑑𝑖𝑎𝑛(𝑡|𝑥) = ൞ 

## MLP as binary classifier 

- When the network is used as a binary classifier, the **sigmoid** function is commonly used for the output layer 

- The output value 𝑦 is interpreted as probability for one of the classes (the other probability is obviously 1 −𝑦 ) 

- A sample is assigned to class "+" if 𝑦 >  0.5 and to class "-" if 𝑦 <  0.5 

   - 0.5 is a "tie", and can be assigned indifferently to each class (in pratice, this will occurs with extremely low probability) 

## Binary Cross-Entropy 

- For a binary classifier, the Mean Square Error is not a good choice for the loss function: 

◆ In the training set, we have as desired output the class (represented as **0** or **1** ), and not the _probability_ of the class. Thus the MSE could give a high loss value even for perfect classification! 

- A better choice is _**binary cross-entropy** ,_ defined as: 𝐿 𝑦, 𝑡= −[𝑡log 𝑦+ 1 −𝑡log(1 −𝑦)] 

   - **Question** : what is the derivative of 𝐿 wrt ? 𝑦 

## Binary Cross-Entropy 

◆ A better choice is _**binary cross-entropy** ,_ defined as: 𝐿 𝑦, 𝑡= −[𝑡log 𝑦+ 1 −𝑡log(1 −𝑦)] 

• **Question** : what is the derivative of 𝐿 wrt ? 𝑦 

**==> picture [466 x 206] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑑<br>=<br>𝑡∙log 𝑦+ 1 −𝑡∙log 1 −𝑦<br>𝑑𝑦 [−]<br>𝑑log 𝑦 𝑑log 1 −𝑦<br>− =<br>−𝑡∙ 1 −𝑡∙<br>𝑑𝑦 𝑑𝑦<br>𝑡 1 −𝑡<br>−<br>𝑦 [+] 1 −𝑦<br>**----- End of picture text -----**<br>


## Binary Cross-Entropy 

- A better choice is _**binary cross-entropy** ,_ defined as: 𝐿 𝑦, 𝑡= −[𝑡log 𝑦+ 1 −𝑡log(1 −𝑦)] 

• **Question** : what is the derivative of 𝐿 wrt ? 𝑦 

**==> picture [647 x 276] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑑<br>=<br>𝑡∙log 𝑦+ 1 −𝑡∙log 1 −𝑦<br>𝑑𝑦 [−]<br>𝑑log 𝑦 𝑑log 1 −𝑦<br>− =<br>−𝑡∙ 1 −𝑡∙<br>𝑑𝑦 𝑑𝑦<br>𝑡 1 −𝑡<br>−<br>𝑦 [+] 1 −𝑦<br>For  𝑡= 1  we have<br>For  𝑡= 0  we have<br>only this part<br>only this part<br>**----- End of picture text -----**<br>


## Binary Cross-Entropy 

◆ **Question** : If 𝑡 can only have the values 1 or 0 with probability masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using the Binary Cross-Entropy (BCE) loss function? 

## Binary Cross-Entropy 

- **Question** : If 𝑡 can only have the values 1 or 0 with probability 

   - masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using the Binary Cross-Entropy (BCE) loss function? 

𝑦[∗] = arg min 1 −𝑡log(1 −𝑦)] 𝑦[𝔼][𝑡~𝑃(𝑡|𝑥)][ −[𝑡log 𝑦+] 

**==> picture [42 x 71] intentionally omitted <==**

We can replace the expected value with its definition 

## Binary Cross-Entropy 

◆ **Question** : If 𝑡 can only have the values 1 or 0 with probability masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using the Binary Cross-Entropy (BCE) loss function? 

𝑦[∗] = arg min 1 −𝑡log(1 −𝑦)] 𝑦[𝔼][𝑡~𝑃(𝑡|𝑥)][ −[𝑡log 𝑦+] 

For 𝑡= 0 we can ignore this part 

For 𝑡= 1 we can ignore this part 

## Binary Cross-Entropy 

◆ **Question** : If 𝑡 can only have the values 1 or 0 with probability masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using the Binary Cross-Entropy (BCE) loss function? 

𝑦[∗] = arg min 1 −𝑡log(1 −𝑦)] 𝑦[𝔼][𝑡~𝑃(𝑡|𝑥)][ −[𝑡log 𝑦+] = arg min 𝑡= 0 𝑥∙ −log 1 −𝑦 + 𝑃 𝑡= 1 𝑥∙[−log 𝑦] 𝑦[𝑃] 

We can minimize this by taking the derivative with respect to 𝑦 and equating it to 0 

## Binary Cross-Entropy 

**==> picture [648 x 320] intentionally omitted <==**

**==> picture [723 x 179] intentionally omitted <==**

**==> picture [518 x 182] intentionally omitted <==**

𝑡= 1 𝑥 𝑦= 𝑃 

## Binary Cross-Entropy 

◆ **Question** : If 𝑡 can only have the values 1 or 0 with probability masses 𝑃(𝑡= 1|𝑥) and 𝑃 𝑡= 0 𝑥= 1 −𝑃(𝑡= 1|𝑥) ,  what is the output found by a _perfect_ learning algorithm using the Binary Cross-Entropy (BCE) loss function? 

𝑦[∗] = arg min 1 −𝑡log(1 −𝑦)] 𝑦[𝔼][𝑡~𝑃(𝑡|𝑥)][ −[𝑡log 𝑦+] = arg min 𝑡= 0 𝑥∙ −log 1 −𝑦 + 𝑃 𝑡= 1 𝑥∙[−log 𝑦] 𝑦[𝑃] = 𝑃(𝑡= 1|𝑥) 

So, the BCE will lead to the same result that we had with the MSE. Then, why should we use the BCE? 

## Why is binary cross-entropy better than MSE (for 

## binary classifiers)? 

- Suppose we have a sample with true class 𝑡= 0 and the network has output 𝑦≈1 

◆ Remember our activation is a sigmoid 

**==> picture [332 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
a@ y<br>net<br>“SO? 0 2 4 6<br>We should be there<br>**----- End of picture text -----**<br>


We are here 

## Why is binary cross-entropy better than MSE (for binary classifiers)? 

- Suppose we have a sample with true class 𝑡= 0 and the network has output 𝑦≈1 

◆ Remember our activation is a sigmoid 

We are here y **Problem** : here the derivative of y is **small** ; so, because of the chain rule, the back propagation algorithm will move the weights **slowly** a@ net “SO? 0 2 4 6 We should be there 

## Why is binary cross-entropy better than MSE (for binary classifiers)? 

◆ **But** : the derivative of the output activation function is multiplied by the derivative of the loss function… 

**==> picture [31 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Loss<br>**----- End of picture text -----**<br>


**==> picture [699 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
2.5<br>If  𝑦  is wrong (in this<br>2<br>case   around 1 for<br>𝑦<br>𝑡= 0 ) the derivative<br>1.5<br>of the loss function<br>is much higher for<br>1<br>the  cross-<br>binary<br>entropy (it tends to<br>infinity) 0.5<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>𝑦<br>MSE Loss Bin. Cross-entr.<br>**----- End of picture text -----**<br>


For 𝑡= 0 

## Why is binary cross-entropy better than MSE (for binary classifiers)? 

◆ **But** : the derivative of the output activation function is multiplied by the derivative of the loss function… 

**==> picture [705 x 331] intentionally omitted <==**

**----- Start of picture text -----**<br>
Loss derivative with respect to y, for t=0<br>20<br>18 Derivative of<br>If  𝑦  is wrong (in this  16 1<br>=<br>BCE<br>case   around 1 for<br>𝑦 14<br>1−𝑦<br>𝑡= 0 ) the derivative  12<br>of the loss function<br>10 Derivative of<br>is much higher for<br>8 MSE = 2𝑦<br>the  cross-<br>binary<br>6<br>entropy (it tends to<br>4<br>infinity)<br>2<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>dMSE/dy dBCE/dy 𝑦<br>**----- End of picture text -----**<br>


For 𝑡= 0 

## Why is binary cross-entropy better than MSE (for 

## binary classifiers)? 

- If we consider the combined effect of the derivative of 𝜎(𝑛𝑒𝑡) and the derivative of the loss function we have: 

Derivative of Loss with respect to net, for t=0 

**==> picture [701 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>Derivative of<br>0.9<br>BCE wrt  𝑛𝑒𝑡<br>0.8<br>0.7 Derivative of<br>𝑑𝐿 𝑑𝐿 𝑑𝑦<br>MSE wrt  𝑛𝑒𝑡<br>0.6<br>𝑑𝑛𝑒𝑡 [=] 𝑑𝑦 [∙] 𝑑𝑛𝑒𝑡<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6<br>𝑛𝑒𝑡<br>For  𝑡= 0 dMSE/dnet dBCE/dnet<br>**----- End of picture text -----**<br>


## Why is binary cross-entropy better than MSE (for binary classifiers)? 

◆ If we consider the combined effect of the derivative of 𝜎(𝑛𝑒𝑡) and the derivative of the loss function we have: 

**==> picture [711 x 376] intentionally omitted <==**

**----- Start of picture text -----**<br>
Derivative of Loss with respect to net, for t=0<br>1<br>0.9<br>0.8<br>𝑑𝐿 𝑑𝐿 𝑑𝑦 0.7<br>0.6<br>𝑑𝑛𝑒𝑡 [=] 𝑑𝑦 [∙] 𝑑𝑛𝑒𝑡 This is bad : the<br>0.5<br>result is wrong,<br>0.4 but the gradient is<br>small (in absolute<br>0.3 value)<br>0.2<br>0.1<br>0<br>-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6<br>𝑛𝑒𝑡<br>For  𝑡= 0 dMSE/dnet dBCE/dnet<br>**----- End of picture text -----**<br>


## MLP as multi-class classifier 

- Usually, for _s_ classes, the network uses a _**one-hot encoding**_ : 

   - The network has _s_ outputs 

   - ▪ In the ground truth, all the outputs are 0 except the one corresponding to the correct class, which is one 

- Example: 

   - With _s_ =4 

      - Class 0 is represented as [1 0 0 0] 

      - Class 1 is represented as [0 1 0 0] 

      - • Class 2 is represented as [0 0 1 0] 

      - • Class 3 is represented as [0 0 0 1] 

## MLP as multi-class classifier 

- In this case, using a sigmoid activation for the output layer would not give the best results 

   - While each output is in [0, 1], they cannot be interpreted as probability since their sum is not guaranteed to be 1 

- A better choice is the _**softmax**_ activation: 

For the _k_ -th component of the output, 

𝑒[𝑛𝑒𝑡][𝑘] 

= 𝑛𝑒𝑡 𝑦𝑘 = 𝑓 𝑘 𝑠−1 𝑗 𝑒[𝑛𝑒𝑡] σ 𝑗=0 

- Notice that the value of 𝑦𝑘 depends on all the other neurons in the output layer! 

## MLP as multi-class classifier 

◆ **Question** : suppose that for a particular 𝑘 , 𝑛𝑒𝑡𝑘 ≫𝑛𝑒𝑡 , ∀𝑗≠𝑘 𝑗 

- What would be the value of ? 𝑦𝑘 

- ▪ What would be the value of for ? 𝑦 𝑗≠𝑘 𝑗 

## MLP as multi-class classifier 

- **Question** : suppose that for a particular 𝑘 , 𝑛𝑒𝑡𝑘 ≫𝑛𝑒𝑡 , ∀𝑗≠𝑘 𝑗 

   - What would be the value of ? 𝑦𝑘 

   - What would be the value of for ? 𝑦 𝑗≠𝑘 𝑗 

- **Answer** : in this case 𝑒[𝑛𝑒𝑡][𝑗] /𝑒[𝑛𝑒𝑡][𝑘] ≈0 for 𝑗≠𝑘 ; thus: 

▪ ≈1 𝑦𝑘 

▪ ≈0 𝑦 𝑗≠𝑘 

## MLP as multi-class classifier 

◆ A good loss function for this case is _**categorical cross-entropy** :_ 

**==> picture [268 x 95] intentionally omitted <==**

Since we are using a 1-hot encoding, only one of the 𝑡𝑗 will be ≠0 

## MLP as multi-class classifier 

◆ A good loss function for this case is _**categorical cross-entropy** :_ 

**==> picture [268 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑠−1<br>𝐿 𝑡<br>log 𝑦<br>𝑗 𝑗<br>𝑦, 𝑡= −෍<br>𝑗=0<br>**----- End of picture text -----**<br>


- The properties of this loss are similar to those of BCE: 

- ▪ With a perfect learning algorithm, 𝑦𝑘 will tend to 𝑃(𝑡𝑘 = 1|𝑥) 

- ▪ The gradient of 𝐿 with respect to 𝑛𝑒𝑡𝑘 will not become small if the current value of 𝑦𝑘 is wrong 

## MLP as a multi-class classifier 

- Example: suppose that we have a 3-class classification problem, 1 𝑡 = 1 

- and that the network is examining a sample of class (so 1 while 𝑡 = 𝑡 2 3 = 0) 

- For the 3 output neurons, suppose that 𝑛𝑒𝑡2 = 1 and 𝑛𝑒𝑡3 = −1 ; 𝑛𝑒𝑡 ? 

- if we change 1 , what will be the values of 𝑦1, 𝑦2, 𝑦3 

## MLP as a multi-class classifier 

Softmax outputs with net2=1, net3=-1 

**==> picture [511 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>-6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6<br>y1 y2 y3 net1<br>**----- End of picture text -----**<br>


## MLP as a multi-class classifier 

Here are the gradients of the Categorical Cross-Entropy with respect to net1, net2 and net3 (with the softmax activation) 

**==> picture [621 x 351] intentionally omitted <==**

**----- Start of picture text -----**<br>
Gradient of the CCE loss wrt net1, net2 and net3, for net2=1, net3=-1<br>3<br>2.5<br>2<br>t =1<br>1<br>1.5<br>t =t =0<br>2 3<br>1<br>0.5<br>0<br>-6 -4 -2 0 2 4 6<br>-0.5<br>-1<br>-1.5<br>**----- End of picture text -----**<br>


dL/dnet1 dL/dnet2 dL/dnet3 net1 

## MLP as a multi-class classifier 

Here are the gradients of the Categorical Cross-Entropy with respect to net1, net2 and net3 (with the softmax activation) 

Gradient of the CCE loss wrt net1, net2 and net3, for net2=1, net3=-1 

**==> picture [621 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>Notice that even if the loss<br>2.5 depends only on  𝑦_1<br>(because  𝑡_2=𝑡_3=0) , the<br>2 gradient wrt net2 and net3<br>t =1 is not null (because  𝑦_1<br>1<br>1.5<br>t =t =0 depends also on net2 and<br>2 3<br>net3)<br>1<br>0.5<br>0<br>-6 -4 -2 0 2 4 6<br>-0.5<br>-1<br>-1.5<br>dL/dnet1 dL/dnet2 dL/dnet3 net1<br>**----- End of picture text -----**<br>


