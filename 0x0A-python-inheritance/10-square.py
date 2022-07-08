#!/usr/bin/python3
"""
Module 10-square
Class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class square that inherits from the Rectangle class"""
    def __init__(self, size):
        """ Initializes the class instance """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area():
        """ Method that returns the area of the class"""
        return self.__size * self.__size
