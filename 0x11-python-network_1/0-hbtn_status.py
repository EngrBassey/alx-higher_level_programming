#!/usr/bin/python3
"""Module to display body response"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body_res = response.read()
        utf_8_res = body_res.decode('utf-8')

        print("Body response:")
        print("    - type:", type(body_res))
        print("    - content:", body_res)
        print("    - utf8 content:", utf_8_res)
