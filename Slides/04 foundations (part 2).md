# **Machine Learning Foundations p.02 Prof. Mario Vento Prof. Diego Gragnaniello** 

## Performance evaluation and generalization 

- The algorithm usually optimizes the parameters wrt the Training Set 

- However, if you measure the performance on the Training Set, you may not detect overfitting 

- What you really want to measure is how well your algorithm will perform on new data (i.e. data **different** from those used in training)… The ability of an algorithm to show a similar performance on the training set and on new data is called **generalization** 

How can you reliably measure the _future_ performance of your algorithm? 

## Performance evaluation and generalization 

## • You want to estimate this: 

𝔼 𝑥 Performance(𝑓, 𝑥) 

Expected performance of learned function f 

Average • But you cannot use this estimator: performance on 𝑁 training set 1 Performance with 𝑥 𝑓, 𝑥𝑖 , 𝑖 ∈𝑇𝑟𝑎𝑖𝑛𝑖𝑛𝑔𝑆𝑒𝑡 𝑁[෍] 𝑖=1 because of the overfitting problem… 

So, what can you do? 

## Test Set 

- A possible solution to estimate the expected performance on new data is to use a **Test Set** , that is a set of data that has been obtained **independently** of the Training Set: 

1 𝑀 𝔼 ≅ Performance 𝑥 Performance(𝑓, 𝑥) 𝑓, 𝑥 𝑗 𝑀[σ][𝑗=1] with 𝑥 ∈𝑇𝑒𝑠𝑡𝑆𝑒𝑡 𝑗 

- This estimate would not be affected by the overfitting of the learning algorithm 

## Test Set 

- Of course, also this estimate is based on the Law of Large Numbers; thus the estimate is good if: 

   - The Test Set is large enough 

   - The samples in the Test Set are independent of each other (and 

   - independent of the Training Set!) 

   - The samples in the Test Set follow the same distribution of probability as 

   - the samples the system will see in its operation 

## Test Set 

◆ **Warning** : the performance estimate on the Test Set is an estimate; even if the Test Set is large, there is always a (small but not null) probability that it is very different from the true expected performance on future data 

## Test Set 

## ◆ **Question** 

- If the test set gives me a better estimate of the expected performance, can 

- I use it during the training phase to obtain a better system? 

- For example, can I look at the errors on the test set, and adjust my learning 

- algorithm so as to avoid these errors? 

## Test Set 

## ◆ **Answer** 

   - If you do this, it becomes less probable that the average performance on 

   - the test set is a good estimate of the expected performance on future data 

   - ◆ the test set is no longer independent of the training, since part of it is actually used to guide the training 

   - Thus, you would need _another_ Test Set to estimate what is the expected 

   - performance on future data! 

- So, you DON’T DON’T DON’T use the Test data during the training phase; you only use them AFTER the training for evaluating the performance of the algorithm 

## An extended experiment 

- In order to illustrate the previous concepts, we will make a "controlled" experiment in which we know what the true answer is 

- The problem will be simple enough to allow us to compute _exactly_ the expected performance on future data 

## An extended experiment 

- The task: we want to learn a classification function that classifies a real number in the range 0, 10 into two classes, A and B 𝑓: 𝑥∈ 0,10 →{𝐴, 𝐵} 

- ◆ We will be "cheating", in the sense that we will know in advance the _true_ function, that is unknown to the learning algorithm: if 𝑥< 5 

- 𝑥= 

- 𝑓𝑡𝑟𝑢𝑒 𝐵 if 𝑥≥5 

- ቊ[𝐴] 

## An extended experiment 

## ◆ This is the true function: 

**==> picture [496 x 217] intentionally omitted <==**

**----- Start of picture text -----**<br>
True function<br>0 1 2 3 4 5 6 7 8 9 10<br>A B<br>**----- End of picture text -----**<br>


## An extended experiment 

◆ In order to compute the expected performance, we will also know 𝑥 in advance the probability distribution of (that is also unknown to the learning algorithm): 

𝑝 𝑥= 0.1 ∀𝑥∈[0,10] 

(uniform probability distribution) 

## An extended experiment 

◆ Hypothesis space: we choose the following family of functions, having a single parameter 𝜃 : if 𝑥< 𝜃 𝑓𝜃 𝐵 if 𝑥≥𝜃 𝑥= ቊ[𝐴] 

**Question** : what is the true optimal value of 𝜃 ? 

## An extended experiment 

