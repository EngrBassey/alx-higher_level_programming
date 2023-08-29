#!/usr/bin
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except:
        raise
