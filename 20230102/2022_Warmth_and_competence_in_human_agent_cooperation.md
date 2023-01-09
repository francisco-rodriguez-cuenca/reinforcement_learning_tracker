# Warmth and competence in human-agent cooperation

* Kevin R. McKee - Deepmind
* Xuechunzi Bai - Princeton
* Susan T. Fiske - Princeton

Proc. of the 21st International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2022), P. Faliszewski, V. Mascardi, C. Pelachaud, M.E. Taylor (eds.), May 9–13, 2022, Online.

    Kevin R. McKee, Xuechunzi Bai, and Susan T. Fiske. 2022. Warmth and Competence in Human-Agent Cooperation. In Proc. of the 21st International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2022), Online, May 9–13, 2022, IFAAMAS, 33 pages.

## Abstract

* AI agents trained with deep reinforcement learning are capable of communicating with humans
* Studies primarly evaluate human compatability through "objective" metrics such as task performance -> obscures variation in levels of trust and subjective preference.
* Uses the game of Coins -> 2 player social dilemma
    * Measure the preferred agents by participants
    * Perceptions of warmth and competence predict their stated preferences for different agents
* Implementation of a new "partner choice" framework to elicit revealed preferences:
  * Participants play a round with an agent
  * Participants are asked if they want to continue with that agent or play alone
* As with stated preferences, social perception better predicts participants' revealed preferences than does objective performance
* Recommendation of the inclusion of social perception and subjective preference into studies

## Introduction

Contributions:

* A. Demonstrates how reinforcement Learning can be used to train human-compatible agents for a temporal and spatially extended mixed-motive game
* B. Measures both stated and revealed preferences, introducing a partner choice for the latter
* C. Examines how fundamental social perceptions affect stated and revealed preferences over agents, above and beyond traditional objective metrics

Social perception:

* Two underlying qualities:
  * Competence: Consistent with traditional ML scoring
  * Warmth: How aligned are this actor's goals and interests with one's own

Behavioural experiment:

* Train RL agents to play Coins, a mixed-motive game, varying agent hyperparameters known to influence cooperation and performance
* Three co-play experiments recruit human participants to interact with the agents:
  * measure participants' judgement of agent warmth and competence
  * elicit participant preference over the agents

Stated preferences:

* Mostly used in experiments, often by directly asking participants
* Insightful tools for research
* Vulnerable to experimenter demand - Experimenter demand effects refer to changes in behavior by experimental subjects due to cues about what constitutes appropriate behavior.
* Limited ecological validity

Eliciting revealed preferences:

* Do people want to interact with the agent, if given the chance not to?
* Well established revealed preference paradigm in evolutionary biology and behavioural economics
* In incentivised experiments, parner-choice measures mitigate experimenters demand 
* In the context of algorithmic development, we can view partner choice as stand-in for the choice to adopt an AI system
* Empowers participants with an ability to embrace or leave an interaction with an agic - and thus incorporate an ethic of autonomy into human-agent interaction research

## Headings

1. Introduction
2. Methods
   1. Task
   2. Agent design and training
   3. Study design for human-agent studies
3. Results
   1. Agent training
   2. Human-agent studies
4. Discussion

## Discussion

* This experiment demonstrates that artificial agents trained with DRL can cooperate and compete with humans in temporally and spatially extended mixed-motive games.

Prediction of preference

* Agents elicited varying perceptions of warmth and competence
* Predicting users' preferences can be done with objective features and improved with people's perceptions (stated or revealed)
* Participants prefer warm agents over cold agents but, unexpectedly, also incompetent agents over competent agents

Mixed motive games

* Mixed-motive games open new challenges related to motive alignment and explotability
* Participants who played with (and exploited) altruistic agents expressed guilt and contrition. -> conflicts with research suggesting that humans are "keen to exploit benevolent AI"

Incentivised partner choices

* Incentivised partner choices can help test whether new algorithms represent innovations people can be motivated to adopt
* Close correspondance between stated and revealed preferrences -> stated preferences are still relevant (and cheap), can strenghen objective measures

Preferences are not a panacea

* Does not solve the fundamental question of value alignment:
    How to ensure that AI systems are properly aligned with human values and how to guarantee that AI technology remains properly ameniable to human control" - Gabriel and Ghazavi
* Gabriel and Ghazavi identify shortcuts with both objective and subjective metrics