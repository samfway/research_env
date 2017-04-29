#!/usr/bin/env python
from __future__ import division

__author__ = "Sam Way"
__copyright__ = "Copyright 2017, The Clauset Lab"
__license__ = "BSD"
__maintainer__ = "Sam Way"
__email__ = "samfway@gmail.com"
__status__ = "Development"


import numpy as np
from scipy import stats


# DBLP Adjustments from "The misleading narrative..." 
GROW_SLOPE = 0.131873
GROW_INTER = -258.286620
DBLP_SLOPE = 0.010588
DBLP_INTER = -20.434804

grow_adjust = lambda x: (2011*GROW_SLOPE+GROW_INTER)/(x*GROW_SLOPE+GROW_INTER)  # GROW correction
dblp_adjust = lambda x: (2011*DBLP_SLOPE+DBLP_INTER)/(x*DBLP_SLOPE+DBLP_INTER)  # DBLP correction

adjust = lambda x: (grow_adjust(x) * dblp_adjust(x))

def JSD(P, Q, base=2):
    """
        Jensen-Shannon divergence (symmetrized version of KL div.)

        Implementation built up from definition of KL divergence:
        https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence
        https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

        Code from:
        http://stackoverflow.com/questions/15880133/jensen-shannon-divergence
    """ 

    _P = P / np.linalg.norm(P, ord=1)
    _Q = Q / np.linalg.norm(Q, ord=1)
    _M = 0.5 * (_P + _Q)
    return 0.5 * (stats.entropy(_P, _M, base=base) + stats.entropy(_Q, _M, base=base))
