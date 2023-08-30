#!/usr/bin/python3
"""Sqaure C"""


class Square:
    """Square block"""
    def __init__(self, size=0):
        self.__size = size

    """Gitter property"""
    @property
    def size(self):
        """gitter func"""
        return self.__size
    """setter property"""
    @size.setter
    def size(self, value):
        """Intance Atribute"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """area func instance"""
    def area(self):
        """area func"""
        return self.__size ** 2
