#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    result = sentence()
    print(result)
