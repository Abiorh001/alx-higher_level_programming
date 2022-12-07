#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if "C" not in i and 'c' not in i:
            print(i, end='')
