#!/usr/bin/python3
"""class with predefined number of slots of just first_name"""


class LockedClass:
    """if user defined, no new items can be added to list"""
    __slots__ = ['first_name']
