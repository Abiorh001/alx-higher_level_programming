#!/usr/bin/python3
'''A class is having a constructor and exceptions'''


class Square():
    '''A class is created which have a size of 0'''
    def __init__(self, size=0):
        if size != int(size):
            try:
                raise TypeError("size must be an integer")
            except TypeError as te:
                print(te)
        if int(size) < 0:
            try:
                raise ValueError("size must be >= 0")
            except ValueError as ve:
                print(ve)
        self.__size = size
