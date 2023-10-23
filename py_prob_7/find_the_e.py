#!/usr/bin/env python3

import sys
import re

#Search for every cut site found in the bionet collection of restriction 
#enzymes in a user provided FASTA file. For each sequence report the
#sequence id
#enzyme name
#number of fragments
#average fragment length
#max fragment length
#min fragment length

#fasta: make dictionary for each line, making each second set 

#fasta parser:

fasta = sys.argv[1]

enzymes = sys.argv[2]


sequence_dictionary = {}
enzyme_dictionary = {}

line_number = 0
with open(enzymes, 'r') as cut_sites:
	for line in cut_sites:
		line_number += 1
		line = line.rstrip()
		if '^' not in line:
			grabby = 'placeholder'
		else:

			line_list = re.search(r'^(\w+\-?\w+|\w+\-?\w+\s\(\w+\))\s{2,}((\w*)\^\w*)$', line) #because I hate your guts, that's why. I hope this breaks. I hope you accidentally delete a character and save the file. I hope you go through a tithe of the pain I went through to make this in the first place.
			name = line_list.group(1)

			cut = line_list.group(2)

			if 'E' in cut:
				print(line, "on line", line_number)
#for seq in sequence_dictionary:
	

#finder = re.findall(r'[G].{2}[G]', seq)
#finder
#for i in finder:
#	seq = re.sub(i, f'{i[0:1]}\t{i[1:]}', seq)
#	print(seq)

