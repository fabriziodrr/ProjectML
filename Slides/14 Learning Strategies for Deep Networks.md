

## Machine Learning
Learning Strategies for
## Deep Networks
## Prof. Mario Vento
## Prof. Diego Gragnaniello

The problemwith deep learning
◆GradientDescentalgorithmsonlyensureto finda localminimum
of the lossfunction
▪Q: Isthisa problemfor training Deep NeuralNetworks?

The problemwith deep learning
◆GradientDescentalgorithmsonlyensureto finda localminimum
of the lossfunction
▪Q: Isthisa problemfor training Deep NeuralNetworks?
▪A: Surprisingly, itisnot. Ithasbeenshownexperimentallythatfor deep
models, the localminimum hasa valuethatisusallynotmuchlargerthan
the global one (so itisa good value)
•But then, whyDeep Networks mayfailto learnthe assignedtask?

The problemwith deep learning
◆Often, training stopslong beforethe gradientis0:

The problemwith deep learning
◆Often, training stopslong beforethe gradientis0:
gradientisnot
convergingto 0
butthe errorrate
hasstabilized

The problemwith deep learning
◆GradientDescentmakes small steps basedon the localstructure
of the lossfunction
◆Evenifthesestep willarriveto a good localminimum, theymay
follow an extremelylong pathto arrivethere

The problemwith deep learning
◆Considerthis: ifyouonlyhaveone parameter, thereisonlyone
path(thatisquitestraightforward) for goingfrom the initialpoint
to the closestlocalminimum
## 퐽(휃)
## 휃
## Initialvalue
Local minimum

The problemwith deep learning
◆But alreadywith twoparameters, the pathcan becomemuch
more complicated...
## 휃
## 1
## 휃
## 2
GradientDescent,
beingbasedon
localdecisions, may
notchoosethe
shortestpathto
arriveto the local
minimum...

The problemwith deep learning
◆With manylayers, the problembecomesworse, becausethe
gradientof the lossarrivesatthe initiallayersonlyafter
traversinga lotof otherlayers
▪Problemswith vanishinggradients(mitigatedby ReLU)
▪Especiallyatthe beginningof training:
•laterlayersare quitefar from their"destination";
•so the gradientinformation thattheypropagate back can be muchdifferent
from the one thatwouldbe seennearthe optimum value
## •thisphenomenoniscalledgradientdegradation!

## Degradation
◆A way of explainingdegradationisthatthe earlierlayersdo not
seedirectlythe lossfunction:
▪theyonlyhavean indirectviewof the lossthroughthe successive layers,
and optimizetheirweights basedon thisview
▪thisindirectviewcan be quite"inaccurate" ifthe successive layersare
far from the optimalposition
•thusthe earlierlayers"wastetime" movingin a directionthatisnotthe most
directpathtowardsthe optimalweights

## Degradation
◆To understandthe problemof degradation, wewillmake an
experimentwith a simplenetwork trainedto classifythe MNIST
dataset:
Input LayerHiddenLayer #1
## 2 Nodes
Activation: ReLU
HiddenLayer #2
## 18 Nodes
Activation: ReLU
## Output Layer
## 10 Nodes
## Activation: Softmax

## Degradation
◆To understandthe problemof degradation, wewillmake an
experimentwith a simplenetwork trainedto classifythe MNIST
dataset:
Input LayerHiddenLayer #1
## 2 Nodes
Activation: ReLU
HiddenLayer #2
## 18 Nodes
Activation: ReLU
## Output Layer
## 10 Nodes
## Activation: Softmax
Wewilllook at
whathappens
inside the Hidden
## Layer #1
Wemade this
layersmall so as
to make easy to
visualizethe
effectof the
weights on the
loss.

## Degradation
◆After 2 epochsof training, letuslook atthe averageLoss
(categoricalcross-entropy) asa functionof twoof the weights of
HiddenLayer #1
w1
w2
## Darkerblue
meanssmaller
lossvalue
The gradient
wouldnow
movethe
weights
towardsthis
point

