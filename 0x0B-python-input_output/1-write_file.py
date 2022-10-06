#!/usr/bin/python3
"""
Function that print out content of a file
"""


def write_file(filename="", text=""):
    """ Function that writes in a file """
    with open(filename, 'w', encoding='utf-8') as f:
        s = f.write(str(text))
    return s
