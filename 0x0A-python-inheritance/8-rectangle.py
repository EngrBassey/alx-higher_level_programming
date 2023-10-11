#!/usr/bin/python3

"""Module that raises an exception"""


class BaseGeometry:
    """ function that raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")

class Rectangle(BaseGeometry):
    """function that inherit base geometry"""

    def __init__(self, width, height):
        super.__init__(self)
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.intger_validation("height", height)
