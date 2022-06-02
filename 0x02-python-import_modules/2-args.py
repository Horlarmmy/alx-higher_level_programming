#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv)))
        for i in range(len(argv)):
            if i != 0:
                print("{:d}: {)".format(i, argv[i]))

