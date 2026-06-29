

## Machine Learning
ReinforcementLearning
## Prof. Mario Vento
## Prof. Diego Gragnaniello

ReinforcementLearning
◆A naturallearning paradigm:
Color recognitionDevice utilization

ReinforcementLearning
◆Complexcontrol
◆Environment interaction

ReinforcementLearning
◆The importanceof simulation

ReinforcementLearning
◆2024 project work
◆In the future

The problem
◆Youare designingan agentthatinteractswith an environment
◆The agent observesthe currentconditionof the environment
througha set of statevariabless
◆At each(discrete) time instant t
k
, the agent choosesan actiona
to affectthe environment
◆Asa result, the environmentproducesa new state s’, and a
rewardrthatcan be positive (the agent isdoingwellitstask) or
negative (the agent isdoingsomethingwrong)

The problem
◆You wantto learnan optimalbehaviorfor youragent (i.e. choose
the actions thatmaximizethe totalrewards)

The problem
◆The rewarddependsalsoon the state (i.e. on the pasthistory);
the consequencesof an action maybe notrewarded
immediately!
◆Youwantto optimizethe overall behaviorof youragent, notonly
the immediate rewards
◆The relation betweenstate, action, new state and rewardmaynot
be deterministic(i.e. youcan havea stochasticrelation)

## Episodes
◆An episodeisa sequenceof states, actions and rewardsthatcan
be observedfor yoursystem
◆Startingfrom a state s
## 0
## :
## ▪s
## 0
, a
## 0
, r
## 1
, s
## 1
, a
## 1
, r
## 2
, s
## 2
, a
## 2
, ..., r
n-1
, s
n-1
, a
n-1
, r
n
, s
n
▪An episode may have a finite length because of the nature of the problem
(e.g. a game); in thiscase the system reachesa terminal statefrom which
youcannotcontinue
▪Alternatively, youmayartificiallyterminate an episodeafter a finite number
of steps for computationalreasons(in thiscase, the system doesnotarrive
to a terminal state)

## Episodes
s
## 0
Youstart from a state s
## 0
Your system can obtainfrom
the environmentsome
information aboutthe state
(e.g. a feature vector).
Note thatthe observed
information on the state may
be incomplete (i.e. youdon't
haveallthe information
neededto predictthe behavior
of the environment)

## Episodes
s
## 0
Given the information
available, yoursystem
choosesan action a
## 0
among
the set of availableactions.
a
## 0

## Episodes
s
## 0
The environmentrespondsto
the action a
## 0
with a new state
s
## 1
and a rewardr
## 1
## .
Your system cannotpredictr
## 1
and s
## 1
from s
## 0
and a
## 0
## :
•the relationshipbetween
themmaybe deterministic,
butunknownto yoursystem
•itmaydependon some
unobservablepart of the
state
•itmayevenbe stochastic
a
## 0
s
## 1
r
## 1

## Episodes
s
## 0
Note thatthe rewardr
i
may
dependnotjust on the last
action a
i-1
, butmaybe related
to some actions thatare very
far in the past
a
## 0
s
## 1
r
## 1
s
## 2
r
## 2
a
## 1
The valueof
thisrewardmaybe causedby thataction

## Episodes
s
## 0
An episodemayend ata
terminal state, i.e. a state in
whichyoursystem cannot
performmore actions.
Evenifyoursystem doesnot
reacha terminal state, you
maytruncatethe episodeata
predefinedmaximum lengthfor
making the learning problem
tractable.
a
## 0
s
## 1
r
## 1
s
## 2
r
## 2
a
## 1
s
n
r
n
a
## 2
a
n-1
Terminal state

Example: AutonomousRover
Level #0: idealsimulationon discrete grid
Envand State information:
## •gridspace(e.g., 4x4)
•rover position
## Actions:
•moveleft/ right/ up / down
Terminal state:
•the rover reachesthe Finish line or hits an object
## Reward:
•-1000 ifithits the rock
•+1000 ifitreachesthe Finish line

Example: AutonomousRover
Level #1: idealsimulationw/o grid
Envand State information:
•closedspace4m x 4m
•idealrover position
## Actions:
•forward/ backward(speed, duration)
## •steering (degree)
Terminal state:
•the rover reachesthe Finish line or hits an object
## Reward:
•-1000 ifithits the rock
•negative rewardfor long paths
•positive rewardifitapproachesthe goal
•+1000 ifitreachesthe Finish line

Example: AutonomousRover
Level #2: realsimulationw/o movingobjects
Envand State information:
•closedspace4m x 4m
•real(noisy) rover position (sensors)
## Actions:
•forward/ backward(speed, duration)
## •steering (degree)
Terminal state:
•the rover reachesthe Finish line or hits an object
## Reward:
•-1000 ifithits the rock
•negative rewardfor long paths
•positive rewardifitapproachesthe goal
•+1000 ifitreachesthe Finish line

Example: AutonomousRover
Level #3: realsimulationw/ movingobjects
Envand State information:
•closedspace4m x 4m
•real(noisy) rover position (sensors)
•camera / ultrasounddata (sensors)
## Actions:
•forward/ backward(speed, duration)
## •steering (degree)
## •perceptionalgorithm
Terminal state:
•the rover reachesthe Finish line or hits an object
## Reward:
•-10000 ifithits a person
•-1000 ifithits the rock
•negative rewardfor long paths
•positive rewardifitapproachesthe goal
•+1000 ifitreachesthe Finish line

Example: AutonomousRover
Level #4: real-world experiment
Envand State information in the wild:
•closedspace4m x 4m
•real(noisy) rover position (sensors)
•camera / ultrasounddata (sensors)
Actions in the wild:
•forward/ backward(speed, duration)
## •steering (degree)
## •perceptionalgorithm
Terminal state:
•the rover reachesthe Finish line or hits an object
## Reward:
•-10000 ifithits a person
•-1000 ifithits the rock
•negative rewardfor long paths
•positive rewardifitapproachesthe goal
•+1000 ifitreachesthe Finish line

Example: AutomaticPark Assist

Example: AutomaticPark Assist
State information: the distancesread
by the sonarsaroundthe car
Action: the commandgivento the
steering wheeland to the
accelerator/brake
Terminal state: whenthe car is
parked, or the maximum allowedtime
hasexpired
Reward: in the terminal state, a
positive valueifthe car isparallelto the
sidewalkand atthe prescribed
distancefrom it;
also, a negative rewardisgivenin
eachstate ifthe car hits anothercar or
the sidewalk

