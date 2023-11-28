#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

message = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit > 5:
    print(message, "greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(message, "less than 6 and not 0")
else:
    print(message, "0 and is 0")
