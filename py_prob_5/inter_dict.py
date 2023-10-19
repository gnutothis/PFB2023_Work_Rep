#!/usr/bin/env python3

import sys

fav_things = {'book' : 'Jitterbug Perfume', 'song' : 'Tom Petty - I Won\'t Back Down', 'tree' : 'Cedar'}

for i in fav_things:
  print(i)

print('Please select from the options above.')
x = input()

print(fav_things[x])

print('Great! Now we would like additional help from you in growing our list of favorite things. Please input the key or category you would like to add.')
key = str(input())

print('Now please enter the value for that key. E.g., what your favorite is.')
val = str(input())

fav_things[key] = val

print(fav_things)
