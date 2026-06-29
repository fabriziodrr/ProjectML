# **Machine Learning Foundations p.03 Prof. Mario Vento Prof. Diego Gragnaniello** 

## Dataset Augmentation 

◆ In some applications, we can find some "transformations" that are easy to apply, and we are sure that they **do not affect** the desired result 

## Dataset Augmentation 

# ◆ Example: Object recognition from an image 

**==> picture [244 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
mirror<br>rescale<br>Hyer ih<br>Original<br>image<br>rotate<br>**----- End of picture text -----**<br>


## Dataset Augmentation 

- We can extend ("augment") the training set applying randomly these transformations 

   - We reduce the overfitting 

   - In this way, we make our system "robust" with respect to those transformations 

- We must be sure that the transformations do not change the desired output 

   - Example: for digit recognition, we cannot turn an image upside-down, since '6' would be confused with '9' 

## Dataset Augmentation 

## ◆ Way 1 

▪ Given a training set T, we generate a larger training set T' by applying to each element x in T a set of transformations 𝜏 𝜏 in advance 1,…, k decided (including the "null" transformation that leaves x as it is) 

**==> picture [338 x 24] intentionally omitted <==**

- Applicable when T is small and the number of possible transformations is also small 

   - But sometimes you have "infinite" possible transformations: e.g., rotations of an image can be performed with different angles. What can you do then? 

## Dataset Augmentation 

## ◆ Way 2 

   - Each time the learning algorithm needs a sample from the training set T: 

      - A sample x is chosen from T 

      - A set of transformations 𝜏 1,…, 𝜏 k is chosen according to a probability distribution 

      - 𝑥[′] = 𝜏 𝜏 …𝜏 𝑥 

      - The learning algorithm is given 𝑘 𝑘−1 1 

- Applicable when the learning algorithm performs several iterations over the training set (or subsets of it) 

- ▪ As we will see, this is the case with Neural Networks 

## Dataset Augmentation 

- **Question** : if we find a way to generate an unlimited number of augmented data (e.g. by applying some randomized transformations), can we solve our learning task even if we start with a small initial training set? 

- **Hint** : What are the characteristics that a training set should have to be considered good? 

## Dataset Augmentation 

- **Answer** : augmented data are **not independent** from the original data used to generate them 

   - Additionally, augmentation may alter the probability distribution with respect to the original input space 

- Thus, while augmentation may help reducing the overfitting problem, a very large dataset obtained _only_ through augmentation may still be inadequate for the learning task 

## Regularization 

- One way to reduce variance / overfitting is to modify a learning algorithm so that it _prefers_ "simpler" solutions over "complex" ones 

   - The "no free lunch" theorem tells that we cannot do this in a general way, 

   - but must taylor it to the specific problem we want to solve 

   - If our learning algorithm is formulated as an optimization problem wrt the 

   - parameters, we can easily do this by slightly modifying the performance function to be optimized 

## Regularization 

- Without regularization: 

𝜃[∗] = arg min𝜃 𝐿(𝜃, 𝑇𝑟𝑎𝑖𝑛) 

- With regularization: 

   - 𝜃[∗] 𝐿 = arg min𝜃 𝜃, 𝑇𝑟𝑎𝑖𝑛+ 𝜆∙𝑅(𝜃) 

**==> picture [77 x 64] intentionally omitted <==**

**==> picture [84 x 63] intentionally omitted <==**

hyper-parameter used to control the strength of regularization 

additional loss term measuring how "complex" are the parameters; does not depend on the training set 

## Regularization example 

- Suppose we have the following training set, obtained by adding noise to a sinusoidal function: 

## Regularization example 

## ◆ We try to fit a 14 degree polynomial _without regularization_ 

## Regularization example 

**==> picture [831 x 158] intentionally omitted <==**

- In this way, the learning algorithm will prefer polynomials with smaller 

- coefficients over polynomials with larger ones 

- How much this preference is taken into account will depend on the value of 𝜆 

## Regularization example 

◆ 𝜆 =0.1    (underfitting): 

## Regularization example 

# ◆ 𝜆 =0.01    (less underfitting): 

## Regularization example 

◆ 𝜆 =0.001    (almost optimal): 

## Regularization 

# ◆ **Question** : regularization reduces the overfitting; so it is always beneficial to add regularization to a learning algorithm? 

## Regularization 

- **Answer** : regularization reduces the variance error, but it 

      - increases the bias error. 

- Thus, it may improve the result, but also make it worse, depending on the balance between the two effects 

   - In other words, "no free lunch"… 

## Performance evaluation 

◆ Until now, we have assumed that the same performance/loss function is used both on the training set (during the training phase) to find the optimal parameters, and on the validation/test set to evaluate how well the system performs the intended task 

## Performance evaluation 

- However, the learning algorithm may impose some constraints on the function (e.g. we will see that neural networks require a _differentiable_ function) 

- On the other hand, the evaluation of the performance on the test set should reflect the needs of the application, even if this requires a performance measure that is not suitable for the learning algorithm 

## Performance evaluation 

- In the following, we will see some measures that are frequently used in applications to evaluate the performance of a classification system 

- These measures reflect the needs of the application, and are typically used for the validation and test sets 

- ▪ as we will see in a future lecture, different measures are used for the _training_ of a classification system 

## Performance evaluation: accuracy 

- A very common measure for classification problems: 

   - 𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦= 

- # 𝑜𝑓𝑠𝑎𝑚𝑝𝑙𝑒𝑠𝑐𝑜𝑟𝑟𝑒𝑐𝑡𝑙𝑦𝑐𝑙𝑎𝑠𝑠𝑖𝑓𝑖𝑒𝑑 

# 𝑜𝑓𝑡𝑜𝑡𝑎𝑙𝑠𝑎𝑚𝑝𝑙𝑒𝑠 

   - 𝐸𝑟𝑟𝑜𝑟= 1 −𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 

- Works well with _closed-world_ problems 

   - Closed-world: the sample **must** belong to one of the classes 

- For open-world problems: you may add a pseudo-class "Others" (also during the training) 

## Performance evaluation: accuracy 

• **Question** : accuracy, as defined before, is measured on a finite set of values (e.g. the validation set or the test set). But, according to the Law of Large Numbers, it can be interpreted as an estimate of some property related to future data. **Which property is estimated by accuracy?** 

## Performance evaluation: accuracy 

- **Answer** : accuracy estimates the **probability** that the classifier gives the correct answer on future data. 

   - This can be easily shown by considering that accuracy is the _average_ of the following function:[if 𝑓] 𝑥is correct. 

   - 𝐶𝑜𝑟𝑟𝑒𝑐𝑡 𝑓, 𝑥= 0 if 𝑓 𝑥is not correct 

   - ቊ[1] 

and the expected value 𝔼𝑥[𝐶𝑜𝑟𝑟𝑒𝑐𝑡 𝑓, 𝑥] is equal to the probability that the classifier 𝑓 is correct. 

## Performance evaluation: accuracy 

- Accuracy considers all the errors equivalent 

- In many real world problems, different kinds of error may have different consequences 

   - **Example** : consider a system used for the quick test for CoViD-19: 

      - what are the consequences if a person with the disease is classified as "negative"? 

      - and what if a person without the disease is classified as "positive"? 

## Classification matrix 

||**class 1**|**class 2**|**class 3**|
|---|---|---|---|
|**class 1**|77%|12%|11%|
|**class 2**|8%|83%|9%|
|**class 3**|8%|0%|92%|
|Samples of true class 2 that<br>the system assigned to class 1||||



- Gives a better picture of the system performance 

- But it is not a single number… 

## Classification matrix 

||**class 1**|**class 2**|**class 3**|
|---|---|---|---|
|**class 1**|77%|12%|11%|
|**class 2**|8%|83%|9%|
|**class 3**|8%|0%|92%|



- In the matrix you can report the actual number of samples for each true class/assigned class combination 

- Alternatively, you can report the percentages with respect to each row, or with respect to each column 

   - **Warning** : If you use the percentages, you should be aware of whether they are computed on rows or on columns, since the meaning is different! 

## Classification matrix 

## Class assigned by the system 

|True class||**class 1**|**class 2**|**class 3**|
|---|---|---|---|---|
||**class 1**|77%|12%|11%|
||**class 2**|8%|83%|9%|
||**class 3**|8%|0%|92%|



- **Question** : given the classification matrix above, can we conclude that, when the system assigns class 1, in most of the cases the true class is also class 1? 

## Classification matrix 

## Class assigned by the system 

|True class||**class 1**|**class 2**|**class 3**|
|---|---|---|---|---|
||**class 1**|77%|12%|11%|
||**class 2**|8%|83%|9%|
||**class 3**|8%|0%|92%|



- **Answer** : No. The table above reports the percentage per row (the sum of each row is 100%); so the values on different rows are not directly comparable. 

## Classification matrix 

## Class assigned by the system 

|True class||**class 1**|**class 2**|**class 3**|
|---|---|---|---|---|
||**class 1**|77%|12%|11%|
||**class 2**|8%|83%|9%|
||**class 3**|8%|0%|92%|



- From the table, we know that 77% of the samples of class 1 are assigned to class 1, and 8% of the sample of class 2 are assigned to class 1. 

- What if in the dataset we have 100 samples of class 1, and 1000 samples of class 2? 

## Classification matrix 

## Class assigned by the system 

|True class||**class 1**|**class 2**|**class 3**|
|---|---|---|---|---|
||**class 1**|77%|12%|11%|
||**class 2**|8%|83%|9%|
||**class 3**|8%|0%|92%|



- What if in the dataset we have 100 samples of class 1, and 1000 samples of class 2? 

- In this case, 77 samples of class 1 are assigned to class 1, and 80 samples of class 2 are assigned to class 1. **So, if a sample is assigned to class 1, it is more likely that it belongs to true class 2 than to true class 1!** 

## Binary classifiers 

- Only two classes, usually called **positive** (+) and **negative** (-) 

- A very important case in many applications 

- True Positive (TP): positive samples classified as positive 

- True Negative (TN): negative samples classified as negative 

- • False Negative (FN): positive samples classified as negative 

- • False Positive (FP): negative samples classified as positive 

**Question** : what is the relation between TP, TN, FP, FN and the classification matrix? 

## Precision and Recall 

- Total samples: Tot=TP+TN+FP+FN 

- Accuracy = (TP+TN)/Tot 

- Error = (FP+FN)/Tot 

- **measures** : 

- **Two important** 

- **Precision** : how many of the samples classified as positive are truly positive? 

   - Precision = TP / (TP + FP) 

- **Recall** : how many of the truly positive samples are classified as positive? 

   - Recall = TP / (TP + FN) 

## Precision and Recall 

- **High precision** : the system is mostly right when it says "positive" (no false alarms) 

- **High recall** : the system is mostly right when it says "negative" (no _missed_ samples) 

## Example 

- A system for recognizing if an image contains a car (Positive = car, Negative=no car) 

- We gave the system 25 test images (12 positive, 13 negative); we had the following responses: 

## System response 

|truth||Car|No car|
|---|---|---|---|
||Car|8|4|
||No car|1|12|



- **Question** : What is the precision? What is the recall? 

## Example 

- A system for recognizing if an image contains a car (Positive = car, Negative=no car) 

- We gave the system 25 test images (12 positive, 13 negative); we had the following responses: 

## System response 

|truth||Car|No car|
|---|---|---|---|
||Car|8|4|
||No car|1|12|



- Precision= 8 / (8+1) = 88.9% 

- Recall= 8 / (8+4) = 66.7% 

## Another example 

- Company ACME Pharmaceuticals has developed a new test for a rare disease 

   - _A priori_ probability of the disease is: 

𝑃 • 𝑃+𝑁[= 10][−4] 

- Accuracy on people having the disease is reported to be: 100% 

- ▪ Accuracy on people not having the disease is reported to be: 99% 

- ◆ We get tested, and our result is **positive** 

**Should we be worried?** 

## Another example 

- Let us compute Precision and Recall for this test… 

- We know that, out of 10000 persons, 9999 are healthy and 1 has the disease 

   - On the 9999 healthy people, 1% of errors 

## System response 

|truth||Positive|Negative|
|---|---|---|---|
||Disease|1|0|
||Healthy|100|9899|



**Precision and recall?** 

## Another example 

- Let us compute Precision and Recall for this test… 

- We know that, out of 10000 persons, 9999 are healthy and 1 has the disease 

   - On the 9999 healthy people, 1% of errors 

## System response 

|truth||Positive|Negative|
|---|---|---|---|
||Disease|1|0|
||Healthy|100|9899|



**Precision: 1%            Recall: 100%** So the system is only credible when it says "Negative" 

## F-Score / F-Index 

- Used to have a synthetic measure comprising both precision and recall 

- Harmonic mean of precision and recall: 

2∙𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∙𝑅𝑒𝑐𝑎𝑙𝑙 

◆ 𝐹 −𝑠𝑐𝑜𝑟𝑒= 1 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙 

**Question** : why the harmonic mean and not the arithmetic mean? **Hint** : consider what happens when one precision/recall is very small 

## Tunable systems 

- Many binary classifiers can be "tuned", by changing an operating 𝜏 

- parameter (usually a threshold) for having more precision or more recall 

   - 𝜏 𝜏 in 

   - Example: _Choose "Positive" if probability> , else "Negative"_ (higher this case gives higher precision and lower recall) 

## Tunable systems 

◆ Changing 𝜏 we have a different balance of the two kinds of error: 

**==> picture [464 x 307] intentionally omitted <==**

**----- Start of picture text -----**<br>
False positive rate<br>𝐹𝑃<br>𝐹𝑃+ 𝑇𝑁<br>on<br>Na False negative rate<br>𝐹𝑁<br>𝑇𝑃+ 𝐹𝑁<br>𝜏<br>Tunable operating<br>parameter<br>**----- End of picture text -----**<br>


## ROC Curve 

- Acronym of "Receiver Operating Characteristic" 

- Condenses in one chart the relation between the two kinds of 𝜏 

- error when varying 

- 𝜏 is implicit in the curve (each point of the curve represents a different value of 𝜏 ) 

**==> picture [692 x 234] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑇𝑃 & OO<br>𝑇𝑃+ 𝐹𝑁 Each point<br>> / correspond to a<br>different  𝜏<br>This is recall. QQ], This is NOT<br>o | / precision<br>Also, it is the<br>complement<br>of the FN  𝐹𝑃<br>rate.<br>False positive rate ————<br>𝐹𝑃+ 𝑇𝑁<br>**----- End of picture text -----**<br>


