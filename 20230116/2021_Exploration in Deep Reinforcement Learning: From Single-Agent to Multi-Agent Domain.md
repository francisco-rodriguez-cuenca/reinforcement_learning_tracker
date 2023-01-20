# Exploration in Deep Reinforcement Learning: From Single-Agent to Multi-Agent Domain

2021 -IEEE Transactions on Neural Networks and Learning Systems

Updated 12 January 2023

## Abstract

* DRL and MARL is known to be sample inefficient, preventing real-world applications
* One bottleneck is the exploration challenge: how to efficiently explore the environment collecting informative experiences
* Comprehensive survey on existing exploration methods for both single-agent and multi-agent RL.
* First: identify challenges
* Second: Survey with two categories: uncertainity-oriented exploration and motivation-oriented exploration, as well as other notable exploration methods
* Both algorithmic analysis and comparison on DRL benchmarks
* Summarization and future directions

## Sections

1. Introduction
2. Preliminaries
   1. Markov Decision Process & Markov Game
   2. Reinforcement Learning Methods
      1. Value-based methods
      2. Policy Gradient Methods
      3. Actor-Critic Methods
      4. MARL Algorithms
   3. Basic Exploration Techniques
      1. Epsilon-Greedy
      2. Upper Confidence Bounds
      3. Entropy Regularization
      4. Noise Perturbation
   4. Exploration based on Bayesian Optimization
      1. Gaussian Process-Upper Confidence Bounds (GP-UCB)
      2. Thompson Sampling (TS)
3. What Makes Exploration Hard in RL
   1. Large State-action Space
   2. Sparse, Delayed Rewards
   3. White-noise Problem
   4. Multi-agent Exploration
4. Exploration in Single-agent DRL
   1. Uncertainity-oriented Exploration
      1. Exploration under Epistemic uncertainty
         1. Parametric Posterior-based Exploration
         2. Non-parametric Posterior-based Exploration
      2. Exploration under Aleatoric Uncertainty
      3. Exploration under Both Types of Uncertainty
   2. Intrinsic Motivation-oriented Exploration
      1. Prediction Error
      2. Novelty
      3. Information Gain
   3. Other Advanced Methods for Exploration
      1. Distributed Exploration
      2. Exploration with Parametric Noise
      3. Safe Exploration
5. Exploration in Multi-Agent DRL
   1. Uncertainty-oriented Exploration
   2. Intrinsic Motivation-oriented Exploration
   3. Other Methods for Multi-Agent Exploration
6. Discussion
   1. Empirical Analysis
   2. Open Problems
      1. Exploration in Large Open space
      2. Exploration in Long-horizon Environments with Extremely Sparse, Delayed Rewards
      3. Exploration with White Noise Problem
      4. Convergence
      5. Multi-Agent Exploration
      6. Safe Exploration
7. Conclusion

## 7. Conclusion

* Suggestions and insights:
  * Current Exploration methods are evaluated mainly in terms of cumulative rewards and sample efficient on a handful of well-known environments
  * The essential connections beteen different exploration methods are to be further revealed
  * Exploration among large action space. long horizon environments and convergence analysis are relatively lacking studies
  * Multi-Agent Exploration can be even more challenging due to complex multi-agent interactions. Coordinated exploration with decentralized executionand exploration under non-stationarity may be the key problems to address.
