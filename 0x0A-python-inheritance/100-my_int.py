#!/usr/bin/python3
''' class MyInt that inherits from int '''


class MyInt(int):
    ''' MyInt is a rebel. MyInt has == and
        != operators inverted
    '''
    def __init__(self, number):
            self.number = number

    def __eq__(self, other):
        if self.number == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
        if self.number != int(other):
            return False
        else:
            return True
