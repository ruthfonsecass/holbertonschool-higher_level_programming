#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:

        if 'a'<= char <= 'z':
            char_maj = chr(ord(char) - 32)
            result += char_maj
        else:
            result += char
    print("{}".format(result))
