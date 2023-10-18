#!/usr/bin/env python3

dna_full = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTTCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGGGGGGGGGGGG'

dna = dna_full[99:200]

ants = dna.count('A') + dna.count('T') + dna.count('a') + dna.count('t')

gncs = dna.count('G') + dna.count('C') + dna.count('g') + dna.count('c')

ratio = ants/(gncs + ants)

print(dna)

print(ants)

print(gncs)

print(ratio)
