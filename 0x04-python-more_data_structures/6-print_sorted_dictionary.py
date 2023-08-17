#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.items(), key=lambda x: x[0])
    for key, va in sorted_dic:
        print("{}: {}".format(key, va))
