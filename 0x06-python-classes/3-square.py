#!/usr/bin/python3
"""Sqaure C"""


class Square:
    """Square block"""
    def __init__(self, size=0):
        self.__size = size
        """Intance Atribute"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
    """Area square block"""
    def area(self):
        """Area square block"""
        return self.__size ** 2
