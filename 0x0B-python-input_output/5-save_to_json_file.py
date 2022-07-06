#!/usr/bin/python3
'''A module that defines a function that writes
an object to a text file, using JSON format
'''
import json


def save_to_json_file(my_obj, filename):
    """saves into json format"""
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
