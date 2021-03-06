from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import numpy as np
from scipy import special
import pandas as pd


alpha = 0.01
scale = 1


def function(x, beta):
    return np.log(x) / special.gamma(alpha) * special.gamma(beta) * np.power(x, alpha - beta)

# betas = np.concatenate([np.linspace(0.015, 0.019, 5),
#                         np.linspace(0.02, 0.1, 9)])
betas = np.linspace(0.02, 0.1, 9)
sizes = [1000, 100000]
stats = dict()
for beta in betas:
    mean_and_var = []
    for size in sizes:
        means_and_vars = []
        for _ in range(40):
            samples = np.random.gamma(shape=beta, scale=scale, size=size)
            simulations = function(samples, beta)
            means_and_vars.append([simulations.mean(), np.sqrt(simulations.var() / size)])
        mean_and_var.append(np.array(means_and_vars).mean(axis=0))
    stats[beta] = mean_and_var
dataframe = pd.DataFrame(stats).T
dataframe.columns = sizes
