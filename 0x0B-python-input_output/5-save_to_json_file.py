#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object my_object to a text file called filename,
    using JSON representation"""

    with open(filename, 'w') as f:
        filename = f.write(json.dumps(my_obj))
    return filename
