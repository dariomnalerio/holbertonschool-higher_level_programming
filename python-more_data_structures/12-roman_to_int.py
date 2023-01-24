#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for i in roman_string:
        current = numbers[i]
        if current > prev:
            result += current - 2 * prev
            # 2 * prev because we already added the previous value to result
        else:
            result += current
        prev = current
    return result