## Degradation
◆After 2 epochsof training, letuslook atthe averageLoss
(categoricalcross-entropy) asa functionof twoof the weights of
HiddenLayer #1
w1
w2
However, the Loss seenby Hidden
Layer #1 dependson the current
weights of HiddenLayer #2 and of
the Output Layer
## Whathappenswhenthoselayers
changetheirweights?
## Darkerblue
meanssmaller
lossvalue
The gradient
wouldnow
movethe
weights
towardsthis
point

## Degradation
◆After 40epochsof training, the averageLoss with respectto the
sametwothe weights of HiddenLayer #1 nowbecomes:
## Darkerblue
meanssmaller
lossvalue
The gradient
wouldnow
movethe
weights
towardsthis
point
w1
w2

## Degradation
◆After 40epochsof training, the averageLoss with respectto the
sametwothe weights of HiddenLayer #1 nowbecomes:
The changein the following layers
has"moved" the position of the
optimalweights for thislayerto a
completelydifferentpart of the
weight space!
Thus, thislayerhas"wasted" its
time movingtowardsthe wrong
point!
w1
w2
## Darkerblue
meanssmaller
lossvalue
The gradient
wouldnow
movethe
weights
towardsthis
point

## Degradation
◆After 40epochsof training, the averageLoss with respectto the
sametwothe weights of HiddenLayer #1 nowbecomes:
The more layersfollow the one we
are considering, the worsethe
problembecomes.
Thisisway degradationisa
concernfor deep architectures.
w1
w2
## Darkerblue
meanssmaller
lossvalue
The gradient
wouldnow
movethe
weights
towardsthis
point

## Degradation
Anotherexampleof degradation:
[He et al., 2016]

## Degradation
[He et al., 2016]
Thisisnotoverfitting: wegetworse
performance on the training set
Anotherexampleof degradation:

## Degradation
◆How can wereduce degradation?

## Degradation
◆How can wereduce degradation?
◆One idea isto make the gradientof the lossarriveatthe first
layerswith lessintermediate steps

## Degradation
◆How can wereduce degradation?
◆One idea isto make the gradientof the lossarriveatthe first
layerswith lessintermediate steps
▪But wewantto havemanylayers(Deep Learning);
howdo wereconcilethesetwogoals?

## Degradation
◆How can wereduce degradation?
◆One idea isto make the gradientof the lossarriveatthe first
layerswith lessintermediate steps
◆Wemake a non-sequentialarchitecture, in whichthe gradient
propagatesthroughseveralpaths:
▪some of themshort, to addressthe degradationproblem
▪some of themlonger, to getthe benefits of deep learning

Skip connections
◆The basicidea isto use asa building blocka group of layersthat
include a skip connection(i.e. a connection thatskips some of
the layers)
## Weight Layer
ReLU
## Weight Layer
## 푥
## 푦=푓(푥)
## We
replace
this:
(푓isthe compositionof the linear combinationperformedby
the first weight layer, the ReLUactivation functionand the
linear combinationperformedby the second weight layer)

Skip connections
◆The basicidea isto use asa building blocka group of layersthat
include a skip connection(i.e. a connection thatskips some of
the layer)
## Weight Layer
ReLU
## Weight Layer
... with this:
## Weight Layer
ReLU
## Weight Layer
## +
## Skip
connection
## 푥
## 푦=푓(푥)
## 푥
## 푦=ℎ푥=푥+푓(푥)
## 푓(푥)

Skip connections
◆Notes
▪in order to make a skip connection, 푥and 푓(푥)must havethe sameshape
## (thismayrequirepadding)
▪Here wehaveusedtwoweight layersand one non-linear layer, butthe
building blockcouldhavemore...
▪Also, the kindof weight layerisnotessential(e.g. theycouldbe fully
connectedor convolutional)
◆Duringgradientpropagation, the skip connections providea
"fast lane" for the gradientto quicklyarriveto the previous
layers

Skip connections
◆Whythe skip connection helps the gradientpropagation?
## Weight Layer
ReLU
## Weight Layer
## +
PreviousLayer
## Weight Layer
ReLU
## Weight Layer
PreviousLayer
## 푥
## 푦=푓(푥)
## 푥
## 푦=ℎ푥=푥+푓(푥)
## 푓(푥)

