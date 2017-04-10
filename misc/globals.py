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
from research_env.misc.util import *

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
FIGS_DIR = os.path.join(PROJ_DIR, 'notebooks/figures/')
DATA_DIR = os.path.join('/Users/samfway/Documents/Work/ClausetLab/Projects/faculty_hiring/data/')
DBLP_DIR = '/Users/samfway/Documents/Work/ClausetLab/projects/faculty_hiring/data/profiles_DBLP_Nov16/'

BS_FACULTY_FILE = os.path.join(DATA_DIR, 'faculty_bs_CURRENT.txt') 
CS_FACULTY_FILE = os.path.join(DATA_DIR, 'faculty_cs_CURRENT.txt') 
HS_FACULTY_FILE = os.path.join(DATA_DIR, 'faculty_hs_CURRENT.txt') 

BS_INST_FILE = os.path.join(DATA_DIR, 'inst_bs_CURRENT.txt')
CS_INST_FILE = os.path.join(DATA_DIR, 'inst_cs_CURRENT.txt')
HS_INST_FILE = os.path.join(DATA_DIR, 'inst_hs_CURRENT.txt')


# Colors
ACCENT_COLOR_1 = np.array([176., 116., 232.]) / 255.

# Load the standard set of files
# Business
bs_inst = institution_parser.parse_institution_records(open(BS_INST_FILE, 'rU'))
all_bs_faculty = [person for person in faculty_parser.parse_faculty_records(open(BS_FACULTY_FILE, 'rU'),
                                                                            school_info=bs_inst,
                                                                            ranking='pi')]
bs_faculty = load.load_assistant_profs(open(BS_FACULTY_FILE, 'rU'), 
                                       school_info=bs_inst, 
                                       ranking='pi', 
                                       year_start=1970, 
                                       year_stop=2012)
# bs_faculty_df = convert_faculty_list_to_df(bs_faculty)

# Computer Science
cs_inst = institution_parser.parse_institution_records(open(CS_INST_FILE, 'rU'))
all_cs_faculty = [person for person in faculty_parser.parse_faculty_records(open(CS_FACULTY_FILE, 'rU'),
                                                                            school_info=cs_inst,
                                                                            ranking='pi')]
cs_faculty = load.load_assistant_profs(open(CS_FACULTY_FILE, 'rU'), 
                                       school_info=cs_inst, 
                                       ranking='pi', 
                                       year_start=1970, 
                                       year_stop=2012)
# cs_faculty_df = convert_faculty_list_to_df(cs_faculty)

# History
hs_inst = institution_parser.parse_institution_records(open(HS_INST_FILE, 'rU'))
all_hs_faculty = [person for person in faculty_parser.parse_faculty_records(open(HS_FACULTY_FILE, 'rU'),
                                                                            school_info=hs_inst,
                                                                            ranking='pi')]
hs_faculty = load.load_assistant_profs(open(HS_FACULTY_FILE, 'rU'), 
                                       school_info=hs_inst, 
                                       ranking='pi', 
                                       year_start=1970, 
                                       year_stop=2012)
# hs_faculty_df = convert_faculty_list_to_df(hs_faculty)
