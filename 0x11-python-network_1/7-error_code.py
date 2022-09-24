#!/usr/bin/python3
import sys
import requests


if __name__ == '__main__' and if len(sys.argv) > 1:
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
