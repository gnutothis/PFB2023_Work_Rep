#!/usr/bin/env python3

import sys

# script will: read in a file consisting of a single line of nucleotides,
# make a set containing the unique nuceotide character,
# make a dictionary with each key nucleotide corresponding with the number of that nucleotide in the list,
# write a new file with this dictionary.


# sys.argv[1] is the data file, sys.argv[2] is the new dictionary file, sys.argv[3] is the new table file
read_in_nucleotides = sys.argv[1]

write_out_dict = sys.argv[2]

write_table = sys.argv[3]

dictionary = {}

with open(read_in_nucleotides, 'r') as dna_string, open(write_out_dict, 'w') as new_dict, open(write_table, 'w') as new_table:
  
	read_dna_string = dna_string.read() #Changed this so I can make usable_dna_string stripped of the end newline char.
	usable_dna_string = read_dna_string.rstrip('\n')

	uniq_nucs = set(usable_dna_string) #can't just use dna_string. Have to actually read in the file. Currently only opened for reading.
	
	for i in uniq_nucs:
		
		x = usable_dna_string.count(i)  #using usable_... because dna_string is a textwrapper

		dictionary[i] = int(x)

	print(dictionary) #This will print the dictionary, complete with curly braces

	new_dict.write(str(dictionary)) #This will make a file out of the dict, complete with curly braces.

	for i in dictionary:
		new_table.write(f'{i}\t{dictionary[i]}\n') #Had lots of errors, then got this figured out, but it only printed \'i\', go figure. Added the fstring so a tab separated the i and the parsing of the key.
		

