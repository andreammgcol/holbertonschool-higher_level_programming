#!/usr/bin/python3
import json


def load_from_json_file(filename):
    ''' that creates an Object from a “JSON file” '''
    with open(filename, mode='r') as f:
        return json.load(f)
