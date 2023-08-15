#!/usr/bin/python3
def multiple_returns(sentence):
    _len = len(sentence)

    if _len == 0:
        return None
    else:
        my_var = sentence[0]
    return _len, my_var
