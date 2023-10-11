#!/usr/bin/python3

'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''

    def area(self):
        ''' Method that calculates de area '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' Method that validates the value '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """function that inherit base geometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
