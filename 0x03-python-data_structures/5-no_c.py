#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        '''here it meanss continue with the for loop going up dont go down '''
        new_string += my_string[i]
    return new_string

