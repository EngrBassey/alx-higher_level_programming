#!/usr/bin/python3
""" Module to handle Networking request errs"""

if __name__ == '__main__':
    import sys
    import urllib.request

    get_url = sys.argv[1]

    try:
        with urllib.request.urlopen(get_url) as resp:
            body_msg = resp.read().decode('utf-8')
            print("{}".format(body_msg))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
