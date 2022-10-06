#!/usr/bin/python3
"""
Function that print out content of a file
"""


def read_file(filename=""):
    """ A function that prints out """
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        print(content)
