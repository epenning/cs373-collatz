#!/usr/bin/env python3 

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# list cache of calculated cycle lengths for each number 1 to 1000000
cycle_lengths = [0] * 1000000

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
    # optimization, top half of range cycle lengths > bottom half
    if i < j/2 + 1 :
        i = j//2 + 1
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
    # check if cycle length of n is already known in cache
    if cycle_lengths[n] :
        return cycle_lengths[n]
    count = 1
    m = n
    while m > 1 :
        if m % 2 == 1 :
            # m is odd
            # optimization, resulting number always even
            #so combine two steps
            m = m + (m >> 1) + 1
            count += 2
        else :
            # m is even
            m = m//2
            count += 1
        # check if cycle length of m is already known in cache
        if m < 1000000 and cycle_lengths[m] :
            count = cycle_lengths[m] + count - 1
            break
    assert count > 0
    # save cycle length of n in cache
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
        # pass to collatz_eval so first number < second to avoid duplicate code
        v = collatz_eval(i, j) if  ( i < j )  else collatz_eval(j, i)
        collatz_print(w, i, j, v)
        