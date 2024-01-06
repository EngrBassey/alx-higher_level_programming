#!/usr/bin/python3
"""Module to display body response"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        body_res = resp.read()
        utf_8_res = body_res.decode('utf-8')

        print("Body response:")
        print("    - type: {}".format(type(body_res)))
        print("    - content: {}".format(body_res))
        print("    - utf8 content: {}".format(utf_8_res))
