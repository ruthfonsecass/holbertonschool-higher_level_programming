#!/usr/bin/python3
def no_c(my_string):
    char = "c, C"

    my_string = "".join(x for x in my_string if x not in char)
    print(my_string)
