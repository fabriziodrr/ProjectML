# **Machine Learning Reject option Prof. Mario Vento Prof. Diego Gragnaniello** 

## Must we always give an answer? 

◆ In many applications of classifiers, the cost  incurred as a consequence of a classification error can be so high that, in dubious cases, it may be better if the system admits its inability to process the input sample, and defer it to some alternative process (for example, a human operator) that is more expensive, but also more reliable 

## Must we always give an answer? 

- **Example** : consider an automatic system that reads the address on an envelope to perform the dispatching of (paper) mail 

- a) If the system reads correctly the address, the envelope is automatically sent to the correct destination 

   - b) If the system gives an incorrect address, the envelope is sent to the wrong place, and must be returned back and re-processed, with a waste of time and money 

   - c) If the system refuses to give an answer, a human operator has to manually enter the address; but then, the envelope arrives to its intended destination 

- Obviously, alternative c) is much better than b); however, the cost of c) is significantly higher than a) 

## Reject option 

- We want to transform a system that only gives an information 𝑥 

- about the class of the input sample into a system that may also decide to "reject" some of the samples 

- ▪ We call the additional component that perform this latter task a " **reject option** " 

## Reject option 

◆ We want to transform a system that only gives an information about the class of the input sample 𝑥 into a system that may also decide to "reject" some of the samples 