Example: video games and robotics
◆Learnplaying simplegames verywell:
▪Breakout
▪Lunarlander
◆Surpasshuman performance playing complex games
◆Learning dexterity

Example: autonomousdriving
◆Simulation
▪Learnto drive
▪Learnto park
▪Learnto race
◆From simulationto realworld
▪Learnto drive in the traffic
◆Real world
▪Movethe trainedagent to a real-world application

An extendedexample
◆In order to understandthe operationof learning algorithm, wewill
presenta complete examplefor a simpleproblem
◆In ourproblemwewillhavea discrete set of states, a discrete set
of actions, and the relationships:
## 푠
## 푡
## ,푎
## 푡
## →푠
## 푡+1
## 푠
## 푡
## ,푎
## 푡
## →푟
## 푡+1
willbe deterministic... butunknownto ouragent!

An extendedexample: the enviroment
1.Ouragent     can move(with no memory) in the 2D discrete gridenvironmentdepictedbelow.
2.9 possiblestates: {A, B, C, D, E, F, G, H, I}.
3.The initialstate isalwaysA.
4.3 finalstates: {C, H, I} with reward{+1, -1, +2}, respectively.
5.No rewardfor intermediate states.
6.3 possibleactions: {Up, Down, Right}, eachmovesthe agent in the obviousdirection.
7.The action hasno effectifthereisno cellin thatdirection.
GOAL: finda policy, i.e., the functionthatselectthe next
action giventhe currentstate, thatoptimizesthe
discountedfuture reward, with 훾=0.99
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
An extendedexample: the Qfunction
Let’sdefinea tableQ(s, a):
-one rowfor eachstate s;
-one columnfor eachaction a:
The Q(s, a) valueisa running estimate of future reward(untilthe end of the episode!)
of takingthe action a from state s
WeinitializeQto zerosfor simplicity
(itshouldbe initializedwith random values)
푸(풔,풂)UpDownRight
## A0.000.000.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00

An extendedexample
Now weare ready to runEpisode1:
## •startingfrom 푠
## 0
## =퐴
•welook for the action maximizingfuture reward: 푎
## 0
## =argmax
## 푎
## 푄(푠
## 0
## ,푎)
푸(풔,풂)UpDownRight
## A0.000.000.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Since allthe 3 actions havethe maximum Qvalue, the algorithmmaychooseone atrandom.
→suppose thatthe algorithmchooses푎
## 0
## =푅푖푔ℎ푡
푸(풔,풂)UpDownRight
## A0.000.000.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode1
## 푎
## 0
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Sinceallthe 3 actions havethe maximum Qvalue, the algorithmmaychooseone atrandom.
→suppose thatthe algorithmchooses푎
## 0
## =푅푖푔ℎ푡
## Wehave푠
## 1
## =퐻, 푟
## 1
=−1and the new state isterminal.
푸(풔,풂)UpDownRight
## A0.000.000.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode1
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Since allthe 3 actions havethe maximum Qvalue, the algorithmmaychooseone atrandom.
→suppose thatthe algorithmchooses푎
## 0
## =푅푖푔ℎ푡
## Wehave푠
## 1
## =퐻, 푟
## 1
=−1and the new state isterminal.
## →weupdate 푄푠
## 0
## ,푎
## 0
## =푓푖푛푎푙푟푒푤푎푟푑=푟
## 1
## =−ퟏ
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode1
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
The expected
future reward
ifweare in A
and go Right

An extendedexample
Now wemust start Episode2.
The algorithmcan chooseeitherUp or Down;
→suppose itchooses푎
## 0
## =푈푝
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
## →update: 푄푠
## 0
## ,푎
## 0
## =푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
## →update: 푄푠
## 0
## ,푎
## 0
## =푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 풓
## ퟏ
is known and
providedby the env

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
## →update: 푄푠
## 0
## ,푎
## 0
## =푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 풓
## ퟏ
is known and
providedby the env
## 풎풂풙
## 풂
## 푸풔
## ퟏ
,풂isan estimation

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
## →update: 푄푠
## 0
## ,푎
## 0
## =푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+훾⋅푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 풓
## ퟏ
is known and
providedby the env
## 풎풂풙
## 풂
## 푸풔
## ퟏ
,풂isan estimation
discount for the estimation,
e.g., 훾=0.99

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
## →update: 푄푠
## 0
## ,푎
## 0
## =푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+훾⋅푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑
## =푟
## 1
## +0.99⋅max
## 푎
## 푄푠
## 1
## ,푎=0
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode2
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Now wemust choosethe nextaction 푎
## 1
The algorithmcan chooseeitherUp, Down or Right;
→suppose itchooses푎
## 1
## =푈푝
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## Episode2
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
We have푠
## 2
## =퐵, 푟
## 2
=0and the new state isNOT terminal.
## →update: 푄푠
## 1
## ,푎
## 1
## =푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+훾⋅푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑=
## =푟
## 2
## +0.99⋅max
## 푎
## 푄푠
## 2
## ,푎=0
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## Episode2
## 푎
## 0
## 푠
## 1
## ,푠
## 2
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Now wemust choosethe nextaction 푎
## 2
The algorithmcan chooseeitherUp, Down or Right;
→suppose itchooses푎
## 2
## =푅푖푔ℎ푡
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.000.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## Episode2
## 푠
## 2
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
We have푠
## 3
## =퐶, 푟
## 3
=+1and the new state isterminal.
## →update: 푄푠
## 2
## ,푎
## 2
## =푓푖푛푎푙푟푒푤푎푟푑=푟
## 3
## =+ퟏ
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 3
## Episode2
## 푎
## 2
## 푠
## 2
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Now wemust start Episode3.
The algorithmcan chooseeitherUp or Down;
→suppose itchooses푎
## 0
## =푈푝
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode3
## 푎
## 0
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
푸(풔,풂)UpDownRight
## A0.000.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode3
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
Then wehave푠
## 1
## =퐵, 푟
## 1
=0and the new state isNOT terminal.
## →update: 푄푠
## 0
## ,푎
## 0
## ←푖푚푚푒푑푖푎푡푒푟푒푤푎푟푑+훾⋅푒푥푝푒푐푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑=
## =푟
## 1
## +0.99⋅max
## 푎
## 푄푠
## 1
## ,푎=ퟎ.ퟗퟗ
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 0
## Episode3
## 푎
## 0
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
→nowthe system willchoose푎
## 1
## =푅푖푔ℎ푡.
We have푠
## 2
## =퐶, 푟
## 2
=+1and the new state isterminal.
## →update: 푄푠
## 1
## ,푎
## 1
## ←푓푖푛푎푙푟푒푤푎푟푑=푟
## 2
## =+ퟏ
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 2
## Episode3
## 푎
## 1
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

