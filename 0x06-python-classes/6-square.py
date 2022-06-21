#!/usr/bin/python3
'''Defines a square class'''


class Square:
    '''This represents object made of square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes a new square object
        Args:
            size (int): The size of the square object
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''This returns the size of the object'''
        return self.__size

    @property
    def position(self):
        '''Retrieves the position of this Square
        Returns: tuple - The position of this square
        '''
        return self.__position

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

    @position.setter
    def position(self, value):
        '''Updates the position of this Square
        Args:
        value (tuple): The new position of this Square.
        '''
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        '''Returns area of a square'''
        return self.__size ** 2

    def my_print(self):
        '''prints the character # in stdout
        in a square shape
        '''
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("{}".format('#' * self.size))
