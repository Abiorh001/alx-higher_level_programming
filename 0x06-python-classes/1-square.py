#!/usr/bin/python3
''' We created a class and a constructor using __init__ '''


class Square():
    ''' The size is been private by using double underscored '''
    def __init__(self, size):
        self.__size = size
