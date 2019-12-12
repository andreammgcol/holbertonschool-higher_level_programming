#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    sum = 0
    for i in range(1, length):
        num = int(sys.argv[i])
        sum += num
    print("{}".format(sum))
