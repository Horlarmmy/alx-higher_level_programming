#!/usr/bin/python3
"""
Module Rectangle inherited from Base class
Class Rectangle
"""

from models.base import Base


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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets a new value for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """ Gets the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets a new value for the x position"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets a new value for the y position"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ This prints the Rectangle with #"""
        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Prints the string representation of the Rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update attribute of an instance
           Args:
               -id attribute
               -width attribute
               -height attribute
               -x attribute
               -y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        return {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}