An extendedexample
In the following episodes, the system willalwayschoose:
## 1.푎
## 0
## =푈푝
## 2.푎
## 1
## =푅푖푔ℎ푡
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 2
## Episode4
## 푎
## 1
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0

Q-Learning –making errors
◆During the learning phase, it is useful to make some “errors”,
i.e. to choose a non-optimal action from time to time, so as to
get a more accurate estimate of Q for those state/action pairs
▪“you learn by making mistakes”
▪Trade-off: Exploitationvs Exploration
Make yourdecision
usingthe knowledge
youhavelearnedso
far...
Tryto gain more
knowledge...

An extendedexample(continued)
Once the system haslearnedthatthe path퐴→퐵→퐶isgood, itwillcontinue to use it.
However, thereisa betterpath퐴→퐸→퐹→퐺→퐼thathasneverbeenexplored...
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 2
## Episode4
## 푎
## 1
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0

Q-Learning –making errors
◆A simple way of introducing an amount of "exploration" is using
what is called an 휺-greedy policy during training:
## 푎
## 푡
## ←
## ൝
argmax
## 푎
## 푄(푠
## 푡
## ,푎)withprobability1−휀
arandomaction,withprobability휀
◆The largerthe valueof 휀(in the interval[0,1]), the more
deliberate "errors" willbe introduced
◆휀can be large atthe beginningof the training, and thenitcan be
progressivelyreduced

An extendedexample(continued)
With an 휀-greedypolicy thereisa small (butnot-null) probabilitythatthe algorithmchooses
action Down in 푠
## 0
,eventhoughUp looks more promising
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G0.000.000.00
## H0.000.000.00
## I0.000.000.00
## Episode19
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0

An extendedexample(continued)
From there, the algorithmmayrandomlyarriveto state I.
In thiscase, we update 푄푠
## 3
## ,푎
## 3
## ←푟
## 4
## =+2
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.000.00
## G+2.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 2
## Episode19
## 푎
## 1
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0
## 푠
## 3
## 푠
## 4
## 푎
## 2
## 푎
## 3

An extendedexample(continued)
In a differentepisode, the algorithmmayrepeatthe samepath.
In thiscase, we update 푄푠
## 2
## ,푎
## 2
## ←푟
## 3
## +훾∙max
## 푎
## 푄푠
## 3
## ,푎=+1.98
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.000.00
## F0.000.00+1.98
## G+2.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 2
## Episode42
## 푎
## 1
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0
## 푠
## 3
## 푎
## 2

An extendedexample(continued)
In a differentepisode, the algorithmmayrepeatthe samepath.
In thiscase, we update 푄푠
## 1
## ,푎
## 1
## ←푟
## 2
## +훾∙max
## 푎
## 푄푠
## 2
## ,푎=+1.96
푸(풔,풂)UpDownRight
## A+0.990.00-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.00+1.96
## F0.000.00+1.98
## G+2.000.000.00
## H0.000.000.00
## I0.000.000.00
## 푠
## 2
## Episode59
## 푎
## 1
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0

An extendedexample(continued)
In a differentepisode, the algorithmmayrepeatthe samepath.
In thiscase, weupdate 푄푠
## 0
## ,푎
## 0
## ←푟
## 1
## +훾∙max
## 푎
## 푄푠
## 1
## ,푎=+1.94
푸(풔,풂)UpDownRight
## A+0.99+1.94-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.00+1.96
## F0.000.00+1.98
## G+2.000.000.00
## H0.000.000.00
## I0.000.000.00
## Episode73
## 푠
## 1
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG
## 푠
## 0
## 푎
## 0

An extendedexample(continued)
From thispoint on, the algorithmwillchoosemostprobablythe path퐴→퐸→퐹→퐺→퐼,
especiallyifno cost isassociatedwith transitionstates
푸(풔,풂)UpDownRight
## A+0.99+1.94-1.00
## B0.000.00+1.00
## C0.000.000.00
## D0.000.000.00
## E0.000.00+1.96
## F0.000.00+1.98
## G+2.000.000.00
## H0.000.000.00
## I0.000.000.00
## Episode74
## BC
## +1
## D
## AH
## −1
## I
## +2
## EFG

◆Undefined number of states
◆Not deterministic rewards
## ◆...
→Cannot represent the expected future reward with a Table
→Can we use a Neural Network?
Whatifthe problemismore complex?

How do welearnthe policy?
◆Sincewecannotlearndirectly휋from a set of examples, wehave
to finda way to express 휋in termsof some otherfunctionthatwe
can learn
◆In the scientificliterature thereare severalways of doingthis
reformulation; the choiceof the methoddependsalsoon factors
suchas:
▪whetheryouwanta deterministicpolicy or a stochasticone
▪whetheryouraction spaceisdiscrete or continuous
▪whetheryouwantto collectyourlearning data usingthe verysamepolicy
youare tryingto learn, or youwantto use experimentsperformedwith
differentpolicies to improvethe policy youare learning

How do welearnthe policy?
◆In the following wewillpresentone particulartechnique, that
works for deterministicpolicies and for discrete action spaces
(butwewillseehowto extenditto continuousaction spaces
later)
◆Sincethistechnique usesan auxiliaryfunctioncommonlycalled
푄, itisnamedQ-Learning
◆Key idea: movethe problemfrom policy learning to future reward
learning

◆Key idea: insteadof directlylearning the policy(difficult!), we
wantto learnto predictfuture reward(i.e., the Qfunction) using
a NeuralNetwork (noteasy, butlessdifficult).
▪Once the NN istrained, the policy isto selectactions thatmaximizesthe future
rewardestimatedby the NN ateachtime instant
Q-learning approach
## Neural
## Network
Whatisthe action thatmaximizes
future rewardgiventhe currentstate?

