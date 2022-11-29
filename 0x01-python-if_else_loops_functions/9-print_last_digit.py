#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    tempfile = number[-1]
    print("{}".format(tempfile), end='')
    return tempfile
