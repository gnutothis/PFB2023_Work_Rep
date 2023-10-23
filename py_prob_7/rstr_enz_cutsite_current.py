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

with open(fasta, 'r') as seq_file:
	for line in seq_file:
		if '>' in line:
			line = line.lstrip('>').rstrip() #remove flanking '>' and '\n'
			line = line.split()[0] #keep gene ID (first portion of line) as line variable
			sequence_dictionary[line] = '' #add gene ID to dictionary
			key = line
		else:
			line = line.rstrip() #remove '\n'
			sequence_dictionary[key] = sequence_dictionary[key] + line #append line of sequence to dictionary under the current key

with open(enzymes, 'r') as cut_sites:
	for line in cut_sites:
		line = line.rstrip()
		if '^' not in line:
			print('skip!')
		else:
			line_list = re.search(r'^(\w+\-?\w+|\w+\-?\w+\s\(\w+\))\s{2,}((\w*)\^\w*)$', line) #because I hate your guts, that's why. I hope this breaks. I hope you accidentally delete a character and save the file. I hope you go through a tithe of the pain I went through to make this in the first place.
			name = line_list.group(1)

			cut = line_list.group(2)

			cut_index = len(line_list.group(3))

			cut_seq = re.sub(r'\^', '', cut)
			
			enzyme_dictionary[name] = [cut_seq, cut_index]

#add regex to the enzyme dictionary
nt_dictionary = {}

for enzyme in enzyme_dictionary:
		char_list = enzyme[0].split('')


#Now use both dictionaries in order to make a new one!
for seq in sequence_dictionary:
	

#finder = re.findall(r'[G].{2}[G]', seq)
#finder
#for i in finder:
#	seq = re.sub(i, f'{i[0:1]}\t{i[1:]}', seq)
#	print(seq)

