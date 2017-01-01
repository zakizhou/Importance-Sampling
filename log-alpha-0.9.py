from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import numpy as np
import pandas as pd


alphas = [0.9]
scale = 1
sizes = [1000, 100000]

dataframe = pd.DataFrame(columns=["alpha", "samples", "theta_2_exceptation", "theta_2_std"])


def function(x):
    return np.log(x)


for alpha in alphas:
    for size in sizes:
        samples = function(np.random.gamma(shape=alpha, scale=scale, size=size))
        dataframe.loc[len(dataframe)] = [alpha, size, samples.mean(), np.sqrt(samples.var() / size)]
        dataframe['samples'] = dataframe['samples'].astype(int)
pivot = dataframe.pivot_table(index=["alpha", "samples"]).T