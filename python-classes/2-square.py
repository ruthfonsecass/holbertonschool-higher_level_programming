#!/usr/bin/python3
class Square:
    def _init__ (self, size=0):
        if isinstance(size, int):
            self.size = size
            try:
                raise TypeError("size must be an integer")
            except size < 0:
                raise ValueError("size must be >= 0")
