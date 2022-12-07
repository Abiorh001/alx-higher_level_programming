#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    my_list = set(my_list)
    for i in my_list:
        total += i
    return total
