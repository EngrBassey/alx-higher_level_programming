#!/usr/bin/python3
"""Module to appends a file"""


def append_write(filename="", text=""):
    """functuion to append to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return(f.write(text))
