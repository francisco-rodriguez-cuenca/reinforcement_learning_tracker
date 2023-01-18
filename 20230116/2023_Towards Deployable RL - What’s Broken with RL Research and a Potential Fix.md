# Towards Deployable RL - What’s Broken with RL Research and a Potential Fix

* Shie Mannor - Technion and Nvdia Research
* Aviv Tamar - Technion

A Deployable RL manifesto:

https://avivtamar.substack.com/p/deployablerl

## Abstract

* Point out difficulties with current research
* The current situation is not likely to lead to "deployable RL": RL that works in practical situations and is economically viable

## Sections

1. Introduction
2. Generalist Agents VS Deployable RL Systems
3. Principles of Deployable RL Research
4. Actionable Next Steps

## 1. Introduction

* RL is not living up to our expectations.
* Here are five popular research practices that were relevant for 2015, but are currently stagnating the field:
  * __Overfitting to Specific Benchmarks__
    * Nearly every paper is required to show some distinction for one of the popular benchmarks (Atari, Mujoco...)
    * Research on tweaks that will most likely only work for specific benchmarks is abundant
    * Progress in benchmarks does not yield tangible real-world value
  * __Wrong Focus__
    * Current benchmarks ignore the deployable nature of situated (RL-driven) agents completely, focusing on algorithms rather than on a system/engineering view.
    * OpenAI GYM abstracts away all system-design issues
    * This hampers progress since in many practical problems, figuring out what are the useful states, actions, and rewards is a critical component of the development process
  * __Detached Theory__
    * Useful theory seems to be quite rare:
      * Regret minimization is overly pessimistic
      * There is a lot of prior knowledge that is not accounted for
      * finite states and actions are not a good model for many problems of interest
      * Focus on unimportant qualities
  * __Uneven Playing Grounds__
    * Performance is confounded by resources available to the implementer:
      * Proficiency in hyper-parameter tuning
      * Size of NN
      * Prior knowledge about the problem/solution
      * Variability of scale and the current trend at top conferences to prefer masive experimentation over conceptual novelty, can inhibit long-term progress
  * __Lack of Experimental rigor__
    * Impressive singular experiments give a false sense of progress
    * We need more rigorous evaluation of difficulty and success: stability, deployment time and cost, testability and life-cycles are critical
    * The publication standard is that failure cases are almost never reported, stability is impossible to tell, and software design issues are not discussed.

## 2. Generalist Agents vs Deployable RL Systems

* Two views:
  * __Generalist/AI first__: Future progress will be made by focusing attention on large-scale training of agents that solve diverse problems, with the hope that along the way a generalist agent will develop, and be a useful component in various real world problems
  * __Deployable RL/RL second__: Seek to design RL algorithms that solve concrete real world problems
* The five problems of the introduction are relevant to both approaches
* With the current knowledge of the field, we should seek the second (Deployed RL) approach.

## 3. Principles of Deployable RL Research

* At present, RL is __uneconomical to deploy__.
* To change it:
  * Research on how to deploy it effectively
  * Better understanding of the gains RL brings
* They propose a constructive model with three general principles:
  * __Challenges instead of benchmarks__:
    * _Challenge_: _problem sponsored by a group of researchers from academia/industry, instead of comparing algorithms, solve a real world problem and bring real world value
    * _Credit for contributing challenges_: A rigorous presentation of a challenge (description, community and supporting platform) should be credited
    * _Measurable progress is the main criterion for publication_: Every publication should explain the limitations and issues with the proposed algorithm and how it addresses problems specifically.
    * _Weight class_: Computing power available should be reported to address the significance of the results
  * __Theory papers shoud address specific challenges__:
    * The goal of the research should be well justified in terms of its potential impact on real world problems. Should also consider problems that have to do with the life cycle of software such as data acquisition, debugging, testability and performance deterioration.
  * __Design Patterns Oriented Research__:
    * Real-world RL based systems should have conceptual solutions to problems where issues such as terstability, debuggability, and other system life-cycle issues are addressed.
    * We forsee that one way to make significant progress on a challenge would be by developing novel design patterns for it.

## 4. Actionable Next Steps:

* To us, deployable RL means RL that can work at scale, be economically feasibl, and can eventually be put in the field.
* Here is what you can do:
  * __Contribute challenges__: 
    * Requires deep understanding of the application domain, with many disciplines of impact (healthcare, engineering...)
    * Might require industry and academia joining forces
  * __Frame your own research__: Frame the research effort within deployable RL principles.
  * __Critize others' research__: Coordinate with researchers, reviewers and area chairs. Ask how a paper gets the field closer to real-world impact.