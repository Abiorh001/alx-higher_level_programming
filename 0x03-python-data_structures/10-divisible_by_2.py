#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = [item % 2 == 0 for item in my_list]
    return newlist
