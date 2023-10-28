#!/usr/bin/env python3

import sys
from Bio import SeqIO

file = sys.argv[1]
output = sys.argv[2]

for seq_record in SeqIO.parse(sys.argv[1], 'fastq'):

    print(seq_record.format('qual'))
    input()
