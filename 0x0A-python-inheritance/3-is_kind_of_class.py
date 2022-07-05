#!/usr/bin/python3
"""
Module is_kind_of_class
Function is kind of class
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if ots an insttance of the class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
