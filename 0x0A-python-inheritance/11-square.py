#!/usr/bin/python3
"""
Module 10-square
Class Square                                      """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class square inherit fron rectangle"""
    def __init__(self, size):
        """ Initializes the class instance """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size)

    def area():
        """Method that returns the area"""
        return self.__size * self.__size

    def __str__():
        """ method that returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
