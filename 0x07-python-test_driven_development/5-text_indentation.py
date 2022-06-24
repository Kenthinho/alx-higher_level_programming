#!/usr/bin/python3
'''This module defines the function 'text_indentation'
which prints a text with 2 new lines after each of these
characters: ., ? and :
'''


def text_indentation(text):
    """prints a text with 2 new lines after each of these
    characters: ., ? and :
    Arg:
        text - which represents a string data type
    Raises:
        TypeError - if text is not of string data type
    Return:
        None value
    """
    new_text = ""
    if type(text) != str:
        raise TypeError("text must be a string")

    for word in text:
        if word == " " and len(new_text) == 0:
            continue
        if word in '.?:':
            new_text += word
            print(new_text)
            print()
            new_text = ""
        else:
            new_text += word
    print(new_text, end='')
