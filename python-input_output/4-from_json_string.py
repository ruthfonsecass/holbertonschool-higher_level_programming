#!/usr/bin/python3

"""
This module contains a function returns an object
(Python data structure) represented by a JSON string.
"""

import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
