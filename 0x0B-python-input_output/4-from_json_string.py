#!/usr/bin/python3
'''A module that defines a function that
returns an object (Python data structure)
represented by a JSON string
'''
import json


def to_json_string(my_str):
    '''Gets a json object'''
    return json.loads(my_str)
