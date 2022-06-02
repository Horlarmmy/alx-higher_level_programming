#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {:s}" .format(argv[1]))
    else:
        print("{:d} arguments:".format(len(argv)))
        for i in range(len(sys.argv)):
            if i != 0:
                print("{:d}: {:s}".format(i, argv[i]))

