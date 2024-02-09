#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError ("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n\n", end,"")
        if i + 1 < len(text) and text[i + 1] == " ":
            print(end="")
