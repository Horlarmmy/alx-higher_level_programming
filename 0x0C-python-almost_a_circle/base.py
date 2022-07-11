#!/usr/bin/python3
"""
Module Base
Class Base
"""


class Base:
    """ A base class with a private atrribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ An instantation of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
