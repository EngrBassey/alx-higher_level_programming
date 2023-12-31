#!/usr/bin/python3

"""Rectangle function"""


class Rectangle:
    """function rep"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (init): The width of the new rectangle
            height (init): The height of the new rectangle
        """

        type(self).number_of_instances += 1
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        results = []
        for i in range(self.__height):
            for _ in range(self.__width):
                results.append(str(self.print_symbol))
            if i != self.__height - 1:
                results.append('\n')
        return (''.join(results))

    def __repr__(self):
        rect = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return rect

    def __del__(self):
        self.number_of_instances -= 1
        print("Bye rectangle...")
