#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_key = a_dictionary.copy().items()
    for key, val in new_key:
        if val == value:
            del a_dictionary[key]
    return (a_dictionary)
