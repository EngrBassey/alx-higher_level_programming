#!/usr/bin/python3
def no_c(my_string):
    my_var = 'cC'
    new_string = ''
    for i in my_string:
        if i not in my_var:
            new_string += i
    return (new_string)
