#!/usr/bin/env python3

import sys

fav_query = sys.argv[1]

fav_things = {'book' : 'Jitterbug Perfume', 'song' : 'Tom Petty - I Won\'t Back Down', 'tree' : 'Cedar'}

print(fav_things['book'])

fav_thing = 'book'

print(fav_things[fav_thing])

print(fav_things['tree'])

for i in fav_things:
  print(fav_things[i])

print(fav_things[fav_query])
