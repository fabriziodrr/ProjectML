# **Machine Learning Foundations p.01 Prof. Mario Vento Prof. Diego Gragnaniello** 

## Before we start… 

- … we will briefly refresh our memory about probability (see Chapter 3 of the textbook) 

- **Random variabile** : a variable that can take different values randomly 

   - Example: the temperature in a room 

## Discrete random variable 

- **Discrete random variable** : a random variable that takes value from an enumerable set of values 

• Examples: the next number of a dice 

𝑥∈𝑋= {𝑥1, 𝑥2, … } 

**Question** : does the set X need to be finite? 

## Discrete random variable 

- **Discrete random variable** : a random variable that takes value from an enumerable set of values 

• Examples: the next number of a dice 

𝑥∈𝑋= {𝑥1, 𝑥2, … } 

**Question** : does the set X need to be finite? **Hint** : Consider as an example the set of the natural numbers. Is it an enumerable set? 

## Discrete random variable 

- A discrete random variable 𝑥 is associated to a **Probability Mass Function** 𝑃: 𝑋→ℝ having the following properties: 

𝑃 𝑥 ≥0 ∀𝑥 ∈𝑋 𝑖 𝑖 𝑃 𝑥 = 1 𝑖 ෍ 𝑖 

## Discrete random variable 

- A discrete random variable 𝑥 is associated to a **Probability Mass Function** 𝑃: 𝑋→ℝ having the following properties: 

𝑃 𝑥 ≥0 ∀𝑥 ∈𝑋 𝑖 𝑖 𝑃 𝑥 = 1 𝑖 ෍ 𝑖 **Question** : What is the maximum value that 𝑃 𝑥𝑖 can have? 

## Discrete random variable 

• Examples of discrete random variable 𝑥 and associated to a **Probability Mass Function** 𝑃: 𝑋→ℝ 

- _Fair_ coin: 

**==> picture [116 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
• 𝑥 =T or C<br>𝑖<br>• = 1<br>𝑃 𝑥<br>( 𝑖 ) Τ2<br>**----- End of picture text -----**<br>


• 6-faces fair dice: • 𝑥𝑖 = 𝑖, 𝑖= 1, … , 6 • = 1 𝑃 𝑥 : 𝑖 Τ6 

**==> picture [155 x 300] intentionally omitted <==**

**----- Start of picture text -----**<br>
PT) 𝑥𝑖 𝑃 𝑥𝑖<br>1 1ൗ2<br>2 1ൗ2<br>en 𝑥𝑖 𝑃 𝑥𝑖<br>1 1ൗ6<br>2 1ൗ6<br>3 1ൗ6<br>4 1ൗ6<br>5 1ൗ6<br>6 1ൗ6<br>**----- End of picture text -----**<br>


## Continuous random variable 

- A **continuous random variable** is a random variable that takes value from a continuous set of values 𝑥∈𝑋 

   - A continuous set 𝑋 has always an infinite number of elements 

   - 𝑋 does not need to be of dimension 1; for instance, it can be: 𝑋⊆ℝ[𝑛] 

## Continuous random variable 

- A continuous random variable 𝑥 is associated to a **Probability Density Function** 𝑝: 𝑋→ℝ having the following properties: 

𝑥≥0 ∀𝑥∈𝑋 𝑝 𝑥𝑑𝑥= 1 𝑝 න 𝑋 **Question** : What is the maximum value that 𝑝 𝑥 can have? 

## Continuous random variable 

- A continuous random variable 𝑥 is associated to a **Probability Density Function** 𝑝: 𝑋→ℝ having the following properties: 

𝑥≥0 ∀𝑥∈𝑋 𝑝 𝑥𝑑𝑥= 1 𝑝 න 𝑋 **Question** : What is the maximum value that 𝑝 𝑥 can have? **Hint** : If you have answered 1, your answer is wrong. 

## Expected value 

