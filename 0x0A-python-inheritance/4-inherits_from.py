#!/usr/bin/python3
"""
Module inherits_from
Function inherit from
"""


def inherits_from(obj, a_class):
    """ Returns True if the obj inherits from the class"""
    if type(obj) is  a_class:
        return False
    return isinstance(obj, a_class)
