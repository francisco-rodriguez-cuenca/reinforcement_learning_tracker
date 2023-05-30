# Independent and Decentralized Learning in Markov Potential Games

Chinmay Mheshwari - UC, Berkeley
Manxi Wu -  Cornell University & UC, Berkeley
Druv Pai - UC, Berkeley
Shankar Sastry - UC, Berkeley

    Maheshwari, C., Wu, M., Pai, D., & Sastry, S. (2022). Independent and Decentralized Learning in Markov Potential Games. arXiv preprint arXiv:2205.14590.

## Abstract

* __Multi-agent Reinforcement Learning Dynamics__ -> Analyze its convergence properties in __infinite-horizon discounted Markov Potential Games__
* Focus on the __independent__ and __decentralized__ setting -> Players can only observe the realized state and their own reward on every stage
* Players do not have knowledge of the game model and cannot coordinarte with each other

Learning Dynamics:

1. Players update their estimate of a prturbed Q-function that evaluates their total contingent payoff based on the realized one-stage reward in an asynchronous manner
2. Players independently update their policies by incorporatinh a smoothed optimal one-stage deviation strategy based on the estimated Q-function

* Q-function estimates are updated at a faster rate than policies
* Policies induced by these learning dynamics converge to a stationary Nash equilibrium in Markov Potential Games with propbability 1

Summary : Agents can reach a stationary Nash equilibrium in Markov potential games through simple learning dynamics under the minimum information environment.

## Sections

1. Introduction
2. Related Works
3. Game Model
4. Independent and Decentralized Learning Dynamics
5. Numerical Experiments
6. Conclusions

## Introduction

MARL - Multi-Agent Reinforcement Learning

* Studies the interactions among multiple players in a dynamic environment, where the utilities and state transition are jointly determined by the players actions
* Autonomous driving, adaptative traffic control, e-commerce, real-time strategy games

Markov Potential Game

* A game is said to be a potential game if the incentive of all players to change their strategy can be expressed thorugh a single gobal function called the potential function
* Mixed competitive and cooperative scenario
* Markov games which satisfy the conditions for MPG's:
  * Identical interest games - cooperation
  * Stochastic Congestion Games - competition through congestion
* The change of utility of any player from unilaterally deviating their policy can be evaluated by the change on the potential function
* A stationary Nash equilibrium can be solved as the global optimum of the potential function

Gradient-based algorithms

* Used to compute the stationary Nash Equilibrium
  * Gradient calculation require agents to compute the value function or its derivatives for the policy update which necesitates access to simulator/oracle or coordination/communication between players

How can naive players learn a stationary Nash Equilibrium through simple updates without coordination and without knowledge of the game?

* This papers answers by proposing and independent and decentralized multi-agent reinforcement learning dynamics
* Prove's its convergence to stationary Nash equilibrium in infinite-horizon discounted Markov Potential Games.

Minimal Information Environment

* Each player only observes the realized state and their own realized reward
* Players do not know the existence of other players, nor their own or foes' utility functions or the state transition probability function

Learning Dynamics

* Players individually deploying a decentralized tow-scale q-learning dynamics

1. Players mantain a q-estimate for each value-action pair
2. Players update their policies based on the updated q-estimate

* Players are self-interested
* Learning is asynchronous and heterogeneous among players
  * Only the q-estimate of the realized state-action pair is updated
  * Only the policy regarding the realized state is updated
  * Each player counts the number of times a state and action is realized and adjusts the stepsize for updating hat state and action element according to the counter
* The dynamics have two timescales: the q-estimate is updated at a faster rate than the policy update

Proof

* These learning dinamics lead to an approximate Nash equilibrium with probability 1, which becomes a Nash equilibrium when the payoff perturbation goes to zero

## Conclusion

* Nash equilibrium can be achieved in Markov potential games under the minimum information environment without coordination among players
