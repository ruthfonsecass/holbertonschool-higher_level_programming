#!/usr/bin/python3
class Square:
    def _init__ (self, size=0):
        if isinstance(size, int):
            self.size = size
        if size < 0:
            try:
                raise ValueError("size must be >= 0")
            except TypeError:
                print("size must be an integer")