**==> picture [464 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Usually 𝑦 is an<br>Input Output output vector<br>𝑥 Original 𝑦<br>Note:<br>𝑦<br>classifier<br>**----- End of picture text -----**<br>


Note: 𝑦 is obviously a function of 𝑥 ; we will implicitly assume this relation in the following. 

This is our original classifier; we will call it a 0-reject classifier, since no input is rejected. 

## Rejection option 

- We transform a system that gives an information of the class of the input sample into a system that may decide to "reject" the input sample 

- To do this we evaluate the reliability of the classification act 

- ◆ We reject if the decision is too risky 

Classifier 

## Reject option 

- How do we decide if the given sample must be accepted or rejected? 

- We have to take into account the reliability (as an estimation of the risk of error) so as the implication of a missing decision (reject) and the cost of reject and that of an error 

## Preliminary assumptions 

- 𝐶 > 0 

- We may assume that there is a cost 𝑒 ("error cost") if a 𝐶 > 0 

- sample is accepted, but its result is wrong, and a cost 𝑟 ("reject cost") if a sample is rejected 

- **Question** : What is the relation between 𝐶 and 𝐶 ? 𝑒 𝑟 

## Preliminary assumptions 

- 𝐶 > 0 

- We may assume that there is a cost 𝑒 ("error cost") if a 𝐶 > 0 

- sample is accepted, but its result is wrong, and a cost 𝑟 ("reject cost") if a sample is rejected 

- **Question** : What is the relation between 𝐶 and 𝐶 ? 𝑒 𝑟 

- ◆ **Answer** : It must be 𝐶𝑟 < 𝐶𝑒 , otherwise it would never be convenient to reject a sample… 

## Preliminary assumptions 

- 𝐶 > 0 

- We may assume that there is a cost 𝑒 ("error cost") if a 𝐶 > 0 

- sample is accepted, but its result is wrong, and a cost 𝑟 ("reject cost") if a sample is rejected 

- **Question** : What is the relation between 𝐶 and 𝐶 ? 𝑒 𝑟 

- ◆ **Answer** : It must be 𝐶𝑟 < 𝐶𝑒 , otherwise it would never be convenient to reject a sample… 

   - Note: for simplicity we are assuming that the costs are independent of the class of the sample, and of the kind of error made by the classifier 

## Preliminary assumptions 

◆ So, we can formulate our goal as the minimization of: 𝔼 𝑥 𝐶(𝑥) where: 1 if 𝑥is accepted and 𝑦is correct 𝐶 𝐶 𝑒 if 𝑥is accepted and 𝑦is wrong 𝐶 𝑟 if 𝑥is rejected 𝑥= ൞ 

## Chow's algorithm 

- Defined by C. K. Chow in 1970 

- Assumes that the output of the classifier is, for each class, an estimate of the probability of that class: 𝑦𝑖 ≈𝑃(𝑡𝑖 = 1|𝑥) 

   - Note: This is what happens for the MLP if we use the softmax function for the last layer, **if the learning algorithm behaves perfectly** 

## Chow's algorithm 

◆ With this assumption, if we indicate with 𝑣 the class that has the maximum probability ( 𝑣= arg max 𝑦𝑖 ), what is the expected cost if 𝑖 𝑥 we accept sample ? And what is the expected cost if we reject this sample? 

## Chow's algorithm 

◆ With this assumption, if we indicate with 𝑣 the class that has the maximum probability ( 𝑣= arg max 𝑦𝑖 ), what is the expected cost if 𝑖 𝑥 we accept sample ? And what is the expected cost if we reject this sample? 

- 𝑥 : 

- If we accept sample 

𝔼 = 𝑃 𝑡 = 1 𝑥∙1 + 𝑃 𝑡 = 0 𝑥∙𝐶 𝐶(𝑥) 𝑣 𝑣 𝑒 𝑥|𝑎𝑐𝑐𝑒𝑝𝑡 ∙1 + ∙𝐶 + ∙𝐶 = 𝑦𝑣 1 −𝑦𝑣 𝑒 = 𝑦𝑣 1 −𝑦𝑣 𝑒 

- 𝑥 : 

- If we reject sample 

𝔼 = 𝐶 𝐶(𝑥) 𝑟 𝑥|𝑟𝑒𝑗𝑒𝑐𝑡 

## Chow's algorithm 

- So, we should reject if the expected cost of acceptance is larger than the expected cost of reject: 

+ ∙𝐶 > 𝐶 𝑦𝑣 1 −𝑦𝑣 𝑒 𝑟 

= 𝐶 −𝐶 ∙𝐶 𝑒 𝑟 > 𝑦𝑣 𝑒 −𝑦𝑣 𝑦𝑣 ∙(𝐶𝑒 −1) 

**==> picture [179 x 104] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐶 −𝐶<br>𝑒 𝑟<br><<br>𝑦𝑣<br>𝐶 −1<br>𝑒<br>**----- End of picture text -----**<br>


Reject if this condition is true; accept if it is false 

## Chow's algorithm limitations 

- Chow's algorithm is optimal if its assumptions are satisfied 

- What happens if the classifier does not output a probability estimate? Consider for example the LVQ classifier… 

- What happens if the probability estimate is not accurate? Consider for example that you may have overfitting problems… 

## The algorithm by M. Vento et al 

◆ M. Vento et al., " _To reject or not to reject: that is the question - An answer in case of neural classifiers_ ," in IEEE Transactions on Systems, Man, and Cybernetics, Part C, vol. 30, no. 1, pp. 84-94, 2000 

## The algorithm by M.Vento et al. 

- The basic assumptions: 

- You have a function 𝜓(𝑦) (called "reliability function") that is (positively) correlated with the reliability of the answer of the classifier 

- ▪ You have a validation set that can be used to determine an optimal threshold 𝜏 for 𝜓 𝑦 

- Thus, the rule used for the reject option has the form: ▪ 𝑥 if 

- Accept the input 𝜓(𝑦) ≥𝜏 

- ▪ 𝑥 if 

- Reject the input 𝜓 𝑦< 𝜏 

## The reliability functions 

- The paper propose several possible definitions for 𝜓(𝑦) for different kinds of neural networks 

- The proposed functions try to characterize two types of situations where the output of the classifier is likely to be wrong: 𝑥 

- a) The input is very different from all the inputs seen during the training phase 

   - b) The input 𝑥 is _ambiguous_ , in the sense that it lies near the border between two adjacent classes 

## The reliability functions 

**==> picture [227 x 294] intentionally omitted <==**

**----- Start of picture text -----**<br>
Input samples near the<br>border between two<br>classes<br>Input sample very<br>different from those in<br>the training set<br>**----- End of picture text -----**<br>


