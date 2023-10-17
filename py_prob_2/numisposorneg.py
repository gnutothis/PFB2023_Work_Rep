#!/usr/bin/env python3

import sys

num1 = float(sys.argv[1])

print(num1)

if num1 > 0:
  print('positive')

  if num1 < 50:
    print(num1 , 'is smaller than 50.')
    
    if num1 % 2 == 0:
      print(num1 , 'is an even number that is smaller than 50.')

elif num1 < 0:
  print('negative')

elif num1 == 0:
  print('number is equal to zero.')

