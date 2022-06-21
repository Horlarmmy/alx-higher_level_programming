#!/usr/bin/python3
"""
Module 2-square
Define class Square
"""


class Square:
    """ class Square that defines the object by its size"""
    def __init__(self, size=0):
        """ Initializes the square object that store the size
        Args:
            param1 (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
