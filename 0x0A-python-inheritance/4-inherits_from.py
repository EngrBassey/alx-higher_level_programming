#!/usr/bin/python3

"""function that checks a subclass of an object"""


def inherits_from(obj, a_class):
    """func implementation"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
