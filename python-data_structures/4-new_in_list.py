#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > listLength:
        return my_list
    new_list = my_list.copy()
    new_list.insert(idx, element)
    return new_list
