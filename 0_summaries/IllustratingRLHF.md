# Illustrating Reinforcement Learning from Human Feedback


* Same as Reinforcement Learning from Human Preferences
* Using human feedback as a measure of performance/loss function.
* RLHF has enabled language models to align a model trained on a general corpus of data to that of complex human values.

## RLHF: Let's take it step by step

Steps of training a model with RLHF:

1. Pretraining a Language Model (LM)
2. Gathering data and training a reward model
3. Fine tuning the LM with Reinforcement Learning

### Pretraining Laguage Models

* RLHF uses a language model that has already been pretrained with classical pretraining objectives, like GPT 3.
* This language model can be further fine-tuned on additional text or conditions (augmented data), but doesn't need to be for RLHF. For example, Open-Ai fine tunes on human text deemed "preferable" and Anthropic follows "helpful, honest and harmless criteria.

### Reward Model training

* The underlying goal is to get a model or system that takes in a sequence of text and returns a scalar reward which should represent human preference.

    Summarize Human preference into a model.

1. Sampling a set of prompts from a predefined dataset
2. Using the initial Language Model to genererate new text
3. Human anotators are used to rank generated text outputs, and generate a measure of reward. 
4. Train with {sample, reward} pairs a supervised "Reward Model" that takes in the text and returns the reward.

### Fine-tuning with RL

* The idea is to frame the problem as a Reinforcement Learning algorithm:
  * The policy is the parameters of a copy of the initial Language Model as it is updated by  the RL algorithm.
  * The action space is the vocabulary of the original model (referred as tokens, in the order of 50k)
  * The observation space is the possible input prompts (Very large, numebr of tokens^lenght of vocabulary)
  * The reward function is a combination of the Reward model return and a penalty measuring distance from the initial Language Model (don't want it to be too different, incohenrent phrases that return high reward gaming the reward model, uses kl distance generally)

To update the policy, PPO is usually used although A2C can be used also.

## Open-source tools for RLHF

## What's next for RLHF?

RLHF performance is only as good as its human annotations (optional initial fine-tuning with human generated text and human rankings for the reward model)
Human annotators can disagree, which adds potential variance to the training data without ground truth.

## Further reading