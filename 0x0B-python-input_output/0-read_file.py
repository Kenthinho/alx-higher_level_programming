#!/usr/bin/python3
'''A module that defines a function that
prints to standard output
'''


def read_file(filename=""):
    '''A function that prints text file to stdout
    Args:
        filename: (str) name or path to file
    Return:
        None
    '''
    with open(filename, encoding='utf8') as f:
        for line in f:
            print(line, end='')
