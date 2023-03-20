# Deep symbolic regression for physics guided by units constraints: toward the automated discovery of physical laws

## Abstract

* Symbolic regression is the study of algorithms that automate the search for analytic expressions that fit data
* Deep Learning achievments have not been translated to physics, where we have important additional constraints due to units
* $\Phi$-SO: a Physical Optimization framework for recovering analytical symbolic expressions for physics data using DL to learn units constraints
* System built from the ground up top propose solutions where physical units are consistent by construction:
  * This is useful for elimination of physically impossible solutions
  * restricts enormously the freedom of the equation generator, vastly improving performance
* Used to:
  * Fit noiseless data: like attempting to derive an analytical property of a phisical model
  * Obtain Analytical approximations to noisy data

##  3.3 Learning

* "Kind of RL"
  * The training of the network that generates the distribution of symbols relies on a KIND OF reinforcement learning strategy, in which the algorithm generates a set of trial symbolic functions, and compute a scalar reward for each function by confronting it to the data, iteratively reinforceing it to produce better results. The hope is that, by trial and error, the learned parameters of the network will converge to values that are able to generate a symbolic function that fits the data well.

## 7. Conclusions

* Built from the ground up to make use of the highly restrictive constraint that equations must have balanced units.
* The heart of the algorithm is an embedding that generates a sequence of mathematical symbols while cumulatively keeping track of physical units.
* DRL of Petersen et Al. 