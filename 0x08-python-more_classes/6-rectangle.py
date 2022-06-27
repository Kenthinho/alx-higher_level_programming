#!/usr/bin/python3
'''A module made for working with a rectangle
'''
number_of_instances = 0


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
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        '''Returns a string representation of this Rectangle.'''
        if self.width == 0 or self.height == 0:
            return ''
        else:
            result = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(result)

    def __repr__(self):
        '''Returns a representation of this Rectangle's initialization.'''
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        '''frees the memory of the instance of the class Rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