## ROC Curve 

Here the system Here the system answers always answers always "negative" (TP=0) "positive" (TN=0) 100% ee O ~~D~~ So / |] // | // 0% 0% 100% 

## ROC Curve 

**==> picture [899 x 406] intentionally omitted <==**

**----- Start of picture text -----**<br>
◆ The more the ROC is close to the "ideal" curve (green),<br>the better the detector → better  class separation<br>Here the system<br>gives always the  Ideal system<br>a correct answer<br>a<br>100%<br>2<br>g<br>D // ROC<br>9<br>/<br>®/<br>0%<br>0% 100%<br>**----- End of picture text -----**<br>


## ROC Curve 

- The more the ROC is close to the "ideal" curve (green), 

- the better the detector → better **class separation** 

- ◆ Sometimes, the **area under the ROC curve (AUROC)** is used as a performance measure 

Ideal system 

100% The area under the curve is 1 for the ideal system. g / It becomes D / ROC smaller as the 9 / real curve becomes more ®/ different from the ideal one. 0% 0% 100% 

## ROC Curve: an example 

◆ Suppose we have trained a binary classifier; for each sample 𝑥 the system outputs a real value 𝑓(𝑥) ∈[0,1] that represents an estimate of the probability that sample is in the "positive" class 

## ROC Curve: an example 

