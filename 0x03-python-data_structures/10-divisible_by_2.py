#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''printing true if the number in a list is divisible by 2 else false'''
    list_result = []
    for number in my_list:
        if (number % 2) == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return(list_result)