◆Key idea: insteadof directlylearning the policy(difficult!), we
wantto learnto predictfuture reward(i.e., the Qfunction) using
a NeuralNetwork (noteasy, butlessdifficult).
▪Once the NN istrained, the policy isto selectactions thatmaximizesthe future
rewardestimatedby the NN ateachtime instant
Q-learning approach
## Neural
## Network
EstimatedQ
for action #1
EstimatedQ
for action #2
EstimatedQ
for action #N
## ...
Whatisthe action thatmaximizes
future rewardgiventhe currentstate?

◆Key idea: insteadof directlylearning the policy(difficult!), we
wantto learnto predictfuture reward(i.e., the Qfunction) using
a NeuralNetwork (noteasy, butlessdifficult).
▪Once the NN istrained, the policy isto selectactions thatmaximizesthe future
rewardestimatedby the NN ateachtime instant
Q-learning approach
## Neural
## Network
Whatisthe action thatmaximizes
future rewardgiventhe currentstate?
EstimatedQ
for action #1
EstimatedQ
for action #2
EstimatedQ
for action #N
## ...
Select the
maximum

◆Key idea: insteadof directlylearning the policy(difficult!), we
wantto learnto predictfuture reward(i.e., the Qfunction) using
a NeuralNetwork (noteasy, butlessdifficult).
▪Once the NN istrained, the policy isto selectactions thatmaximizesthe future
rewardestimatedby the NN ateachtime instant
Q-learning approach
## Neural
## Network
Whatisthe action thatmaximizes
future rewardgiventhe currentstate?
EstimatedQ
for action #1
EstimatedQ
for action #2
EstimatedQ
for action #N
## ...
Select the
maximum
Based on myfuture rewardestimation, the best action isAction #2

◆Goal: learn the best policy with a neural network
(i.e., agent uses NN to select actions maximizing the future reward)
◆Two steps solution:
Q-learning approach

◆Goal: learn the best policy with a neural network
(i.e., agent uses NN to select actions maximizing the future reward)
◆Two steps solution:
1.Train a Neural Networkto estimate future reward
▪Inputs:
## •푐푢푟푟푒푛푡푠푡푎푡푒=풔
## •푎푐푡푖표푛퐼푤표푢푙푑푡푎푘푒=풂
▪Output: 푒푠푡푖푚푎푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑푓표푟푒푎푐ℎ푠,푎=푸풔,풂
Q-learning approach
## 푸(풔,풂)
## (풔,풂)
NeuralNetwork

◆Goal: learn the best policy with a neural network
(i.e., agent uses NN to select actions to maximize the future reward)
◆Two steps solution:
1.Train a Neural Networkto estimate future reward
▪Inputs:
## •푐푢푟푟푒푛푡푠푡푎푡푒=풔
## •푎푐푡푖표푛퐼푤표푢푙푑푡푎푘푒=풂
▪Output: 푒푠푡푖푚푎푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑푓표푟푒푎푐ℎ푠,푎=푸풔,풂
2.Select best action: for each time instant (i.e., for each state 풔)
1.Compute 푸풔,풂
## 풊
for each possible actions 풂
## 풊
(do multiple NN predictions)
2.Select the action corresponding to the maximum value of 푸
→select argmax
## 풂
## 풊
## 푸풔,풂
## 풊
## ,∀풔
Q-learning approach
## 푸(풔,풂)
## (풔,풂)
NeuralNetwork

◆Goal: learn the best policy with a neural network
(i.e., agent uses NN to select actions to maximize the future reward)
◆Two steps solution:
1.Train a Neural Networkto estimate future reward
▪Inputs:
## •푐푢푟푟푒푛푡푠푡푎푡푒=풔
## •푎푐푡푖표푛퐼푤표푢푙푑푡푎푘푒=풂
▪Output: 푒푠푡푖푚푎푡푒푑푓푢푡푢푟푒푟푒푤푎푟푑푓표푟푒푎푐ℎ푠,푎=푸풔,풂
2.Select best action: for each time instant (i.e., for each state 풔)
1.Compute 푸풔,풂
## 풊
for each possible actions 풂
## 풊
(do multiple NN predictions)
2.Select the action corresponding to the maximum value of 푸
→select argmax
## 풂
## 풊
## 푸풔,풂
## 풊
## ,∀풔
Q-learning approach
## 푸(풔,풂)
## (풔,풂)
NeuralNetwork

Are wethereyet?
◆We can easilyrepresentthe policy 흅usinga neuralnetwork
◆How do wetrainthisnetwork?
▪Thislooks like a classificationproblem(ifthe actions are discrete) or a
regressionproblem(ifthe actions are continuous), right?

Are wethereyet?
◆We can easilyrepresentthe policy 흅usinga neuralnetwork
◆How do wetrainthisnetwork?
▪Thislooks like a classificationproblem(ifthe actions are discrete) or a
regressionproblem(ifthe actions are continuous), right? Wrong!
a)Wedon'thavea training set!
(and in general itmakes no senseto build one)
b)Wedon'tknow the desiredoutput for a givenstate!

a) No training set
◆Wedon'thavea training set. Our"experience" isgivenby the
possibilityof interactingwith the environment(the real
environmentor, more likely, a simulationof the environment)
Can wejust record some (or possibly, many) interactions with the
environmentto collecta training set?

a) No training set
◆Wedon'thavea training set. Our"experience" isgivenby the
possibilityof interactingwith the environment(the real
environmentor, more likely, a simulationof the environment)
Can wejust record some (or possibly, many) interactions with the
environmentto collecta training set?
Short Answer: No, wecan't

a) No training set
◆In a supervisedlearning problem(classificationor regression),
weassume independentsamples and decisions.
▪Independeddecisions: the nextinput thatthe system willreceiveisnot
influencedby the previousdecisionsmade by the system.
•Thus, ifwecollecta (sufficientlylarge) random sample of input values, thiscan
be usedby oursystem to getan idea of the inputs itwillreceivein the future.
◆Instead, in a reinforcementlearning problem, weknowthatthe
input samples givento ouragent are notindependent.
▪Dependentdecisions: the nextinput (state+reward) thatthe agent will
receiveisstronglyinfluencedby previousdecisionstaken.
•Previousaction takenyields the system in the currentstate thatdeterminesthe
nextaction to take.

