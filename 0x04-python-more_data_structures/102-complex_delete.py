#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key, values in a_dictionary.items():
            if values == value:
                a_dictionary.pop(key, None)
                break
            return a_dictionary