Skip connections
◆Considerfirst whathappenswithouta skip connection
## Weight Layer
ReLU
## Weight Layer
PreviousLayer
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푥
## 푦=푓(푥)
Thisisthe gradient
receivedfrom the
layersdownstream
Thispart dependson the
weights of the layersA and
## B.
## A
## B

Skip connections
◆Considerfirst whathappenswithouta skip connection
## Weight Layer
ReLU
## Weight Layer
PreviousLayer
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푥
## 푦=푓(푥)
Thisisthe gradient
receivedfrom the
layersdownstream
Thispart is"unstable",
changingitsvaluesuntilA
and B reachconvergence
## A
## B

Skip connections
◆Considerfirst whathappenswithouta skip connection
## Weight Layer
ReLU
## Weight Layer
PreviousLayer
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푥
## 푦=푓(푥)
Thisisthe gradient
receivedfrom the
layersdownstream
Also, ifsome component of
thisissmall, the
correspondingcomponent
of the gradientwrt푥willbe
small
## A
## B

Skip connections
◆Nowconsiderwhathappenswitha skip connection
## Weight Layer
ReLU
## Weight Layer
## +
PreviousLayer
## 푥
## 푦=ℎ푥=푥+푓(푥)
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕ℎ
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## ∙1+
## 휕푓
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## +
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푓(푥)

Skip connections
◆Nowconsiderwhathappenswitha skip connection
## Weight Layer
ReLU
## Weight Layer
## +
PreviousLayer
## 푥
## 푦=ℎ푥=푥+푓(푥)
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## +
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푓(푥)
Thispart hasthe same
problemthatwehaveseen
before...

Skip connections
◆Nowconsiderwhathappenswitha skip connection
## Weight Layer
ReLU
## Weight Layer
## +
PreviousLayer
## 푥
## 푦=ℎ푥=푥+푓(푥)
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## +
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푓(푥)
... butthispart isthe gradient
receivedfrom downstream,
propagatedwithoutchanges!

Skip connections
◆Nowconsiderwhathappenswitha skip connection
## Weight Layer
ReLU
## Weight Layer
## +
PreviousLayer
## 푥
## 푦=ℎ푥=푥+푓(푥)
The previouslayerneedsto
receivethe gradient
## 휕퐿표푠푠
## 휕푥
## Thisiscomputedas:
## 휕퐿표푠푠
## 휕푥
## =
## 휕퐿표푠푠
## 휕푦
## +
## 휕퐿표푠푠
## 휕푦
## ∙
## 휕푓
## 휕푥
## 푓(푥)
So, thispart of the gradient
makes the previouslayer
immediatelymoveitsweights in
the rightdirection, without
havingto waitfor convergence
of layersA and B
## A
## B

## Residuallearning
◆Another way of viewingthe skip connections isthateachbuilding
block, insteadof learning itsownfunctionℎ(푥), islearning the
residual:
## 푓(푥)=ℎ(푥)−푥
◆For thisreason, thistechnique iscalledresiduallearning

ResNet
◆Introducedin 2016, ResNetisa CNN
architecturethatusesthe residualblocksto train
a large numberof layers
◆Improvedthe classificationperformance on the
ImageNetchallenge
A ResNetwith 34
layers

Normalizationof layerinputs
◆An effectivetechnique for speedingup the learning of deep
networks isto reduce the "coupling"betweenthe layersby
making the laterlayersindependentof the meanand of the
varianceof the outputs of the earlierlayers
◆In thisway, the laterlayersare lessaffectedby the factthat
earlierlayersare undergoinglarge weights updates (thatmodify
the meanand varianceof theiroutput) duringthe initialphasesof
the training

Normalizationof layerinputs
◆Thiswouldbe easy ifweknewin advancethe meanand the
standard deviationof the outputs of a layer
PreviousLayer
NormalizationLayer
## Next Layer
## 푋
## 푋
## ′
## =
## 푋−휇
## 휎
Thislayerdoesjust a
linear transformation
## Thislayernowreceives
inputs with mean=0 and
stddev=1