a) No training set
◆Thus, we cannot collect a random sample of independent input
values, for example:
▪We can collect samples for a given behaviour of the system (policy 휋), i.e.,
keeping the neural network weights frozen
▪As soon as we update the neural network weights, the behaviour changes,
even if slightly (policy 휋’)
→The system will visit a different set of states (with different probabilities)!
→The previously collected samples are not useful anymore
Note: a proper training set is only possible in very simple problems, e.g., when the space of the
possible states is "simple" enough, so that we can explore it entirely with a suitably chosen
policy. These cases are of very limited interest.

b) No desiredvalue
◆Also, ourgoal isto estimate the future reward, i.e., the sum of all
future rewardsgivenby the environment:
## 푟
## 푡+1
## +푟
## 푡+2
## +⋯+푟
## 푁
▪Theyare unknown:
•Future rewardsdependon future states
•Future statesdependon future actions
•The action attime 푡mighthaveconsequencesthatwillbe evidentmuchlater...
◆Even ifwealwaysselectthe best action (i.e., the one that
maximizesthe future reward), wedo notknow, in general, whatis
the "desiredvalue" of the estimationprovidedby the NN

Select the best action once the NN istrained
s
t
## (풔
## 풕
## ,풂
## ퟎ
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
## 푸풔
## 풕
## ,풂
## ퟎ
## =ퟑ.ퟓ

Select the best action once the NN istrained
s
t
## 푸풔
## 풕
## ,풂
## ퟎ
## =ퟑ.ퟓ
## ...
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions

Select the best action once the NN istrained
s
t
## 푸풔
## 풕
## ,풂
## ퟎ
## =ퟑ.ퟓ
## ...
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ
## ...
## 푸풔
## 풕
## ,풂
## 푵
## =−ퟏ.ퟏ
## (풔
## 풕
## ,풂
## 푵
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions

Select the best action once the NN istrained
s
t
## 푸풔
## 풕
## ,풂
## ퟎ
## =ퟑ.ퟓ
## ...
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ
## ...
## 푸풔
## 풕
## ,풂
## 푵
## =−ퟏ.ퟏ
## (풔
## 풕
## ,풂
## 푵
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
Max. estimatedreward
→Select 풂
## 풊
## 푎
## 푖

ImprovingNN estimationusingthe new experience
s
t
## 푸풔
## 풕
## ,풂
## ퟎ
## =ퟑ.ퟓ
## ...
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ
## ...
## 푸풔
## 풕
## ,풂
## 푵
## =−ퟏ.ퟏ
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
Max. estimatedreward
→Select 풂
## 풊
## 푎
## 푖
s
t+1
r
t+1
At instant t+1wehavenew pieceof
informationfrom the environment:
## •풓
## 풕+ퟏ
## =ퟎ.ퟑ
## •풔
## 풕+ퟏ
## =풕풉풆풏풆풘풔풕풂풕풆

ImprovingNN estimationusingthe new experience
s
t
## 푸풔
## 풕
## ,풂
## ퟎ
## =ퟑ.ퟓ
## ...
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ
## ...
## 푸풔
## 풕
## ,풂
## 푵
## =−ퟏ.ퟏ
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
Max. estimatedreward
→Select 풂
## 풊
## 푎
## 푖
s
t+1
r
t+1
Wewantto use thisnew pieceof information
to verify/improvethe rewardestimationdoneat
the previousinstant t
At instant t+1wehavenew pieceof
informationfrom the environment:
## •풓
## 풕+ퟏ
## =ퟎ.ퟑ
## •풔
## 풕+ퟏ
## =풕풉풆풏풆풘풔풕풂풕풆

NN estimationattime instant t
s
t
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ=풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
## 푎
## 푖
s
t+1
r
t+1
s
t+2
r
t+2
s
n
r
n
Whenwewereattime instant t:
This isthe future rewardfrom 풔
## 풕
on ifweselectthe best action.
Itisunknown, thusweestimateditusingthe NN:
## →for 푎
## 푖
itisestimatedas7.1

NN estimationattime instant t+1
s
t
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ=풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
## 푎
## 푖
s
t+1
r
t+1
s
t+2
r
t+2
s
n
r
n
Whenwewereattime instant t:
## 푸풔
## 풕
## ,풂
## 풊
## ==ퟎ.ퟑ+풓
## 풕+ퟐ
## +⋯+풓
## 풏
Nowthatweare attime instant t+1
(after receivingthe new pieceof information)
## Thisisstillunknown
## Thisis
known

NN estimationattime instant t+1
s
t
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ=풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
## 푎
## 푖
s
t+1
r
t+1
s
t+2
r
t+2
s
n
r
n
Whenwewereattime instant t:
## 푸풔
## 풕
## ,풂
## 풊
## ==ퟎ.ퟑ+풓
## 풕+ퟐ
## +⋯+풓
## 풏
Nowthatweare attime instant t+1
(after receivingthe new pieceof information)
## Thisis
known
## Thisisstillunknown
→let’sestimate it
usingthe sameNN!
This isthe future reward
from 풔
## 풕+ퟏ
on ifweselect
the best action

NN estimationattime instant t+1
s
t
## 푸풔
## 풕
## ,풂
## 풊
## =ퟕ.ퟏ=풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## (풔
## 풕
## ,풂
## 풊
## )
NeuralNetwork
## {푎
## 0
## ,...,푎
## 푁
## }
## Possibleactions
## 푎
## 푖
r
t+1
s
t+2
r
t+2
s
n
r
n
Whenwewereattime instant t:
## 푸풔
## 풕
## ,풂
## 풊
## =ퟒ.ퟒ=ퟎ.ퟑ+ퟒ.ퟏ
Nowthatweare attime instant t+1
(after receivingthe new pieceof information)
## Thisis
known
## (풔
## 풕+ퟏ
## ,풂
## ′
## )
NeuralNetwork
## ...
## 푸풔
## 풕+ퟏ
## ,풂
## 풋
## =ퟒ.ퟏ
## ...
## Thisisstillunknown
→let’sestimate it
usingthe sameNN!
(selectingthe max)
s
t+1
Wetest allactions for
the new state 풔
## 풕+ퟏ
## ...

## Whichestimationisbetter?
s
t
## 푎
## 푖
r
t+1
s
t+2
r
t+2
s
n
r
n
s
t+1
At time instant t, weneedto estimate all
rewardsfrom t+1 to the end of the episode
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟕ.ퟏ
thistask isharderfor the NN

