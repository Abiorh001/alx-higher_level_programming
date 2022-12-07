#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return 
    else:
        higest_number = my_list[0]
        for number in my_list:
            if number > higest_number:
                higest_number = number
                return higest_number