- Suppose we have a test set with 10 samples, and the results on the test set are given by the following table: 

|ID#|True class|Classifier output|For each𝑥𝑖<br>in the test<br>set, this is<br>the value of<br>𝑓(𝑥𝑖)|
|---|---|---|---|
|1|0|0.01||
|2|0|0.42||
|3|0|0.00||
|4|0|0.61||
|5|0|0.02||
|6|1|0.90||
|7|1|0.93||
|8|1|0.73||
|9|1|0.48||
|10|1|0.39||



## ROC Curve: an example 

◆ We can use our classifier as a tunable system by introducing an 𝜏 operating parameter and interpreting the classifier output in this way:[if][𝑓] 𝑥≤𝜏 𝐶𝑙𝑎𝑠𝑠 1 if 𝑥> 𝜏 𝑓 𝑥= ቊ[0] 

## ROC Curve: an example 

## ◆ For instance, choosing 𝜏= 0.4 : 

||ID#|True class|Classifier output|Assigned class||False|
|---|---|---|---|---|---|---|
||1|0|0.01|0||Positives|
||2|0|0.42|1|||
||3|0|0.00|0|||
||4|0|0.61|1|||
||5|0|0.02|0|||
||6|1|0.90|1|||
||7|1|0.93|1|||
||8|1|0.73|1|||
||9|1|0.48|1||False|
||10|1|0.39|0||Negative|



