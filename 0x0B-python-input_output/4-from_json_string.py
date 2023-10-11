#!/usr/bin/python3
''' Module for to_json_string func '''
import json


def from_json_string(my_str):
    ''' returns the JSON string representation of an object (string) '''
    return json.loads(my_str)
