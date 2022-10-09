#!/usr/bin/python3
"""
Function that returns an object of JSON string
"""

import json


def from_json_string(my_str):
    """ Function that returns of object of string"""
    ans = json.loads(my_str)
    return ans
