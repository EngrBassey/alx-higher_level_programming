#!/usr/bin/python3

"""Module that raises an exception"""


class BaseGeometry:
    """ function that raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
