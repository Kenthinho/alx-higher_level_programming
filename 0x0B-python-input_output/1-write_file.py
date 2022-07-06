#!/usr/bin/python3
'''
A module that defines a function
that prints a certain number of lines
'''


def write_file(filename="", text=""):
    '''A function that writes a string to a text file
    (UTF8) and returns the number of characters written
    Args:
        filename: (str) name of file or path to write to
        text: (str) text to write to file
    Return:
        number of text
    '''
    with open(filename, mode='w', encoding='utf8') as f:
        f.writes(text)
    return len(text)
