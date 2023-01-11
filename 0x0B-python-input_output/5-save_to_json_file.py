#!/usr/bin/python3
''' 5-save_to_json_file.py
'''

import json


def save_to_json_file(my_obj, filename):
    ''' writes an Object to a text file, using a JSON representation'''

    with open(filename, "w") as f_obj:
        json.dump(my_obj, f_obj)
