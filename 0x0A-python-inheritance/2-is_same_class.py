#!/usr/bin/python3
"""
Module 2-is_same_class
Function is same class
"""


def is_same_class(obj, a_class):
    """ Returns True if its the same class, else False"""
    if issubclass(a_class, int):
        return True
    else:
        return False
