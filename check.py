from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
import numpy as np
from scipy.stats import gamma, norm
import matplotlib.pyplot as plt


def function(x):
    return (x > 4) * np.exp(- (x**2) / 2. + ((x - 5)**2) / 2.)

samples = np.random.normal(5, 1, size=100)
values = function(samples)