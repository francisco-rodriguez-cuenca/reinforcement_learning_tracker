# Towards Automating Codenames Spymasters with Deep Reinforcement Learning

Sherman Siu - Cheriton School of Computer Science

Submitted to the Journal of Machine Learning Research I (2022)

Looks like a graduate thesis - One star

## Introduction

* Codenames is a good benchmark for both human-AI cooperation and text-based reinforcement learning.
* Traditional multi-agent RL techniques tend to work well when agents work with each other but fail when co-operating with humans
* Text-based games are an open problem for AI-based research
  * One of the main challenges is the large action-space available to agents
  * Text-based games are a good benchmark for natural language understanding

[Overview of Codenames]

Contributions

1. Formulate a game of Codename's from a spymaster's perspective as a Markov Decision Process, implement it as an OpenAI gym environment
2. Demonstrate that several agents (SAC, PPO, A2C...) do not cause converge. Random and simple greedy are better
3. Formulated on simplified versions (ClickPixel, Whack-a-mole), A2c converges when the environment is small and fail when the environment is big

## Sections

1. Introduction
   1. Overview of Codenames
   2. My contributions
2. Related Works
   1. Pairwise Word Similarity
   2. Automating the Spymaster
   3. Automating the guessers
3. Methodology
   1. Formulation of Codenames as MDP
   2. Codenames Gym environment
      1. State Encoding Method
      2. Action encoding method
      3. Spymaster strategy
      4. Guesser Strategy
      5. Word Embeddings
      6. Approximate Nearest Neighbour Acceleration
   3. RL Agents
   4. ClickPixel Gym Environment
   5. Whack-A-Mole Gym Environment
4. Results
   1. ClickPixel
   2. Whack-a-Mole
5. Limitations
6. Future Work
7. Conclusion

## Limitations

* Does not include all codenames rules and nuance
  * Formulates codenames as a single agent environment but a true game of codenames is zero sum with two players
  * Does not take into account that the hints given by an agent are received also by the opposite team.

## Future Work

* Collect a large dataset of human games to learn a scoring function
* Fine tune a model such as FLAN-T5 on predicting properties about synthetic Codenames games that are encoding using a text template. Further fin-tune the LLM using Reinforcement Learning from Human Feedback (RHFL).
  
## Conclusion

* None of SAC, PPO and A2C are good enough - fail when compared to random or naive greedy
* The best (though failing) is A2C as evaluated in the ClickPixel Environment