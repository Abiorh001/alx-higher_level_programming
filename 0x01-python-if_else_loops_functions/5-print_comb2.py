#!/usr/bin/python3
for number in range(0, 100):
    if number >= 0 and number <= 9:
        print("0{}".format(number), end=", ")
    if number > 9:
        print(number, end=", ")
