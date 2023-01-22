#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    set_sum = 0
    for i in set1:
        set_sum += i
    return set_sum
