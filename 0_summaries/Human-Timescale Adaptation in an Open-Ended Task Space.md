# Human-Timescale Adaptation in an Open-Ended Task Space

## Abstract

* We demonstrate that training an RL agent at scale leads to general in-context learning algorithm that can adapt to** open-ended novel embodied 3D problems as quickly as humans**
* Displays on-the-fly hypothesis driven exploration, efficient exploitation of acquired knowledge and can successfully be prompted with first-person demonstrations.
* Three ingredients:
  1. Meta-reinfrocement learning accross a vast, smooth and diverse task distribution
  2. A policy parameterized as a large-scale attention-based memory architecture
  3. An effective automated curriculum that prioritazes tasks at the frontier of the agent's acapabilities
* We demonstrate characteristic scaling laws with respect to network size, memory lenght and richness of the training task distribution
* Foundation for increasingly general and adaptive RL agents that perform well across ever-larger open-ended domains

## Sections

1. Introduction
2. Adaptative Agent
   1. Open-ended task space: XLand 2.0
   2. Meta-RL
   3. Auto-curriculum Learning
   4. RL Agent
      1. Learning Algorithm
      2. Memory architecture
      3. Agent Architecture
      4. Going beyond few shots
   5. Distillation
3. Experiments and Results
   1. AdA shows human-timescale adaptation
      1. Single-agent
      2. Multi-agent
   2. Architecture influences performance
   3. Auto-curriculum learning improves performance
   4. Scaling the agent improves performance
      1. Scaling Network Size
      2. Scaling Memory Length
   5. Scaling the task pool increases performance
      1. Scaling the size of the task pool
      2. Scaling acomplexity of the task pool
   6. Distillation improves performance and enables scaling agents
   7. Training on more trials with skip memory enables many-shot adaptation
   8. AdA can leverage prompting with first-person demonstrations
4. Related Work
   1. Procedural environment generation
   2. Open-ended learning
   3. Adaptation
   4. Transformers in RL and beyond
5. Conclusion
6. Authors and contributions
7. Acknowledgements

## 5. Conclusions

* Foundation models have demonstrated an ability to acquire a large knowledge-base of information, and apply this rapidly to new scenarios
* We demonstrate (first time) and agent that is capable of rapid in-context adaptation across a vast, open-ended task space at a timescale similar to humans.
* This Adaptative Agent (AdA) explores held-out taks in a structured way, refining its policy towards optimal behaviour given only a few interactions with the task.
* AdA shows scalable performance as a function of a number of parameters, context lenght and richness of the training task distribution.
* Method based on black-box meta RL, previously thought hard to scale. We show that state of the art automatic-curriculum techniques can shape the data distribution to provide sufficient signal for learning in an open-ended task space.
* Better than RNN and Transformers are crucial in the Distillation phase.
* The future of AI will inevitably involve training increasingly large models with increaingly general and adaptative capabilities.
* Recipe for 500M parameter model.
* AdA shows rapid and scalable adaptation of myriad kinds, from tool use to experimentation, from division of labor to navigation.