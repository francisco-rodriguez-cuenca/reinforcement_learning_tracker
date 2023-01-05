# Towards learning abstractions via reinforcement learning

Erik Jergéus
Leo Karlsson Oinonen
Emil Carlsson
and Moa Johansson

Chalmers University of Technology, Gothenburg, Sweden

AIC 2022, 8th International Workshop on Artificial Intelligence and Cognition

Keywords: Reinforcement Learning, Multi-Agent Systems, Neuro-symbolic systems, emergent communication

## Abstract

* New approach of synthesis of efficient communication schemes in multi-agent rl systems
* Combine symbolic methods with machine learning - neurosymbolic system
* Reinforcement learning is interleaved with steps to extende the current language with novel higher-level concept, allowing generalization and more informative communication via shorter messages
* This aproach allows agents to converge more quickly on a small construction task

## Introduction

* Learning to communicate and coordinate via interactions is often viewed as a prerequesite for developing artificial agents capable to do complex machine-to-machine and machine-to-human-communication
* A striking characteristic that has been overlooked in the literature is the ability to derive concepts and abstractions from primitives, via interaction

human Builder-architect experiments

* The architect is given the drawing of a shape, and has to instruct the builder on how to construct it from samall blocks.
* As the experiment progressed, participants developed more concise instructions (e. L-shape)

Study

* Our constribution here is an  initial feasability study of a neuro-symbolic multi-agent reinforecement learning framework for the builder-architect task
* Inspired by neuro-symbolic program synthesis, the agent interleave reinforcement learning to train their neural network, with symbolic reflection to introduce new concepts for common action sequences
* Agents learn to construct the given shapes faster when allowed the capability to introduce abstractions

## Sections

1. Introduction
2. Implementation
   1. The Environment
   2. Seep Reinforcement Learning
   3. Abstraction Phase
3. Experimental Results
4. Conclusion and Future Work.

## Conclusion and Future work

Conclusion

* Neuro-symbolic framework for learning liguistic abstractions via a combination of reinforcement learning, symbolic reasoning and interactions between agents.
* Results suggest that it is feasible for reinforcement learning to develop useful abstractions by alternating between neural learning and symbolic abstraction
* The introduced abstract concepts also greatly improve the performance of the agents.

Future work

* Extend to more complex environments:
  * The agents might need to first develop several inmediate abstractions, before being useful. Solving this exploration-explotation dilemma seems like a fundamental problem.
* Explore scenarios where agents do not share exactly the same understanding of a message and are required to reason in a recursive fashion.
