#!/usr/bin/python3
"""A module with a class MyList that inherits from class list"""


class MyList(list):
    """A class list that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
