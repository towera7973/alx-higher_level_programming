#!/usr/bin/python3
"""loads from object to json"""
import json


def from_json_string(my_str):
    """The function that returns an object (Python data structure) represented by a JSON string:"""
    return json.loads(my_str)
