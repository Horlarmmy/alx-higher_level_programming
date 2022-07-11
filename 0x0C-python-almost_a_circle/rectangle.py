#!/usr/bin/python3
"""
Module Rectangle inherited from Base class
Class Rectangle
"""

from base import Base


class Rectangle(Base):
    """ Class Rectangle that inherit from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantation of the class Rectangle
        Args:
            __width: width
            __height: height
            __x: position x
            __y: position y
            id: id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def height(self):
        """ The getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ The setter function for height"""
        self.__height = value

    @property
    def width(self):
        """ Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets a new value for the width"""
        self.__width = value

    @property
    def x(self):
        """ Gets the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets a new value for the x position"""
        self.__x = value

    @property
    def y(self):
        """ Gets the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets a new value for the y position"""
        self.__y = value
