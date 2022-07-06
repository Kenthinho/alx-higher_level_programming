#!/usr/bin/python3
'''A script to create a student class
'''


class Student:
    '''Creates a class Student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''To json object'''
        return self.__dict__
