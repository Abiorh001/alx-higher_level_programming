#!/usr/bin/python3
'''CREATING RECTANGLE CLASS WITH INSTANCES'''


class Rectangle:
    '''RECTANGLE CLASS'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''getter for widght'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if self.value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