## ROC Curve: an example 

## ◆ If we change 𝜏= 0.6 : 

||ID#|True class|Classifier output|Assigned class||False|
|---|---|---|---|---|---|---|
||1|0|0.01|0||Positive|
||2|0|0.42|0|||
||3|0|0.00|0|||
||4|0|0.61|1|||
||5|0|0.02|0|||
||6|1|0.90|1|||
||7|1|0.93|1|||
||8|1|0.73|1|||
||9|1|0.48|0||False|
||10|1|0.39|0||Negatives|



For our system, a smaller value of 𝜏 means more False Positive; a 𝜏 larger value of means more False Negatives 

## ROC Curve: an example 

- If we want to obtain the ROC curve, we need to compute the 𝜏 

- number of TP, TN, FP and FN for every value of 

- However, since the samples in the test set are finite, the process is simple. We can: 

   - First, sort the samples according to the value of 𝑓(𝑥) 

   - and then choose some values of 𝜏 that are between adjacent values of 𝑓(𝑥) 

## ROC Curve: an example 

## ◆ Here is our table sorted on 𝑓(𝑥) : 

||ID#|True class|Classifier output||||
|---|---|---|---|---|---|---|
||3<br>1|0<br>0|0.00<br>0.01|||we just need to<br>choose one value|
||5|0|0.02|||of𝜏between each|
||10|1|0.39|||pair of values of|
||2<br>9<br>4|0<br>1<br>0|0.42<br>0.48<br>0.61|||𝑓(𝑥), plus one<br>value smaller than<br>the smallest𝑓(𝑥)<br>and one value|
||8|1|0.73|||larger than the|
||6|1|0.90|||largest𝑓(𝑥)|
||||||||
||7|1|0.93||||



