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

## 1. Introduction

* A policy maps the states of an environment to the actions of an agent. Through Reinforcement Learning, the agent learns the policy through trial-and-error, while in Demonstration Learning, the agent learns from a dataset of interactions on the environment performed by an expert.
* Through Inverse Reinforcement Learning, demonstrations can also be used to train a reward function, and avoid designing it.
* Rl is more inefficient and potentially unsafe in real-world learning settings, while Demonstration Learning is completely reliant on demonstrations, which can be difficult to engineer and generalize, and suffers all defects of the demonstrator, including noise, inaccuracies or inconsistencies.
* Demonstration Learning can be refered as Imitation Learning, Behaviour cloning and some kinds of offline reinforcement Learning.

## 10. Conclusion

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

## 2. Problem Definition

* Demonstration Learning is a mixture of Supervised Learning and Reinforcement Learning. The goal of Demonstration learning is to have an agent perform a task by learning from interactions demonstrated by an expert demonstrator and recorded in a dataset.
* In Demonstration learning, the agent has access to a dataset of $N$ demonstrations. Each demonstration is the sequence of visited states and the respective actions chosen by the expert demonstrator. The agent's policy is estimated from the behaviours shown in the dataset.
* Families of methods of Demonstration Learning:
  * __Behaviour cloning__:
    * Family of methods where the policy is trained to ouput the demonstrated action for a given state. 
    * The problem becomes a classification for discrete action spaces or a regression for continuous action spaces.
  * __Inverse Reinforcement Learning__:
    * Demonstration are used to formulate a reward function.
    * Reinforcement Learning in which the agent is rewarded for how similar the action is to the one in the dataset for a given state
  * __Offline Reinforcement Learning__:
    * The demonstrations include the environment rewards in addition to states and actions.
    * The policy is learned by maximizing the accumulated reward for all trajectories.
    * The goal is to learn by interacting with the dataset and generalize instead of naively imitate the expert demonstrator.

## ChatGPT Summary of the above

Demonstration Learning is a machine learning paradigm in which an agent learns to perform a task by imitating an expert's behavior, based on demonstrations. Learning from demonstrations improves the learning process's efficiency and reduces the programmer's effort compared to traditional Reinforcement Learning. However, demonstration learning faces challenges in creating a dataset, selecting the demonstrator, and training an agent. The main challenge is generalizing to unseen scenarios as demonstrations only cover a subset of scenarios. Demonstration Learning has advantages in reducing the need for expert programming and being more data-efficient and safe than RL. It has applications in robotics, video games, healthcare, and industry. The focus of researchers should be on developing benchmarks and datasets. The dataset is a set of demonstrations made by an expert teacher, and the learner maps the state-action pairs in the dataset. Two types of mapping are required in the process: record mapping and embodied mapping.

## 3. Demonstration Dataset

* The dataset is a set of demonstrations made by an expert teacher, each corresponding to a sequencce of state-action pairs.
* The first part is choosing the demonstrator, then the demonstration technique and the way data is stored. 
* Ideally, the pairs in the data map directly to state-action pairs usable by the learner, however correspondence issues may irise when there are differences between the demonstrator and the learner's contexts.

### 3.1 choosing the demonstrator

* You have to choose who controls the demonstrator and who executes the demonstration, which may o r may not be the same, as in teleoperation, where a human cotrolds the agent, who then demonstrates the task.
* If the agent executing the demonstrations is different from the learning agent, the state-action pairs will likely need to be mapped to the learner's space.

### 3.2 Demonstrator and Learniner Matching

* Two types of mapping:
  * Record mapping:
    * Maps the teacher's state-action pairs to the recorded state-action pair space
  * Embodied mapping: 
    * Maps the recorded state action pairs to the learner's state-action pair space