#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx is None and idx > my_list:
        return my_list
    new_list = my_list.replace("idx", "element")
    print(new_list)
