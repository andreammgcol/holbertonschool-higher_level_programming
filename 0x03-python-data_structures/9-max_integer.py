#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is "":
        return None
    else:
        j = my_list[0]
        for i in my_list:
            if i > j:
                j = i
        return j
