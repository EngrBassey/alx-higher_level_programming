#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """function that interchange operators"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
