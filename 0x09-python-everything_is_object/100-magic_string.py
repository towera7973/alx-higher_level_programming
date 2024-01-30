#!/usr/bin/python3

def magic_string():

    if hasattr(magic_string, 'calls'):
        magic_string.calls += 1
    else:
        magic_string.calls = 1

    return ', '.join(['Holberton'] * magic_string.calls)