## ROC Curve: an example 

## ◆ Here is our table sorted on 𝑓(𝑥) : 

**==> picture [572 x 357] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||
|---|---|---|---|
|𝜏|
|ID#|True class|Classifier output|-|
|0.100|
|3|0|0.00|
|0.006|
|1|0|0.01|
|0.014|
|5|0|0.02|
|0.201|
|10|1|0.39|
|0.403|
|2|0|0.42|
|0.450|
|9|1|0.48|
|0.546|
|4|0|0.61|
|0.670|
|8|1|0.73|
|0.814|
|6|1|0.90|
|0.918|
|7|1|0.93|
|0.942|

**----- End of picture text -----**<br>


## ROC Curve: an example ◆ Now, for each value of 𝜏 we can count the number of TP, TN, FP and FN: 

||𝜏|TP|TN|FP|FN||
|---|---|---|---|---|---|---|
||-0.100|5|0|5|0||
||0.006|5|1|4|0||
||0.014|5|2|3|0||
||0.201|5|3|2|0||
||0.403|4|3|2|1||
||0.450|4|4|1|1||
||0.546|3|4|1|2||
||0.670|3|5|0|2||
||0.814|2|5|0|3||
||0.918|1|5|0|4||
||0.942|0|5|0|5||



## ROC Curve: an example 

- From TP, TN, FP and FN, we can compute the TP rate and the FP rate: 

|𝜏|TP|TN|FP|FN|TP rate|FP rate|
|---|---|---|---|---|---|---|
|-0.100|5|0|5|0|1|1|
|0.006|5|1|4|0|1|0.8|
|0.014|5|2|3|0|1|0.6|
|0.201|5|3|2|0|1|0.4|
|0.403|4|3|2|1|0.8|0.4|
|0.450|4|4|1|1|0.8|0.2|
|0.546|3|4|1|2|0.6|0.2|
|0.670|3|5|0|2|0.6|0|
|0.814|2|5|0|3|0.4|0|
|0.918|1|5|0|4|0.2|0|
|0.942|0|5|0|5|0|0|



## ROC Curve: an example 

- Finally, the TP rate and FP rate can be plotted to obtain the ROC curve: 

Each point correspond to a different 𝜏 

**==> picture [531 x 321] intentionally omitted <==**

**----- Start of picture text -----**<br>
ROC curve<br>TP  1<br>rate 0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.2 0.4 0.6 0.8 1<br>**----- End of picture text -----**<br>


FP rate 

## ROC Curve: an example 

◆ We can also easily compute the Area Under the ROC curve: 

**==> picture [646 x 317] intentionally omitted <==**

**----- Start of picture text -----**<br>
AUROC=0.88<br>ROC curve<br>TP  1<br>rate 0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.2 0.4 0.6 0.8 1<br>**----- End of picture text -----**<br>


FP rate 

