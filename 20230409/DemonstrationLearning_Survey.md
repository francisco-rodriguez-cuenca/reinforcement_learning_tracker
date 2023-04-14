# [A Survey of Demonstration Learning](https://arxiv.org/pdf/2303.11191)

NOVA LINCS 
Universidade da Beira Interior

## Abstract

* Demostration Learning is a paradigm in which an agent learns to perform a task by imitating the behaviour of an expert shown in demonstrations.
* Learning from demonstrations accelerates the learning process by improving sample efficiency, and reduces the programmer's effort.
* Survey of demonstration learning:
  * Formal introduction of the demonstration problem and challenges
  * Overview of the Demonstration Learning Process:
    * Creation of the dataset
    * Learning methods from demonstrations
    * Optimization by combination with other ML methods
  * Review benchmarks and their strengths and limitations
  * Advantages and disadvantages of Demonstration Learning, main applications
  * Open problems and research directions

## Sections

1. Introduction
2. Problem Definition
3. Demonstration Dataset
   1. Choosing the Demonstrator
   2. Demonstrator and Learner Matching
   3. Choosing the demonstration technique
      1. Direct Demonstrations
         1. Teleoperation
         2. Kinesthetic
         3. Shadowing
      2. Indirect Demonstration
         1. Observation
         2. Sensors on Teacher
         3. Data Representation
      3. Raw Features
         1. Manually Designed Fetures
         2. Extracted Features
         3. Time as a Feature
      4. Dataset Limitations
         1. Incomplete Data
         2. Inadequate Data
4. Learning from Demonstrations
   1. Learning Problems
   2. Policy Learning
      1. Behaviour Cloning
      2. Offline Reinforcement Learning
      3. Classification
      4. Regression
   3. Model Learning
   4. Inverse Reinforcement Learning
   5. Other Learning Methods
      1. Reinforcement Learning
      2. Evolutionary Algorithms
      3. Transfer Learning
      4. Adaptive Learning
      5. Active Learning
      6. Generative Adversarial Imitation Learning (GAIL)
      7. Embedding Space
      8. Sequence Models
   6. Multi-agent
   7. Learning Modifications
5. Evaluation
   1. Quantitative
   2. Qualitative
6. Benchmarks
7. Applications
   1. Assistive Robots
   2. Autonomous Navigation
   3. Manipulators
   4. Humanoid Robots
   5. Video-Games
8. Advantages and Disadvantages
   1. Advantages
   2. Disadvantages
9. Future Directions
   1.  Benchmarking
   2.  Context Problem
   3.  Goal Specification
   4.  General Demonstration Learning Framework
   5.  General Feature Extraction
   6.  Generalization
   7.  Hyper-parameter Selection
   8.  Long-Horizon Tasks
   9.  Multi-Agent Demonstration Learning
   10. Learning from Sub-Optimal Data
   11. Safety Concerns
10. Conclusion

## Introduction

* A policy maps the states of an environment to the actions of an agent. Through Reinforcement Learning, the agent learns the policy through trial-and-error, while in Demonstration Learning, the agent learns from a dataset of interactions on the environment performed by an expert.
* Through Inverse Reinforcement Learning, demonstrations can also be used to train a reward function, and avoid designing it.
* Rl is more inefficient and potentially unsafe in real-world learning settings, while Demonstration Learning is completely reliant on demonstrations, which can be difficult to engineer and generalize, and suffers all defects of the demonstrator, including noise, inaccuracies or inconsistencies.
* Demonstration Learning can be refered as Imitation Learning, Behaviour cloning and some kinds of offline reinforcement Learning.

## Conclusion

* Demonstration Learning reduces the overhead of programming by teaching an agent a task through demonstrations
* Two phases:
  * Building the dataset
    * Choosing the demonstrator
    * Recording the demonstrations
    * Representing the data
    * Other limitations
  * Training an agent
* Main Challenge: Generalization to unseen scenarios,
  * Demonstrations only cover a subset of scenarios, if the agent wanders to out-of-distribution states, the consequences can be catastrophic
  * Offline RL try to reduce the distributional shift
  * Model learning allows the agent to generate new transitions without interaction
  * Other ways of behaviour refinement: reinforcement learning, transfer learning, querying the teacher, evolutionary learning
* Applied to robots and videogames, domains of healthcare and industry
* Advantages:
  * Reducing the requirement of expert programming
  * More data-efficient than RL
  * More safe generally than RL
* Disadvantages:
  * Requires a good framework for creating the dataset and estimating the policy.
* The authors argue that the researchers focus should be on benchmarks and datasets.