#!/usr/bin/env python3

import sys

#defining variables from sys.argvs in the commandline
name = sys.argv[1]
fav_color = sys.argv[2]
fav_activity = sys.argv[3]
fav_animal = sys.argv[4]

#using f\"\" strings to call sys.argv variables set above.
print(f"My name: {name}")

print(f"My favority color: {fav_color}")

print(f"My favority leisure activity: {fav_activity}")

print(f"My favority animal: {fav_animal}")

