#!/usr/bin/python3
def only_diff_element(set_1, set_2):
    return (list(set(set_1) - set(set_2)) + list((set(set_2) - set(set_1))))
