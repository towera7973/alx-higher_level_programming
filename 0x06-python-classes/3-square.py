#!/usr/bin/python3
class Square:
    """
    a class Square that defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of square.
        """
        return self.__size ** 2
