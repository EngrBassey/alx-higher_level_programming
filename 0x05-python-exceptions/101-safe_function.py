#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as res:
        print("Exception: ", res, file=sys.stderr)
        return None
