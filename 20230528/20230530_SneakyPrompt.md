# [SneakyPrompt: Evaluating Robustness of Text-to-image Generative Models' Safety Filters](https://arxiv.org/pdf/2305.12082)

## Abstract

* One challenging problem of text-to-image generative models is the generation of Not-Safe-For-Work (NSFW) content
* SneakyPrompt
  * First adversarial attack framework to evaluate the robustness of real-world safety filters in state-of-the-art generative models.
  * Searches for alternate tokens in a prompt that generates NSFW images so that the generated prompt (advesarial prompt) bypasses existing safety filters
  * Uses RL to guide an agent with positive rewardson semantic similarity and bypass success.
* Evaluation
  * SneakyPrompt successfully generatess NSFW content on default closed-box safety filter DALL-E 2
  * Bypasses also several state-of-the-art safety filters on a StableDifussion model
  * Succesfully generates NSFW content and outperforms existing adversarial attacks

## Sections

1. Introduction
2. Related Work and Preliminary
3. Problem Formulation
   1. Definitions
   2. Threat Model
4. Methodology
   1. Overview
   2. Baseline Search with Heuristics
   3. Guided Search via Reinforcement Learning
5. Experimental Setup
6. Evaluation
   1. RQ1: Effectiveness in bypassing safety filters
   2. RQ2: Performance compared to baselines
   3. RQ3: Study of different parameter selection
   4. RQ4: Explanation of bypassing
7. Possible Defenses
   1. Defense Type I: Input Filtering
   2. Defense Type II: Training Improvement
8. Conclusion

## 8. Conclusion

