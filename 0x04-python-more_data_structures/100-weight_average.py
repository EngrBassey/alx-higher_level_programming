#!/usr/bin/python3
def weight_average(my_list=[]):
    my_pd = 0
    my_adds = 0

    if not my_list:
        return 0
    for i, j in my_list:
        my_pd += i * j
        my_adds += j
    return (my_pd / my_adds)
