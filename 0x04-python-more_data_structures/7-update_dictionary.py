#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    key_value = {key: value}
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
