#!/usr/bin/python3

"""Rectangle function"""


class Rectangle:
    """function rep"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (init): The width of the new rectangle
            height (init): The height of the new rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(self._width, int):
            raise TypeError("width must be an integer")
        if self._width < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(self._height, int):
            raise TypeError("height must be an integer")
        if self._width < 0:
            raise ValueError("height must be >= 0")
        self._height = value
