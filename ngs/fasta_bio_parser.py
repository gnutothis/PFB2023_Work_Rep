#!/user/bin/env python3

#seq name, description, sequence

from Bio import SeqIO

x = 0
for seq_record in SeqIO.parse("Ecoli.fasta", "fasta"):
	x +=1
	print('ID', seq_record.id)
	print('Sequence', seq_record.seq)

# # sequences
# # nucleotides
# ave length seq
# shortest seq length
# ave GC content
# highest GC content
# lowest GC content
	print(
print	('Number of seq', x)