- Given a random variable 𝑥∈𝑋 and a function 𝑓: 𝑋→ℝ , the **expected value** of 𝑓 is defined as follows: 

For a discrete 𝑥 : 

For a continuous 𝑥 : 

𝔼 𝑃 𝑥[𝑓 𝑥𝑓(𝑥) 𝑥] ≝෍ 𝑥 𝔼 𝑥𝑑𝑥 𝑥[𝑓 𝑝 𝑥𝑓 𝑥] ≝න 𝑋 

## Expected value 

## • Examples 

**==> picture [653 x 362] intentionally omitted <==**

**----- Start of picture text -----**<br>
on 𝑥𝑖 𝑃 𝑥𝑖<br>• 1 1ൗ2<br>Fair  coin:<br>• 𝑥 =T or C 2 1ൗ2<br>𝑖<br>3<br>• 𝑃 𝑥 = 1 𝔼𝑥[𝑥] ൗ2<br>( 𝑖 ) Τ2<br>•<br>𝔼𝑥 > 𝑥= 1.5<br>𝑥𝑖 𝑃 𝑥𝑖<br>a ee<br>1 1ൗ6<br>• 2 1ൗ6<br>6-faces fair dice:<br>• 3 1ൗ6<br>𝑥𝑖 = 𝑖, 𝑖= 1, … , 6<br>• 𝑃 𝑥 = 1 4 1ൗ6<br>𝑖 Τ6<br>• ; 5 1 ,<br>𝔼𝑥 [ 𝑥= 3.5 | ൗ6<br>6 1ൗ6<br>𝔼 𝑥 21<br>P| 𝑥[ ] ൗ6<br>**----- End of picture text -----**<br>


## Example 

- Problem: 6-faces **unfair** dice: 

   - the result «3» has increased probability by 10% 

   - the result «2» has decreased probability by 10% 

• 𝑥𝑖 = 𝑖, 𝑖= 1, … , 6 

|𝑥𝑖|𝑃<br>𝑥𝑖|
|---|---|
|1|ൗ<br>1 6|
|**2**|?|
|**3**|?|
|4|ൗ<br>1 6|
|5|ൗ<br>1 6|
|6|ൗ<br>1 6|
|𝔼𝑥[𝑥]|?|



## Example 

- Problem: 6-faces **unfair** dice: 

   - the result «3» has increased probability by 10% 

   - the result «2» has decreased probability by 10% 

**==> picture [623 x 241] intentionally omitted <==**

**----- Start of picture text -----**<br>
• 𝑥𝑖 = 𝑖, 𝑖= 1, … , 6 en 𝑥𝑖 𝑃 𝑥𝑖<br>• = 1 1 1<br>𝑃 () 𝑥𝑖 Τ6 , 𝑖≠2,3 ൗ6<br>• 𝑃 𝑥 = 1 1 2 1 2 1<br>( 2 ) Τ6 −Τ10 = Τ30 = Τ15 ൗ15<br>• 𝑃 () 𝑥3 = 1Τ6 + 1Τ10 = 8Τ30 = 4Τ15 3 4ൗ15<br>4 1ൗ6<br>5 1ൗ6<br>6 1ൗ6<br>𝔼 𝑥 ?<br>𝑥[ ]<br>|<br>**----- End of picture text -----**<br>


## Example 

## • Problem: 6-faces **unfair** dice: 

- the result «3» has increased probability by 10% 

- • the result «2» has decreased probability by 10% 

**==> picture [623 x 242] intentionally omitted <==**

## Example 

- Problem: 6-faces **unfair** dice: 

   - the result «3» has increased probability by 10% 

   - the result «2» has decreased probability by 10% 

   - What happens if you bet on even numbers against odd ones? 

|𝑥𝑖|𝑃<br>𝑥𝑖|
|---|---|
|1|ൗ<br>1 6|
|**2**|ൗ<br>1 15|
|**3**|ൗ<br>4 15|
|4|ൗ<br>1 6|
|5|ൗ<br>1 6|
|6|ൗ<br>1 6|
|𝔼𝑥[𝑥]|ൗ<br>18 5|



## Example 

- Problem: 6-faces **unfair** dice: 

   - the result «3» has increased probability by 10% 

   - the result «2» has decreased probability by 10% 

   - What happens if you bet on even numbers against odd ones? 

• 1 1 1 𝑃 𝑒𝑣𝑒𝑛= () Τ15 + Τ6 + Τ6 = 0.4 • 4 1 1 𝑃 ( 𝑜𝑑𝑑= ) Τ15 + Τ6 + Τ6 = 0.6 

|𝑥𝑖<br>𝑃<br>𝑥𝑖<br>~~Pt~~|𝑥𝑖<br>𝑃<br>𝑥𝑖<br>~~Pt~~|
|---|---|
|1|ൗ<br>1 6|
|**2**|ൗ<br>1 15|
|**3**|ൗ<br>4 15|
|4|ൗ<br>1 6|
|5|ൗ<br>1 6|
|6<br>~~|~~|ൗ<br>1 6|
|𝔼𝑥[𝑥]<br>~~|~~|ൗ<br>18 5|



## Samples and the Law of Large Numbers 

- Given a random variable 𝑥 with probability mass 𝑃 or probability density 𝑝 , we use the notations: 

**==> picture [234 x 81] intentionally omitted <==**

to denote that 𝑥 are **observations** 1, 𝑥2, … , 𝑥𝑘 **samples** (i.e. individual ) of 𝑥 . 

## Samples and the Law of Large Numbers 

• Informally, we say that two samples 𝑥𝑖 and 𝑥𝑗 are **independent** if the way we have obtained the observations ensures that the value of 𝑥𝑖 is not affected by the value of 𝑥 and vice versa 𝑗 **Question** : do you remember the _formal_ definition of independence? **Hint** : It is related to the _joint_ probability mass/density of 𝑥𝑖 and 𝑥𝑗 

## Samples and the Law of Large Numbers 

- The **Law of Large Numbers** states that (under rather general conditions) you can approximate the expected value of a function with the arithmetic mean of the function computed on a large number of independent samples: 

1 𝑛 lim 𝑓(𝑥𝑖) = 𝔼𝑥[𝑓 𝑥] 𝑛→∞ 𝑛[෍] 𝑖=1 where the 𝑥𝑖 are independent samples of the random variable 𝑥 . 

## Samples and the Law of Large Numbers 

**==> picture [371 x 90] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 𝑛<br>lim<br>𝑓(𝑥𝑖) = 𝔼𝑥[𝑓 𝑥]<br>𝑛→∞ 𝑛 [෍]<br>𝑖=1<br>**----- End of picture text -----**<br>


To compute this, you need to know the probability mass/density function. Also, in the continuous case, you need to compute an integral 

## Samples and the Law of Large Numbers 

**==> picture [403 x 248] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 𝑛<br>lim<br>𝑓(𝑥𝑖) = 𝔼𝑥[𝑓 𝑥]<br>𝑛→∞ 𝑛 [෍]<br>𝑖=1<br> n<br>To compute this, you only need<br>independent samples of the random<br>variable  𝑥 (much more convenient)<br>**----- End of picture text -----**<br>


## Samples and the Law of Large Numbers 

1 𝑛 lim 𝑓(𝑥𝑖) = 𝔼𝑥[𝑓 𝑥] 𝑛→∞ 𝑛[෍] 𝑖=1 

- Example: fair coin tossing 

   - _Fair_ coin: Large Number of observations: 

   - • 𝑥 = T or C TTCTCCTTCCTTTCTCTCCTTC… 𝑖 

   - • = 1 𝑃 𝑥 𝑖 Τ2 The larger the number of tosses 

   - • −→𝔼𝑥 𝑓 𝑥 = 1.5 →The more # of Ts equals to # of Cs! 1 

   - = 

   - → 𝑃 𝑥𝑖 Τ2 → 𝔼𝑥 𝑓 𝑥 = 1.5 

## Samples and the Law of Large Numbers 

- 1 𝑛 𝑥 

- 𝑓(𝑥𝑖) ≅𝔼𝑥 𝑓 

- 𝑛[෍] 𝑖=1 

- • Almost all machine learning methods use the Law of Large Numbers to approximate the expected value of some function with the average computed over a finite number of samples 

- Remember that this approximation is good only if 

   - _n_ is large enough 

   - 𝑥 

   - the samples respect the probability distribution of 

   - the samples are independent 

## Basic Machine Learning concepts 

- **Training set** : a finite set of data that is given to the learning algorithm 

   - **For supervised learning** : the training set includes both examples of inputs to the function to be learned, and the corresponding desired outputs 

   - **For unsupervised learning** : the training set includes only examples of input data 

   - **For reinforcement learning** : there is no training set 

- The training set is composed by samples of the data on which the desired system will be required to operate 

## Availability of the training set 

- Learning scenarios may differ depending on _when_ the training set is available 

   - Batch Learning 

   - Incremental learning 

   - Lifelong or natural learning 

## Availability of the training set 

- Batch Learning 

   - The algorithm receives in advance all the training data, and performs the learning operation on it ( **Training Phase** ) 

   - Subsequently, the trained algorithm is used for solving new problems ( **Working Phase** ) without further learning 

**Training phase Working phase** The entire training set is available here New problems, but the system does not change 

**Note:** in Machine Learning, the term "Batch" is used also in an entirely unrelated meaning, that we will introuce in the context of neural networks 

## Availability of the training set 

- Incremental learning 

   - Only a part of the required training data is initially available, and it is used to perform an initial training of the algorithm. After a first training phase, the algorithm is put in a working phase. 

   - During the working phase, the algorithm does not learn. However, it may be used to collect new data. 

   - ▪ Periodically, the new data collected is used for a new training phase, in which the algorithm improves its performance. 

**==> picture [538 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
…<br>Training Working Training Working<br>Initial training data Additional training data<br>New problems New problems<br>**----- End of picture text -----**<br>


## Availability of the training set 

• Lifelong or natural learning (aka online learning) ▪ Only a part of the required training data is initially available, and it is used to perform an initial training of the algorithm 

- Subsequently, the algorithm is used for solving new problems, but can use the the information obtained on the corresponding new data to improve its performance (simultaneous working and training) ▪ **Note:** This requires that in the working phase the system has some kind of feedback on its performance 

**==> picture [494 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial training Working + Training<br>/ SSA | 7<br>Initial training data<br>New problems; the system<br>also learns from them<br>**----- End of picture text -----**<br>


## Types of data 

• The information provided to a learning-based system can be of different types; the learning algorithms that can be used depend on the kind of input data you have 

## Types of data 

- Numeric data 

   - Values associated to some measurable characteristic 

• Examples: height of a person; intensity level of a pixel in an image 

- Can be continuous or discrete (quantized) 

- Often an individual example is represented by several values, called _**features**_ , collected in a vector ( _**feature vector**_ ) 

   - Example: a person may be rapresented using: (age, height, weight) 

- Multi-dimensional vectors are possible (e.g. an image can be represented as a bi-dimensional vector) 

## Types of data 

- Categorical data 

   - Choice in a finite set, representing qualitative characteristics, or the presence/absence of some property 

      - Example: Blood type: 0, A, B, AB 

      - Example: Education Level: High-school, Bachelor, Master, PhD 

   - NOTE: Although the choice can be _encoded_ with numeric values, numeric operations are “semantically” not meaningful 

      - For example, you can encode the Blood type as follows: 0-->0, A-->1, B-->2, AB-->3 

      - ▪ In this case, does it have any meaning to compute the arithmetic mean of the Blood type of a group of persons? 

## Types of data 

- "One-hot encoding" for categorical data 

   - A choice with 𝑘 distinct values is encoded using a numerical vector with 𝑘 components; all components have the value 0 except the one corresponding to the specific value of the categorical information, which has the value 1 

   - • Example, for the blood types seen before: 

|**Blood type**|**One-hot**<br>**encoding**|**One-hot**<br>**encoding**|**One-hot**<br>**encoding**|**One-hot**<br>**encoding**|
|---|---|---|---|---|
|0|1|0|0|0|
|A|0|1|0|0|
|B|0|0|1|0|
|AB|0|0|0|1|



- Many learning algorithms (e.g. neural networks) work better if categorical data use one-hot encoding 

## Types of data 

- Structured data 

   - Strings or sequences: variable-length sequences of values, where the position in the sequence and the relation with predecessors/successors have an important meaning 

      - Example: An audio stream 

   - Trees: structures made of components connected by hierarchical relationships 

      - Example: an HTML document 

   - Graphs: structures made of components (nodes) connected by general relationships (edges) 

      - Example: a chemical compound, where the atoms are represented by nodes and the chemical bonds by edges 

## Data representation 

- Given an object of interest for your application, you can have different ways of representing it with a set of data 

   - Different kinds of measurements 

   - Different levels of detail 

   - Different ways of representing the information 

   - As a designer of a system, you may have the possibility of influencing, at least to some extent, some aspects of the way the objects of interest are represented 

   - Does this affect the effectiveness of a machine learning system? 

## Data representation 

- Can you see an animal in this image? 

## Data representation 

- The very same image, with resolution reduced to 5% 

**==> picture [427 x 421] intentionally omitted <==**

## Data representation 

# • The reduced image, with pixel values rescaled 

## The importance of data representation for learning 

- In our example, using the right representation, the recognition task becomes much easier… 

   - Notice that we have not added information; actually the processing steps _reduced_ the amount of information in the successive images... 

- In general, in a classic machine learning system, the choice of the correct features is an important part of the system design 

   - The features used can be the result of some (possibly complex) processing of 

   - the original raw data 

## Architecture of a classical Machine Learning system 

**==> picture [524 x 236] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>a<br>Feature<br>Extraction Learning<br>TS ee —<br>Age:27<br>Height:169<br>Raw data<br>= |<br>Defined "by hand" using:<br>**----- End of picture text -----**<br>


- Background knowledge about the problem 

- Trial and error 

- Statistical methods for choosing the most useful features from a large set of available features 

## Parameters 

- In general, we want to find an unknown function 𝑓 the optimizes some performance measure, given a set T of training data 

   - Problem: how do we represent the function that we want to find inside an 

   - algorithm 

- To make the problem manageable, we usually limit our attention to a _parametrized family of functions_ , i.e. a set of related functions that have the same "mathematical structure" but differ from each other in 𝜃 

- the values of a tuple of _**parameters**_ 

## Parameters 

- : ℝ→ℝ 

- Example, if we have to find a function 𝑓 , we may choose the family of 2nd degree polynomials 

   - In this case, 𝑓(𝑥) = 𝑎0 + 𝑎1𝑥+ 𝑎2𝑥[2] 

   - 𝜃= (𝑎0, 𝑎1, 𝑎2) are the parameters that individuate one particular 2nd degree polynomial 

- The family of functions obtainable by changing the parameters is also called the _**hypothesis space**_ of our algorithm, and each function in this set is called a _**hypothesis**_ 

## Parameters 

- Another example: if we know that the function that we want to learn is _periodic_ with period 𝑇 , we can use what we remember about Fourier series to choose a family of functions with the following structure: 

𝑘 2𝜋𝑖𝑥 2𝜋𝑖𝑥 𝑥= 𝑏 𝑎 𝑠𝑖𝑛 + 𝑏 𝑐𝑜𝑠 𝑓 0 𝑖 𝑖 + ෍ 𝑇 𝑇 𝑖=1 In this case, the parameters are: 𝜃= (𝑎1, 𝑎2, … , 𝑎𝑘, 𝑏0, 𝑏1, … , 𝑏𝑘) 

## Parameters 

• The learning problem can often be formulated as the maximization of a performance function (or equivalently the minimization of a **loss function** _L_ over the training data) by searching for the optimal set of 𝜃 * parameters 

**Question** : what is the meaning of the "arg min" operation? 

𝜃[∗] = arg min𝜃 𝐿(𝜃, 𝑇𝑟𝑎𝑖𝑛) 

## Hyper-Parameters 

- In many cases, you have several related families of functions that can be used in a given learning algorithm; the choice of a particular family is done by fixing some _hyper-parameters_ before starting the learning 

- Example: suppose your algorithm can work with polynomial functions 

   - The degree of the polynomials is a hyper-parameter 

   - Once you have chosen the degree, you have a parameter vector that define a particular polynomial 

## The overfitting problem 

- Is it always a good idea to find the optimal parameters with respect to the training data? 

- To answer this question, we will first examine an extended example 

## The overfitting problem 

**Example** : Suppose we have a supervised learning problem and you want to learn an unknown function that relates two variables 𝑥 and 𝑡 ; the training data are in the following plot: 

## The overfitting problem 

**Spoiler** : For this example, the “true function” (unknown to the learning 𝑒 algorithm!) used to generate the training set was 𝑓(𝑥) = sin 2𝜋𝑥+ , where 𝑒 is a Gaussian random noise term. 

**==> picture [132 x 78] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ideally, a learning<br>algorithm should<br>reconstruct this<br>function<br>**----- End of picture text -----**<br>


## The overfitting problem 

**Note** : In this example, we know the "true function" (i.e. the ideal result that we want from the learning system) because we have actually "created" the problem starting from the "true function": first we decided which was the desired function, and then we built the training data from it. We did this in order to be able to evaluate if the learning algorithm does a good job or not. 

When you use machine learning to solve a real world problem, of course you don't know what is the "true solution" of the problem… 

## The overfitting problem 

Now, let us try to solve our example using Machine Learning. 

First, we have to choose a family of functions (our _**hypothesis space**_ ), in which each member of the family (a _hypothesis_ ) can be represented using a vector of parameters. 

Then, we have to choose a performance measure (or, equivalently, a loss function) that we want to optimize. 

## The overfitting problem 

- A possible approach: we approximate the unknown function with a polynomial: 𝑓(𝑥) = 𝑎0 + 𝑎1𝑥+ 𝑎2𝑥[2] + ⋯+ 𝑎𝑀𝑥𝑀 

Then the learning algorithm has to choose the best coefficients of the polynomial (i.e. the ones that minimize our loss measure with respect to the training data). 

- **Note** : We will not actually see an algorithm for doing this now; we will just show the result. We will present such an algorithm in a future lecture. 

**Question** : which are the parameters in this case? And the hyperparameters? 

## The overfitting problem 

between As a loss function, we may for example use the _mean square error_ the computed 𝑓(𝑥) and the points in the training data: 

**==> picture [389 x 38] intentionally omitted <==**

where (𝑥𝑖, 𝑡𝑖) are the points in the training set. 𝑡 Note that this loss function has a mimumum (0) if 𝑖 = 𝑓(𝑥𝑖) , and its value becomes larger the more each 𝑓(𝑥𝑖) becomes different from the 𝑡 . corresponding 𝑖 

Thus, by finding the coefficients 𝑎0, … , 𝑎𝑀 that minimize this function, we will ensure that we choose a function that is close to the points in the training set. 

## The overfitting problem If we choose a polynomial of degree 0 we are quite far from the “true” function: 

**==> picture [122 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
"Best" 0-degree<br>polynomial<br>"Ideal" function<br>**----- End of picture text -----**<br>


## The overfitting problem With degree 1 things are a little better: 

**==> picture [122 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
"Best" 1-degree<br>polynomial<br>"Ideal" function<br>**----- End of picture text -----**<br>


## The overfitting problem 

With degree 3 the approximation becomes good: 

## The overfitting problem 

With 𝑀= 3 , the approximation is good, but not perfect. 

- What happens if we increase the degree? 

- Since we have 10 data points, we could find a 9th degree polynomial that passes exactly through all of them, and so the error on the training data would be 0. 

Would it be a good idea? 

## The overfitting problem 

This is what we have with degree 9: 

## The overfitting problem 

**Question** : what is the value of the loss function in this case? 

## The overfitting problem 

The loss function has an optimal value (it is 0, which is the minimum value that the chosen function can have). And, in fact, on the points of the training set the learned function passes _exactly_ on the coordinates of each training point! 

Note: the "true function" does not passes exactly on the training point because we added some Gaussian noise in the construction of the training set… 

## The overfitting problem 

We are fitting a “model” (i.e. a hypothesis space; in our case a polynomial function) to a set of data. If the model is too complex (high model _capacity_ ), as in the case of the 9th degree polynomial, it will fit very well the training data, but it may (as in this example) diverge from the underlying “true” function that we wanted to approximate, on points that were not present in the training set. 

## The overfitting problem 

## The trade-off: 

- If the model is too simple, it may not be able to approximate well the desired function (e.g. the 0-degree polynomial in our previous example); this is called **bias error** 

- If the model is too complex, it may fit very well the training data, but diverge from the real desired function, and thus give a bad approximation for x values that were **not** in the training data; this is called **variance error** 

- NOTE: often (as in our example) the complexity of the model is tied to the value of the hyper-parameters 

## The overfitting problem 

Another point of view on overfitting: 

• In our problem, what we _really_ wanted was a function that is as close as 𝑥 . In possible to the "true function" for all the possible random values of other words, we wanted to minimize the _expected value_ of some distance measure between the found function and the true one (the so called _empirical error_ ). 

- For instance, using the square error as our measure, we really wanted to minimize: 

𝔼 𝑥 2 𝑥[ 𝑓𝑡𝑟𝑢𝑒 𝑥−𝑓 ] 

## The overfitting problem 

However, we are not able to compute this expected value, and so we approximated it using the Law of Large Numbers! 

**==> picture [514 x 230] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑁<br>1<br>2<br>𝔼 𝑥 ≅<br>𝑥 𝑓𝑡𝑟𝑢𝑒 𝑥−𝑓 (𝑡𝑖 −𝑓(𝑥𝑖)) [2]<br>𝑁 [෍]<br>𝑖=1<br>What we wanted to  What we actually<br>minimize minimized (our loss<br>function)<br>This is because of<br>the Law of Large<br>Numbers<br>**----- End of picture text -----**<br>


**The variance error is simply the error caused by this approximation.** 

The overfitting problem **NOTE** : as a consequence of this, overfitting depends not only on the model, but also on how many training data (i.e., samples) you have for computing this approximation: 

**==> picture [156 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
"Best" 9-degree<br>polynomial, but with<br>a training set  .<br>extended to 100<br>points.<br>Note that it is almost<br>identical to the true<br>function…<br>**----- End of picture text -----**<br>


## The overfitting problem 

- Overfitting depends not only on the model, but also on how many training data you have: 

- A model is not "too simple" or "too complex" in absolute terms 

- The very same model can be too simple if you have a lot of training data, and too complex if you have few training data 

Also, you may have overfitting problems if the training samples are not truly independent, or if they have a different probability distribution from the data that your system will encounter in its real operation… 

An example of classification: Remote Sensing Images 

## An example of classification: Remote Sensing Images 

- Input data 

   - Images aquired by a satellite 

   - For each pixels, a feature vector representing the "color" of the area in several wavelength bands (may include non-visible bands such as infrared and ultraviolet) 

      - For the Landsat7 program: 8 bands available 

An example of classification: Remote Sensing Images 

- The task: classify each area of the image as: 

   - Residential Area 

   - Sea / Water bodies 

   - Cultivated land 

   - Woods (Vegetation 1) 

   - Mediterranean bush (Vegetation 2) 

An example of classification: Remote Sensing Images 

- First problem: which features would you use for the task? 

   - All the features in the raw data? 

   - A subset of the features in the raw data? 

   - Some derived features computed from the raw data? 

## Let us visualize some points in the training set using 2 features 

(Figure colors represent the classes) 

**==> picture [157 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
Using feature 4 and 5<br>**----- End of picture text -----**<br>


Using feature 3 and 4 

**In which subspace the classification task is easier?** 

An example of classification: Remote Sensing Images 

# • Second problem: how do we represent a _model_ ? What is our hypotheses space? 

- An example of classification: Remote Sensing Images 

- Second problem: how do we represent a _model_ ? What is our hypotheses space? 

   - A possible solution: if we use two features, we can represent a class using an ellipse in the used feature space (which is a plane) 

      - If the feature vector of a pixel lies in the ellipse of a class, the pixel is assigned to that class 

## Learning the model 

- We find ellipses covering the training samples of each class 

Is this model unique? 

## Learning the model 

- We find ellipses covering the training samples of each class 

Another model for the same training data (red). Which one is better? 

## Learning the model 

- We find ellipses covering the training samples of each class 

What happens when we consider points NOT in the training set? 

## Learning the model 

- We find ellipses covering the training samples of each class 

## Learning the model 

- We find ellipses covering the training samples of each class 

In this case, the "black" model was overfitting 

## Learning the model 

• We find ellipses covering the training samples of each class 

In this case, the "red" model generalizes too much 

## Final results 

## “No free lunch” theorem 

- Given two learning algorithms A1 and A2, and a training set S, sampled from an unknown data distribution, if 𝐹 is the target function to be learned from S, it can be demonstrated that the _expected empirical error_ on all the data (not just on S) with respect to all the possible 

- functions 𝐹 is the same: 

   - 𝔼 𝔼 𝑒𝑟𝑟𝑜𝑟 𝐹 −𝔼 = 0 𝐹 𝑥 𝐴1 𝑥[𝑒𝑟𝑟𝑜𝑟𝐴2(𝐹)] 

- This means that if A1 is better than A2 on a target function 𝐹 1, then there will surely exist a function 𝐹 2 on which A2 is better than A1! 

## Bias and variance error 

- A learning algorithm should minimize the expected error on the entire data distribution, **not** only in the Training Set (the “empirical error”) 

- The empirical error can be decomposed into two terms: 

Error=Bias+Variance+Noise 

## ▪ where: 

- Bias = error due to wrong assumptions in the algorithm (e.g. the Hypothesis Space does not contain the target function) 

- Variance = error due to sensitivity to variations in the Training Set (e.g. **overfitting** ) 

- Noise = error due to inherent ambiguity in the data (irreducible error) 

## Bias and variance error 

- Often a trade-off between bias and variance 

   - E.g. increasing the model capacity reduces bias and increments variance 

- Complex learning algorithms may perform well with respect to bias but then have poor performance on variance! 

- Until the ’90s, theoretical analysis focused only on bias 

   - Now we understand that we need to find the right balance between bias and variance 

## No free lunch: considerations 

- No single algorithm will solve all your machine learning problems better than every other algorithm. 

- Make sure you completely understand a machine learning problem and the data involved before selecting an algorithm to use. 

- All models are only as good as the assumptions that they were created with and the data that was used to train them. 