## Batch Normalization
◆During training, the true휇and 휎can be approximatedby
computing theirestimatorson the minibatch(thisiswhythe
technique iscalledbatch normalization)
PreviousLayer
NormalizationLayer
## Next Layer
## 푋
## 푋
## ′
## =
## 푋−휇
## 푚푖푛푖푏푎푡푐ℎ
## 휎
## 푚푖푛푖푏푎푡푐ℎ
Training phase

## Batch Normalization
◆Duringtest/operationof the network, the true휇and 휎are
approximatedby usingtheirestimatorson the training set
PreviousLayer
NormalizationLayer
## Next Layer
## 푋
## 푋
## ′
## =
## 푋−휇
## 푡푟푎푖푛
## 휎
## 푡푟푎푖푛
## Test/operationphase

## Batch Normalization
◆A Batch Normalizationlayerisslightlymore complex:
## 푋
## ′
## =훾∙
## 푋−휇
## 휎
## +훽
▪where훾and 훽are parameterslearnedby the layer
◆Itisusuallyappliedbeforethe non-linear activation functionfor
betterresults
## Weight Layer
Batch normalization
ReLU
Thislayerdoesnotrequirethe bias
weights, sincetheirroleistakenby
the 훽of the batch normalization

## Batch Normalization
◆Common misconception(in students):
thinking thatbatch normalizationisusedto
normalizethe inputs of the neuralnetwork
## (wrong!)
◆Correct: Batch Normalizationisappliedto
intermediate valuescomputedby the network,
i.e. to the output of some layer, beforepassing
itto the nextlayer

## Batch Normalization
◆Whydoesbatch normalizationhelp the network to learnfaster?

## Batch Normalization
◆Considerfirst whathappenswithoutbatch normalization
PreviousLayer
## Next Layer
## 푋
Duringnetwork training, layerB receives
the values푋producedby layerA, and
triesoptimizeitsownweights to
minimizethe function:
## 피
## 푋
## 퐿표푠푠(푋,푊
## 퐵
## )
## A
## B
Expectedvalueof the loss,
with respectto the inputs
receivedfrom layerA

## Batch Normalization
◆Considerfirst whathappenswithoutbatch normalization
PreviousLayer
## Next Layer
## 푋
Duringnetwork training, layerB receives
the values푋producedby layerA, and
triesoptimizeitsownweights to
minimizethe function:
## 피
## 푋
## 퐿표푠푠(푋,푊
## 퐵
## )
However, the probabilitydistribution
of 푿dependson 푾
## 푨
, the weights of
layerA.
Duringthe training, 푾
## 푨
change, and
thuslayerB cannotnowitstruegoal
functionuntillayerA isnearto its
convergence!
## A
## B

## Batch Normalization
◆Nowconsiderwhathappenswith batch normalization
PreviousLayer
## Next Layer
Duringnetwork training, layerB receives
the values푋′producedby the
normalizationlayer, and triesoptimizeits
ownweights to minimizethe function:
## 피
## 푋
## ′
## 퐿표푠푠(푋′,푊
## 퐵
## )
## A
## B
Expectedvalueof the loss,
with respectto the inputs
receivedfrom the
normalizationlayer
NormalizationLayer
## 푋
## 푋
## ′
## =훾
## 푋−휇
## 푡푟푎푖푛
## 휎
## 푡푟푎푖푛
## +훽

## Batch Normalization
◆Nowconsiderwhathappenswith batch normalization
PreviousLayer
## Next Layer
Duringnetwork training, layerB receives
the values푋′producedby the
normalizationlayer, and triesoptimizeits
ownweights to minimizethe function:
## 피
## 푋
## ′
## 퐿표푠푠(푋′,푊
## 퐵
## )
The probabilitydistributionof 푋′still
dependson 푊
## 퐴
## .
However, the meanand stddevof 푿′
are nowindependentof layerA
(the meanis휷and the varianceis휸).
## A
## B
NormalizationLayer
## 푋
## 푋
## ′
## =훾
## 푋−휇
## 푡푟푎푖푛
## 휎
## 푡푟푎푖푛
## +훽

