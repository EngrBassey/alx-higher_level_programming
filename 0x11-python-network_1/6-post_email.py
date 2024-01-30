#!/usr/bin/python3
"""script to get email address"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email_args = sys.argv[2]

    r = requests.post(url, data={'email': email_args})
    print(r.text)
