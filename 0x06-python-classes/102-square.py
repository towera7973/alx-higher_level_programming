#!/usr/bin/python3
""" a class Square that defines a square by: (based on 4-square.py)"""
class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0):
        """ init square
        Argment:
            value (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: making it a private size.
        Returns:Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int or float.

        Argment:
            value (int): size of the square.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns the area
        Returns: area of squire.
        """
        return self.__size**2

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size
