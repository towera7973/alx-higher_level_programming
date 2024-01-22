#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)
    except Exception as wrong_fct:
        print("Exception: {}".format(wrong_fct), file=sys.stderr)
        return None
    else:
        return output
