#!/usr/bin/env python3

import requests
import json
import sys
import os

webhook_url = os.environ.get('slack_webhook_url')

error = f"""

MISSING PARAMETER: You must pass a text file to the script as an argument.

EXAMPLE: {sys.argv[0]} some/path/to/file.txt

"""

def file_to_json(path_to_file):
    with open(path_to_file, 'r') as f:
        message = f.read()
        json_data = json.dumps({'text': message})
        return json_data

try:
    filename = sys.argv[1]
    payload = file_to_json(filename)
    r = requests.post(url=webhook_url, data=payload)
    print(r.status_code)
except IndexError:
    print(error)


