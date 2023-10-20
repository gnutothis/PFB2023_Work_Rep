#!/usr/bin/env python3

import sys

#open fastq, run through each line. Count number of lines 
#count number of characters. Report: totnum lines, char, ave line lengt

fastq_file = sys.argv[1]

line_number_list = []

number_of_lines = 0

number_of_chars = 0 

with open(fastq_file, 'r') as fqf:
	for line in fqf:
		number_of_lines += 1
		current_char_number = len(line)
		number_of_chars += current_char_number
	print(f'There are {number_of_lines} lines in this file')
	print(f'There are {number_of_chars} total characters in this file')
	print(f'There are, on average, {number_of_chars/number_of_lines} characters per line')

