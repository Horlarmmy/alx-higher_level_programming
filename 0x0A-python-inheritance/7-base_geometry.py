#!/usr/bin/python3
"""
Module basegeometry                               Class BaseGeometry
"""


class BaseGeometry():
    """ A Base Geometry class """
    def area(self):
        """ method to compute area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validates the integers"""
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
