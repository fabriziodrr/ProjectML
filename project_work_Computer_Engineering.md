

Machine Learning Project work:
“Waste typeidentification”
Mario Vento and Diego Gragnaniello

Link to the training dataset

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions:
◆Natural photosof differentresolution
◆Preprocessedphotos(e.g., background removed)
◆Multiple objects(of the sameclass) in the photo
◆Some class isnotfullyrepresentedby the objectsin
the training set (i.e., some wasteobjectsmaynotbe in
the training set, butthisisnormal)

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions:
◆4 classes
BatteryMetalOrganicPlastic

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions:
◆4 classes
◆3 multi-classes
## Clothing
-Clothes
-Shoes
## Glass
-Brown
-Green
-Transparent
## Papery
-Paper
-Cardboard

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions:
◆4 classes
◆3 multi-classes
◆1 «other» class
## Undifferentiated

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions:
◆4 classes
◆3 multi-classes
◆1 «other» class
BatteryMetalOrganicPlastic
## Undifferentiated
## Clothing
-Clothes
-Shoes
## Glass
-Brown
-Green
-Transparent
## Papery
-Paper
-Cardboard

The task to address
◆The goal isto recognizea broadclass of
images of wasteobjectsin diverse conditions:
◆4 classes
◆3 multi-classes
◆1 «other» class
## Label 0: Battery
## Label 1: Clothing
## Label 2: Glass
## Label 3: Metal
## Label 4: Organic
## Label 5: Papery
## Label 6: Plastic
## Label 7: Undifferentiated

Competitionand rules
◆Images are acquiredby differentcamerasand
in verydifferentconditionsand can be post-
processedin serveralways
◆Images maynotrepresentanykindof objectfor
eachcathegory
◆Youcannotextendthe training set
◆You candecide the split

IMPORTANT: Plan youexperiments
◆Do hypothesis on why your model is not working
◆Design an experiment to verify that specific hypothesis
◆Analyze results and comment them, thus select how to
proceed
◆Do a general plan of the experiments
▪Which hyperparameters you want to explore?
▪Which models/training paradigms to compare?
▪How much time does it takes?

IMPORTANT: Model training and
validation isnota feed-forwardprocess
◆Alternate trainings and validations:
◆After each validation, try to understand which samples
are misclassified and why
◆Change your model and/or training set to improve the
performance
◆Ifthe performance seemsverygood, be sure thatthe
validationset ischallengingenough
◆Keep track of yourcountermeasures(evenifnot
successful) for the finalproject presentation

What you can use
◆Youcannotextendthe providedtraining set
◆You candecide the train/val/cross-val split
◆Youcanuse data augmentationtechniques
◆Any PyTorchalgorithm(whatever kindof classifier,
includingnon-neuralones, preprocessing, training
strategy, validation), BUT:
▪You must be ableto explainwhatyouhaveused
▪Itmust be runnablewith PyTorch
## ▪inside Google Colab;
▪in testusinglessthan4 GB GPU RAM;
▪in trainingusinglessthan5 GB GPU RAM;

Performance willbe evaluatedon a private test set
measuringthe overall:
◆Balancedaccuracy, i.e., the aritmeticmeanamong
True Positive Rates (TPR) of the 8 classes:
Bal.Acc= (TPR_battery+TPR_clothing+TPR_ glass
## +
TPR_ metal  +TPR_ organic+TPR_
papery+
TPR_ plastic+TPR_ undifferentiated) / 8
Model evaluation(1 of 2)

In the evaluationwewillconsiderthe resources
neededby the model and itscomputationalcomplexity
Youhaveto selectthe best trade-off among:
◆Bal.Accperformance, largerisbetter
◆GPU memoryrequired(duringtest), lessisbetter
◆Processing frame rate (duringtest), i.e., howfast
the methodcan processthe input sample usinga
certainGPU, largerisbetter
Model evaluation(2 of 2)

Share the load
◆Eachmemberof the team willbe
requestedto submitan estimate of the
individualeffortcontributedby all
members
▪To prevent"free riders"
▪Submissionswillbe "blind" (eachmemberwill
notseethe submissionsof othermembers)

What you must submit
1.A link via mail or Moodleto:
1.a Google Drive folder
(do notcreate a SharedDrive)
2.The folder must be renamedwith yourteam name
(seecolumn B of the team composition sheet)
3.Make the link accessibleto all
4.Do notaddProfessorsto directory members

What you must submit
2.The directory must contain:
a)The Python Notebook to trainthe solution, eventually
includingthe code to generate data usingaugmentation
b)The train/validationsplit protocol
(NOT THE DATA, butthe sample list asCSV file)
c)The files of the savedmodels/weights after the training
d)The code neededto test yoursystem
(test script; seenextslide)
e)The full report (10 pages) and slides (5 minutes talk)

What you must submit
The test script must be a Google ColabNotebook containing:
◆The code to load yourtrainedmodel
◆A "predict" functionwith the following specification:
▪Prototype: predict(X)
▪where: X isthe tensorcontaininga batch of test samples; the shapeof X is:
(batch_size, rows, cols, 3); the typeisuint8
▪returnvalue: the tensorwith the predictionon the batch; the shapeof the
returnvalueis:
(batch_size, 1); the typeisuint8 and containsthe labels
Note1: do notchangethe correspondancebetweenlabels and class]
Note 2: batch_sizeisthe numberof samples in the batch, and isnota fixed
value; the functionmust work independentlyof thisvalue
◆The predictfunctionwillnotseethe wholetest set atonce
◆The predictfunctionmust performallthe required
preprocessingon the batch of test data, and the
postprocessingon the resultsbeforereturningthem

Whatyoumust submit: the presentation
◆5-minutes presentation(slide in English):
1.Do notrestate the problem/describethe dataset
2.Go straightto yoursolution
1.The rationaleto collect/organizethe dataset, includingthe
dataset split intotraining and validationsets.
2.The pre-processing pipelines adopted.
3.The network architecturescompared.
4.The training hyperparametersetting, includingthe loss
function.
3.Let usknow whatchallenges youencontered, howyou
triedto addressthem, whatdidnotwork and why, what
contermeasureyouadopted, whattakehomemessages
yougetfrom the results...

Whatyoumust submit: the report
◆10-pages font 12 report (in English):
1.Do notrestate the problem/describethe dataset
2.Do notchronologicallypresentyourexperimentswithout
explaininghowyouplan them
3.Let usunderstandwhathypothesisyoudidaboutthe
problem, howyoumanagedto solve itand the results
Ifyouwant, youcan presentin Italian.

IMPORTANT: Don’tforgetto
◆Write the names of allthe team membersin
the Google Drive folder (in a text file)
◆Ensurethatthe linkyousubmitisreadableto
anyone(no authorizationmust be requested)
◆Make sure thatthe test script iscompliant
with the specification(ifyouhavedoubts
aboutthe specification, ask)

DEADLINE: beginningof July (TBD)
◆Tentativeproject work discussion: July, 10th
(time and room to be defined)
◆All team membersmust discussthe project
(includingthosethatbook for theirindividual
oralexamin September or later)