#!/usr/bin/env python3 

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

import sys

# list cache of calculated cycle lengths for each number 1 to 1000000
cycle_lengths = [None] * 1000000

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0 and j > 0
    maximum = 1
    for n in range(i, j+1) :
        cycle = cycle_length(n)
        if cycle > maximum:
            maximum = cycle
    assert maximum > 0
    return maximum

# ------------
# cycle_length
# ------------

def cycle_length (n) :
    """
    n the number for which to find the cycle length
    return the cycle length of n
    """
    assert n > 0
    if cycle_lengths[n] != None :
        return cycle_lengths[n]
    count = 1
    while n > 1 :
        if n % 2 == 1 :
            # n is odd
            n = 3*n + 1
        else :
            # n is even
            n = n//2
        count += 1
    assert count > 0
    cycle_lengths[n] = count
    return count

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v = collatz_eval(i, j) if  ( i < j )  else collatz_eval(j, i)
        collatz_print(w, i, j, v)
        
# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)
