#!/usr/bin/python3
''' Module for to_json_string func '''
import json


def save_to_json_file(my_obj, filename):
    ''' returns the JSON string representation of an object (string) '''
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
