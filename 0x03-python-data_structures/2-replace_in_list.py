#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_length=len(my_list)
    if idx<0 and idx > list_length:
        return(my_list)
    else:
        my_list[idx]=element
        new_list=my_list
        return(new_list)
