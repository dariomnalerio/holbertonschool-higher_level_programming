#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print(my_list[i], end="")
                printed += 1
    except Exception as exc:
        raise exc
    print()
    return printed
