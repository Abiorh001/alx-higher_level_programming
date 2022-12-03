#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    mine = my_list[:]
    if 0 <= idx <= len(my_list):
        mine[idx] = element
        return mine
    else:
        return my_list
