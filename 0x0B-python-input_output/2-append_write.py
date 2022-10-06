#!/usr/bin/python3
"""
Function that append at the end of a file
"""


def append_write(filename="", text=""):
    """ Function that appends a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        s = f.write(str(text))
    return s
