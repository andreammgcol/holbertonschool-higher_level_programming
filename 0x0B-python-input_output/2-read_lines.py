#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    ''' function that reads n lines of a text file (UTF8)
        and prints it to stdout'''
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if count < nb_lines or nb_lines <= 0:
                print(line, end='')
            count += 1
