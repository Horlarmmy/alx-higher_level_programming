#!/usr/bin/python3
"""
Module Square
Class Square that inherits from the class Base
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ An initialization of the square class
        Args:
            size: size of the square
            x: position on x axis
            y: position on y axis
            id: id of the square
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets a new value for the size"""
        if type(value) is not int:
            raise TypeError("width must an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """ returns a printable representation of tbe square"""
        return "[Square] ({}) {}/{} - {}" .format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update attribute of an instance
           Args:
               -id attribute
               -size attribute
               -x attribute
               -y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args) is not int and args[0] is None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __dec__(self):
        """Return a string representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def to_dictionary(self):
        """Return the dictionary representation of the square class"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
