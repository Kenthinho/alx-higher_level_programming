#!/usr/bin/python3
'''Defines a square class'''


class Square:
    '''This represents object made of square'''

    def __init__(self, size=0):
        '''Initializes a new square object
        Args:
            size (int): The size of the square object
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''Returns area of a square'''
        return self.__size ** 2
