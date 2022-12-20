#!/usr/bin/python3
'''A class is having a constructor and exceptions'''


class Square():
    '''A class is created which have a size of 0'''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''An instance is created to get the square of size'''
        return self.__size * self.__size

    def size(self):
        '''A getter is created'''
        return self.__size

    def size(self, value):
        '''A setter is created to set the value of size'''
        self.__size = value
