#!/usr/bin/python3
letters_delete = ['q', 'e']
for i in range(97, 123):
    letter = chr(i)
    if letter not in letters_delete:
        print(letter, end='')
