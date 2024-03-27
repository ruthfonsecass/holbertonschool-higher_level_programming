#!/usr/bin/python3
def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    """
    if not isinstance(text, str):
        raise TypeError ("text must be a string")
    for i in range(len(text)):
        if text[i - 1] in ".?:" and i > 0 and text[i] is " ":
            continue
        print(text[i], end="")
        if text[i] is "." or text[i] is "?" or text[i] is ":":
            print("\n")
