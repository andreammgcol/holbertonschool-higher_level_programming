#!/usr/bin/python3
'''
BaseGeometry module
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rectangle '''

    def __init__(self, width, height):
        '''
        Instantiation with width and height
        Arguments:
        @width: width size
        @height: height size
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculate area of Rectangle
            Return: area
        '''
        return (self.__width * self.__height)

    def __str__(self):
        ''' Return rectagle description '''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
