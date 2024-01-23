#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)"""

class Square:
    """ a created class square with a construction bellow ._init__"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
