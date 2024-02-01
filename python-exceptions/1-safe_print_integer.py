#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in range(value):
            print("{:d}".format(i), end='')
        return True
    except ValueError:
        return False