#!/usr/bin/python3
'''Defines a square class'''


class Square:
    '''This represents object made of square'''

    def __init__(self, size=0):
        '''Initializes a new square object
        Args:
            size (int): The size of the square object
        '''
        self.__size = size

    @property
    def size(self):
        '''This returns the size of the object'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the size to a given value'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        '''Returns area of a square'''
        return self.__size ** 2

    def __eq__(self, other):
        """Define the '==' comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the '!=' comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the '<' comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the '<=' comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the '>' comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the '>=' comparison to a Square."""
        return self.area() >= other.area()
