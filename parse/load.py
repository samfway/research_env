#!/usr/bin/env python
from __future__ import division

__author__ = "Sam Way"
__copyright__ = "Copyright 2017, The Clauset Lab"
__license__ = "BSD"
__maintainer__ = "Sam Way"
__email__ = "samfway@gmail.com"
__status__ = "Development"


import numpy as np
import cPickle as pickle
from os import path
from collections import Counter
from bs4 import BeautifulSoup


def parse_gs_page(faculty_record, gs_page, save_as=None):
    """ Parse citation data from an individual's faculty profile. """
    faculty_record['gs_info_loaded'] = False

    if not path.isfile(gs_page):
        return 

    raw_html = open(gs_page, 'rU').read()
    soup = BeautifulSoup(raw_html, 'html.parser')
    popup_hist = soup.find('div', id="gsc_md_hist")

    # Get the counts
    popups = popup_hist.find_all('a', attrs={"class":"gsc_g_a"})
    counts = [int(p.text) for p in popups]

    # Get the years
    popup_years = popup_hist.find('div', id="gsc_md_hist_b")
    popup_year_spans = popup_years.find_all('span', attrs={"class":"gsc_g_t"})
    years = [int(p.text) for p in popup_year_spans]

    # Get profile info
    profile_div = soup.find('div', id="gsc_prf_i")
    gs_name = profile_div.find('div', id="gsc_prf_in").text
    gs_info_lines = [p.text for p in profile_div.find_all('div', attrs={"class":"gsc_prf_il"})]

    # Info table
    gs_stats_table = {}
    stats_table = soup.find('table', id="gsc_rsb_st")
    rows = stats_table.find_all('tr')
    headers = [h.text.encode('utf8') for h in rows[0].find_all('th')]
    for row in rows[1:]:
        vals = [td.text.encode('utf8') for td in row.find_all('td')]
        gs_stats_table[vals[0]] = {}
        gs_stats_table[vals[0]][headers[1]] = int(vals[1])
        gs_stats_table[vals[0]][headers[2]] = int(vals[2])

    # Get citations for their top 100 papers
    paper_table = soup.find('table', id='gsc_a_t')
    papers = paper_table.find_all('tr', attrs={'class':'gsc_a_tr'})
    paper_years = []
    paper_citations = []
    for paper in papers:
        try:
            cites = int(paper.find('td', attrs={'class':'gsc_a_c'}).text)
            year = int(paper.find('td', attrs={'class':'gsc_a_y'}).text)

            paper_years.append(year)
            paper_citations.append(cites)
        except:
            pass    
    
    gs_info = {}
    gs_info['citation_traj'] = dict(zip(years, counts))
    gs_info['top_paper_year_cites'] = zip(paper_years, paper_citations)
    gs_info['stats_table'] = gs_stats_table
    gs_info['name'] = gs_name
    gs_info['info_lines'] = gs_info_lines
    
    if save_as is not None:
        pickle.dump(gs_info, open(save_as, "wb"))
    
    faculty_record['gs_info'] = gs_info
    faculty_record['gs_info_loaded'] = True


def load_gs_pkl(faculty_record, gs_pkl_file):
    """ Load GS information from pickle file. """
    faculty_record['gs_info_loaded'] = False
    try:
        gs_info = pickle.load(open(gs_pkl_file, "rb" )) 
        faculty_record['gs_info'] = gs_info
        faculty_record['gs_info_loaded'] = True
    except:
        pass


def load_gs_data(faculty_records, gs_dir, use_pickles=True, make_pickles=False):
    """
        Load Google Scholar citation data into faculty profiles.

        Inputs:
          faculty_records - parsed records of faculty
                   gs_dir - directory containing downloaded GS homepages
              use_pickles - use pre-made pickles of parsed GS information (faster)
             make_pickles - create pre-made pickles to make loading faster for next time.

        Expectations:
          - Faculty records will contain a "gs" field, indicating their GS profile ID.
          - The gs_dir directory will containing files named <GS_ID>.html, corresponding
            to each person's Scholar page.
          - The page will have been saved with the "Citation Indices" link clicked, and 
            the histogram of citations loaded.
    """

    count = 0
    total = 0

    for person in faculty_records:
        if 'gs' in person:
            gs_file = path.join(gs_dir, person['gs'] + '.html')
            gs_pkl_file = path.join(gs_dir, person['gs'] + '.pkl')
        
            if path.isfile(gs_pkl_file) and use_pickles and not make_pickles:
                load_gs_pkl(person, gs_pkl_file)
            else:  # Note, if the pickle file doesn't exist, we try to parse from HTML
                if not make_pickles:
                    gs_pkl_file = None  # Do not create a pickle file
                parse_gs_page(person, gs_file, save_as=gs_pkl_file)

            if person['gs_info_loaded']:
                count += 1
            total += 1

    print 'Loaded GS info for %d of %d records.' % (count, total)
            
