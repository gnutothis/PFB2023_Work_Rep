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
			continue
		else:
			line_list = re.search(r'^(\w+\-?\w+|\w+\-?\w+\s\(\w+\))\s{2,}((\w*)\^\w*)$', line) #because I hate your guts, that's why. I hope this breaks. I hope you accidentally delete a character and save the file. I hope you go through a tithe of the pain I went through to make this in the first place.
			name = line_list.group(1)

			cut = line_list.group(2)

			cut_index = len(line_list.group(3))

			cut_seq = re.sub(r'\^', '', cut)
			
			enzyme_dictionary[name] = [cut_seq, cut_index, '' ]

#add regex to the enzyme dictionary in the empty third string entry.
nt_dictionary = {'A': '[A]', 'C': '[C]', 'G': '[G]', 'T': '[T]', 'U': '[U]', 'R': '[GA]', 'Y': '[CT]', 'K': '[GT]', 'M': '[AC]', 'S': '[GC]', 'W': '[AT]', 'B': '[GTC]', 'D': '[GAT]', 'H': '[ACT]', 'V': '[GCA]', 'N': '[AGCT]'}

for enzyme in enzyme_dictionary:
	char_list = list(enzyme_dictionary[enzyme][0])
	x = 0
	for char in char_list:
		enzyme_dictionary[enzyme][2] = enzyme_dictionary[enzyme][2] + nt_dictionary[char]
		char_list[x] = nt_dictionary[char]
		x += 1
		

#Fix the index issue! We need to add an '[GATC]' to the beginning of regex's with a cut index of zero, 
#and we need to add one to the end of cut indexes equal to the length of the binding sequence.
#This will ensure all sites are found and the sequence is properly broken into fragments when we run the script below this one.

#for enzyme in enzyme_dictionary:
#	if enzyme_dictionary[enzyme][1] == 0:
#		enzyme_dictionary[enzyme][1] += 1
#		enzyme_dictionary[enzyme][2] = '[GATC]' + enzyme_dictionary[enzyme][2]

#	if enzyme_dictionary[enzyme][1] == len(enzyme_dictionary[enzyme][0]):
#		print(enzyme_dictionary[enzyme][2])
#		enzyme_dictionary[enzyme][2] = enzyme_dictionary[enzyme][2] + '[GATC]'
#		print(enzyme_dictionary[enzyme][2])
#Now use both dictionaries in order to make a new one!	

fragment_dictionary = {} # f_d={'':{'':''}} store sequences for each enzyme
#with tabs delimiting cuts.

cut_data_dictionary = {} # c_d_d={'':{'':0,0,0,0}} store number of fragments,
#ave frag length, max frag and min frag length for each seq/enzyme combo.

for entry in sequence_dictionary:
	seq = sequence_dictionary[entry]
	fragment_dictionary[entry] = {}
	cut_data_dictionary[entry] = {}
#	print(seq)
	for enzyme in enzyme_dictionary:
#		print(f'enzyme{enzyme}')
# enzyme for the current loop. make four-integer list.
		cut_regex = enzyme_dictionary[enzyme][2]
#		print(f'{enzyme}\'s cut site: {cut_regex}')
		n = enzyme_dictionary[enzyme][1]
#		print(f'the index {n}')
		cut_set = set(re.findall(cut_regex, seq))
		if bool(cut_set) == True: #Making sure we don't make dictionary 
#entries for uncut sequences.
			cut_data_dictionary[entry][enzyme] = [0,0,0,0] #assign sequence and
# enzyme for the current loop. make four-integer list.
			fragment_dictionary[entry][enzyme] = seq
			c_dict = cut_data_dictionary[entry][enzyme]
			f_dict = fragment_dictionary[entry][enzyme]
			for i in cut_set:
				f_dict = re.sub(i ,f'{i[0:n]}\t{i[n:]}', f_dict)
			fragments = f_dict.split('\t')
			fragments = [len(x) for x in fragments]
			c_dict = [len(fragments), sum(fragments)/len(fragments), max(fragments), min(fragments)]
				
			print(c_dict)
#			c_dict[0] = len(
			break
 
		
#		finder = re.findall(, seq)

#		for i in finder:

#			sequence_dictionary[seq] = re.sub(i, f'{[0:1]}\t{i[1:]}', seq)
#			print(seq)

