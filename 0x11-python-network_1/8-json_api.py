#!/usr/bin/python3
"""
    script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ''}

    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=data)
    try:
        html = req.json()
        if len(html) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(html.get('id'), html.get('name')))
    except ValueError:
        print('Not a valid JSON')
