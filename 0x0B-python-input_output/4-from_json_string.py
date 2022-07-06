#!/usr/bin/python
"""function that returns the JSON representation
    of an object (string)
"""

import json


def from_json_string(my_str):
    """module from_json_strin
    returns python objects
    """
    return json.loads(my_str)
