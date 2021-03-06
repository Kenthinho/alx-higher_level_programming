#!/usr/bin/python3
'''returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''This returns the list of available attributes and methods of an object
    Args:
        obj: any object
    Return:
        returns the lsit of available attributes and methods of an object
    '''
    return dir(obj)
