#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    new_dictionary = a_dictionary.copy()
    for key in a_dictionary:
        new_dictionary[key] *= 2
    return new_dictionary
