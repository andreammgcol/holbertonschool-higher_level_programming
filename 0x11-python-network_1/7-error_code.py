#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL
    and displays the body of the response
"""

import requests
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
        print(req.text)
    else:
        print(req.text)
