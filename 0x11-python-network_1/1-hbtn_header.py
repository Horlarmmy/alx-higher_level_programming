#!/usr/bin/python3
"""
A script that shows the value of X-Request-Id
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        heade = response.getheader('X-Request-Id')
        print(heade)
