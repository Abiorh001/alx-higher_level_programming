#!/usr/bin/python3
def print_square(size):
    '''FUNCTION TO PRINT # IN LENGHT OF SIZE
       Args:
           para1 = interger
           para2 = interger
        Raise:
            TypError if size is not an integer
            ValueError if size is less than zero
        Return:
            None
    '''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
