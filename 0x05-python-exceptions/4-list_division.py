#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    try:
        for i in range(list_length):
            try:
                var_1 = my_list_1[i]
                var_2 = my_list_2[i]
                my_list.append(var_1 / var_2)
            except (TypeError, ValueError):
                print("wrong type")
                my_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                my_list.append(0)
            except IndexError:
                print("out of range")
                my_list.append(0)
    finally:
        return my_list
