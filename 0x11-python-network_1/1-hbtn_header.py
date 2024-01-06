#!/usr/bin/python3

""" module to fetch X-header-ID"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