## Batch Normalization
◆Nowconsiderwhathappenswith batch normalization
PreviousLayer
## Next Layer
Duringnetwork training, layerB receives
the values푋′producedby the
normalizationlayer, and triesoptimizeits
ownweights to minimizethe function:
## 피
## 푋
## ′
## 퐿표푠푠(푋′,푊
## 퐵
## )
The probabilitydistributionof 푋′still
dependson 푊
## 퐴
## .
However, the meanand stddevof 푋′are
nowindependentof layerA.
Thisreducesthe impact of the
changesin A on the optimization
problemfacedby layerB.
## A
## B
NormalizationLayer
## 푋
## 푋
## ′
## =훾
## 푋−휇
## 푡푟푎푖푛
## 휎
## 푡푟푎푖푛
## +훽

GreedySupervisedPre-Training
◆Anothertechnique thatcan speed-up the training of verydeep
networks
◆The basicidea isto start the training of the initiallayersusinga
network with lessdepththanthe finalone, so thattheycan
quicklylearn(beingcloserto the output) some weights thatare
reasonablygood
◆Then, the  initiallayersare placedinside the finalnetwork and
the training isfinished

GreedySupervisedPre-Training
InitialLayer 1
InitialLayer 2
## Temporaryoutput
layer(s)
input
output
Pre-Training: the initiallayersare
trainedusinga pre-training network
thatisshallowerthanthe final
network
The pre-training network usesthe
sametraining set, desiredoutput
and lossfunctionasthe final
network

GreedySupervisedPre-Training
InitialLayer 1
InitialLayer 2
## Temporaryoutput
layer(s)
input
output
After Pre-Training: the output layers
layersof the pre-training network
are discarded

GreedySupervisedPre-Training
InitialLayer 1
InitialLayer 2
Finaloutput layer(s)
input
output
The otherlayersof the finalnetwork
are addedwith random initial
weights
The finalnetwork isthentrained
## Intermediate 3
## Intermediate 4
The initiallayerskeepthe weights
learnedduringpre-training asinitial
values

GreedySupervisedPre-Training
◆The advantageisthatin the training of the finalnetwork, the
initiallayersdo notstart from random weights, butare already
close to theiroptimalvalues
▪Thus, the training of the finalnetwork isfasterand lessprone to
degradation
◆Youcan repeatthistechnique severaltimes, building your
network incrementally

GreedySupervisedPre-Training
InitialLayer 1
InitialLayer 2
Finaloutput layer(s)
input
output
## Intermediate 3
## Intermediate 4
Theselayerslearnslowly, because
theyare far from the output layer
wherethe lossfunctionis
computed, and so receivea very
distortedgradientuntilthe
intermediate and finallayersare
nearconvergence.
WithoutusingGSPT:

GreedySupervisedPre-Training
InitialLayer 1
InitialLayer 2
Finaloutput layer(s)
input
output
Theselayerslearnslowly, since
theyreceivetheirinputs from the
initiallayers, and thusthe function
theytryto optimizeiscontinuosly
changinguntilthe initiallayersare
nearconvergence.
## Intermediate 3
## Intermediate 4
WithoutusingGSPT:

GreedySupervisedPre-Training
Theselayerslearnquickly, because
theyare close to the output layer.
Using GSPT: pre-training phase
InitialLayer 1
InitialLayer 2
## Temporaryoutput
layer(s)
input
output

GreedySupervisedPre-Training
InitialLayer 1
InitialLayer 2
Finaloutput layer(s)
input
output
Theselayerslearnquicky, sincethe
initiallayersare alreadyneartheir
point of convergence.
## Intermediate 3
## Intermediate 4
Using GSPT: finaltraining phase
## Theselayershavealreadylearned
theirweights, or theyonlyneedto
performminor adjustments.

