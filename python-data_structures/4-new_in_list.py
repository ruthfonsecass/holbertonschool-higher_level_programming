#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list(my_list)
    if idx is None and 0 <= idx < my_list:
        return copy_list
    if 0 <= idx < len(copy_list):
        copy_list[idx] = element
