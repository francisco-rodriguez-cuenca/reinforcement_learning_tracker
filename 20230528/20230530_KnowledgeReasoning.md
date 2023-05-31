# [Reinforcement Learning with Knowledge Representation and Reasoning: A Brief Survey](https://arxiv.org/pdf/2304.12090) INT INT

May have some exagerated claims

## Abstract

* Obstacles in RL:
  * Poor system generalization
  * low sample efficiency
  * safety and interpretability concerns
* Most of the work has focused on the computational aspect
  * value functions/policies
  * atomic components of rewards, states and actions
* Neglecting the rich high-level declarative domain knowledge of facts, relations and rules obtained a priori o through reasoning
* __Knowledge Representation and Reasoning__ methods
  * usually using logical languages
  * enable more abstract representation and efficient learning in RL

## Sections

1. Introduction
2. Background
   1. RL
   2. KRR
3. KRR for efficiency of RL
   1. Task Representation
      * Reward Machines
      * Temporal Logics
   2. Symbolic Planning
4. KRR for generalization of RL
   1. One-shot transfer Learning
   2. Continuous/Lifelong Learning
5. KRR for safety/interpretability of RL
6. Challenges
   1. Increasing the spectrum of KRR/RL Methods
   2. Analyzing Theoretical Properties
   3. Applying in More Complex Domains
7. Conclusions

## 1. Introduction

* There is a _theory-to-application_ gap that hinders the wide deployment of RL techniques in real-world problems:
  * _low sample efficiency_
  * _poor generalization capabilities_
  * _lack of consideration of critical concerns such as safety, interpretability and robustness_
* __Knowledge Representation and Reasoning (KRR)__
  * Abstracts the representation in RL by formal languages
  * Problems can be defined more compactly and solved more efficiently and transparently
  * Rich declarative domain knowledge of objects and therir relations can be provided a priori or acquired through reasoning over time, and incorporated into the learning process
* Advantages
  * Traditional representations in RL require all possible states/actions to be represented explicitly
    * Formal language representations allow a more general and intuitive way of specifying and using knowledge of a problem
  * RL depends critically on the use of reward functions, usually handcrafted by an expert designer
    * Simple policies or rewards from human instructions and domain constraints can be easily encoded in formal languages
  * Existing RL methods cannot reason over facts or beliefs
    * Difficult to implement transfer learning, analogical analysis or rule-based reasoning
    * Formal descriptive languages to represent tasks can better facilitate transfer learning (generalization)
  * Black-box training of existing RL is largely opaque to users
    * Difficult to understand and trust, unsuitable for safety-critical domains
    * Policies consisting of explicit symbolic expressions can ease human understanding

