#!/usr/bin/python3
'''A module that defines a function that
returns JSON representation of an object
'''
import json


def to_json_string(my_obj):
    '''Converts to a json object'''
    return json.dumps(my_obj)
