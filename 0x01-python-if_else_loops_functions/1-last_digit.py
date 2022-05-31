#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(str(number)[-1])
if (num > 5):
    message = 'and is greater than 5'
if (num == 0):
    message = 'and is 0'
if (num < 6 and num != 0):
    message = 'is less than 6 and is not 0'
print(f"Last digit of {number:d} is {num} {message}")