◆ Performance measure: in order to evaluate a hypotesis, we will use the following performance measure: 𝑥is correct if 𝑓𝜃 𝑃𝑒𝑟𝑓 0 if 𝑓𝜃 𝑥is wrong 𝜃, 𝑥= ቊ[1] ◆ From the definition of it follows that: 𝑓𝜃 1 if 𝑥< min{𝜃, 5} . 𝑃𝑒𝑟𝑓 0 if min{𝜃, 5} ≤𝑥< max{𝜃, 5} 1 if 𝑥≥max{𝜃, 5} 𝜃, 𝑥= ൞ 

## An extended experiment 

## ◆ Now, we build a training set by randomly sampling 3 values for class A and 3 values for class B 

Training set 

**==> picture [664 x 27] intentionally omitted <==**

**----- Start of picture text -----**<br>
0 1 2 3 4 5 6 7 8 9 10<br>A B<br>**----- End of picture text -----**<br>


## An extended experiment 

- Given the training set, what is the best value for the parameter 𝜃 ? 

▪ To find out, we compute the average of the performance measure on the samples in the training set as a function of 𝜃 

## An extended experiment 

## ◆ Given the training set, what is the best value for the parameter 𝜃 ? 

**==> picture [581 x 338] intentionally omitted <==**

**----- Start of picture text -----**<br>
Avg Perf<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10<br>**----- End of picture text -----**<br>


𝜃 

## An extended experiment 

- So, we have the maximum average performance on the training set for any 

𝜃∈[4.85,6.05] 

- What is the value of 𝜃 that the algorithm will choose in this interval depends on the particular learning algorithm 

- ▪ For instance, an algorithm 1 may favor low values of 𝜃 , and thus choose 𝜃 1 = 4.9 

- ▪ A different algorithm 2 may favor large values of 𝜃 , and thus choose 𝜃2 = 6.0 

   - Another algorithm 3 may try to balance, and thus choose the middle value of the interval, 𝜃3 = 5.45 

## An extended experiment 

◆ In order to evaluate the performance after the training, we need a test set. Suppose that we build a test set with 6 samples 

Training and test set 

**==> picture [654 x 29] intentionally omitted <==**

**----- Start of picture text -----**<br>
0 1 2 3 4 5 6 7 8 9 10<br>training A training B test A test B<br>**----- End of picture text -----**<br>


## An extended experiment 

## ◆ Now, we can estimate the future performance using the test set, as a function of 𝜃 

**==> picture [598 x 316] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10<br>Avg Training Perf Avg Test Perf 𝜃<br>**----- End of picture text -----**<br>


## An extended experiment 

◆ We can evaluate the 3 algorithms on the test set: ▪ For algorithm 1 ( 𝜃1 = 4.9 ), the test set average performance is 1.00 ▪ For algorithm 2 ( 𝜃2 = 6.0 ), the test set average performance is 0.83 ▪ For algorithm 3 ( 𝜃3 = 5.45 ), the test set average performance is 0.83 ▪ Thus, in this case, the measure on the test set correctly identifies the algorithm that is closer to the true function ( 𝜃= 5.0 ) 

## An extended experiment 

- However, also the estimate on the test set can be different from the true expected performance (in this case, because the test set is small) 

◆ In our example, we can easily compute the true expected performance on future samples: 10 𝔼𝑥 𝑃𝑒𝑟𝑓(𝜃, 𝑥) 𝑝 𝑥𝑃𝑒𝑟𝑓 𝜃, 𝑥𝑑𝑥= = න 0 min 𝜃,5 10 𝑑𝑥= = 0.1 ∙න 𝑑𝑥+ 0.1 ∙න 0 max 𝜃,5 = 0.1 ∙ min 𝜃, 5 + 10 −max{𝜃, 5} 

## An extended experiment 

## ◆ So, this is the true expected performance on future data: 

**==> picture [614 x 338] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10<br>Avg Training Perf Avg Test Perf True Expected Performance<br>𝜃<br>**----- End of picture text -----**<br>


## An extended experiment 

◆ As you can see, the performance measured on Test Set for some values of 𝜃 is an underestimate of the expected future performance, and for other values it is an overestimate 

## An extended experiment 

## ◆ With a larger test set (20 samples instead of 6): 

**==> picture [637 x 364] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10<br>Avg Test Perf True Expected Performance<br>**----- End of picture text -----**<br>


## An extended experiment 

- On many values of 𝜃 the estimate on a larger test set is improved (i.e. it is closer to the expected future performance), 

   - but there are still values of 𝜃 for which there is a significant difference between the true expected performance and its estimate 

## Test Set 

## ◆ **Question** 

◆ For a given task, is it a good idea to create **once** a _**standard**_ **test set** and to use it **forever** to evaluate all the proposed algorithms for solving this task? 

## Test Set 

## ◆ **Answer** 

- While this is a common practice (because it saves a lot of work, and it 

- makes easier to compare different algorithms), **in the long term** this may lead to incorrect results 

