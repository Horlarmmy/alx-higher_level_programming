#!/usr/bin/python3
"""
Function that saves a json file
"""

import json


def save_to_json_file(my_obj, filename):
    """ Function that returns saves the obj in a jsonnfile"""
    ans = json.loads(str(my_obj))
    with open(filename, 'w',) as f:
        f.write(str(ans))
