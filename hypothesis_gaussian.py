import numpy as np
from scipy.stats import multivariate_normal, lognorm
from scipy.special import logsumexp

# Hypothesis 1: all the data comes from the same data source (1)
# Hypothesis 2: the first half comes from data source (1), the second half comes from data source (2)

"""Data simulation"""
# Define some parameters to simulate data generation
mu1 = 2.0
sigma1 = 1.0

mu2 = -2.0
sigma2 = 1.0

# Data option 1: same data source (1)
# Data option 2: two different data sources (1, 2)
data_option_2 = False
N = 100
data1 = mu1 + sigma1 * np.random.randn(N, )

if data_option_2:
    data2 = mu2 + sigma2 * np.random.randn(N, )
else:
    data2 = mu1 + sigma1 * np.random.randn(N, )

data_combined = np.concatenate((data1, data2), axis=0)

"""Model selection / Hypothesis tesing"""
# Now calculate
# log posterior_odds = log prior_odds + log likelihood_ratio
#  - log posterior_odds         = log p(H1|DI)/P(H2|DI)
#  - log prior_odds             = log P(H1|I)/P(H2I)
#  - log likelihood_ratio       = log P(D|H1I)/P(D|H2I)
# The variable I represents all our background information

# Let's assume our prior belief in both hypotheses is equal: P(H1|I) = P(H2I)
# Now log_prior_odds is then log(1) = 0
log_prior_odds = 0

# Calculate log P(D|HI) by integrating out theta in p(Dtheta|HI)=p(D|HI)p(theta|HI)
mu_prior = multivariate_normal(mean=0., cov=5.)
spread_prior = lognorm(1.0, scale=5.0)

num_mc_samples = 1000
log_p_D_given_H1I = []
for i in range(num_mc_samples):
    mu_sample = mu_prior.rvs()
    spread_sample = spread_prior.rvs()
    log_p_D_given_H1I.append(np.sum(multivariate_normal(mean=mu_sample, cov=spread_sample).logpdf(data_combined)))
# In the next line, we do a log-sum-exp over our list.
#  - The outer log puts the evidence on log scale
#  - The sum is over the MC samples
#  - The exp cancels the log in the distribution.logpdf()
log_p_D_given_H1I = logsumexp(log_p_D_given_H1I) - np.log(num_mc_samples)

# Calculate log P(D|H2I)
mu_prior = multivariate_normal(mean=[0., 0.], cov=[[5., 0.], [0., 5.]])
spread_prior = lognorm([1., 1.], scale=[5.0, 5.0])

log_p_D_given_H2I = []
for i in range(num_mc_samples):
    mu_sample = mu_prior.rvs()
    spread_sample = spread_prior.rvs()
    log_p_D_given_H2I.append(np.sum(multivariate_normal(mean=mu_sample[0], cov=spread_sample[0]).logpdf(data1)) +
                               np.sum(multivariate_normal(mean=mu_sample[1], cov=spread_sample[1]).logpdf(data2)))
# In the next line, we do a log-sum-exp over our list.
#  - The outer log puts the evidence on log scale
#  - The sum is over the MC samples
#  - The exp cancels the log in the distribution.logpdf()
log_p_D_given_H2I = logsumexp(log_p_D_given_H2I) - np.log(num_mc_samples)

# Calculate the log_likelihood ratio
log_likelihood_ratio = log_p_D_given_H1I - log_p_D_given_H2I

# So to conclude, our log posterior odds is
log_posterior_odds = log_prior_odds + log_likelihood_ratio

print(f'Hypothesis 1 is {10 * (log_posterior_odds / np.log(10))}dB more likely than hypothesis 2')

print(f'In other words, Hypothesis 1 is {np.exp(log_posterior_odds)} more likely than hypothesis 2')
