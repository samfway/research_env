#!/usr/bin/env python

__author__ = "Sam Way"
__copyright__ = "Copyright 2014, The Clauset Lab"
__license__ = "BSD"
__maintainer__ = "Sam Way"
__email__ = "samfway@gmail.com"
__status__ = "Development"


import argparse
import string
import re
from faculty_hiring.parse.faculty_parser import parse_faculty_records


def interface():
    args = argparse.ArgumentParser()
    args.add_argument('-o', '--output-file', help='Output file')
    args.add_argument('-i', '--faculty-file', help='Faculty profiles')
    args.add_argument('-g', '--gs-file', help='Google scholar TSV')  # Name\tPlace\tGS_ID
    args = args.parse_args()
    return args


if __name__=="__main__":
    args = interface()
    
    # Load all faculty 
    faculty = [f for f in parse_faculty_records(open(args.faculty_file, 'rU'))]
    
    # Load records to be linked
    to_update = {}
    for line in open(args.gs_file,'rU'):
        pieces = line.strip().split('\t')
        if len(pieces) == 3:
            to_update[pieces[0]] = pieces[1:]

    # Figure out the index of each person
    index_ids = {}
    for f, person in enumerate(faculty):
        if person.facultyName in to_update:
            if to_update[person.facultyName][0] == person.place:
                index_ids[f] = to_update[person.facultyName][1]

    assert(len(index_ids) == len(to_update))

    # Slide the Google Scholar ID in before the email 
    output = open(args.output_file, 'w')
    current_record = -1
    add_this = None
    for line in open(args.faculty_file, 'rU'):
        if line.startswith('# facultyName'):
            current_record += 1
            if current_record in index_ids:
                add_this = index_ids[current_record]
        elif line.startswith('# email'):
            if add_this is not None:
                output.write('# gs          : %s\n' % (add_this))
                add_this = None
        output.write(line)
    output.close()
