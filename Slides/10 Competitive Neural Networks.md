# **Machine Learning Competitive Neural Networks Prof. Mario Vento Prof. Diego Gragnaniello** 

## Competitive Neural Networks 

- The basic idea is thet neurons are in competition with each other with respect to some metrics, with one neuron winning 

- ▪ Requires **lateral connections** to find the winner 

- The answer of the network is the answer given by the winner 

- During learning, the weight update depends on the result of the competition 

   - Often (not always) only the winner is allowed to update its weights 

## Learning Vector Quantization (LVQ) 

# ◆ Proposed by T. Kohonen in the '80s 

- Architecture: 

Lateral connections 

## Learning Vector Quantization (LVQ) 

# ◆ A LVQ can be used for unsupervised learning 

▪ Neural clustering algorithm 

# ◆ A LVQ can be used for supervised learning ▪ Multi-class classifier 

## LVQ Neuron 

- A LVQ neuron 𝑖 𝒘 with the same contains a vector of weights 𝑖 

- dimension as the input space 

- The neuron computes a distance function between the input vector and the weights vector 

   - Example: Euclidean distance 

      - For neuron 𝑖 : 𝑑 = −𝑥 𝑖 σ (𝑤 )[2] 𝑗 𝑖𝑗 𝑗 

      - Other distance functions can be used 

- The **winner** is the neuron with the smallest distance: 

- ▪ 𝑑 

- 𝑣= arg min𝑖 𝑖 

## Unsupervised LVQ 

# ◆ The network is used for **clustering** , i.e. dividing the input samples into "homogeneous" groups 

- You assign a neuron for each desired cluster 

- ▪ You need to know in advance the number of clusters 

## Unsupervised LVQ 

- Learning: a random sample 𝒙 is extracted from the training set and the competition is run 

- Only the winner neuron 𝑣 updates its weights: 

   - 𝒙 

   - Weights are made "closer" to the training input 

𝒘 ←𝒘 + 𝛼∙ 𝒙−𝒘 𝑣 𝑣 𝑣 

**==> picture [211 x 56] intentionally omitted <==**

Note: these are vectors 

- 𝛼 is the _learning rate_ between 0 and 1 

- The update is repeated until a maximum number of iterations, possibly with 𝛼 

- decreasing 

   - Alternatively, learning can stop if the neurons are not changing too much 

## Unsupervised LVQ 

- After the training, the network is used for dividing the input samples into the defined clusters: 

- ▪ 𝒙 For each input sample , the competition is run 

- ▪ 𝒙 The sample is assigned to the cluster corresponding to the winning neuron 𝑣 

𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝒙= 𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑑 𝑣where 𝑣= arg min𝑖 𝑖 

## Example 

- We want to divide into two clusters the following set of points 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [99 x 88] intentionally omitted <==**

## Example 

- We use 2 LVQ neurons, initialized with random weights 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [55 x 80] intentionally omitted <==**

**==> picture [99 x 88] intentionally omitted <==**

**==> picture [104 x 40] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial neuron<br>positions<br>**----- End of picture text -----**<br>


## Example 

## ◆ At each, step, we choose a random training sample 

**==> picture [141 x 88] intentionally omitted <==**

**==> picture [132 x 39] intentionally omitted <==**

**----- Start of picture text -----**<br>
Chosen training<br>sample<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

