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

    """area func"""
    def area(self):
        """area instance func"""
        return self.__size
    """print func"""
    def my_print(self):
        """conditions"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
