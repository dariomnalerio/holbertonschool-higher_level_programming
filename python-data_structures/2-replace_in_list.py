#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    listLength = len(my_list)
    if idx > 0 or idx <= listLength:
        my_list[idx] = element
    return my_list
