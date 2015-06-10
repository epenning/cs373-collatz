#!/usr/bin/env python3 

# -------
# imports
# -------

import sys

from Collatz import cycle_length

# ------------
# print_cycle_lengths
# ------------

def print_cycle_lengths (w) :
    for n in range(1,1000000) :
        w.write(str(cycle_length(n)) + "\n")

# ------------
# main
# ------------

if __name__ == '__main__':
    print_cycle_lengths (sys.stdout)
    
    