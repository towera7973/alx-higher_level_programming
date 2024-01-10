#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace number on replace on position search in a list """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
            new_list=my_list
    return (new_list)
