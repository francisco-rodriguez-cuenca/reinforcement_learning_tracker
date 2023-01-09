# Backward Curriculum Reinforcement Learning

Kyung Min Ko
Sajad Khodadanian
Siva Theja Maguluri

Georgia Tech

    Ko, K., Khodadadian, S., & Maguluri, S. T. (2022). Backward Curriculum Reinforcement Learning. arXiv preprint arXiv:2212.1421

## Abstract

Current Reinforcement Learning:

* Forward-generated trajectories to train the agent
  * Give the agent little guidence, so the agent can explore as much as possible
  * Trade-off = Losing sample efficiency

Novel Approach

* Reverse Curriculum Reinforcement Learning
    * Starts training the agent using the backward trajectory of the episode rather than the forward trajectory
    * This gives the agent a strong reward signal, so the agent can learn in a more sample-efficient manner
    * Only requires a minor change in the algorithm -> Reversing the order of the trajectory before training the agent
    * Can be applied to any state-of-the-art algorithms

## Introduction

Current Reinforcement Learning

* Really sparse natural reward function since it is only given when the agent completes the task.
* A lot of times the agent is blind to the task so it discovers optimal policy without any guidence from the human:
  * Large amount of computational power and samples to learn

Reverse Curriculum Reinforcement Learning

* Uses trajectories in reverse order to train the agent
* This enables our agent to start training by recognizing the goal of the task
* Result: Agents are trained in an efficient way by utilizing strong reward signals during "reverse learning"
* Does not need modification of neural structure nor new information, can be applied to any algorithm : PPO, A3C, SAC

2 simple steps:

1. Collect the trajectory of the agent as usual
2. Flip the order of the trajectory of the episode to train our agent

Curriculum Learning

* Manually changes the order of the training process to train more efficiently

Tested

* Tested on REINFORCE (Sutton) and REINFORCE with baseline
* Cart-Pole V1 and Lunar-Lander_v2 - OpenAi Gym (Discrete Action Spaces)
* Investigated the effects of return normalization technique, variation of learning rate and structure of neural network

## Sections

1. Introduction
2. Related Works
3. Preliminaries
4. Reverse Curriculum Learning
   1. Reverse Curriculum Learning in REINFORCE
   2. Reverse Curriculum Learning in REINFORCE with baseline
5. Experimental Result
   1. Cartpole Environment
   2. Lunar Lander Environment
   3. Return Normalization 
   4. Comparison between Deep and Shallow Networks
6. Conclusion
7. Acknowledgement

## Conclusion

* Does need fewer samples
* Best fits while doing simple tasks like Cartpole with shallow networks
* Future work: apply  on state-of-the-art algorithms on different environments