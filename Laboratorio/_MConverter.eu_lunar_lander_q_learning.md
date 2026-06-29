---
jupyter:
  colab:
    gpuType: T4
    provenance:
    - file_id: "https://github.com/pytorch/tutorials/blob/gh-pages/\\_downloads/9da0471a9eeb2351a488cd4b44fc6bbf/reinforcement_q_learning.ipynb"
      timestamp: 1685542641157
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.10
  nbformat: 4
  nbformat_minor: 0
---

:::: {.cell .code execution_count="1" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":22717,\"status\":\"ok\",\"timestamp\":1779956515224,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="fIyqkT7Hl3D-" outputId="8d018c54-0702-4406-9c6d-558be37079a7"}
``` python
from google.colab import drive
drive.mount('/content/gdrive')
import os
os.chdir('/content/gdrive/MyDrive/Didattica/ML/Exercises/Exercise13_reinforcement_learning/')
!ls
```

::: {.output .stream .stdout}
    Mounted at /content/gdrive
     2D_explorer.ipynb		   kuka_rl_PPO_parallel.ipynb
     Acrobot-v1_model.pth		   OLD
     CartPole-v1_model.pth		   policy_dqn.pt
     DDPG				  'PyBullet Quickstart Guide.gdoc'
     kuka_rl_DQN_con_soluzioni.ipynb   pybullet_save_video.ipynb
     kuka_rl_DQN.ipynb		   runs
     kuka_rl_PPO.ipynb
:::
::::

::: {.cell .code execution_count="2" executionInfo="{\"elapsed\":1,\"status\":\"ok\",\"timestamp\":1779956515240,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="JJ2_WchBKlN3"}
``` python
# For tips on running notebooks in Google Colab, see
# https://pytorch.org/tutorials/beginner/colab
%matplotlib inline
```
:::

::: {.cell .markdown id="D_tfhnmKKlN8"}
# Reinforcement Learning (DQN) Tutorial

**Author**: [Adam Paszke](https://github.com/apaszke)
[Mark Towers](https://github.com/pseudo-rnd-thoughts)

This tutorial shows how to use PyTorch to train a Deep Q Learning (DQN) agent
on the CartPole-v1 task from [Gymnasium](https://www.gymnasium.farama.org)\_.

**Task**

For a full description of the task, please visit the [Gymnasium\'s website](https://gymnasium.farama.org/environments/box2d/).

**Packages**

First, let\'s import needed packages. Firstly, we need
[gymnasium](https://gymnasium.farama.org/)\_ for the environment,
installed by using `pip`. This is a fork of the original OpenAI
Gym project and maintained by the same team since Gym v0.19.
If you are running this in Google Colab, run:
:::

:::: {.cell .code execution_count="3" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6120,\"status\":\"ok\",\"timestamp\":1779956521361,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="J9yvzhSeKlN-" outputId="b6e7fbab-8dba-43a5-cf46-d97d8ad36691"}
``` python
%%bash
pip3 install gymnasium[classic_control]
```

::: {.output .stream .stdout}
    Requirement already satisfied: gymnasium[classic_control] in /usr/local/lib/python3.12/dist-packages (1.3.0)
    Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium[classic_control]) (2.0.2)
    Requirement already satisfied: cloudpickle>=1.2.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium[classic_control]) (3.1.2)
    Requirement already satisfied: typing-extensions>=4.3.0 in /usr/local/lib/python3.12/dist-packages (from gymnasium[classic_control]) (4.15.0)
    Requirement already satisfied: farama-notifications>=0.0.1 in /usr/local/lib/python3.12/dist-packages (from gymnasium[classic_control]) (0.0.6)
    Collecting pygame-ce>=2.1.3 (from gymnasium[classic_control])
      Downloading pygame_ce-2.5.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (11 kB)
    Downloading pygame_ce-2.5.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (12.8 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 93.8 MB/s eta 0:00:00
    Installing collected packages: pygame-ce
    Successfully installed pygame-ce-2.5.7
:::
::::

:::: {.cell .code execution_count="4" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6446,\"status\":\"ok\",\"timestamp\":1779956527809,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="PYYRYOm7IUOj" outputId="ffa43bf3-4ff5-47df-fe75-050b6d2bff60"}
``` python
%%bash
pip3 install ufal.pybox2d
#pip3 install gymnasium[box2d]
```

::: {.output .stream .stdout}
    Collecting ufal.pybox2d
      Downloading ufal_pybox2d-2.3.10.5-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (550 bytes)
    Downloading ufal_pybox2d-2.3.10.5-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (3.6 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 30.1 MB/s eta 0:00:00
    Installing collected packages: ufal.pybox2d
    Successfully installed ufal.pybox2d-2.3.10.5
:::
::::

::: {.cell .markdown id="iLYB47xXKlN_"}
We\'ll also use the following from PyTorch:

- neural networks (`torch.nn`)
- optimization (`torch.optim`)
- automatic differentiation (`torch.autograd`)
:::

::: {.cell .code execution_count="5" executionInfo="{\"elapsed\":8022,\"status\":\"ok\",\"timestamp\":1779956535832,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="Ks_CLvERKlN_"}
``` python
import gymnasium as gym
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple, deque
from itertools import count

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
```
:::

::: {.cell .code execution_count="6" executionInfo="{\"elapsed\":34,\"status\":\"ok\",\"timestamp\":1779956535868,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="uMtT73nqFiyA"}
``` python
# set up matplotlib
is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display

plt.ion()

# if GPU is to be used
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```
:::

::: {.cell .code execution_count="7" executionInfo="{\"elapsed\":14,\"status\":\"ok\",\"timestamp\":1779956535887,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="7082qtPfF1je"}
``` python
env_name = "LunarLander-v3"
```
:::

::: {.cell .code execution_count="8" executionInfo="{\"elapsed\":422,\"status\":\"ok\",\"timestamp\":1779956536310,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="xI5QafHBFnRO"}
``` python
env = gym.make(env_name, render_mode="rgb_array")
```
:::

::: {.cell .markdown id="aBcKRnN4KlOA"}
## Replay Memory

We\'ll be using experience replay memory for training our DQN. It stores
the transitions that the agent observes, allowing us to reuse this data
later. By sampling from it randomly, the transitions that build up a
batch are decorrelated. It has been shown that this greatly stabilizes
and improves the DQN training procedure.

For this, we\'re going to need two classes:

- `Transition` - a named tuple representing a single transition in
  our environment. It essentially maps (state, action) pairs
  to their (next_state, reward) result, with the state being the
  screen difference image as described later on.
- `ReplayMemory` - a cyclic buffer of bounded size that holds the
  transitions observed recently. It also implements a `.sample()`
  method for selecting a random batch of transitions for training.
:::

::: {.cell .code execution_count="9" executionInfo="{\"elapsed\":20,\"status\":\"ok\",\"timestamp\":1779956536340,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="DzvvWhOLKlOB"}
``` python
Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):

    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
```
:::

::: {.cell .markdown id="TqdHq81TKlOB"}
Now, let\'s define our model. But first, let\'s quickly recap what a DQN is.

## DQN algorithm

Our environment is deterministic, so all equations presented here are
also formulated deterministically for the sake of simplicity. In the
reinforcement learning literature, they would also contain expectations
over stochastic transitions in the environment.

Our aim will be to train a policy that tries to maximize the discounted,
cumulative reward
$R_{t_0} = \sum_{t=t_0}^{\infty} \gamma^{t - t_0} r_t$, where
$R_{t_0}$ is also known as the *return*. The discount,
$\gamma$, should be a constant between $0$ and $1$
that ensures the sum converges. A lower $\gamma$ makes
rewards from the uncertain far future less important for our agent
than the ones in the near future that it can be fairly confident
about. It also encourages agents to collect reward closer in time
than equivalent rewards that are temporally far away in the future.

The main idea behind Q-learning is that if we had a function
$Q^*: State \times Action \rightarrow \mathbb{R}$, that could tell
us what our return would be, if we were to take an action in a given
state, then we could easily construct a policy that maximizes our
rewards:

\begin{align}\pi\^*(s) = \arg!\max_a  Q\^*(s, a)\end{align}

However, we don\'t know everything about the world, so we don\'t have
access to $Q^*$. But, since neural networks are universal function
approximators, we can simply create one and train it to resemble
$Q^*$.

For our training update rule, we\'ll use a fact that every $Q$
function for some policy obeys the Bellman equation:

\begin{align}Q\^{\pi}(s, a) = r + \gamma Q\^{\pi}(s\', \pi(s\'))\end{align}

The difference between the two sides of the equality is known as the
temporal difference error, $\delta$:

\begin{align}\delta = Q(s, a) - (r + \gamma \max_a\' Q(s\', a))\end{align}

To minimize this error, we will use the [Huber
loss](https://en.wikipedia.org/wiki/Huber_loss)\_. The Huber loss acts
like the mean squared error when the error is small, but like the mean
absolute error when the error is large - this makes it more robust to
outliers when the estimates of $Q$ are very noisy. We calculate
this over a batch of transitions, $B$, sampled from the replay
memory:

\begin{align}\mathcal{L} = \frac{1}{\|B\|}\sum\_{(s, a, s\', r)  \in  B} \mathcal{L}(\delta)\end{align}

\begin{align}\text{where} \quad \mathcal{L}(\delta) = \begin{cases}
\frac{1}{2}{\delta\^2} & \text{for } \|\delta\| \le 1, \\
\|\delta\| - \frac{1}{2} & \text{otherwise.}
\end{cases}\end{align}

### Q-network

Our model will be a feed forward neural network that takes in the
difference between the current and previous screen patches. It has two
outputs, representing $Q(s, \mathrm{left})$ and
$Q(s, \mathrm{right})$ (where $s$ is the input to the
network). In effect, the network is trying to predict the *expected return* of
taking each action given the current input.
:::

::: {.cell .code execution_count="10" executionInfo="{\"elapsed\":23,\"status\":\"ok\",\"timestamp\":1779956536364,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="IEqLiTp5KlOC"}
``` python
class DQN(nn.Module):

    def __init__(self, n_observations, n_actions):
        super(DQN, self).__init__()
        self.layer1 = nn.Linear(n_observations, 128)
        self.layer2 = nn.Linear(128, 128)
        self.layer3 = nn.Linear(128, n_actions)

    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        return self.layer3(x)
```
:::

::: {.cell .markdown id="LbfBupduKlOD"}
## Training

### Hyperparameters and utilities

This cell instantiates our model and its optimizer, and defines some
utilities:

- `select_action` - will select an action accordingly to an epsilon
  greedy policy. Simply put, we\'ll sometimes use our model for choosing
  the action, and sometimes we\'ll just sample one uniformly. The
  probability of choosing a random action will start at `EPS_START`
  and will decay exponentially towards `EPS_END`. `EPS_DECAY`
  controls the rate of the decay.
- `plot_durations` - a helper for plotting the duration of episodes,
  along with an average over the last 100 episodes (the measure used in
  the official evaluations). The plot will be underneath the cell
  containing the main training loop, and will update after every
  episode.
:::

::: {.cell .code execution_count="11" executionInfo="{\"elapsed\":22099,\"status\":\"ok\",\"timestamp\":1779956558468,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="_J_v7N3rKlOD"}
``` python
# BATCH_SIZE is the number of transitions sampled from the replay buffer
# GAMMA is the discount factor as mentioned in the previous section
# EPS_START is the starting value of epsilon
# EPS_END is the final value of epsilon
# EPS_DECAY controls the rate of exponential decay of epsilon, higher means a slower decay
# TAU is the update rate of the target network
# LR is the learning rate of the ``AdamW`` optimizer
BATCH_SIZE = 128
GAMMA = 0.99
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 1000
TAU = 0.005
LR = 1e-4

# Get number of actions from gym action space
n_actions = env.action_space.n
# Get the number of state observations
state, info = env.reset()
n_observations = len(state)

policy_net = DQN(n_observations, n_actions).to(device)
target_net = DQN(n_observations, n_actions).to(device)
target_net.load_state_dict(policy_net.state_dict())

optimizer = optim.AdamW(policy_net.parameters(), lr=LR, amsgrad=True)
memory = ReplayMemory(10000)


steps_done = 0


def select_action(state):
    global steps_done
    sample = random.random()
    eps_threshold = EPS_END + (EPS_START - EPS_END) * \
        math.exp(-1. * steps_done / EPS_DECAY)
    steps_done += 1
    if sample > eps_threshold:
        with torch.no_grad():
            # t.max(1) will return the largest column value of each row.
            # second column on max result is index of where max element was
            # found, so we pick action with the larger expected reward.
            return policy_net(state).max(1)[1].view(1, 1)
    else:
        return torch.tensor([[env.action_space.sample()]], device=device, dtype=torch.long)


episode_durations = []

def render_env(img, title):
    plt.figure(1)
    plt.clf()
    plt.imshow(img)
    plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated
    if is_ipython:
      display.display(plt.gcf())
      display.clear_output(wait=True)


def plot_durations(show_result=False):
    plt.figure(2)
    durations_t = torch.tensor(episode_durations, dtype=torch.float)
    if show_result:
        plt.title('Result')
    else:
        plt.clf()
        plt.title('Training...')
    plt.xlabel('Episode')
    plt.ylabel('Duration')
    plt.plot(durations_t.numpy())
    # Take 100 episode averages and plot them too
    if len(durations_t) >= 100:
        means = durations_t.unfold(0, 100, 1).mean(1).view(-1)
        means = torch.cat((torch.zeros(99), means))
        plt.plot(means.numpy())

    plt.pause(0.001)  # pause a bit so that plots are updated
    if is_ipython:
        if not show_result:
            display.display(plt.gcf())
            display.clear_output(wait=True)
        else:
            display.display(plt.gcf())
```
:::

::: {.cell .markdown id="CX-0Opo4KlOE"}
### Training loop

Finally, the code for training our model.

Here, you can find an `optimize_model` function that performs a
single step of the optimization. It first samples a batch, concatenates
all the tensors into a single one, computes $Q(s_t, a_t)$ and
$V(s_{t+1}) = \max_a Q(s_{t+1}, a)$, and combines them into our
loss. By definition we set $V(s) = 0$ if $s$ is a terminal
state. We also use a target network to compute $V(s_{t+1})$ for
added stability. The target network is updated at every step with a
[soft update](https://arxiv.org/pdf/1509.02971.pdf)\_ controlled by
the hyperparameter `TAU`, which was previously defined.
:::

::: {.cell .code execution_count="12" executionInfo="{\"elapsed\":1,\"status\":\"ok\",\"timestamp\":1779956558470,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="ZopAnw1fKlOE"}
``` python
def optimize_model():
    if len(memory) < BATCH_SIZE:
        return
    transitions = memory.sample(BATCH_SIZE)
    # Transpose the batch (see https://stackoverflow.com/a/19343/3343043 for
    # detailed explanation). This converts batch-array of Transitions
    # to Transition of batch-arrays.
    batch = Transition(*zip(*transitions))

    # Compute a mask of non-final states and concatenate the batch elements
    # (a final state would've been the one after which simulation ended)
    non_final_mask = torch.tensor(tuple(map(lambda s: s is not None,
                                          batch.next_state)), device=device, dtype=torch.bool)
    non_final_next_states = torch.cat([s for s in batch.next_state
                                                if s is not None])
    state_batch = torch.cat(batch.state)
    action_batch = torch.cat(batch.action)
    reward_batch = torch.cat(batch.reward)

    # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
    # columns of actions taken. These are the actions which would've been taken
    # for each batch state according to policy_net
    state_action_values = policy_net(state_batch).gather(1, action_batch)

    # Compute V(s_{t+1}) for all next states.
    # Expected values of actions for non_final_next_states are computed based
    # on the "older" target_net; selecting their best reward with max(1)[0].
    # This is merged based on the mask, such that we'll have either the expected
    # state value or 0 in case the state was final.
    next_state_values = torch.zeros(BATCH_SIZE, device=device)
    with torch.no_grad():
        next_state_values[non_final_mask] = target_net(non_final_next_states).max(1)[0]
    # Compute the expected Q values
    expected_state_action_values = (next_state_values * GAMMA) + reward_batch

    # Compute Huber loss
    criterion = nn.SmoothL1Loss()
    loss = criterion(state_action_values, expected_state_action_values.unsqueeze(1))

    # Optimize the model
    optimizer.zero_grad()
    loss.backward()
    # In-place gradient clipping
    torch.nn.utils.clip_grad_value_(policy_net.parameters(), 100)
    optimizer.step()
```
:::

::: {.cell .markdown id="P7A71D_4KlOF"}
Below, you can find the main training loop. At the beginning we reset
the environment and obtain the initial `state` Tensor. Then, we sample
an action, execute it, observe the next state and the reward (always
1), and optimize our model once. When the episode ends (our model
fails), we restart the loop.

Below, `num_episodes` is set to 600 if a GPU is available, otherwise 50
episodes are scheduled so training does not take too long. However, 50
episodes is insufficient for to observe good performance on CartPole.
You should see the model constantly achieve 500 steps within 600 training
episodes. Training RL agents can be a noisy process, so restarting training
can produce better results if convergence is not observed.
:::

:::::::: {.cell .code execution_count="13" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":541}" executionInfo="{\"elapsed\":798603,\"status\":\"ok\",\"timestamp\":1779957357073,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="j2EQnM3RKlOF" outputId="6c77b7d6-213f-4ba9-d495-ea64f42aca36"}
``` python
import matplotlib.pyplot as plt
do_rendering = False  # slow down the execution

if torch.cuda.is_available():
    num_episodes = 600
else:
    num_episodes = 200

for i_episode in range(num_episodes):
    # Initialize the environment and get it's state
    state, info = env.reset()
    state = torch.tensor(state, dtype=torch.float32, device=device).unsqueeze(0)
    for t in count():
        action = select_action(state)
        observation, reward, terminated, truncated, _ = env.step(action.item())
        reward = torch.tensor([reward], device=device)
        done = terminated or truncated

        if terminated:
            next_state = None
        else:
            next_state = torch.tensor(observation, dtype=torch.float32, device=device).unsqueeze(0)

        # Store the transition in memory
        memory.push(state, action, next_state, reward)

        # Move to the next state
        state = next_state

        # Perform one step of the optimization (on the policy network)
        optimize_model()

        # Soft update of the target network's weights
        # θ′ ← τ θ + (1 −τ )θ′
        target_net_state_dict = target_net.state_dict()
        policy_net_state_dict = policy_net.state_dict()
        for key in policy_net_state_dict:
            target_net_state_dict[key] = policy_net_state_dict[key]*TAU + target_net_state_dict[key]*(1-TAU)
        target_net.load_state_dict(target_net_state_dict)

        if do_rendering:
          screen = env.render()
          render_env(screen, t)

        if done:
            episode_durations.append(t + 1)
            plot_durations()
            break

print('Complete')
plot_durations(show_result=True)
plt.ioff()
plt.show()
```

::: {.output .stream .stdout}
    Complete
:::

::: {.output .display_data}
    <Figure size 640x480 with 0 Axes>
:::

::: {.output .display_data}
![](57cad15c9fdc778a3352ba3c9b22c0be7c25ebf5.png)
:::

::: {.output .display_data}
    <Figure size 640x480 with 0 Axes>
:::

::: {.output .display_data}
    <Figure size 640x480 with 0 Axes>
:::
::::::::

::: {.cell .markdown id="SBNzU7qxKlOG"}
Here is the diagram that illustrates the overall resulting data flow.

.. figure:: /\_static/img/reinforcement_learning_diagram.jpg

Actions are chosen either randomly or based on a policy, getting the next
step sample from the gym environment. We record the results in the
replay memory and also run optimization step on every iteration.
Optimization picks a random batch from the replay memory to do training of the
new policy. The \"older\" target_net is also used in optimization to compute the
expected Q values. A soft update of its weights are performed at every step.
:::

::: {.cell .code execution_count="14" executionInfo="{\"elapsed\":11,\"status\":\"ok\",\"timestamp\":1779957357098,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="hlzV3gUpHHM1"}
``` python
torch.save(policy_net, '%s_model.pth' % env_name)
```
:::

::: {.cell .code execution_count="16" executionInfo="{\"elapsed\":41,\"status\":\"ok\",\"timestamp\":1779958774754,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="mEZwfZIknkmc"}
``` python
policy_net = torch.load('%s_model.pth' % env_name, weights_only=False)
```
:::

:::: {.cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":1899,\"status\":\"ok\",\"timestamp\":1779958782991,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="rGoXV47YqYce" outputId="3b2d5f29-3c0f-4869-fd54-0d53898d1b42"}
``` python
policy_net.eval()
frames = []

# Initialize the environment and get it's state
state, info = env.reset()
state = torch.tensor(state, dtype=torch.float32, device=device).unsqueeze(0)
while True:
    action = select_action(state)
    observation, reward, terminated, truncated, _ = env.step(action.item())
    reward = torch.tensor([reward], device=device)
    done = terminated or truncated

    if terminated:
        next_state = None
    else:
        next_state = torch.tensor(observation, dtype=torch.float32, device=device).unsqueeze(0)

    # Move to the next state
    state = next_state

    screen = env.render()
    frames.append(screen)

    if done:
        print("Episode finished after {} timesteps".format(len(frames)))
        break
env.close()
```

::: {.output .stream .stdout}
    Episode finished after 323 timesteps
:::
::::

:::: {.cell .code execution_count="18" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":221}" executionInfo="{\"elapsed\":6888,\"status\":\"ok\",\"timestamp\":1779958789948,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-120}" id="3UQOUrswmVJm" outputId="103020ba-87d6-4148-b293-ebed8bb69821"}
``` python
import matplotlib.pyplot as plt
import matplotlib.animation
from IPython.display import HTML
plt.figure(figsize=(frames[0].shape[1]/100.0, frames[0].shape[0]/100.0), dpi = 50)
patch = plt.imshow(frames[0])
plt.axis('off')
animate = lambda i: patch.set_data(frames[i])
ani = matplotlib.animation.FuncAnimation(plt.gcf(), animate, frames=len(frames), interval = 50)
HTML(ani.to_html5_video())
```

::: {.output .execute_result execution_count="18"}
    <IPython.core.display.HTML object>
:::
::::
