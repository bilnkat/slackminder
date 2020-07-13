#!/usr/bin/env python3

import requests
import json
import sys
import os

global env_var_name
env_var_name = ''

missing_file_error_message = f"""

MISSING PARAMETER: You must pass a NON-EMPTY text file to the script as an argument.

EXAMPLE: {sys.argv[0]} some/path/to/file.txt

"""

def check_file_is_empty(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        content = content.replace('\n', '')
        content = content.replace(' ', '')
        content = content.replace('\t', '')
        if not content[0]:
            return True
        else:
            return False

def file_to_json(path_to_file):
    global env_var_name
    with open(path_to_file, 'r') as f:
        dict = {}
        env_var_name = ''
        while not env_var_name:
            env_var_name = f.readline().strip()
        dict[env_var_name] = os.environ.get(env_var_name)
        message = f.read().strip()
        dict['message'] = json.dumps({'text': message})
        return dict

try:
    filename = sys.argv[1]
    if not check_file_is_empty(filename):
        payload = file_to_json(filename)
    else:
        raise IndexError
    if payload[env_var_name] != None:
        r = requests.post(url=payload[env_var_name], data=payload['message'])
        print(r.status_code)
    else:
        print(f'''MISSING ENVIRONMENT VARIABLE/VALUE: There is no environment variable: {env_var_name} or no webhook URL: {env_var_name} found''')
except IndexError:
    print(missing_file_error_message)