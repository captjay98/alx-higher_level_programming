#!/usr/bin/python
"""function that returns the JSON representation of an object (string)
"""


import json


def from_json_string(my_str):
    """module from_json_strin
    returns the object represented by a JSON string
    """
    return json.loads(my_str)
