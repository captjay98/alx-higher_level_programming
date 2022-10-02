#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response
"""


if __name__ == '__main__':
    from urllib import request
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except HTTPError as e:
        print("Error code:" ,e.code)
