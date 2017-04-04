#!/usr/bin/env python
from __future__ import division

__author__ = "Sam Way"
__copyright__ = "Copyright 2017, The Clauset Lab"
__license__ = "BSD"
__maintainer__ = "Sam Way"
__email__ = "samfway@gmail.com"
__status__ = "Development"


# Standard imports
from samplotlib.util import *
from faculty_hiring.misc.util import *
from faculty_hiring.parse import faculty_parser, institution_parser, load

import numpy as np
import scipy as sp
import pandas as pd
import os
import palettable
from collections import Counter
from scipy import stats


# Seed the random number generator (#reproducibility)
np.random.seed(9)


# Project directory setup
PROJ_DIR = '/Users/samfway/Documents/Work/ClausetLab/Projects/research_env/'
FIGS_DIR = os.path.join(PROJ_DIR, 'figures')
DATA_DIR = os.path.join('/Users/samfway/Documents/Work/ClausetLab/Projects/faculty_hiring/data/')

BS_FACULTY_FILE = os.path.join(DATA_DIR, 'faculty_bs_CURRENT.txt') 
CS_FACULTY_FILE = os.path.join(DATA_DIR, 'faculty_cs_CURRENT.txt') 
HS_FACULTY_FILE = os.path.join(DATA_DIR, 'faculty_hs_CURRENT.txt') 

BS_INST_FILE = os.path.join(DATA_DIR, 'inst_bs_CURRENT.txt')
CS_INST_FILE = os.path.join(DATA_DIR, 'inst_cs_CURRENT.txt')
HS_INST_FILE = os.path.join(DATA_DIR, 'inst_hs_CURRENT.txt')

# Colors
ACCENT_COLOR_1 = np.array([176., 116., 232.]) / 255.
