#!/usr/bin/env python3 

# -------
# imports
# -------

import sys

from Collatz import cycle_length, collatz_print

# ------------
# write_sample
# ------------

def write_sample_out (w) :
    """
    prints original 4 inputs to win and solutions to wout
    w a writer to expected output file
    """
    
    collatz_print(w, 1, 10, 20)
    collatz_print(w, 100, 200, 125)
    collatz_print(w, 201, 210, 89)
    collatz_print(w, 900, 1000, 174)

# ------------
# main
# ------------

if __name__ == '__main__':
    write_sample_out (sys.stdout)