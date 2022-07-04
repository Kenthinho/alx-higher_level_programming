#!/usr/bin/python3
'''checks if an object is exactly an instance of
the specified class
'''


def is_same_class(obj, a_class):
    '''Returns True if an object is exactly an
    instance of the specified class.
    Args:
        obj (any) - object argument
        a_class (any) - A class to be compared against
    Return:
        bool - True if obj is exactly an instance
        of `a_class`.
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
