#!/usr/bin/python3
"""Sqaure C"""


class Square:
    """Square block"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Gitter property"""
    @property
    def size(self):
        """gitter func"""
        return self.__size
    @property
    def position(self):
        return self.__position
    """setter property"""
    @size.setter
    def size(self, value):
        """Intance Atribute"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    """Setter property"""
    @position.setter
    def position(self, value):
        """Intance Atribute"""
        if self.__position != len(value) or type(value) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """Intance func"""
    def area(self):
        """area instance func"""
        return self.__size
        """my_print func"""
    def my_print(self):
        """my_print intance"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("_" * self.__position[0] + '#' * self.__size)