- To understand this, consider that, however large the test set, there is always a probability (possibly very small, but greater than 0), that for some function 𝑓 , the estimate of the performance on the test set is significantly different from the expected future performance 

## Test Set 

## ◆ **Answer** 

- For example, we may call 𝑃𝑒𝑟𝑟 the probability that, on a random function 𝑓 , the estimate of performance on the test set differs from the true expected future performance by more than 20% 

- If we have a good test set, 𝑃𝑒𝑟𝑟 is very small, but not 0. Suppose for instance that 𝑃 = 10[−5] 𝑒𝑟𝑟 

- If we use the same test set to evaluate 20000 different algorithms, what is the probability that _for at least one of them_ , the estimated performance differ from the true performance by more than 20%? 

## Test Set 

## ◆ **Answer** 

- The probability is: 

= 1 − 1 −𝑃 18.12% 𝑒𝑟𝑟[20000] 

- So, if many people use the same test set, even if the test set is very good, there is a significant chance that at least one of them will get a very wrong estimate of the true algorithm performance! 

Also, take a look at https://xkcd.com/882/ 

## Generalization vs Model Capacity 

## ◆ Generalization (the ability to perform well on unseen examples) is adversely affected by model capacity 

Capacity (model complexity) 

## Generalization vs Model Capacity 

## ◆ Generalization is adversely affected by model capacity 

**==> picture [381 x 48] intentionally omitted <==**

**----- Start of picture text -----**<br>
Mostly bias<br>Mostly variance<br>error<br>error<br>**----- End of picture text -----**<br>


Capacity (model complexity) 

## What about hyper-parameters? 

- Model capacity depends on the hyper-parameters 

- ◆ How do you find the best value for the hyper-parameters? 

- One possible idea: 

1. Choose a value for the hyper-parameters 2. Train your system with the training set 3. Measure the performance on the test set 4. If not satisfied, change the hyper-parameters and go back to step 2 

**Question** : Is it a good idea? 

## Validation set 

- You must not use the test set to optimize hyper-parameters; if you do, the performance you measure may not reflect the future expected performance of the algorithm 

- You need a third set of data, independent of both the test set and the training set, to optimize the hyper-parameters; this is called the **Validation Set** 

## How to improve your performance? 

## ◆ A Machine Learning _meta_ -algorithm 

Andrew Ng, founder of the Google Brain project: 

**Warning** : this assumes that the learning algorithm has actually found the optimal parameters with respect to the training data… 

## What if data are few? 

- As we saw, a **small training set** increases the possibility of **overfitting** 

- A **small test set** makes the performance measure **inaccurate** 

- ◆ The test set error does not represent the true generalization error 

- If the available input data are scarce, it may be a problem to use a lot of data for the test set… 

What can you do? 

## K-Fold cross validation 

- Divide your data into k independent subsets (e.g. k=10) 

- ◆ Use k-1 subsets to train the algorithm and the remaining one to test it 

   - The performance measure will be inaccurate 

- Repeat chosing a different subset for the testing 

- ▪ You will have to perform k repetitions to explore all the possibilities 

- ◆ Take the average of the k experiments as a measure of the performance 

   - The k different trained systems should be similar to each other, so at the end you choose one of them at random (or you retrain the system with the whole set) 

## K-Fold cross validation 

- Example: suppose that you choose to do 3-fold cross validation (k=3) 

1. You divide **randomly** your data into 3 equal subsets, 𝐷1, 𝐷2, 𝐷3 

2. You train your algorithm on 𝐷1 ∪𝐷2 and measure the performance on 𝐷3 𝑃 

(obtaining the perf. estimate 12) 

3. You train your algorithm on 𝐷1 ∪𝐷3 and measure the performance on 𝐷2 (obtaining the estimate 𝑃13) 

4. You train your algorithm on 𝐷2 ∪𝐷3 and measure the performance on 𝐷1 (obtaining the estimate 𝑃23) 

5. A better estimate of the performance of your algorithm is (𝑃12 + 𝑃13 + 𝑃23)/3 

## Leave-one-out validation 

- Extreme form of k-fold cross validation, where k is the number of 

   - available data samples 

- Very expensive from the computational point of view 

- Used only if your available data is very scarce (e.g. 100 samples) 

## Leave-one-out validation 

- Example: suppose you only have 4 samples in the training set: A, B, C, D 

1. Train your system on A,B,C, then measure performance on D 2. Train your system on A,B,D, then measure peformance on C 3. Train your system on A,C,D, then measure performance on B 4. Train your system on B,C,D, then measure performance on A 5. Take the average of the 4 measures above and use it as an estimate of the future performance of the system trained on A,B,C,D 

