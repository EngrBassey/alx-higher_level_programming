#!/usr/bin/python3

"""Inheritance list"""


class MyList(list):
    """funtion that print sorted inheritance"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
