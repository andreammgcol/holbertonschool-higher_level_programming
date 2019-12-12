#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print('{:d} arguments.'.format(length - 1))
    elif length == 2:
        print('{:d} argument:'.format(length - 1))
    else:
        print('{:d} arguments:'.format(length - 1))
    for i in range(length):
        if i == 0:
            continue
        print('{:d}: {:s}'.format(i, sys.argv[i]))
