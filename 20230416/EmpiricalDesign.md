# [Empirical Design in Reinforcement Learning](https://arxiv.org/pdf/2304.01315)

## Abstract

* Recent studies have highlighted how popular algorithms are sensitive to hyperparameter sttings and implementation details, and that common empirical practice leads to weak evidence.
* This manuscript represents both a call to action and a comprehensive resource on how to do good experiments on Reinforcement Learning.
* Covers:
  * Statistical Assumptions underlying common performance measures
  * how to properly chracterize performance variation and stability
  * hypothesis testing
  * comparing multiple agents
  * base and illustrative example construction,
  * and how to deal with hyper parameter and experimenter's bias

* The objective is to provide answers on how we can use our unprecedented compute to do good science in Reinforcement Learning, as well as to avoid pitfalls in our empirical design

## Sections

1. Reinforcement Learning, an Empirical Science
2. Observational Experiments
   1. Experiment one: a demonstration
   2. Experiment two: characterizing variations in performance
   3. Distributions matter!
   4. Reporting variability in performance
   5. Reporting confidence in performance estimates
   6. Do we really need more runs?
   7. Deciding on the length of an experiment
3. Dealing with Hyperparameters
   1. Understanding hyperparameter sensitivity
   2. Reporting idealized perfomance
   3. Evaluating algorithms for deployment
4. Comparing the Performance of Multiple Algorithms
   1. Designer's curse: with great knowledge comes great responsability
   2. The utility of calibration baselines: what does that line mean anyway?
   3. Ranking algorithms (maybe don't)
   4. Statistically significant comparisons for two fully-specified algorithms
   5. Statistically significant comparisons for multiple fully-specified algorithms
5. Selecting Environments
   1. Diagnostic environments
   2. Benchmark experiments and challenge problems
   3. New (or modified) environments are not always better
6. Common errors in RL experiments
7. Case study: reevaluating previous work
8. Conclusion

Appendix:

1.  Summary of Contributions
2.  Further Experimental Details
    1.  ESARSA and the GridWorld
3.  Computing Tolerance Intervals
4.  More about Hyperparameter Selection
    1.  Understanding hyperparameter sensitivity for multiple parameters
    2.  Developing algorithms and avoiding misleading yourself
    3.  Why can't we just use cross-validation?
    4.  Cross-validation-like procedures for hyperparameter selection
    5.  Even more about treating the hyperparameter optimizer as the algorithm
5.  Agreggating Environments
6.  Understanding our Agents with Multiple Evaluation Metrics
    1.  Measuring the performance of an agent
    2.  Summarizing performance over time
    3.  Offline returns versus online returns
   1.  

## Introduction

