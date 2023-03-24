# [Prevalence of Code Smells in Reinforcement Learning Projects](https://arxiv.org/pdf/2303.10236)

Quote method chaining in pandas: https://davidamos.dev/method-chaining-in-pandas/

## Abstract

* The majority of RL code is not developed by RL Engineers, which may lead to poor program quality yielding bugs, suboptimal performance, mantainability, and evolution problems.
* The study includes 24 popular RL-based Python problems, analyzed with standard software engineering metrics.
* The results that 3.95% of the code base on average contains code smells. 
* The most frequent are:
  * Long method and long method chain, highlighting problems in the definition and interaction of agents
  * Responsibility separation and appropriateness of current abstractions for the definitions of RL algorithms

## Sections

1. Introduction
2. Assessing Quality of RL Projects
3. Methodology
4. Results and Analysis
5. Roadmap for Higher Quality RL
6. Related Work
7. Conclusion and Future Work

## 2. Assesing Quality of RL projects

* 8 code smells measured:
  1. Long Method
  2. Large CLass
  3. Long Parameter List
  4. Long Method Chain
  5. Long Scope Chaining: multiply-nested functions
  6. Long Ternary Conditional Expression
  7. Multiply-Nested Container: containers inside containers
  8. Long Lambda Function

## 7. Conclusion and Future Work

* 20 github projects + 4 ACME examples
* Github:
  * Long Method
  * Large Class
  * Multiple Nested Container
  * Long Parameter List
* ACME:
  * Multiply-Nested Container
  * Long Lambda Function
  * Long Method
  * Long Parameter List
* Projects developed for the ACME framework have less smells than projects by Github users
* Multiply-Nested Container and Long Parameter List code smells indicate that the basic structures used to define RL systems (i.e. environments, states, rewards, and transition vectors) are not appropriate to capture the dimenssionality of the problem at hand, making RL projects hard to understand and mantain
* Future work:
  * Specialized software quality metrics for RL projects
  * The creation of more expressive abstractions that accomodate the complexity of RL problems and algorithms in a simpler way.