Figure from: C. De Stefano, C. Sansone and M. Vento, " _To reject or not to reject: that is the question - An answer in case of neural classifiers_ " 

## The reliability functions for MLP 

# ◆ For the MLP network, the authors propose the following to functions: 

𝜓𝑎 𝑦= 𝑦𝑣 

This tries to recognize when the sample is very different from the training set 

−max 𝜓𝑏 𝑦= 𝑦𝑣 𝑖≠𝑣[𝑦][𝑖] This tries to recognize when the sample is on the border between two classes 

## The reliability functions for LVQ 

◆ For the LVQ networks, the authors assume that each component of the output vector 𝑦𝑖 is the distance between the input 𝑥 and the vector of the weights of the closest neuron belonging to class 𝑖 ◆ In this case, tha class chosen by the classifier is obviously: 𝑣= arg min 𝑦𝑖 𝑖 

## The reliability functions for LVQ 

- For the LVQ network, the authors propose the following to functions: 

This tries to recognize when the sample is very different from the training set 

**==> picture [56 x 51] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑦𝑣<br>𝐷<br>𝑚𝑎𝑥<br>**----- End of picture text -----**<br>


**==> picture [216 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝜓𝑎 𝑦= 𝑚𝑎𝑥 0, 1 −<br>**----- End of picture text -----**<br>


where 𝐷 is defined as: 𝑚𝑎𝑥 

𝐷 = max 𝑚𝑎𝑥 𝑥∈𝑇𝑆[𝑦][𝑣] 

Maximum value of 𝑦𝑣 observed for samples of the training set 

## The reliability functions for LVQ 

## ◆ For the LVQ network, the authors propose the following to functions: 

𝜓𝑏 𝑦= 1 − 

𝑦𝑣 min 𝑖≠𝑣[𝑦][𝑖] 

**==> picture [70 x 83] intentionally omitted <==**

This tries to recognize when the sample is on the border between two classes 

## The reliability functions 

- All the proposed reliability functions have values in [0,1] (although this is not a strict requirement of the algorithm) 

- Since the authors define several reliability functions, you have to choose the one giving the best results on your validation set… 

- Alternatively, you can try to combine them (e.g. using the average, or the product) 

## How to determine the rejection threshold 

- In classification problems regarding real applications, finding a reject rule which achieves the best trade-off between error rate and reject rate is undoubtedly of practical interest. 

- The threshold 𝜎[∗] is computed by maximizing a function Ƥ which measures the classification effectiveness in the considered application domain. 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## How to define the function Ƥ 

◆ 𝑅 𝑐 : recognition rate, percentage of correctly classified samples ◆ 𝑅 𝑐[0] : recognition rate when the classifier is used at 0-reject ◆ 𝑅 : misclassification rate or error rate 𝑒 ◆ 𝑅 𝑒[0] : error rate when the classifier is used at 0-reject 

- 𝑅 𝑟 : reject rate 

- 𝐶 𝑐 : gain of each correct classification 

◆ 𝐶 : cost of each error 𝑒 

◆ 𝐶 𝑟 : cost of each rejection 

Ƥ(𝑅𝑐, 𝑅𝑒, 𝑅𝑟) = 𝐶𝑐 𝑅𝑐 −𝑅𝑐[0] −𝐶𝑒 𝑅𝑒 −𝑅𝑒[0] −𝐶𝑟𝑅𝑟 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Meaning of Ƥ 

Ƥ(𝑅𝑐, 𝑅𝑒, 𝑅𝑟) = 𝐶𝑐 𝑅𝑐 −𝑅𝑐[0] −𝐶𝑒 𝑅𝑒 −𝑅𝑒[0] −𝐶𝑟𝑅𝑟 

◆ Ƥ measures the actual effectiveness improvement when the reject option is introduced, independently of the absolute performance of the classifier at 0-reject. 

◆ The costs can be assigned by quantitatively estimating the consequences of the classification result in the particular domain: the cost of a misclassification is generally attributed by considering the burden of locating and possibly correcting the error or, if this is impossible, by evaluating the consequent damage. ◆ The cost of a reject is that of a new classification using a different technique. 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Relation between Ƥ and 𝜎 

- Since 𝑅𝑐, 𝑅𝑒, 𝑅𝑟 depend on the value 𝜎 

- of the reject threshold , Ƥ is also a function of 𝜎 . 

◆ To highlight such dependence, let 𝐷 and 𝐷 𝑐(ψ) 𝑒(ψ) be, respectively, the occurrence density curves of correctly classified and misclassified samples as a function of the value of . ψ 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Relation between Ƥ and 𝜎 

- 𝐷 

- By definition, the integrals of 𝑐(ψ) and 𝐷 𝑒(ψ) respectively provide the 

- percentage of correctly classified and misclassified samples having values of to . ψ ranging from ψ1 ψ2 

- Their trend should be such that the majority of correctly classified samples is found for high values of ψ , while misclassified samples are . 

- more frequent for low values of ψ 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Relation between Ƥ and 𝜎 

◆ It is thus possible to directly evaluate the classification rate, the error rate and the reject rate for a 𝜎 : given threshold 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Determining the optimal threshold 𝜎[∗] 

# ◆ In this way, Ƥ can be expressed as a function of 𝜎 : 

- The optimal value 𝜎[∗] of the reject threshold 𝜎 is the one for which the 0 0 

- function gets its maximum value. 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Determining the optimal threshold 𝜎[∗] 

- In practice, the functions 𝐷𝑐(ψ) and 𝐷𝑒(ψ) are not available in their analytical form and therefore, for evaluating 𝜎[∗] , they should be experimentally determined in tabular form on a set of labelled samples, adequately representative of the target domain. 

- The optimal threshold 𝜎[∗] can be eventually determined by means of . 

- an exhaustive search among the tabulated values of Ƥ(𝜎) 

Foggia, P., Sansone, C., Tortorella, F., & Vento, M. (1999). Multiclassification: reject criteria for the Bayesian combiner. Pattern recognition, 32(8), 1435-1447. 

## Determining the optimal threshold 𝜎[∗] 

- Since we have a finite number of samples in the validation set, we 𝜎 

- can limit ourselves to considering a finite number of values for 

- Let us call these values: 

𝜎 < 𝜎 < ⋯< 𝜎 < ⋯< 𝜎 1 2 𝑘 𝑚𝑎𝑥 

## Determining the optimal threshold 𝜎[∗] 

◆ You can easily choose these values and compute the corresponding values of 𝐶𝑜𝑟𝑟 and 𝐸𝑟𝑟 if you compute 𝜓 𝑦 for every sample of the validation set, and then sort the samples with respect to 𝜓 𝑦 

▪ This is similar to the computation that we used for the ROC curve… 

## Determining the optimal threshold 𝜎[∗] 

## ◆ For instance, suppose we have the following values for our validation set 

|ID#|𝜓(𝑦)|
|---|---|
|1|0.01|
|2|0.42|
|3|0.00|
|4|0.61|
|5|0.02|
|6|0.90|
|7|0.93|
|8|0.73|
|9|0.48|
|10|0.39|



## Determining the optimal threshold 𝜎[∗] 

## ◆ Here is our table sorted on 𝜓(𝑦) : 

|ID#|𝜓(𝑦)|we just need to<br>choose one value<br>of𝜏between each<br>pair of values of<br>𝜓(𝑦), plus one<br>value smaller than<br>the smallest𝜓(𝑦)<br>and one value<br>larger than the<br>largest𝜓(𝑦)|
|---|---|---|
|3|0.00||
|1|0.01||
|5|0.02||
|10|0.39||
|2|0.42||
|9|0.48||
|4|0.61||
|8|0.73||
|6|0.90||
|7|0.93||



## Determining the optimal threshold 𝜎[∗] 

## ◆ These are the values of 𝜎1, … , 𝜎𝑚𝑎𝑥 : 

|e are the values of𝜎1, … ,|𝜎𝑚𝑎𝑥:||
|---|---|---|
|ID#<br>𝜓(𝑦)<br>3<br>0.00<br>1<br>0.01<br>5<br>0.02<br>10<br>0.39<br>2<br>0.42<br>9<br>0.48<br>4<br>0.61<br>8<br>0.73<br>6<br>0.90<br>7<br>0.93|𝜎|𝜏1<br>𝜏2<br>𝜏𝑚𝑎𝑥|
||-0.100||
||0.006||
||0.014||
||0.201||
||0.403||
||0.450||
||0.546||
||0.670||
||0.814||
||0.918||
||0.942||



## Determining the optimal threshold 𝜎[∗] 

## ◆ These are the values of 𝜎1, … , 𝜎𝑚𝑎𝑥 : 

|e are the values of𝜎1, … ,|𝜎𝑚𝑎𝑥:|
|---|---|
|ID#<br>𝜓(𝑦)<br>3<br>0.00<br>1<br>0.01<br>5<br>0.02<br>10<br>0.39<br>2<br>0.42<br>9<br>0.48<br>4<br>0.61<br>8<br>0.73<br>6<br>0.90<br>7<br>0.93|𝜎|
||-0.100|
||0.006|
||0.014|
||0.201|
||0.403|
||0.450|
||0.546|
||0.670|
||0.814|
||0.918|
||0.942|



Now, for each value of 𝜏 we can simply count the correct samples and the errors that have 𝜓(𝑦) < 𝜏 These are the values of 𝐶𝑜𝑟𝑟(𝜏) and 𝐸𝑟𝑟(𝜏) 

## An algorithm to find the optimal threshold 𝜎[∗] 

1. Sort both errors and correct samples by ψ 

2. for each value of 𝜎 varying in the range of ψ : 

## An algorithm to find the optimal threshold 𝜎[∗] 

1. Sort both errors and correct samples by ψ 

2. for each value of 𝜎 varying in the range of ψ : 1. Count the errors below and above the threshold 

## An algorithm to find the optimal threshold 𝜎[∗] 

1. Sort both errors and correct samples by ψ 

2. for each value of 𝜎 varying in the range of ψ : 1. Count the errors below and above the threshold 2. Count the corrects below and above the threshold 

## An algorithm to find the optimal threshold 𝜎[∗] 

1. Sort both errors and correct samples by ψ 

2. for each value of 𝜎 varying in the range of ψ : 1. Count the errors below and above the threshold 2. Count the corrects below and above the threshold 3. Compute P(𝜎) using costs, e.g., Cr = 3, Ce = 10, Cc = 1 

## An algorithm to find the optimal threshold 𝜎[∗] 

1. Sort both errors and correct samples by ψ 

2. for each value of 𝜎 varying in the range of ψ : 1. Count the errors below and above the threshold 2. Count the corrects below and above the threshold 3. Compute P(𝜎) using costs, e.g., Cr = 3, Ce = 10, Cc = 1 

3. 𝜎 𝜎[∗] Find the maximum value of Ƥ( ), obtain 

4. σ Reject samples with ψ< 

## An algorithm to find the optimal threshold 𝜎[∗] 

||**The curve at varying of σ**|**The curve at varying of σ**|
|---|---|---|
||~~—~~|P(σ)|
|150.00|||
|100.00|||
|50.00|||
|0.00|||
|-50.00|||
|-100.00|||
|-150.00|||
||𝜓0.040.150.220.310.360.460.530.560.610.660.700.750.770.800.880.94||



## Example 

- In this example we will use the MNIST dataset and a MLP network 

   - 1 Hidden layer with 72 neurons 

   - Sigmoid activation function for the hidden layer, softmax for the activation layer 

- We will use 1/3 of the samples as training set, 1/3 as validation set and 1/3 as test set 

   - The network is trained for 40 epochs using the RMSProp optimizer 

## Example 

- Using the 𝜓𝑎 function, we have the following values for 𝐶𝑜𝑟𝑟(𝜎) and 𝐸𝑟𝑟(𝜎) : 

**==> picture [404 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝐶𝑜𝑟𝑟𝐶𝑜𝑟𝑟(𝜏)𝜎<br>𝐸𝑟𝑟(𝜏)<br>| | | |mell<br>𝐸𝑟𝑟 𝜎<br>|<br>𝐸𝑟𝑟(𝜏)<br>a<br>**----- End of picture text -----**<br>


𝜎 

## Example 

- For 𝐶𝑟 = 1, 𝐶𝑒 = 2 , using the 𝜓𝑎 function, we have the following values for the quantity 𝐸𝑟𝑟 C) 𝜎∙ ¢ 𝐶𝑟 −𝐶𝑒 ) + 𝐶𝑜𝑟𝑟 ( 𝜎∙𝐶 ) 𝑟 that we want to **minimize** : 

