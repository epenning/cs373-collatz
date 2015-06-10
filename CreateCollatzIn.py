#!/usr/bin/env python3 

# -------
# imports
# -------

import sys

from Collatz import cycle_length


# -------------
# collatz_print_input
# -------------

def collatz_print_input (w, i, j) :
    """
    print two ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + "\n")

# ------------
# write_sample
# ------------

def write_sample_in (w) :
    """
    prints original 4 inputs to win and solutions to wout
    win a writer to input file
    wout a writer to expected output file
    """
    collatz_print_input(w, 1, 10)
    collatz_print_input(w, 100, 200)
    collatz_print_input(w, 201, 210)
    collatz_print_input(w, 900, 1000)

# ------------
# main
# ------------

if __name__ == '__main__':
    write_sample_in (sys.stdout)
    
    