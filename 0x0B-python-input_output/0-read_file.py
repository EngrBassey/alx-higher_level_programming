#!/usr/bin/python3

"""Module to read a file"""


def read_file(filename=""):
    """functuion to read a file"""

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