> 𝐶𝑜𝑠𝑡 () 𝜎 

**==> picture [75 x 36] intentionally omitted <==**

**----- Start of picture text -----**<br>
Optimal<br>threshold<br>**----- End of picture text -----**<br>


𝜎 

## Example 

- For 𝐶𝑟 = 1, 𝐶𝑒 = 4 , using the 𝜓𝑎 function, we have the following values for the quantity 𝐸𝑟𝑟 () 𝜎∙ ¢ 𝐶𝑟 −𝐶𝑒 ) + 𝐶𝑜𝑟𝑟 ( 𝜎∙𝐶 ) 𝑟 that we want to **minimize** : 

𝐶𝑜𝑠𝑡 𝜎 

**==> picture [248 x 36] intentionally omitted <==**

**----- Start of picture text -----**<br>
Optimal<br>id<br>threshold<br>**----- End of picture text -----**<br>


𝜎 

## Example 

## ◆ For 𝐶𝑟 = 1, 𝐶𝑒 = 2 we obtain the following performance (measured on the test set) 

|**Method**|𝜎|**Error**<br>**rate(%)**|**Reject**<br>**rate(%)**|**avg.**<br>**cost**|
|---|---|---|---|---|
|0-reject|-|3.91%|-|0.0782|
|Chow's algorithm|0.5|3.51%|0.58%|0.0759|
|De St. et al. with𝜓𝑎|0.588|2.97%|1.59%|**0.0753**|
|De St. et al. with𝜓𝑏|0.179|3.18%|1.21%|0.0757|



