#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    measurements = [int(x.strip()) for x in f.readlines()]

increases = 0
prev_window_sum = None
for i in range(2, len(measurements)):
    window_sum = sum(measurements[i - 3 : i])
    increases = increases + 1 if prev_window_sum != None and prev_window_sum < window_sum else increases
    prev_window_sum = window_sum

print(increases)
