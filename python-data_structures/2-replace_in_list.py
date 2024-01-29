#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx is not None and 0<= idx < len(my_list):
        return my_list

    new_list = my_list.replace("idx", "element")
