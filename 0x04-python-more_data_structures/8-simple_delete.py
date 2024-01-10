#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
        '''you can aswell use a_dictionary.pop(key) or remove(key) to delete a key'''
    return a_dictionary
