#!/usr/bin/env python3

dna_full = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTTCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGGGGGGGGGGGG'

dna = dna_full[99:200]

ants = dna.count('A') + dna.count('T') + dna.count('a') + dna.count('t')

gncs = dna.count('G') + dna.count('C') + dna.count('g') + dna.count('c')

gs = dna.count('G') + dna.count('g')

ratio = ants/(gncs + ants)

print(dna)

print(ants)

print(gncs)

print(ratio)

print(gs)

r_dna = dna[::-1]

print(r_dna)

rc_dna = r_dna.replace('A','1')
print(rc_dna)
rc_dna = rc_dna.replace('T', 'A')
print(rc_dna)
rc_dna = rc_dna.replace('C', '2')
print(rc_dna)
rc_dna = rc_dna.replace('G', 'C')
print(rc_dna)
rc_dna = rc_dna.replace('a','1')
print(rc_dna)
rc_dna = rc_dna.replace('t', 'A')
print(rc_dna)
rc_dna = rc_dna.replace('c', '2')
print(rc_dna)
rc_dna = rc_dna.replace('g', 'C')
print(rc_dna)
rc_dna = rc_dna.replace('1', 'T')
print(rc_dna)
rc_dna = rc_dna.replace('2', 'G')

print(rc_dna)
print(len(rc_dna))

print(f'''
Original Sequence   5\'{dna}3\'
Complement          5\'{r_dna}3\'
Reverse Complement  5\'{rc_dna}3\'''')
