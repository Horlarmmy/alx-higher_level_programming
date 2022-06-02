#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv) - 1
    if len(argv) == 1:
        print("{:d} arguments." .format(arg))
    elif len(argv) == 2:
        print("{:d} argument:" .format(arg)
                print("{:d}: {}" .format(arg, argv[1]))
    else:
        print("{:d} arguments:" .format(len(argv) - 1))
        for i in range(len(argv)):
            if i != 0:
                print("{:d}: {}" .format(i, argv[i]))

