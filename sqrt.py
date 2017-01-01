from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import numpy as np
import pandas as pd


alphas = [0.9, 0.01]
beta = 0.5
scale = 1
sizes = [1000, 100000]
stats = dict()
mean_and_var = []

dataframe = pd.DataFrame(columns=["alpha", "samples", "theta_1_exceptation", "theta_1_std"])


def function(x):
    return np.sqrt(x)


for alpha in alphas:
    for size in sizes:
        samples = function(np.random.gamma(shape=alpha, scale=scale, size=size))
        dataframe.loc[len(dataframe)] = [alpha, size, samples.mean(), np.sqrt(samples.var() / size)]
        dataframe['samples'] = dataframe['samples'].astype(int)
pivot = dataframe.pivot_table(index=["alpha", "samples"]).T