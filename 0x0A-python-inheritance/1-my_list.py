#!/usr/bin/python3
'''
class MyList that inherits from list
Public instance method print_sorted(), that prints the list
'''


class MyList(list):

    def print_sorted(self):
        self.sort()
        print(self)
