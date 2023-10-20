#!/usr/bin/env python3

import sys

fasta_file = sys.argv[1]

### read a fasta, store each record separately in a dictionary.
gene_dictionary = {}

with open(fasta_file, 'r') as fasta:
	for line in fasta:
		line = line.rstrip('\n')
		if '>' in line:
			header = line.lstrip('>')
			print(header)
		else:
			gene_dictionary[header]=line
			print(line)

print(gene_dictionary)
