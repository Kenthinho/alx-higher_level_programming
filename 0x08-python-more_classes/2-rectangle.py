#!/usr/bin/python3
'''A module made for working with a rectangle
'''


class Rectangle:
    """Represents a 2D Polygon with 4 perpendicular sides
    """
    def __init__(self, width=0, height=0):
        '''Initializes each instance with its parameters

        Args:
            width - (int) represents the width of the rectangle
            height - (int) represents the height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def height(self):
        '''retrieves the value of the height

        Return: an int value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''modifies the value of the height

        Args (int):
            value - argument supplied
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        '''Retrieves the value of the width

        Return: an int value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''modifies the value of the width
        Args (int):
            value - argument
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        '''computes the area of a rectangle

        Return: int value
        '''
        return self.width * self.height

    def perimeter(self):
        '''computes the perimeter of a rectangle

        Return: int value
        '''
        return 2 * (self.width + self.height)
