# Hypothesis testing according to E.T. Jaynes

In this project, we explore hypothesis testing in a Bayesian context. Specifically, we try to get a grounded answer to the question: "given two data sets of points on the real line, are they best explained by one or two Gaussian distributions?". This question itself might not seem so useful. For one dimensional data, we can just plot them and have a look, can't we? The reason I find this question interesting is that is a) shows the fundamentals in hypothesis testing b) hypothesis testing in many more complicated models work just the same.

# First look at some examples

Let's plot a data set, would you think this could be best explained with one or two Gaussians?

and this one?

Probably, you guessed 2 for the first data set and 1 Gaussian for the second data set. We will try to quantify this intuition using probability theory. Once we understand these principles, we can transfer them to more complicated situations. Imagine for example that your data is high dimensional, or your data consist of time series. It would be way harder to use plotting and intuition to answer the hypotheses, but the math of probability theory will work just the same.

# Hypothesis testing according to probability theory.

In his book _probability theory_, Jaynes derives probablity from only first principles. Hypothesis testing forms an important part in his book. Jaynes argues that we can use Bayes rule just the same when it comes to hypothesis testing. Let's say we have two hypotheses, <img alt="$H_1$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/208fbcc5ce29722c2f701868ac31fc3c.svg" align="middle" width="20.141385pt" height="22.381919999999983pt"/> and <img alt="$H_2$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/912631c954499428b64ab8d828ac8cb6.svg" align="middle" width="20.141385pt" height="22.381919999999983pt"/>. Each hypothesis tries to explain the data in its own way. An example would be 

  * H1: the data can be explained by a straight line, H2: the data can be explained by a third order polynomial
  * H1: the data can be explained by a HMM. H2: the data can be explained by a LDS
  * H1: the data can be explained by one Gaussian. H2: the data can be explained by multiple Gaussians.

Then our posterior belief in a hypothesis follows from:

<img alt="$p(H|D) = \frac{p(D|H)p(H)}{p(D)}$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/d17badbe6e53532e9394b12cef908ede.svg" align="middle" width="150.73278pt" height="33.14091000000001pt"/>

Therefore, our relative belief in one hypothesis over the other follows from:

<img alt="$\frac{p(H_1|DI)}{p(H_2|DI)} = \frac{p(H_1|I)p(D|H_1I)p(D|I)}{p(H_2|I)p(D|H_2I)p(D|I)} = \frac{p(H_1|I)p(D|H_1I)}{p(H_2|I)p(D|H_2I)}$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/aaa902dc18f81da5e23150c327628260.svg" align="middle" width="347.99622pt" height="33.14091000000001pt"/>

We can equally express this in decibels:

<img alt="$10\log_{10} \frac{p(H_1|DI)}{p(H_2|DI)} =  10\log_{10} \frac{p(H_1|I)}{p(H_2|I)} + 10\log_{10} \frac{p(D|H_1I)}{p(D|H_2I)}$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/1703383162964466370a5928aad49569.svg" align="middle" width="379.59949499999993pt" height="33.14091000000001pt"/>

As we assign equal prior belief to the hypotheses, we focus on defining the likelihood of the data given one of the hypotheses.

# Likelihoods of the hypotheses

Our hypotheses in this problem are
  * H1: both data sets can be explained by one Gaussian
  * H2: either data set can be explained by its own Gaussian

How do we formulate a likelihood that translates the hypothesis into probabilities?

A Gaussian uses two parameters, the mean and variance. In order to marginalize over these parameters, we can use:

<img alt="$p(D|H_1) = \int_\theta p(D|H_1\theta)p(\theta|H_1) d\theta$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/0190702315018349c9dedf18c8d40b9e.svg" align="middle" width="240.339495pt" height="26.48447999999999pt"/>

Now for the <img alt="$p(D|H_1\theta)$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/f05f568dc5a587bc2dae27a14cacc78c.svg" align="middle" width="68.67448499999999pt" height="24.56552999999997pt"/> we can use a Gaussian: <img alt="$p(D|H_1\theta) = \prod_{i=1}^{2N}  \mathcal{N}(x_i|\mu, \sigma^2)$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/d5b28e836c5ba77173bc154656c46841.svg" align="middle" width="213.38344500000002pt" height="32.19743999999999pt"/>
For the prior, we use for both hypotheses: <img alt="$p(\mu, \sigma^2) = \mathcal{N}(\mu| 0, 5) \mathcal{L}(\sigma^2|1, 5)$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/ac465699730b27812e90bc85faa9e4b1.svg" align="middle" width="213.57649499999997pt" height="26.70657pt"/>

(Here, <img alt="$\mathcal{L}$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/47291815667dfe5994c54805102e144b.svg" align="middle" width="11.295570000000003pt" height="22.381919999999983pt"/> refers to the log normal distribution: <img alt="$\mathcal{L}(\sigma^2|1,5) = \frac{5}{\sigma^2 \sqrt{2\pi}} e^{\frac{-1}{2}\log^2(\frac{\sigma^2}{5})}$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/722d8ea65360d80830a8dc2125cbd672.svg" align="middle" width="214.60774499999997pt" height="37.953630000000004pt"/>)

To summarize:

