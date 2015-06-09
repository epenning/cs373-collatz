'''
Created on Jun 9, 2015

@author: Erin
'''

import sys

from Collatz import cycle_length, collatz_print


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

def write_sample (win, wout) :
    """
    prints original 4 inputs to win and solutions to wout
    win a writer to input file
    wout a writer to expected output file
    """
    collatz_print_input(win, 1, 10)
    collatz_print_input(win, 100, 200)
    collatz_print_input(win, 201, 210)
    collatz_print_input(win, 900, 1000)
    
    collatz_print(wout, 1, 10, 20)
    collatz_print(wout, 100, 200, 125)
    collatz_print(wout, 201, 210, 89)
    collatz_print(wout, 900, 1000, 174)

if __name__ == '__main__':
    write_sample (sys.stdin, sys.stdout)