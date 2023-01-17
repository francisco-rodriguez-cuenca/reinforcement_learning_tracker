# Towards Deployable RL - What’s Broken with RL Research and a Potential Fix

* Shie Mannor - Technion and Nvdia Research
* Aviv Tamar - Technion

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