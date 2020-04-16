#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL
    and displays the body of the response
"""

from urllib import request, parse, error
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            html = response.read()
        print(html.decode(encoding="utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
