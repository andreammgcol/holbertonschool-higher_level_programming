#!/usr/bin/python3
'''
Function that returns the list of available
attributes and methods of an object.
'''


def lookup(obj):
    '''
    Arguments:
    @obj: object
    Return: list of available attributes
    '''
    return (dir(obj))
