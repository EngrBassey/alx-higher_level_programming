#!/usr/bin/python3
def remove_char_at(str, n):
#if n >= 0:
    if 0 <= n < len(str):
        new_char = str[:n] + str[n+1:]
        return (new_char)
    else n < 0:
        return (str)
