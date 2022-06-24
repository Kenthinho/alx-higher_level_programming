#!/usr/bin/python3
'''This module defines the function 'say_my_name'
and prints its argument
'''


def say_my_name(first_name, last_name=""):
    """Prints both first name and last name
    Args:
        first_name - string data type
        last_name - string data type
    Raises:
        TypeError - if both parameters are not of string data type
    Return:
        None value
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
