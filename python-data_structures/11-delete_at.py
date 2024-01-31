#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx is None and idx >= len(my_list):
        return my_list
    del my_list[idx]
    print(my_list)
