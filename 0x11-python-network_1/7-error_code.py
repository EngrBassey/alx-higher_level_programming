#!/usr/bin/python3
""" Error code #1 """

if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    status = r.status_code

    if status > 400:
        print("Error code: {}".format(status))

    else:
        print(r.text)
