#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return
    return list(set(set_1) .symmetric_difference(set(set_2))) ## could return set_1 ^ set_2
