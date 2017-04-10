#!/usr/bin/env python
from __future__ import division

__author__ = "Sam Way"
__copyright__ = "Copyright 2017, The Clauset Lab"
__license__ = "BSD"
__maintainer__ = "Sam Way"
__email__ = "samfway@gmail.com"
__status__ = "Development"


# DBLP Adjustments from "The misleading narrative..." 
GROW_SLOPE = 0.131873
GROW_INTER = -258.286620
DBLP_SLOPE = 0.010588
DBLP_INTER = -20.434804

grow_adjust = lambda x: (2011*GROW_SLOPE+GROW_INTER)/(x*GROW_SLOPE+GROW_INTER)  # GROW correction
dblp_adjust = lambda x: (2011*DBLP_SLOPE+DBLP_INTER)/(x*DBLP_SLOPE+DBLP_INTER)  # DBLP correction

adjust = lambda x: (grow_adjust(x) * dblp_adjust(x))