- Competition: we find the neuron with the smallest distance from the training sample 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [58 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Winner<br>**----- End of picture text -----**<br>


**==> picture [55 x 82] intentionally omitted <==**

**==> picture [99 x 88] intentionally omitted <==**

## Example 

- Update: the winner neuron is moved to be closer to the sample in the training set 

**==> picture [129 x 36] intentionally omitted <==**

**----- Start of picture text -----**<br>
New position of<br>the winner<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

## ◆ We repeat this learning cycle 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [390 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
Chosen training<br>New position of  sample<br>Winner<br>the winner<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

◆ After a sufficient number of learning cycles: Cluster 1: samples closer to Cluster 2: the 1st  neuron samples closer to the 2nd neuron 

**==> picture [87 x 75] intentionally omitted <==**

**==> picture [99 x 88] intentionally omitted <==**

## Voronoi diagram 

- **Each neuron** create a region in the feature space 

- The union of all regions is a **Voronoi diagram** 

- For each pair of neurons, the region boundary is on the axis in the middle among them 

_2 Points_ 

3 Points 

4 Points 

## Voronoi diagram 

- **Each neuron** create a region in the feature space 

- The union of all regions is a **Voronoi diagram** 

- ◆ For each pair of neurons, the region boundary is on the axis in the middle among them _Construction Editing_ 

## Unsupervised LVQ 

- **Question** : the learning rule 

𝒘 ←𝒘 + 𝛼∙ 𝒙−𝒘 𝑣 𝑣 𝑣 

can interpreted as a step in the Stochastic Gradient Descent; in 𝒙−𝒘 other words, the vector 𝑣 can be interpreted as the opposite of the gradient of a loss function. Which function? 

## Unsupervised LVQ 

**==> picture [680 x 218] intentionally omitted <==**

**----- Start of picture text -----**<br>
◆ Answer :<br>1 1 2<br>𝐽 𝒘𝑣, 𝒙= 𝒘𝑣 −𝒙 [2] = 𝑤 −𝑥<br>𝑣𝑗 𝑗<br>2 2  [෍]<br>𝑗<br>Half of the square<br>of the Euclidean<br>distance between<br>𝒘 and  𝒙<br>𝑣<br>**----- End of picture text -----**<br>


You can easily check that 𝜕𝐽 𝒘𝑣, 𝒙 − = 𝒙−𝒘 𝑣 𝜕𝒘 𝑣 

## Unsupervised LVQ 

◆ Thus, if the set of training points for which neuron 𝑣 is the winner remains stable (which will probably happen after a sufficient 𝛼 number of learning steps, if becomes small enough), the weight vector 𝒘 𝑣 will converge to the point that minimizes the sum of the squared Euclidean distances from this set 

- This point is the _centroid_ of the set (i.e. the point whose coordinates are the arithmetic mean of the corresponding coordinates of all the points in the set) 

## Supervised LVQ 

- The network is used as a **classifier** 

- Each neuron is assigned a class 

   - You can have more than one neuron per class; you may also have a different number of neurons per class (this is a hyperparameter of the algorithm) 

- Learning: only the winner update its weights 

- ▪ If the winner is of the correct class, the weights are moved "closer" to the the training input x 

   - If the winner is of the wrong class, the weights are moved "farther" from x 

## Supervised LVQ 

- Learning: a random sample 𝒙 is extracted from the training set and the competition is run 

- Only the winner neuron 𝑣 updates its weights 

- Update rule: 

▪ 𝒘 ←𝒘 + 𝛼∙ 𝒙−𝒘 if 𝑐𝑙𝑎𝑠𝑠 𝑣= 𝑐𝑙𝑎𝑠𝑠 𝒙 𝑣 𝑣 𝒗 

▪ 𝒘 ←𝒘 𝒙−𝒘 if 𝑐𝑙𝑎𝑠𝑠 𝑣 𝒗 −𝛾∙ 𝑣 𝑣≠𝑐𝑙𝑎𝑠𝑠(𝒙) 

- 𝛼 and 𝛾 are hyperparameters between 0 and 1 

## Supervised LVQ 

- After the training, the network is used for classifying the input samples: 

   - 𝒙 

   - For each input sample , the competition is run 

   - 𝒙 

   - The sample is assigned to the cluster corresponding to the winning neuron 𝑣 

𝑐𝑙𝑎𝑠𝑠 𝒙= 𝑐𝑙𝑎𝑠𝑠 𝑑 𝑣where 𝑣= arg min𝑖 𝑖 

## Example 

## ◆ We have a binary classification problem 

**==> picture [93 x 64] intentionally omitted <==**

Class 2 Class 1 

**==> picture [99 x 70] intentionally omitted <==**

## Example 

- We use 4 LVQ neurons (2 per class), initialized with random weights 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [57 x 100] intentionally omitted <==**

**==> picture [99 x 88] intentionally omitted <==**

Initial neuron positions 

## Example 

# ◆ The learning cycle is similar; if the winner is of the right class, it is moved closer to the training sample 

**==> picture [71 x 52] intentionally omitted <==**

**==> picture [330 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
Old position<br>of the winner<br>𝒙<br>𝒘<br>𝑣<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

# ◆ The learning cycle is similar; if the winner is of the right class, it is moved closer to the training sample 

**==> picture [71 x 52] intentionally omitted <==**

**==> picture [330 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
Old position<br>of the winner<br>𝒙<br>𝒘<br>𝑣<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

- The learning cycle is similar; if the winner is of the right class, it is moved closer to the training sample 

**==> picture [71 x 52] intentionally omitted <==**

**==> picture [330 x 167] intentionally omitted <==**

**----- Start of picture text -----**<br>
Old position<br>of the winner<br>𝒙<br>𝒘<br>𝑣<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

- The learning cycle is similar; if the winner is of the right class, it is moved closer to the training sample 

**==> picture [71 x 48] intentionally omitted <==**

**==> picture [366 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
Old position<br>of the winner<br>𝒙<br>𝒘<br>𝑣<br>𝒘<br>𝑣<br>New position<br>of the winner<br>**----- End of picture text -----**<br>


**==> picture [99 x 88] intentionally omitted <==**

## Example 

## ◆ But if the winner is of the wrong class, it is moved away from the training sample 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [295 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝒙<br>𝒘<br>𝑣<br>Old position<br>of the winner<br>**----- End of picture text -----**<br>


**==> picture [40 x 70] intentionally omitted <==**

## Example 

## ◆ But if the winner is of the wrong class, it is moved away from the training sample 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [442 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
New position<br>of the winner<br>𝒙<br>𝒘<br>𝑣<br>𝒘<br>𝑣<br>Old position<br>of the winner<br>**----- End of picture text -----**<br>


**==> picture [40 x 70] intentionally omitted <==**

## Example 

## ◆ After a sufficient number of learning cycles 

**==> picture [93 x 88] intentionally omitted <==**

Decision regions based on distance from the neurons (similar to NN classifier) Class 1 Class 2 

**==> picture [99 x 88] intentionally omitted <==**

## Number of neurons and complexity 

- Diverse classes may need a different number of neurons 

**==> picture [220 x 122] intentionally omitted <==**

**----- Start of picture text -----**<br>
Class 1<br>Class 2<br>**----- End of picture text -----**<br>


- Decision regions using: - 1 neuron of Class 1 

- - 1 neuron of Class 2 

**==> picture [41 x 49] intentionally omitted <==**

Low performance on Class 1 even on the training set → underfitting. The LVQ network is too simple 

## Number of neurons and complexity 

- Diverse classes may need a different number of neurons 

**==> picture [208 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
Class 1<br>Class 2<br>**----- End of picture text -----**<br>


- Decision regions using: - 2 neuron of Class 1 

- - 1 neuron of Class 2 

**==> picture [41 x 49] intentionally omitted <==**

Better performance on Class 1 on the training set → reduced bias error, verify generalization on the validation set 

## Neuron underutilization 

- A problem with LVQ is that it may happen, if the initial weights are far from where the input samples are located, that the first winning neuron (which is drawn closer to the input) will continue to win, while the others will not be used 

- ▪ This is an extreme case, but it may happen that a subset of the neurons are not used 

## Neuron underutilization 

## ◆ Example 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [56 x 79] intentionally omitted <==**

Initial neuron positions 

## Neuron underutilization 

## ◆ Example 

**==> picture [93 x 88] intentionally omitted <==**

This neuron wins the first competition and is moved closer to the input samples 

## Neuron underutilization 

## ◆ Example 

**==> picture [71 x 88] intentionally omitted <==**

**==> picture [487 x 238] intentionally omitted <==**

**----- Start of picture text -----**<br>
This neuron will continue to win<br>in successive competitions<br>This neuron will never<br>move from its initial<br>position!<br>**----- End of picture text -----**<br>


## Neuron underutilization 

- Solution: the distance used for the competition is "corrected" taking into account the frequency 𝑓𝑖 of usage of the neuron 𝑖 : 

   - Frequency Sensitive Competitive Learning (FSCL) 

   - ▪ Conscience Competitive Learning (C[2] L) 

   - ′ 

   - ▪ Both the algorithms use a modified version 𝑑𝑖 of the distance for computing the winner during the training phase 

## Neuron underutilization 

## ◆ FSCL 

▪ 𝑑′ = 𝑑 𝑖 𝑖 ∙𝑓𝑖 

◆ C[2] L 

▪ 𝑑′ = 𝑑 −𝑏 𝑖 𝑖 𝑖 1 where 𝑏 = 𝑐∙ 𝑖 𝑁[−𝑓][𝑖] with 𝑁 =number of neurons, 𝑐 constant > 0 

## Neuron underutilization 

## ◆ FSCL example 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [337 x 225] intentionally omitted <==**

**----- Start of picture text -----**<br>
This neuron has always<br>won ( 𝑓 =100%)<br>This neuron has never<br>won ( 𝑓 =0)<br>**----- End of picture text -----**<br>


## Neuron underutilization 

## ◆ FSCL example 

**==> picture [44 x 83] intentionally omitted <==**

**==> picture [484 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
This is the winner, even if<br>the true distance is larger<br> 𝑑′ =  𝑑 is<br>(because 𝑖 𝑖 ∙𝑓𝑖<br>smaller)<br>**----- End of picture text -----**<br>


## Neuron underutilization and a priori distribution 

# ◆ Frequency-based distance corrections «regularize» the learning procedure 

- Change the final goal (i.e., the loss function) just like when using a regularization term 

- No free lunch: in some cases, it can decrease the performance 

## Neuron underutilization 

## ◆ Example with unbalanced data distributions 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [56 x 79] intentionally omitted <==**

Initial neuron positions 

## Neuron underutilization 

## ◆ Example with unbalanced data distributions 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [53 x 72] intentionally omitted <==**

**==> picture [55 x 76] intentionally omitted <==**

More wins for Less wins for more samples less samples 

## Neuron underutilization 

## ◆ Example with unbalanced data distributions 

▪ With no frequency-based distance correction: correct 

**==> picture [93 x 88] intentionally omitted <==**

With no correction 

## Neuron underutilization 

- Example with unbalanced data distributions 

   - With no frequency-based distance correction: correct! 

   - With frequency-based distance correction: error! 

**==> picture [93 x 88] intentionally omitted <==**

**==> picture [40 x 62] intentionally omitted <==**

**==> picture [79 x 34] intentionally omitted <==**

**==> picture [232 x 38] intentionally omitted <==**

**----- Start of picture text -----**<br>
With  With no<br>correction correction<br>**----- End of picture text -----**<br>


The result may get worse, e.g., in presence of strong a priori distributions 

## Manifolds 

- A _manifold_ is a space that is _locally_ Euclidean, i.e. in the neighborhood of a given point, the Euclidean distance represents well the “closeness”, but outside of the neighborhood it may give false indications 

   - Points with low Euclidean distance may actually be very far from each 

   - other, if we move only within the manifold 

- Usually “embedded” in larger dimensional Euclidean spaces 

   - But may also be “embedded” in a Euclidean space of the same dimension 

## Manifolds: example 

- We have 2D points that lie on a 1D (non linear) subspace (a curve) 

**==> picture [42 x 38] intentionally omitted <==**

**==> picture [536 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
These points are close in the 2D Euclean space, but very far in the<br>embedded 1D manifold!<br>**----- End of picture text -----**<br>


## Manifolds: example 

- We experience the Earth's surface as it is were a 2D plane 

   - It behaves like a Euclidean plane "locally", i.e. in a neighborhood of the point where we are 

- In reality, it is a 2D manifold embedded in a 3D space 

## Manifolds: example 

**==> picture [29 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
ball<br>**----- End of picture text -----**<br>


… because Frankie did not understand that the shortest path according to Euclidean distance is not necessarily the shortest path in the manifold! 

## Why do we care about manifolds? 

- If we know the manifold, sometimes we can represent each data point using a smaller number of coordinates 

- ◆ For example, if the points lie on a 1D manifold (a curve), one coordinate is sufficient 

- In this way we achieve **dimensionality reduction** 

   - Also, if you reduce your data to 2D or 3D manifold coordinates, you can more easily display it ( **data visualization** ) 

## Why do we care about manifolds? 

- Also, our learning task may become simpler if we express our feature vectors using a coordinate system related to the manifold 

- ◆ For example, distance with respect to the manifold might have better correlation with the probability that two samples are of the same class 

## Why do we care about manifolds? 

- Operations like **sampling** and **interpolation** may give unusable results if performed without taking into account the manifold structure of our data 

   - This can have important consequences for **data augmentation** 

**==> picture [60 x 38] intentionally omitted <==**

**==> picture [395 x 215] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Which point is halfway<br>between A and B?<br>B Right (inside the<br>manifold)<br>Wrong (outside of the<br>manifold)!<br>**----- End of picture text -----**<br>


## Manifolds and learning 

- In such cases, we need a **correspondence** (a “map”) between the coordinates of the Euclidean embedding space (the feature space) and a coordinate system in the embedded manifold 

- How do we obtain that? 

   - Remember, in general your data is not 2D/3D (so you cannot just visualize it to see what is the "shape" of the manifold, or even if there exists a manifold!) 

## Manifolds and learning 

- The map can be learned from a sufficient number of examples 

      - (Manifold learning) 

- This is a form of unsupervised learning 

   - You only know the feature vectors in the training set; you do not know 

   - what are the "manifold coordinates" for each feature vector 

## Self-Organizing Maps (SOM) 

◆ A neural network used for manifold learning 

- Invented by T. Kohonen in the ‘80s 

- Based on Competitive Learning (like LVQ) 

## SOM: structure of the network 

# ◆ The neurons are arranged on a grid with the same spatial structure of the manifold that must be learned: 

**==> picture [81 x 18] intentionally omitted <==**

**----- Start of picture text -----**<br>
2-d space<br>**----- End of picture text -----**<br>


**==> picture [80 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
3-d space<br>**----- End of picture text -----**<br>


## SOM: structure of the network 

- The grid does not need to be rectangular. The structure should reflect the topological properties of the desired manifold (i.e. two connected nodes represent points that are “close” in the manifold) 

An hexagonal 2D grid: each node has 6 immediate neighbors 

## SOM: structure of the network 

## ◆ The position of the neuron in the grid represents the position of a point in the manifold: 

## Manifold coordinate 2 

Manifold coordinate 1 

## SOM: structure of the network 

- Usually, distances in the manifold are expressed counting the number of edges in the shortest path between two neurons: 

Distance=1 

Distance=4 

## SOM: structure of the network 

- Each neuron contains a weight vector with the same dimensionality as the embedding space 

- Thus a neuron represents a correspondance between a **point in the manifold** ( **position of the neuron in the grid** ) and a **point in the embedding space** ( **weights of the neuron** ) 

- The map gives the correspondence for a finite set of points (the neurons); the other points are interpolated (e.g. by linear interpolation) 

## SOM: the learning algorithm 

1. Time 𝑡 =0; initialize the neuron weights at random 2. 𝑡= 𝑡+ 1 3. 𝒙 Extract a sample point in the embedding space 

4. Find the _winner_ neuron 𝑣 , i.e. the neuron having the weights that 

are closest to 𝒙 in Euclidean distance 

5. 𝑢 : Update the weights of each neuron 𝒘 ←𝒘 𝑢 𝑢 + 𝛼(𝑡) ∙𝜃(𝑢, 𝑣, 𝑡) ∙(𝒙−𝒘𝑢 ) 

6. Repeat from 2 until convergence or the maximum number of iterations is reached 

## SOM: the learning algorithm 

◆ 𝛼(𝑡) is the learning rate, and is a decreasing function of time 𝑡 

◆ 𝜃(𝑢, 𝑣, 𝑡) is the _neighborhood function_ ; 𝜃 if 𝑢= 𝑣 𝑢 𝑣 𝑢, 𝑣, 𝑡= 1 , and decreases as gets far from (in manifold distance) 

- Usually 𝜃(𝑢, 𝑣, 𝑡) is non-zero only for a small number of values of 𝑢 , so as 

   - to keep small the number of nodes that must be updated 

- The set of values having 𝜃 𝑢, 𝑣, 𝑡> 0 may also decrease with time 𝑡 

## Example 

- Suppose we have these 2D points, and we want to learn a map 

   - to a 1D manifold 

**==> picture [41 x 66] intentionally omitted <==**

## Example 

## ◆ We decide to use a 1D SOM network with 8 neurons 

Neurons are arranged in a 1- Dimensional grid 

Each neuron has a Manifold coordinate: 0 manifold coordinate (only one because it is Manifold coordinate: 1 a 1D SOM). The manifold Manifold coordinate: 2 coordinate depends on Manifold coordinate: 3 the position of the neuron in the grid. Manifold coordinate: 4 Manifold coordinate: 5 Manifold coordinate: 6 Manifold coordinate: 7 

## Example 

- We decide to use as neighborhood function: 𝜃 𝑢, 𝑣= max{0, 1 −0.5 ∙ 𝑢−𝑣} 

Manifold coordinate: 0 𝜃 0,3 = 0 Manifold coordinate: 1 𝜃 1,3 = 0 

Manifold coordinate: 2 𝜃 2,3 = 0.5 If the winner is 𝑣= 3 , only these three Manifold coordinate: 3 𝜃 3,3 = 1 neurons will be Manifold coordinate: 4 𝜃 4,3 = 0.5 updated Manifold coordinate: 5 𝜃 5,3 = 0 

Manifold coordinate: 6 𝜃 6,3 = 0 Manifold coordinate: 7 𝜃 7,3 = 0 

## Example 

# ◆ Each neuron also has a 2D weight vector, giving its position in the embedding space 

**==> picture [41 x 66] intentionally omitted <==**

**==> picture [86 x 56] intentionally omitted <==**

Initial neuron positions in embbeding space 

## Example 

- Competition: a training sample is chosen, and the winning neuron is selected 

**==> picture [41 x 66] intentionally omitted <==**

Training sample 

Winning neuron 

**==> picture [86 x 80] intentionally omitted <==**

## Example 

- Update: The winning neuron is moved closer to the training sample 

**==> picture [122 x 181] intentionally omitted <==**

## Example 

◆ Update: But also its neighbors (those having 𝜃> 0 ) are moved (less than the winner) 

**==> picture [132 x 227] intentionally omitted <==**

## Example 

# ◆ After a sufficient number of learning cycles, the SOM will approximate the shape of the manifold 

**==> picture [41 x 66] intentionally omitted <==**

**==> picture [65 x 48] intentionally omitted <==**

## Another example 

- We will use the MNIST dataset of handwritten digits 

▪ 60000 training samples, each a 28x28 gray scale image 

## Another example 

# ◆ We will try to learn a 2D manifold for this dataset 

- We will use a rectangular grid of 16x16 neurons 

## Another example ◆ Initial weights of the neurons eeSyALE feasealLoveeTS an)ey feprekflowinfibroid PafasasmeMentenres) (eee(eee)Shek hel Fa-Fivs[AMie beckeauParcs es EailgetyCeePosted RitesSEOCRO Bomitespoo)Gee eeepetspretce Lae)PiPeayaess| beneioeRometed Gee]bediSe:le bowel!Beker!Sa oS oespeerie mia4 Meoa ikepictie) Wheeiees]|eee! faMatttie)tbs (aout2 a Pesvtenyon feed+. yt Goma]y MAEBo ee Care pitytl iti* bowenJ 4, petaoye g baie{ | baerbecA weights of the hates) eM Pe) eee) REO Peed beter) ut) icles) Reeve) Beton) poavond) Goinetid lke feo baal neuron in this Han ng ieee! Pita) fohatcece [so Vibe =| le\icaeel [tea fA ed (See Sa Sree] fee Is-g esel Cie) Cees) pend wi Buea jacketed hepato ee orky] othe Pe stie LtShed beech paumtid fateh [eee leit sat Catlin position of the Petes]pee Oy; pst)Bier) patentEas Reptageedimey Pahree te Poveden!hires! PipesPie 34 feoPra Rise ber)Meme] AvesPate! freekarat **e** ) fp **e** tn **e** d) DarSo **r** at) aeWoets parak!CTE teeoAs **e** | grid Pane ee) Bess] Boater Pwite fated Reeied Mire Gey) ta) et) de pape OSES Wate Ron ers Pores Sarin (Sever) hi SS] Soy Tae Seo Paes Te] ER Aes eS rte) Gee SSeS Rae) erpicheinSie wis) Atenieee)Pied LeeroythreBoekel praiaGSSid)ert)| PierrebesetDSi belBSRSS)pee ses eck)4, sperGaSebem ahabietio!Fehr) Pasarbia!cme) Mesias)(EEREWekcoard (teksParcs)feed] MeetSeid)ftom! [WepatelisisPe (eyriaPte] (eensBeranePea) PeroKiesDe Pe Rose) ee Gee GES Feces Be PeShaes feel) Geis) BRAT] PERS Be SS) AS ea aeee]weeed+ NestCiehae)ay 3+ peakedf **e** aee)we he) eedfatlenyMaus]Miro oe Be)(ee4),fentonaedDak. . betheyreSe ETEMineoSy BEaryeonSo) eat Ceepee es BsMas fomaeens- Parrare **e** sdt et bateeWG5aSte)laa Pame,featNASA fiesaeHee)TSte) beteleee.cesASE] btsfoBah eteSe, se lewdPokeAILGe easea Porat¥oreF |S Bites fagno) Escen fetae F ett) eee] a Re Rd Bee Rises ue) Bea Ea fed iene cece ieee Boh Roe] Paty sed Peeel baton, Mua) pie) Lilo Pernt) Rare bootie Mere Mince, ee ees PES) erat feerch) bese) lect) STS DON) pie) bbe) fect (Praia (idee) Been) Poesia Praetie rete) iy teri bebe! Wield Ri oe ad Pe) RE pate (ee oe) Raton botinoe beibell Btrcbey portal fy Mepaces) [Foal fret betes fabled) iSitead io Siro (ere, [ese pas i SEIS Fee Pactowed Poa sere) Abed [Pee Rema estes) Fake fae Ce eee bite Raed Bice Gael Beead Pad Peaas ee BS es poae Beet] Heed es) BAe Bed) leeetecs) WSR) Reine) Lede] Ect Swe] MAAS) Beisel oeery Cobiaasy pe! ky rarity ei [aect) Roene Oe Se Yh bie Peas lek | |G RS ed Sy see tee Wako ot ye: hep] feet esol Gaaet) beatin Wleetd Geekeghy Bae Estee Miaocesd [aes aurea Sy aa, Lares) tie GaP Rieu Crealpiepeerbassbuns! MeeeEnterbei rats, Ate)filernner ques SsbakePC uPdeca)ied) Mereheeytee)estas BeMos]Pooks!bovitroml [eeMintelteenie)tte?) [eateryeer)[ee PidWiiwitkaeee et) (eer)BaereReid ye) ieeeTeteout)ni Mie!berias] peePccoseEyea Portassanee) twapairae ON fastsatedeee Pepvaaatel ZeePeston oidEtiam Boa)fla Ragesawh GeomPoe (eefeta ReyFrey BaeB SD PS)Fe GoesBets PeleeGea eerra pSen7 esait eines)pee rie)podspe ee(2:+> ealeae)ltbedGeaey esRePetters ene] oebeetBSA) MemeteGeysd Bo)leeke Meares) MaGandDelete)bee RaePeonBcd (hedearEsta) [EACBiot)Fe po baiiea)faxesbey 4) Lee)fooreae)eeome RenteaePes| Eee)foesPO keGe? hyperoTae)Pie Btaotnt) basco: ao oh legate) Cues] EE Te] iced Heese ate 3] gah! Peder) Meese) fens aeeaae RaSie Lita BaconEee BR)Pron kere]arch) Remedyey Fritaimee] GaSeieee) piedWeated eewiedboty (ates)faented ite(eer) eect)bamciae) Breettr [ergEY (enedpare Weeited eeebreeSy Raaabe La aePoteee) ee} ew)Keates bakesbedia afeet (itilSerr bipedphe! (eye)fat Bion Riegel[ett] leFrigateakeae ore!Bystan) PinCbprtind Peaybeater poke)eevee beepee ied atteee hey Pana bax Tae Peres Bewece) ieee’ (pe om nite otal patie leaked feed bic) Kiet aad Leeked eee Vian Genter ated Rested Rates) tice (SSSoeN tke Eaardal poe] Wabi) Ge) Bicace) fees foe) Gees Rca manifold coordinate 1 

## Another example 

## ◆ After 1000 learning steps 

## Another example 

◆ After 100000 learning steps 

## Another example ◆ After 100000 learning steps 

As you can see, the classes are reasonably well separated in the manifold coordinate space (that uses only 2 coordinates) 

REMEMBER: we did not use class information for the manifold learning! 

