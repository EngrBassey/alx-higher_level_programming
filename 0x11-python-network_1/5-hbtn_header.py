#!/usr/bin/python3
""" Python script to retrieve X-request"""

if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
