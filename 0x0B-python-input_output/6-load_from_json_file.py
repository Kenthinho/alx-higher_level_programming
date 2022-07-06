#!/usr/bin/python3
'''A module that defines a function
that load from json
'''
import json


def load_from_json_file(filename):
    """load from json module"""
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
