#!/usr/bin/python3
"""
Function that print out content of a file
"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        print(content)
