#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    increases = 0
    prev = None
    for line in f.readlines():
        measurement = int(line.strip())
        increases = increases + 1 if prev != None and prev < measurement else increases
        prev = measurement
    print(increases)