## Whichestimationisbetter?
s
t
## 푎
## 푖
r
t+1
s
t+2
r
t+2
s
n
r
n
s
t+1
At time instant t, weneedto estimate all
rewardsfrom t+1 to the end of the episode
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟕ.ퟏ
thistask isharderfor the NN
At time instant t+1, weknow 풓
## 풕+ퟏ
and we
haveto estimate 1 rewardless
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟒ.ퟒ
thistask iseasierfor the NN!

## Whichestimationisbetter?
s
t
## 푎
## 푖
r
t+1
s
t+2
r
t+2
s
n
r
n
s
t+1
At time instant t, weneedto estimate all
rewardsfrom t+1 to the end of the episode
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟕ.ퟏ
thistask isharderfor the NN
At time instant t+1, weknow 풓
## 풕+ퟏ
and we
haveto estimate 1 rewardless
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟒ.ퟒ
thistask iseasierfor the NN!
## Thisisworse!
Itiswat weuse to select
the action att
## Thisisbetter.
Servesastarget valueto
improvethe previousone

## Whichestimationisbetter?
s
t
## 푎
## 푖
r
t+1
s
t+2
r
t+2
s
n
r
n
s
t+1
At time instant t, weneedto estimate all
rewardsfrom t+1 to the end of the episode
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟕ.ퟏ
thistask isharderfor the NN
At time instant t+1, weknow 풓
## 풕+ퟏ
and we
haveto estimate 1 rewardless
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟒ.ퟒ
thistask iseasierfor the NN!
MSE loss
## ퟕ.ퟏ−ퟒ.ퟒ
## ퟐ
NN output (attime t)
NN target (attime t) =
## = 풓
## 풕+ퟏ
+NN output (attime t+1)

## Whichestimationisbetter?
s
t
## 푎
## 푖
r
t+1
s
t+2
r
t+2
s
n
r
n
s
t+1
At time instant t, weneedto estimate all
rewardsfrom t+1 to the end of the episode
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟕ.ퟏ
thistask isharderfor the NN
At time instant t+1, weknow 풓
## 풕+ퟏ
and we
haveto estimate 1 rewardless
## 풓
## 풕+ퟏ
## +풓
## 풕+ퟐ
## +⋯+풓
## 풏
## =ퟒ.ퟒ
thistask iseasierfor the NN!
MSE loss
## ퟕ.ퟏ−ퟒ.ퟒ
## ퟐ
NN output (attime t)
NN target (attime t) =
## = 풓
## 풕+ퟏ
+NN output (attime t+1)
Repeatateachtime instant!
After eachNN weight update:
•slightlyimprovesthe future rewardestimation
•slightlyimprovesthe selectedactions (policy)

Do nottrust far estimationtoomuch:
the discountedfuture reward
◆On stochastic systems, the accuracy in predicting future rewards
reduces when they are too far away
◆The agent can select actions and follow a path that seems good but it is not
◆Thus, wemaywantto increasethe impact of an earlyreward
◆We use an hyperparametercalled discountto weight the estimated future
reward with respect to the immediate (known) reward

Do nottrust far estimationtoomuch:
the discountedfuture reward
◆Thus, wemodifythe target valueby discountingfuture reward:
## ෍
## 푖=푡+1
## 푛
## 훾
## 푖−푡−1
## ∙푟
## 푖
where훾isthe discount factorhyperparameterin the range ]0, 1[
◆If훾isclose to 0, yougivemuchmore importanceto immediate rewards
thanto thosethatare far in the future
◆If훾isclose to 1, yougiveimmediate rewardsthe sameimportanceas
thosethatare far in the future
Note: the discountedfuture rewardisfinite and welldefinedevenifthe length
of the episodesisinfinite...

Do nottrust far estimationtoomuch:
the discountedfuture reward
◆Note thatyoucan reformulatediscountedfuture rewardin a
recursive way. In fact:
## 푡푎푟푔푒푡푣푎푙푢푒=෍
## 푖=푡+1
## 푛
## 훾
## 푖−푡−1
## ∙푟
## 푖
## =
## =푟
## 푡+1
## +훾∙෍
## 푖=푡+2
## 푛
## 훾
## 푖−푡−2
## ∙푟
## 푖
Thisiswhatwereceivefrom the
environmentafter selectingthe action
Thisiswhatweestimate using
the NN, whichwediscount by 훾

◆Werewritethe output valueand the target valueattime t:
## 푄푠
## 푡
## ,푎
## 푡
## ≈푟
## 푡+1
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+1
## ,푎′
Observed samples for 푟
## 푡+1
and 푠
## 푡+1
when
the agent choosesaction푎
## 푡
from state 푠
## 푡
The Bellman equationfor Q*
s
t
a
t
## =휋(s
t
## )
## S
t+1
r
t+1
a
t+1
## =휋(s
t+1
## )
The agent operation
selectingthe best action

◆We rewritethe output valueand the target valueattime t+1:
## 푄푠
## 푡
## ,푎
## 푡
## ≈푟
## 푡+1
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+1
## ,푎′
## 푄푠
## 푡+1
## ,푎
## 푡+1
## ≈푟
## 푡+2
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+2
## ,푎′
... thenrepeatfor 푟
## 푡+2
and 푠
## 푡+2
, and so on...
Training iterations!
Note: ateachiterationweuse an extreme
approximationof the SGD usinga single sample!
The Bellman equationfor Q*
s
t
a
t
## =휋(s
t
## )
## S
t+1
r
t+1
s
t+2
r
t+2
a
t+1
## =휋(s
t+1
## )
a
t+2
## =휋(s
t+2
## )

◆We rewritethe output valueand the target valueattime t+1:
## 푄푠
## 푡
## ,푎
## 푡
## ≈푟
## 푡+1
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+1
## ,푎′
## 푄푠
## 푡+1
## ,푎
## 푡+1
## ≈푟
## 푡+2
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+2
## ,푎′
... thenrepeatfor 푟
## 푡+2
and 푠
## 푡+2
, and so on...
The Bellman equationfor Q*
s
t
a
t
## =휋(s
t
## )
## S
t+1
r
t+1
s
t+2
r
t+2
a
t+1
## =휋(s
t+1
## )
a
t+2
## =휋(s
t+2
## )
NN estimations!
Note: Initial NN
estimationcan be
veryrough, e.g.,
random output of a
random initialized
neuralnetwork... it
getbetterwith
experience!
Training iterations!
Note: ateachiterationweuse an extreme
approximationof the SGD usinga single sample!

◆In otherwords, wecan trainthe functionapproximatorthat
computesQusingasourlossfunctionanymeasureof the
"difference" between
## 푄푠
## 푡
## ,푎
## 푡
and 푟
## 푡+1
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+1
## ,푎′
◆For instance, usingmeansquareerror, wecan trainourfunction
approximatorby minimizing:
## 퐿표푠푠=푟
## 푡+1
## +γ∙max
## 푎
## ′
## 푄푠
## 푡+1
## ,푎
## ′
## −푄푠
## 푡
## ,푎
## 푡
## 2
Green: experiencefrom the environment
Red: neuralnetwork’soutput
Blue: Target value
The Bellman equationfor Q*

◆The approximationshownaboveiscorrectonlyif푠
## 푡+1
isnota
terminal state
## 푄
## ∗
## 푠
## 푡
## ,푎
## 푡
## ≈푟
## 푡+1
## +γ∙max
## 푎
## ′
## 푄
## ∗
## 푠
## 푡+1
## ,푎′
◆Ifweknow that푠
## 푡+1
isa terminal state, a betterapproximationis:
## 푄
## ∗
## 푠
## 푡
## ,푎
## 푡
## ≈푟
## 푡+1
Thistermisusedto take intoaccount
whatwillhappenafter푠
## 푡+1
Terminal states

The Q-Learning algorithm
◆Run severalepisodes:
◆Record the transitions푠
## 푡
## ,푎
## 푡
## →푠
## 푡+1
## ,푟
## 푡+1
## .
◆Update the neuralnetwork thatisourestimator of Q
usingthe valuesfrom Bellman equationasdesiredoutputs (target).
◆Any regressionalgorithmcan be usedto model Q, aslong asit
allowson-line learning (in particular, wewilluse a neural
network)

The Q-Learning algorithm
Choose an initial푄(., .)  [e.g. a random initializednetwork]
FOR epIN 1,...,num_episodes
푡←0; choose (possibly randomly) 푠
## 0
WHILE NOT (found terminal state OR reached max episode length)
if rand() < 휺:푎
## 푟푎푛푑표푚
## ;푒푙푠푒:푎
## 푡
## ←argmax
## 푎
## 푄(푠
## 푡
## ,푎)
Send action 푎
## 푡
to the environment
## Get (푠
## 푡+1
## ,푟
## 푡+1
)from the environment
## IF 푠
## 푡+1
is a terminal state:
## 푡푎푟푔푒푡←푟
## 푡+1
## ELSE:
## 푡푎푟푔푒푡←푟
## 푡+1
## +훾∙max
## 푎
## ′
## 푄(푠
## 푡+1
## ,푎
## ′
## )
## END IF
Update the 푄network using(푠
## 푡
## ,푎
## 푡
)as input
and 푡푎푟푔푒푡as desired output
## 푡←푡+1
## END WHILE
## END FOR

