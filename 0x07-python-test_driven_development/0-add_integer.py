#!/usr/bin/python3

""" add Funn """


def add_integer(a, b=98):
    """ functions that add """
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("b must be an integer")

    c = int(a)
    d = int(b)

    return c + d
