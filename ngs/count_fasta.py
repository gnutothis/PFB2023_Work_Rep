#!/usr/bin/env python3
x = 0
with open("Ecoli.fasta", 'r') as file:
		for line in file:
			if ">" not in line:
				x += len(line)
			elif x == 0 and ">" in line:
				continue
			elif x>0 and ">" in line:
				print(x)
				break
