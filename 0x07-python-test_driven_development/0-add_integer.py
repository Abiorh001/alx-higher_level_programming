#!/usr/bin/python3
def add_integer(a, b=98):
    ''' Function for adding two numbers '''
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    ''' raise TypeError if integer is not parsed to a '''
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
