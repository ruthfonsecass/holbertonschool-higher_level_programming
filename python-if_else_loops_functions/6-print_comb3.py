#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 1 and j == 0:
            continue
        print("{}{}".format(i, j), end=",")
