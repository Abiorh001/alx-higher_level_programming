#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i] * 2))
