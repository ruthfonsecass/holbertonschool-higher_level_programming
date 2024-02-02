#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []

    for num in my_list:
        if num % 2 == 0:
            new_list.append(num)
    for i in my_list:
        if my_list[i] and new_list[i] == num:
            return True
        else:
            return False
