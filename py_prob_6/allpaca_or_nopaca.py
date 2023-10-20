#!/usr/bin/env python3
import re
import sys
#comparing and contrasting alpaca gene names based on GO terms. Yeah.
#Real excited here. #hashtagblessed

goterms_1 = sys.argv[1]
file_name1 =	sys.argv[1].rstrip('.tsv').lstrip('*/')

goterms_2 = sys.argv[2]
file_name2 = sys.argv[2].rstrip('.tsv').lstrip('*/')

goterms_3 = sys.argv[3]
file_name3 = sys.argv[3].rstrip('.tsv').lstrip('*/')

with open(goterms_1, 'r') as gene_ids1, open(goterms_2, 'r') as gene_ids2, open(goterms_3, 'r') as gene_ids3:
	set1 = set()
	set2 = set()
	set3 = set()
	for line in gene_ids1:
		if ' ' not in line:
			set1.add(line.rstrip('\n'))
	for line in gene_ids2:
		if ' ' not in line:
			set2.add(line.rstrip('\n'))
	for line in gene_ids3:
		if ' ' not in line:
			set3.add(line.rstrip('\n'))

print(f'{file_name1} genes not in {file_name2}: {set1 - set2}')

print(f'Genes that overlap between {file_name2} and {file_name3}: {set2&set3}')
