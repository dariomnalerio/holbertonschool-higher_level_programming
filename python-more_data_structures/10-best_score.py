#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sorted_dictionary = sorted(a_dictionary)
    return list(sorted_dictionary)[-1]
