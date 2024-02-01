#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    
    max_number = my_list[0]
    for x in range my_list:
        if x > max_number:
            max_number = x
    return max_number
