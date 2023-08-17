#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_y = max(a_dictionary)
        ky = [key, for key, value in a_dictionary.items() if value == max_y][0]
    return (ky)
