#!/usr/bin/env python3 

# -------
# imports
# -------

import sys

from random import randint


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

def write_sample (w) :
    """
    prints original 4 inputs to w
    w a writer to input file
    """
    collatz_print_input(w, 1, 10)
    collatz_print_input(w, 100, 200)
    collatz_print_input(w, 201, 210)
    collatz_print_input(w, 900, 1000)

# ------------
# write_random
# ------------

def write_random (w, n) :
    """
    prints n random ranges to w
    w a writer to input file
    n the number of ranges to print
    """
    for i in range(0, n) :
        collatz_print_input(w, randint(1,1000000), randint(1,1000000))

# ------------
# write_random_limited
# ------------

def write_random_limited (w, n, limit) :
    """
    prints n random ranges to w with a range size limit
    w a writer to input file
    n the number of ranges to produce
    limit half of the maximum size of each range produced
    """
    for i in range(0, n) :
        first = randint(1,1000000)
        second = first + randint(-limit, limit)
        if second < 1 :
            second = 1
        elif second > 1000000 :
            second = 1000000
        collatz_print_input(w, first, second)

# ------------
# main
# ------------

if __name__ == '__main__':
    write_sample (sys.stdout)
    write_random(sys.stdout, 10)
    write_random_limited(sys.stdout, 20, 100000)
    write_random_limited(sys.stdout, 30, 10000)
    write_random_limited(sys.stdout, 40, 100)
    write_random_limited(sys.stdout, 50, 10)
    