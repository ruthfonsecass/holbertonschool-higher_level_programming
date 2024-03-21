#!/usr/bin/python3
"""Module for say_my_name function."""


def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
