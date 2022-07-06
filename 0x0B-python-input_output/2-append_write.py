#!/usr/bin/python3
'''A module that defines a function
that appends to a file
'''


def append_write(filename="", text=""):
    """"Append to the end of a file"""
    with open(filename, mode="a", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
