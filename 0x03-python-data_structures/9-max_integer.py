#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_val = my_list[0]
        for j in range(len(my_list)):
            if isinstance(my_list[j], int):
                if my_list[j] > max_val:
                    max_val = my_list[j]
    return max_val
