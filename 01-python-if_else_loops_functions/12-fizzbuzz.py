#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        string = ""
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            string += str(i)
        print(string, end=" ")
