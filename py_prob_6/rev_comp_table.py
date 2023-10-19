#!/usr/bin/env python3

import sys

fastq = sys.argv[1] #Var used to read in file

rc_fastq = sys.argv[2] #User input name of new file

with open(fastq, 'r') as seqs_table, open(rc_fastq, 'w') as rev_seqs_table:

	for line in seqs_table: #Testing to see if can index 'line' e.g. line[0
		print(line)
		line_list = line.split('\t') #split header and sequence into list
		sequence = line_list[1].rstrip()
		flipped_seq = ''
		for i in sequence:
			if i == 'A':
				flipped_seq = flipped_seq + 'T'
			elif i == 'T':
				flipped_seq = flipped_seq + 'A'
			elif i == 'C':
				flipped_seq = flipped_seq + 'G'
			elif i == 'G':
				flipped_seq = flipped_seq + 'C'
			else:
				flipped_seq = flipped_seq + i
				print('''This script hit a letter that wasn\'t T A G or C. 
It was added as is to the new line.''')
		rev_seqs_table.write(f'{line_list[0]}\t{flipped_seq}\n')
