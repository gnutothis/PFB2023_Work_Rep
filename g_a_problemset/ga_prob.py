#!/usr/bin/env python3

#Using ecoli-0.25.contigs.fasta, write a script that reports:

#The number of contigs in the file
#The shortest contig.
#The longest contig.
#Total contig length.
#The L50 size
#The N50 size

from Bio import SeqIO
A = 0
a = 0
N = 0
contigs = []
for seq in SeqIO.parse('GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna','fasta'):
	contigs = contigs + [len(seq)]
	for i in seq:
		if i == 'a' or 'c' or 't' or 'g':
			a += 1
		elif i == 'A' or 'C' or 'T' or 'G':
			A += 1
		elif i == 'N':
			N += 1
n50 = (sum(contigs)/2)
x = 0 #L50 counter
y = 0 #N50 counter
sorted_contigs = sorted(contigs, reverse=True)
for i in sorted_contigs:
	x += 1
	y += i
	if y >= n50:
		break
	else:
		continue
l50 = x

print(f'''
number of contigs		{len(contigs)}
shortest contig			{min(contigs)}
longest contig			{max(contigs)}
total length			{sum(contigs)}
L50				{l50}
N50				{n50}

number of ATCG		{A}
number of atcg		{a}
proportion of gaps {N/sum(contigs)}
''')













