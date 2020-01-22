#!/usr/bin/python3
def number_of_lines(filename=""):
    ''' function that returns the number of lines of a text file '''
    with open(filename) as f:
        for i, line in enumerate(f):
                pass
    return i + 1