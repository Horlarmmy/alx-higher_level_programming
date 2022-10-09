#!/usr/bin/python3
"""
Function that  creates object from json file
"""

import json


def load_from_json_file(filename):
    """ Function that loads the obj from json"""
    with open(filename, 'w',) as f:
        my_obj = json.load(str(f))
    return my_obj
