#!/usr/bin/python3
classe MyList(list):
def print_sorted(self):
    for i in sorted(self):
        print(i, end='')
    print()
