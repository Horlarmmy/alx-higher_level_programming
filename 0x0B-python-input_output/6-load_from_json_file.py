#!/usr/bin/python3
"""
Function that  creates object from json file
"""

import json


def load_from_json_file(filename):
    """ Function that loads the obj from json"""
    with open(filename, 'r',) as f:
        my_obj = json.load(f)
    return my_obj