The Q-Learning algorithm
Choose an initial푄(., .)  [e.g. a random initializednetwork]
FOR epIN 1,...,num_episodes
푡←0; choose (possibly randomly) 푠
## 0
WHILE NOT (found terminal state OR reached max episode length)
if rand() < 휺:푎
## 푟푎푛푑표푚
## ;푒푙푠푒:푎
## 푡
## ←argmax
## 푎
## 푄(푠
## 푡
## ,푎)
Send action 푎
## 푡
to the environment
## Get (푠
## 푡+1
## ,푟
## 푡+1
)from the environment
## IF 푠
## 푡+1
is a terminal state:
## 푡푎푟푔푒푡←푟
## 푡+1
## ELSE:
## 푡푎푟푔푒푡←푟
## 푡+1
## +훾∙max
## 푎
## ′
## 푄(푠
## 푡+1
## ,푎
## ′
## )
## END IF
Update the 푄network using(푠
## 푡
## ,푎
## 푡
)as input
and 푡푎푟푔푒푡as desired output
## 푡←푡+1
## END WHILE
## END FOR
## 훆-greedy
alternating
Exploitation and
## Exploration
## Experience
## Target
computation
## Learning

Q-Learning –discrete actions
◆Ifthe action set isdiscrete (aisone of a
## 1
## ,...,a
k
), it may be
convenient to define kindependent functions: Q
## 1
## (s
t
## ), Q
## 2
## (s
t
## ),...,
## Q
k
## (s
t
## )
▪Then the functions are evaluated in parallel, and the one with the highest
value is chosen (with the corresponding action)
## 푠
## 푄(푠,푎)
## 푎
## 푠
## 푄(푠,푎
## 1
## )
## 푄(푠,푎
## 2
## )
## 푄(푠,푎푘)
Insteadof organizing
yournetwork like
this...
... youcan organize
itlike this.

Q-Learning –continuousactions
◆If the spaceof actions iscontinuous, the operationof choosing
the nextaction isnottrivial, especiallyifthe spaceis
multi-dimensional:
## 푎
## 푡
## ←argmax
## 푎
## 푄(푠
## 푡
## ,푎)
Youhaveto solve a
maximizationproblem...

Q-Learning –continuousactions
◆An easy solutionisto havean additionalneuralnetwork for this
task. Thisiscalledan "actor-critic" model:
## 푠
## 푄
## 푎
## 푄(푠,푎)
## 푠
## 휋
## 휋(푠)
Criticnetwork: learns
to evaluatea state-
action pair
Actornetwork: learns
to choosethe best
action for a state

Q-Learning –continuousactions
◆The resultingalgorithm, calledDeep DeterministicPolicy
Gradient(DDPG), usesgradient-basedlearning to train
simultaneouslyboththe "critic" and the "actor" networks
◆Wehavealreadyseenhowto trainthe "critic" network Q
▪But howdo wecompute max
## 푎
## ′
## 푄(푠
## 푡+1
## ,푎
## ′
## )?
◆How do wetrainthe "actor" network 휋?

Q-Learning –continuousactions
◆We havealreadyseenhowto trainthe "critic" network Q
▪To compute the target, weapproximatemax
## 푎
## ′
## 푄(푠
## 푡+1
## ,푎
## ′
## )with:
## 푄(푠
## 푡+1
## ,휋푠
## 푡+1
## )
◆How do wetrainthe "actor" network 휋?
▪Wewantthe output of 휋to maximize푄(푠,푎)
▪Thuswecan use the Qnetwork to definea lossfunctionfor 휋
## 퐿표푠푠=−푄(푠,휋푠)

