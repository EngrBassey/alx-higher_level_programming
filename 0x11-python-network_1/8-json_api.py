#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request """

if __name__ == '__main__':
    from sys import argv
    import requests

    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    r = requests.post(url, data)

    try:
        r_dict = r.json()

        if not r_dict:
            print("No result")
        else:
            print("[{}] {}".format(r_dict['id'], r_dict['name']))
    except ValueError:
        print("Not a valid JSON")