## Auxiliaryheads
◆Anothertechnique, relatedto skip connections and pre-training,
isthe use of additionalouputlayers, attachedto intermediate
hiddenlayers
◆Theseouputs, calledauxiliaryheads, are trainedto performthe
sametask asthe primaryouput
◆Theirfunctionisto help ensurethatthe initiallayersreceivea an
adequategradientduringtraining; after training, the auxiliary
heads can be removedfrom the network

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
input
output
## Intermediate 3
## Intermediate 4
Output layer(s)
output
## Auxiliaryhead
The auxiliaryhead is
trainedwith the
sameoutput values
and lossfunctionas
the primaryoutput
The network triesto
optimizethe sum of
the lossesof allits
heads

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
input
output
## Intermediate 3
## Intermediate 4
Output layer(s)
output
Duringtraining, the
gradientcan arrivefaster
to the initiallayersusing
thisroute

## Auxiliaryheads
◆The effectissimilarto pre-training, butyoutrainthe whole
network in one single phase
◆Youcan havemultiple auxiliaryheads atdifferentpositions
◆Youcan changethe "weight" of the auxiliaryheads lossduring
the training
▪The auxiliaryheads can havemore importancein the first epochs, and less
importancewhenthe network isclose to finishingitstraining

## Auxiliaryheads
◆Whyauxiliaryheads help the network to learnfaster?

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
## 푋
## Intermediate 3
## Intermediate 4
## 푌=푓(푍)
## 푍=ℎ(푋)
Considerfirst whathappenswithout
auxiliaryheads
푋network input
푌network output
푍intermediate result
ℎfunctionimplementedby the
initiallayers
푓functionimplementedby the
finallayers(intermediate+output)

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
## 푋
## Intermediate 3
## Intermediate 4
## 푌=푓(푍)
## 푍=ℎ(푋)
Consider first whathappenswithout
auxiliaryheads:
The initiallayersperformtheirlearning
usingthe gradient:
## 휕퐿표푠푠
## 휕푍
## =
## 휕퐿표푠푠
## 휕푌
## ∙
## 휕푓
## 휕푍
Thispart is"unstable" until
the intermediate/finallayers
are nearconvergence.
Thismakes the learning of
the initiallayersslower.

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
## 푋
## Intermediate 3
## Intermediate 4
Aux. output layer(s)
## 푌=푓(푍)
## 푍=ℎ(푋)
## 푌
## ′
## =푔(푍)
Nowconsiderwhathappenswith one
auxiliaryhead:
푔functionimplementedby the
auxiliaryoutput layers

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
## 푋
## Intermediate 3
## Intermediate 4
Aux. output layer(s)
## 푌=푓(푍)
## 푍=ℎ(푋)
## 푌
## ′
## =푔(푍)
Nowconsiderwhathappenswith one
auxiliaryhead:
The initiallayersperformtheirlearning using
the gradient:
## 휕퐿표푠푠
## 휕푍
## =
## 휕퐿표푠푠
## 휕푌
## ∙
## 휕푓
## 휕푍
## +
## 휕퐿표푠푠
## 휕푌′
## ∙
## 휕푔
## 휕푍
Thispart of the gradientismore "stable",
becausethe function푔(푍)hasless
layers, and thuswillconverge fasterthan
## 푓(푍).

## Auxiliaryheads
InitialLayer 1
InitialLayer 2
Output layer(s)
## 푋
## Intermediate 3
## Intermediate 4
Aux. output layer(s)
## 푌=푓(푍)
## 푍=ℎ(푋)
## 푌
## ′
## =푔(푍)
Nowconsiderwhathappenswith one
auxiliaryhead:
The initiallayersperformtheirlearning using
the gradient:
## 휕퐿표푠푠
## 휕푍
## =
## 휕퐿표푠푠
## 휕푌
## ∙
## 휕푓
## 휕푍
## +
## 휕퐿표푠푠
## 휕푌′
## ∙
## 휕푔
## 휕푍
Thus, thispart of the gradienthelps the
initiallayersto converge to the right
weights withouthavingto waitthatthe
intermediate and finallayersare near
theirconvergence.

Auxiliaryheads: example
◆GoogLeNet(Szegedyet
al., 2015), proposedfor the
ImageNetchallenge

Auxiliaryheads: example
## Input
## Output
Auxiliaryheads (with loss
weighted0.3)
"Inception" building blocks,
with severalparallelpaths
whoseoutput is
concatenated