Q-Learning –continuousactions
◆In DDPG, the twonetworks are trainedtogether, interleaving
minibatchesfor training 푄and minibatchesfor training 휋
▪Whenweupdate the weights of 푄, the weights of 휋are notmodified;
▪Analogously, whenweupdate the weights of 휋, the weights of 푄are not
modified

Q-Learning –continuousactions
◆Training the "critic" network 푄
## 푠
## 푡
## 푄
## 푎
## 푡
## 푄(푠
## 푡
## ,푎
## 푡
## )
## 푠
## 푡+1
## 푄
## 휋(푠
## 푡+1
## )
## 푄(푠
## 푡+1
## ,휋(푠
## 푡+1
## ))
## 휋
## +
## *
## 훾
## 푟
## 푡+1
## 푡푎푟푔푒푡
## 퐿
## 퐿표푠푠푓표푟
## 푄(푠
## 푡
## ,푎
## 푡
## )
Theseweights are notupdated!

Q-Learning –continuousactions
◆Training the "actor" network 휋
## 푠
## 푄
## 푎
## 푄(푠,휋(푠))
## 푠
## 휋
## 휋(푠)
## −
## 퐿표푠푠for 휋(푠)
Weuse this...
... asthe lossfor training the actornetwork
Theseweights are
notupdated!

Q-Learning –replay buffer
◆In order to improvethe convergenceof the algorithm, itis
betterto avoidputtingconsecutive statesof an episodein
the sameminibatch
◆An easy solutionisto store the observedtransitions
## 푠
## 푡
## ,푎
## 푡
## →푠
## 푡+1
## ,푟
## 푡+1
in a data structurecalleda replay
buffer
◆Then, the minibatchesfor updatingthe neuralnetwork are builtby
choosingrandom samples from the replay buffer

Q-Learning –replay buffer
environment
driver  / policy
## Qneuralnetwork
target computation
replay
buffer
a
t
r
t+1
s
t+1
## (s
t
, a
t
, s
t+1
, r
t+1
## )
## . . .
## (s
i
, a
i
, s
i+1
, r
i+1
## )
## . . .
## (s
j
, a
j
, s
j+1
, r
j+1
## )
## . . .
recorded
transitions
sampled
transitions
## . . .
## (s
i
, a
i
, target
i
## )
## . . .
## (s
j
, a
j
, target
j
## )
## . . .
training minibatch
## Q(s,a)
## Q(s,a)

Q-Learning –Twin Q-Functions
◆In the basicQ-Learning algorithm, the currentestimate of the
optimalstate-action function푄(푠,푎)isusedfor twodifferent
reasonsduringthe training:
◆Computing the nextaction: 푎
## 푡
## ←argmax
## 푎
## 푄(푠
## 푡
## ,푎)
◆Computing the target value:
## 푡푎푟푔푒푡←푟
## 푡+1
## +훾∙max
## 푎
## ′
## 푄(푠
## 푡+1
## ,푎
## ′
## )

Q-Learning –Twin Q-Functions
◆Sincethe functionismodifiedduringthe training, the algorithm
changesateverytraining step bothitspolicy and the estimates
usedto improveitspolicy
◆Thissimultaneouschangeoftendeterminesan instabilityin the training
algorithm: beforethe Qneuralnetwork haslearnedhowto produce the
target value, the target valuemayhavealreadybeenchanged
significantlybecauseof the changesin the weights of Q

Q-Learning –Twin Q-Functions
◆To make the training more stable, a common technique isto
use twoneuralnetworks (havingthe samearchitecture) for the
function푄
▪One, 푄
## 푎푐푡
, isusedto compute the nextaction:
## 푎
## 푡
## ←argmax
## 푎
## 푄
## 푎푐푡
## (푠
## 푡
## ,푎)
▪The other, 푄
## 푡푎푟푔
, isusedto compute the target value:
## 푡푎푟푔푒푡←푟
## 푡+1
## +훾∙max
## 푎
## ′
## 푄
## 푡푎푟푔
## (푠
## 푡+1
## ,푎
## ′
## )
▪At eachtraining step, onlythe weights of 푄
## 푎푐푡
are updated
▪However, periodically(e.g. every푘steps, where푘isa hyperparameter),
the weights of 푄
## 푎푐푡
are copiedto the network 푄
## 푡푎푟푔
## .

Q-Learning –Twin Q-Functions
## 푄
## 푎푐푡
The valueof 푄used
to choose푎
## 푡
## 푠
## 푡
## 푎
## 푄
## 푡푎푟푔
The valueof 푄used
to compute target
## 푠
## 푡+1
## 푎
Thesetwonetworks have
exactlythe samestructure

Q-Learning –Twin Q-Functions
## 푄
## 푎푐푡
The valueof 푄used
to choose푎
## 푡
## 푠
## 푡
## 푎
## 푄
## 푡푎푟푔
The valueof 푄used
to compute target
## 푠
## 푡+1
## 푎
At eachtraining step, onlythe weights
of thisnetwork are updated(using
StochasticGradientDescent)

Q-Learning –Twin Q-Functions
## 푄
## 푎푐푡
The valueof 푄used
to choose푎
## 푡
## 푠
## 푡
## 푎
## 푄
## 푡푎푟푔
The valueof 푄used
to compute target
## 푠
## 푡+1
## 푎
Periodically, the weights of this
network...
## Weights
... are copiedto thisnetwork.

Q-Learning –Examples
◆DeepMind, DeepReinforcementLearning (2013):
▪The software learnsto play anyAtari2600 8-bit video games withoutany
knowledgeaboutthe game!
▪The (lowres) image of the screen isusedasinput, and the game score
asreward
▪https://www.youtube.com/watch?v=V1eYniJ0Rnk

Q-Learning –Examples
◆BRETT: Berkeley Robot for the Eliminationof TediousTasks
## (2010-2017)
▪The robot learnshowto performmotiontaskslikeassemblingLego bricks
▪https://www.youtube.com/watch?v=JeVppkoloXs

Q-Learning –Examples
◆Learning to walkvia Deep ReinforcementLearning (Google,
## 2019)
▪A four-leggedrobot learnsto walk:
▪https://www.youtube.com/watch?v=n2gE7n11h1Y