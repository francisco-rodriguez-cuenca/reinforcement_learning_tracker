# Foundation Models for Decision Making: Problems, Methods, and Opportunities

A tutorial basically

## Abstract

* Foundation Models trained on data at scale have shown great capabilities
* The intersection of foundation models and decision-making research holds tremendous promise for developing powerful new systems that can effectively interact with other agents and engage in long-term reasoning
* This paper explores the potential of foundation models for decision-making, offering conceptual tools and technical background to better understand the problem space and identify new research directions.

## Sections

1. Introduction
2. Prelimininaries
3. Foundation Models as Conditional Generative Models
4. Foundation Models as Representation Learners
5. Large Language Models as Agents and Environments
6. Open Problems, Challenges and Opportunities
7. Discussion and Perspectives

## 1. Introduction

* Language models ace new scenarios that challenge their decision-making  abilities, such as:
  * Learning from feedback given by external entities.
  * Adapting to modalities not commonly found in large language or vision datasets, such as robot actions.
  * Engaging in long-term reasoning and planning for the future.
* Previous work on decision-making has primarily concentrated on task-specific or tabula rasa settings with limited prior knowledge.

### 1.1 Structure of this report:

* Section 2: relevant background on decision-making
* How foundation models can characterize different components of a decision making system:
  3. Generative Models of behaviour (skill discovery) and of the environment (model-based rollouts)
  4. Representation learners of states, actions, rewards and transition dynamics
  5. Interactive agents and environments, enabling new problems and applications to be considered under a sequential decision making environment
6. Open problems and challenges, propose potential solutions (how to leverage broad data, how to structure environments, what can be improved)

## 7. Discussion and possibilities

* As well as achieving a more sophisticated intelligence, foundational models can also characterize different aspects of a decision making system: generative models of behaviour and the world, representation of world knowledge and interactive agents or environments. 
* Challenges: gap in modalities, ambiguities around environment and task structure, and missing components in foundation models and decision making paradigms
