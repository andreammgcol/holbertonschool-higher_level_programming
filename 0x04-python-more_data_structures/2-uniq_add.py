#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = []
    for x in my_list:
        if x not in uniq_num:
            uniq_num.append(x)
    result = 0
    for x in uniq_num:
        result += x
    return result
