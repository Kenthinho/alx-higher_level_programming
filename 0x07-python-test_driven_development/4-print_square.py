#!/usr/bin/python3
'''This module defines the function 'print_square'
prints a square with the character '#'
'''


def print_square(size):
    """Prints a square with the character # of size (size)
    Arg:
        size - (int) represents the size length of the square
    Raises:
        TypeError - if the value of size is not an integer
        ValueError - if size is less than zero
        TypeError - if size is a float and less than 0
    Return:
        None value
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
