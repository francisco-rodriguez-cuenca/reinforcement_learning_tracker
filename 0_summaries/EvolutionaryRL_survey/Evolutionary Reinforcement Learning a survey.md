# Evolutionary Reinforcement Learning: A Survey

## Abstract

* Reinforcement Learning (RL): machine learning approach that trains agents to maximise cumulative rewards through interactions with environments
* Integration of Rl with DL: impressive achievements in a wide range of challenging tasks.
* Several crucial challenges:
  * Brittle convergence properties caused by hypersensitive parameters
  * Difficulties in temporal credit assignment with long time horizons and sparse rewards
  * lack of diverse exploration, specially in continuos search space scenarios
  * Difficulties in credit assignment in multi-agent reinforcement learning
  * conflicting objectives for rewards
* Evolutionary Computation
  * Mantains a population of learning agents, 
  * has demonstrated promising performance in addresing this limitations
* This article presents a comprehensive survey of state of the art methods for integrating Evvoolutionary Computation with RL: EvoRL

## Sections

1. Introduction
2. Background
   1. Reinforcement Learning
   2. Evolutionary Computation
   3. Discussion
3. Evolutionary Computation in Hyperparameter Optimization
   1. Darwininan evolutionary methods
   2. Lamarckian Evolutionary Methods
   3. Hybrid Methods
   4. Discussion
4. Evolutionary Computation in Policy Search
   1. Evolutionary Strategy (ES) based Methods
   2. Genetic Algorithms (GA) based Methods
   3. Genetic Programming based Methods
   4. Discussion
5. Evolutionary Computation in Exploration
   1. Diversity Encouragement Methods
   2. Evolution-guided Exploration Methods
   3. Discussion
6. Evolutionary Computation in Reward Shaping
   1. Evolution of Reward Functions
   2. Hyperparameter Optimization Methods
   3. Discussion
7. Evolutionary Computation in Meta-RL
   1. Parameter Initialization
   2. Loss Learning
   3. Environment Synthesis
   4. Algorithms Generation
   5. Discussion
8. Evolutionary Computation in Multi-objective RL
   1. Multi-objective Evolutionary Algorithms
   2. Multi-objectivization
   3. Discussion
9. Future Research Directions
   1.  Encodings
   2.  Sampling Methods
   3.  Sample Utilization
   4.  Search Operators
   5.  Algorithmic Frameworks
   6.  Evaluation Methods
   7.  Benchmarks for EvoRL
   8.  Scalable Platforms
10. Conclusion

## 1. Introduction

* EvoRL mantains a population of agents, which offers several benefits:
  * Provision of redundant information for improved robustness
  * Enables diverse exploration
  * Ability to evaluate agents using an episodic fitness metric
  * Ease of generating trade-off solutions through multi-objective Evolutionary Computing algorithms

## 10. Conclusion

* Provide guidance for researchers and practitioners interested in EvoRL.