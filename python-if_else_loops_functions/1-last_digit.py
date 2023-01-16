#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
print(f"The last digit of {number} is {lastDigit} and is", end=" ")
if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
