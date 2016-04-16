#!/usr/bin/env python

import perfectmath

"""
calculate all the perfect numbers below 1000000
source: https://nl.wikipedia.org/wiki/Perfect_getal (Dutch)
"""

i = 10000
x = 2

while x < i:
    if perfectmath.is_perfect_number(x):
        print x

    x += 1
