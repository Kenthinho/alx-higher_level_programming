#!/usr/bin/python3
'''json object'''


class Student:
    '''A student class'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a student instance'''
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    d[key] = value
            return d
        else:
            return self.__dict__
