#!/usr/bin/python3

"""
This module contains a function returns an object
(Python data structure) represented by a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string.
    """
    return json.dumps(my_obj)
