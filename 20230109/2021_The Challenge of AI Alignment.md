# The Challenge of AI Alignment: from Fairer Algorithms to AI Safety

## Sections

1. Introduction
2. Technology & Values
3. Is AI special?
   1. What is AI?
   2. The potential uniqueness of AI systems
4. Technical Approaches to Value Alignment
   1. Top-down and bottom-up approaches
   2. Concrete Problems
   3. Highly Advanced AI
5. The Fundamental Relevance of Value
6. Conclusion

## 1. Introduction

* The challenge of __value alignment__ centres upon the question of how to ensure that AI systems are properly aligned with human values and ameanable to human control.

* Is something special about AI that makes questions about value more complicated or acute?
  * Normative perspective: We are able to encode a richer set of values in AI systems that in simpler artifacts
  * Technological perspective: Greater scope of action and intelligence create new challenges from the perspectives of alignment and control.

## 2. Technology and values

* Definition of value by Friedman and Henry from a technological perspective (2019):
  * what is important to people in their lives, with a focus on ethics and morality
* Do Artifacts have politics? (Landgdon Winner, 1980)
  * Examples
    * Robert Moses: designed bridges in New York City to limit transport flows from poor to nice neighbourhoods
    * Baron Haussman: redesigned the streets of Paris after the French revolution, so that it contained open boulevards that facilitated troop movement and suppressed the possibility of protest (Scott, 2020)
  * technologies draw forth certain modes of social organization
  * The need for large datasets and computer power favors centralized forms of political authority and governance (2018).
* There is no _value neutral_ technology:
  * New technologies make some outcomes more likely and some outcomes less likely to occur, they create new possibilities and sometimes exclude certain possibilities to be realized.
  * Technologists are engaged in a _world-making activity_, there is a level of responsability and the need for methods to ensure that technology alignes with human values (both personal and social)
  * Key methods for value alignment: Stakeholder analysis and citizen consultation
* Technologists need to think about this issues _early on_, including whether to develop new technologies _at all_.

## 3. Is AI Special?

### What is AI?

* Machines are intelligent _to the extent_ that their actions can be expected to match their objectives (Stuart Russell, 2009)
* Machine Learning: family of statistical and algorithmic approaches:
  * Supervised Learning: training a model to identify and respond to patterns in labelled datasets
  * Unsupervised Learning: Aims to uncover patterns in un-labelled data and to perform tasks on that basis
  * Reinforcement Learning: advanced and promising field of AI on which agents learn to maximize a numerical reward signal by interacting with their environment.

### The potential uniqueness of AI Systems

* ML algorithms have the same concerns about injustice, safety, and unintended consequences that are present with other technologies
* _Algorithmic bias_: the potential to manifest a particular set of values:
* _Social value misalignment_: Algorithms in the criminal justice system, healthcare and facial analysis have been found to discriminate against women and non-white folks 
* Challenges:
  * Once the model has been trained is hard to know why it decides one thing or another
  * AI systems can make decisions or chooices that are more meaningful that those encountered by technologies in the past
* Daniel Dennet _degrees of freedom_:
  * A simple switch that can be turned on/off by some environmental change marks a degree of freedom
  * Biological organisms, humans and networks have additional degrees of freedom, and issues of control grow complex and non-linear
  * Hammers and pencils are not able to respond to their environment, but artificial agents can learn new mappings between inputs and outputs, coming up with results that surprise their human designers.
* Daniel Dennet _the intentional stance_:
  * It is most useful to think about AI systems as rational agents that have goals and intentions
  * AI systems have trajectories that "can unfold without any direct dependence on us, their creators, and whose discriminations give thir internal states a sort of meaning to them that may be unknown and not in our service"
* Floridi and Sanders, 2004 AI systems are _moral agents_:
  * Interactivity
  * Autonomy
  * adaptability

## 4. Technological Approaches to Value Alignment

* The alignment ofpowerful Ai systems requires interdisciplinary collaboration, as we need a clear understanding of both the goal of alignment and the technical means.

### Top-Down and Bottom-Up Approaches

Wallach and Allen 2009

* Top-down approaches start by identifying an appropriate moral theory to align with and then designing algorithms capable of implementing it.
  * Based on the possibility that ethical rules can be stated in computer code
  * Isaac Asimov's three laws of robotics
  * Dilemma: either base it on our own moral beliefs, or public principles (primarly utilitarianism)
* Bottom-up approaches focus upon the creation of environments or feedback mechanisms that enable agents to learn from human beahaviour and be rewarded for morally praiseworthy conduct.
  * Inverse Reinforcement Learning: the agent focuses on 'the problem of extracting a reward function given observed, optimal behaviour'
  * Challenges: 
    * Opaque
    * How to ensure that the model is free from bias

### Concrete problems

Reward-hacking:

  * An artificial agent manages to maximise the numerical reward it receives by finding unanticipated sohortcuts or corrupting the feedback system -> Coast Runners
  * Solution:
    * Provide the agent with richer data
    * blunt some of the force of reward hacking by randomizing goals

Take the most efficient path and not consider side effects

Explore the world in a safe way

  * And not make costly mistakes

Evaluate complex agent behaviour

### Highly advanced AI

Stuart Russel, Artificial Geneneral Intelligence:

  * The ultimate goal of AI research is the discovery of a general purpose method that is applicable across all problem types and works effectively for large and difficult stances while making very few assumptions.

Nick Bostrom, superintelligence:

* Any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest

Orthogonality thesis:
* Every intelligence is compatible with any goal (benign or malign)

VS Derek Parfit and Peter Singer:

* hope that substantial moral insight might result from the capacity for instrumental reason.

Instrumental Convergence Thesis (Bostrom and Russell):

* AGI would dislay instrumental goals of self-improvement, self-preservation and resource acquisition in pursuit of its goals, even if it is to the disadvantage of human beings.

Intellligibility and supervision of AGI:

  * How to provide advice and direction to a smarter entity than us.
  * Reward modelling: techniques for supplementing RL with human oversight
    * Recursive reward modelling: The artificial agent is incentivised to help its human instructor better define goals for the AI to pursue
  * Safety via debate: systems debate with each other, competing to provide true answers to human operators

## 5. The fundamental relevance of value

Alignment with what?

* Alignment with instructions
  * Problem: King Midas
* Alignment with true intentions
  * reward modelling approach and contract theory
* Align with human preferences
  * Inversed Reinforcement Learning

* Instructions, intentions and preferrences can all be misinformed, irrational or unethical

How to aggregate individual values to collective judgement

* Systematically sinthesize different types of human preference into an utility function (Armstrong)
* Yudkowsy: Coherent extrapolated volition 
* To achieve _social value alignment_ AI systems ultimately need to embody principles widely endorsed by those affected


Challenges:

* Moral uncertainty: we are ensure if an action/theory is morally right
* Moral pluralism: people ascribe to a variety of reasonable views and perspectives

Citing John Stuart Mill, Hume, Singer...



