#!/usr/bin/python3
"""                                               Module 8-rectangle
Class Rectangle                                   """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry"""
    def _init_(self, width, height):
        """ Initializes the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """ Special method that returns a printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
