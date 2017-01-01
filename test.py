from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from scipy import special

alpha = 0.01
delta = 1e-5
print((special.gamma(alpha + delta) / special.gamma(alpha) - 1) / delta)