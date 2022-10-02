#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL 
and displays the bodyof the response.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]

    req= requests.get(url)
    status = req.status_code
    print(req.text) if status < 400 else print(
        "Error code: {}".format(req.status_code))
