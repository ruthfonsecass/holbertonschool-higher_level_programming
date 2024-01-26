#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
text = "Last digit of {} is {}".format(number, last_digit)

if last_digit > 5:
    text += "and is greater than 5"
elif last_digit == 0:
    text += "and is 0"
elif 0 < last_digit < 6:
    text += "and is less than 6 and not 0"
