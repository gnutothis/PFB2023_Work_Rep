#!/usr/bin/env python3

import sys
import re

bionet = sys.argv[1]
x = 0
with open(bionet, 'r') as enzymes:
	for line in enzymes:
		x+=1
		if 'E' in line:
			print(line, x)