## Example 

## ◆ For 𝐶𝑟 = 1, 𝐶𝑒 = 4 we obtain the following performance (measured on the test set) 

|**Method**|𝜎|**Error**<br>**rate(%)**|**Reject**<br>**rate(%)**|**avg.**<br>**cost**|
|---|---|---|---|---|
|0-reject|-|3.91%|-|0.1564|
|Chow's algorithm|0.75|2.22%|3.51%|0.1237|
|De St. et al. with𝜓𝑎|0.875|1.52%|6.01%|0.1209|
|De St. et al. with𝜓𝑏|0.749|1.59%|5.70%|**0.1208**|



## Example 

## ◆ For 𝐶𝑟 = 1, 𝐶𝑒 = 8 we obtain the following performance (measured on the test set) 

|**Method**|𝜎|**Error**<br>**rate(%)**|**Reject**<br>**rate(%)**|**avg.**<br>**cost**|
|---|---|---|---|---|
|0-reject|-|3.91%|-|0.3128|
|Chow's algorithm|0.875|1.52%|6.02%|0.1818|
|De St. et al. with𝜓𝑎|0.970|0.76%|11.47%|0.1752|
|De St. et al. with𝜓𝑏|0.927|0.89%|10.32%|**0.1744**|



## Example 

# ◆ For 𝐶𝑟 = 1, 𝐶𝑒 = 16 we obtain the following performance (measured on the test set) 

|**Method**|𝜎|**Error**<br>**rate(%)**|**Reject**<br>**rate(%)**|**avg.**<br>**cost**|
|---|---|---|---|---|
|0-reject|-|3.91%|-|0.6256|
|Chow's algorithm|0.938|1.12%|8.54%|0.2646|
|De St. et al. with𝜓𝑎|0.981|0.55%|13.31%|**0.2219**|
|De St. et al. with𝜓𝑏|0.961|0.62%|12.91%|0.2283|