<img alt="$p(D|H_1) = \int_{\mu, \sigma^2}  \mathcal{N}(\mu| 0, 5) \mathcal{L}(\sigma^2|1, 5) \prod_{i=1}^{2N}  \mathcal{N}(x_i|\mu, \sigma^2)d\mu d\sigma^2$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/39aa4c42f3a417fc3cdaf8002985c9b4.svg" align="middle" width="425.287995pt" height="32.19743999999999pt"/>

For hypothesis 2, we hypothesize that each data set is explained by its own Gaussian, therefore it follows that:
 
<img alt="$p(D|H_2) = \int_{\mu_1, \sigma_1^2, \mu_2, \sigma_2^2}  p(\mu_1, \sigma_1^2, \mu_2, \sigma_2^2) p(D_1|H_2\mu_1\sigma_1^2)p(D_2|H_2\mu_2\sigma_2^2)d\mu_1 d\sigma_1^2 d\mu_2 d\sigma_2^2$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/87d6ece124b336da596e1b20ffc3c3ee.svg" align="middle" width="581.521545pt" height="26.70657pt"/>
<img alt="$p(D|H_2) = \int_{\mu_1, \sigma_1^2, \mu_2, \sigma_2^2}  \mathcal{N}(\mu_1| 0, 5) \mathcal{L}(\sigma_1^2|1, 5)\mathcal{N}(\mu_2| 0, 5) \mathcal{L}(\sigma_2^2|1, 5) \prod_{i=1}^{N}  \mathcal{N}(x_i|\mu_1, \sigma_1^2) \prod_{i=N}^{2N}  \mathcal{N}(x_i|\mu_2, \sigma_2^2)d\mu_1 d\sigma_1^2 d\mu_2 d\sigma_2^2$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/7b7ecf632da6d4ed9be88866475c7a39.svg" align="middle" width="823.774545pt" height="32.19743999999999pt"/>

In the code, we approximate the integrals using Monte Carlo samling/estimation.

# Results
When we actually generate the data using two Gaussians, the result is

```
Hypothesis 1 is -636.3810052745309dB more likely than hypothesis 2
In other words, Hypothesis 1 is 2.3009091573828715e-64 more likely than hypothesis 2
```

When we actually generate data using one Gaussian, the result is

```
Hypothesis 1 is 32.102543545221735dB more likely than hypothesis 2
In other words, Hypothesis 1 is 1622.7602258374325 more likely than hypothesis 2
```

In other words, in both cases, the actually correct hypothesis comes out of our hypothesis test. 

In the next section, we provide some intuition

# Intuition
Initially, I was surprised that this method actually works. In all honesty, I started this project to form an argument against Jaynes' method. The following reasoning led me to believe that hypothesis testing would not work: _in hypothis 2, the model has twice as much parameters at its disposal. Of course hypothesis 2 is always going to win, because more parameters can strictly better fit the data_. 

After thes results, I should conclude that my reasoning was false. Let's explore what exactly is false about this reasoning. It is correct that more parameters will result in a strictly higher likelihood of the data given the parameters. However, in our fully probabilistic approach, we use not only the likelihood, but we calculate the marginal probability of the data. This marginal probability follows from multiplying the likelihood with our prior and integrate over all possible parameters. Exacly this prior and integration penalize a model with more parameters. We have two reasonings to arrive at this intuition

  1. When introducing more parameters, we must integrate over more dimensions. A probability distribution must sum to 1, so each dimension now has less density. As we integrate over more dimensions with less density, we penalize larger dimensional models.
  2. We can approximate the integral with the Laplace approximation around the most probable parameter. <img alt="$p(D|H) = \int_\theta p(D|H_1\theta)p(\theta|H_1)d\theta = p(D|H_1\theta_{mp})p(\theta_{mp}|H_1)\sigma_{mp}$" src="https://github.com/RobRomijnders/hypothesis_testing/blob/master/svgs/be691b1e04bac81686f7b5af1e95771b.svg" align="middle" width="444.84874499999995pt" height="26.48447999999999pt"/> In words, we approximate the integral by the likelihood at the most probable parameter, times the prior probability of the most probable parameter, times the uncertainty about the most probable parameter. Let's assume the uncertainty of the most probable parameter does not change much. Then an increase in the likelihood of a model with more parameters will be counteracted with a decrease of the prior probability of a model with more parameters:
    * The maximum likelihood of a model with more parameters will be higher, because with more parameters we can explain more fluctuations in the data
    * However, the prior probability will decrease in case of more parameters. A probability distribution must sum to one. Therefore, each individual probability density will be smaller in case of more parameters.

Personally, I find this a beautiful result. When taking a probabilistic approach, then Bayes rule seems to take care of everything. In this particular case, the marginalisation takes care of models with arbitrary dimensions. This intuition will carry over to more complicated models and hypotheses as well.

# Further reading

  * E.T. Jaynes's book "probability theory, the logic of science"
    * Jaynes discusses hypothesis testing in many chapters, most notably: chapters 4, 6 and 20
  * David Mackay's book "Information theory, inference and learning algorithms"
    * Mackay discusses hypothesis testing in chapter 28. Specifically, I used his Laplace approximation of equation 28.7

As always, I am curious to any comments and questions. Reach me at romijndersrob@gmail.com


