#!/usr/bin/env python3

eco_site = 'GAATTC'
eco_siter = 'CTTAAG'

dna = 'AACGTACGACATTGCAGCTGAATTCACGTGTACGACTGACGTAATGCCTTAAGGACCAGTAAAATGAGACCAGTA'

site_locs = []

dna1 = dna

dna2 = dna

while dna1.find('GAATTC') >0:
  site_locs.append(dna1.find('GAATTC'))
  dna1 = dna1[(site_locs[-1]+1):]

while dna2.find('CTTAAG') >0:
  site_locs.append(dna2.find('CTTAAG'))
  dna2 = dna2[(site_locs[-1]+1)]



print('There are EcoRI cut sites at the following locations:' ,  site_locs)
