#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    '''FUNCTION TO PRINT FIRST AND LAST NAME
       Args:
       para1 = string
       para2 = string
       Raise:
       TypeError if first or last name not a string
       Return:
       None
    '''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}", end="")
