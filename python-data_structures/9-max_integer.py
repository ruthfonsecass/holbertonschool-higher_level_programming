#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    
    max_number = my_list
    for x in my_list:
        if x > max_number:
            max_number = x
            print("{:d}".format(max_number))

