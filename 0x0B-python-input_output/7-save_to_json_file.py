#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    ''' that writes an Object to a text file, using a JSON representation '''
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
