#!/usr/bin/python3

"""Module to read a file"""


def write_file(filename="", text=""):
    """functuion to read a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        read_data = f.write(text)
        return(read_data)
