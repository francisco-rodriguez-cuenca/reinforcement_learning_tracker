# [The self-organization of selfishness: Reinforcement Learning shows how selfish behavior can emerge from agent-environment interaction dynamics](https://arxiv.org/pdf/2302.14778)

## Abstract

* It is known that in biological communities, "free-riders" emerge.
* Free riders are agents that do not contribute to community resources, but do exploit them.
* Most models consider "free-riding" astable trait that evolves through mutation and selection.
* They present a reinforcement learning model that shows that free-riding behaviour and signaling-based coordination can emerge __within a generation__, and it is not a stable trait but dynamic "coagulation" of agent-environment interactions.
* How selfish behaviour can emerge through self-organization, and that the idea of selfishness as a stable trait presumes a model based on mutations.

## Sections

1. Introduction
2. Model Design
   1. Q-Learning
   2. The agents and their world
3. Results
   1. Emergence of Free-Riders and Droppers
   2. Order of Updation
      1. Sequential Updating
      2. Random Updating
   3. Death of Agents
   4. Birth of Agents
   5. Is Past Learning Sufficient for Future?
   6. Patterns of agents accross different environmental estimuli
      1. Number of agents
      2. Evaporation rate
      3. Dispersion rate
      4. Exploration rate
4. Simulation Results
5. Discussion

## 5. Discussion

* Two types of free-riding agents:
  * __Naive free-riders__:
    * They start by randomly trying out free-riding behaviour, but stay with this behaviour because it is energy minima. They are not able to resort to any other type of behaviour, and if depleted of resources, act randomnly.
    * Stable selfish trait, although not genetic
  * __Crafty free-riders__:
    * They discover free-riding behaviour __after__ the system converges. They know dropper behaviour and resort to it if there is a lack of resources, if it is feasible, they free-ride.
    * Really selfish but not attributable to any trait since they can behave otherwise.

* Aims to prove that selfish behaviour is better understood as a learned agent-environment interaction than a stable "genetic" trait.