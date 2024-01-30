#!/usr/bin/python3
""" Module that send POST request and retrived the email """

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    get_url = sys.argv[1]
    get_email = sys.argv[2]

    data = urllib.parse.urlencode({'email': get_email}).encode('utf-8')

    with urllib.request.urlopen(get_url, data) as resp:
        body_msg = resp.read().decode('utf-8')

        print("{}".format(body_msg))
