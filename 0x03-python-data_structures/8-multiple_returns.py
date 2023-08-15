#!/usr/bin/python3
def multiple_returns(sentence):
    _len = len(sentence)

    if _len != 0:
        my_var = sentence[0]
    else:
        return None
    return _len, my_var
