#!/usr/bin/python3
"""
Function that returns the json representation of an object
"""

import json


def to_json_string(my_obj):
    """ Function that return the json rep """
    ans = json.dumps(my_obj)
    return ans
