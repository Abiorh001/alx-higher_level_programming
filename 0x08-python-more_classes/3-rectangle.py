#!/usr/bin/python3
'''creating rectangleclass'''


class Rectangle:
    '''RECTANGLE CLASS'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter for widght'''
        return self.__width

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @width.setter
    def width(self, value):
        '''setter for width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter for height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Return string to print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            to_print += '\n'
            for row in range(self.width):
                to_print += '#'
        return to_print
