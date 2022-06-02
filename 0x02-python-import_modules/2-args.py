#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print("1: {:s}" .format(sys.argv[1]))
else:
    print("{:d} arguments:".format(len(sys.argv)))
    for i in range(len(sys.argv)):
        if i != 0:
            print("{:d}: {:s}".format(i, sys.argv[i]))

