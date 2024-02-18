#!/usr/bin/python3
"""
This module contains a function for writing a string to a text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="") as file:
        file.write(text)
