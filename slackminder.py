#!/usr/bin/env python3

import requests
import json
import sys
import os
import re


# Please set environment variable name to be the same as
# the file name and set this variable name to return the full
# webhook url. Please make sure that your file contains the
# message that will be posted on the Slack channel.

def main():
    try:
        filepath = sys.argv[1]
        env_var_name = get_filename(filepath)
        webhook_url = os.environ.get(env_var_name)
        payload = content_to_json(filepath)
        slack_post = post_request(webhook_url, payload)
        print(slack_post)

    except Exception as e:
        print(e)


def get_filename(filepath):
    pattern = r'\/(\w*).txt$'
    filename = re.search(pattern, filepath)
    return filename[1]


def content_to_json(filepath):
    with open(filepath, 'r') as f:
        message = f.read().strip()
        json_data = json.dumps({'text': message})
        return json_data


def post_request(url, data):
    r = requests.post(url=url, data=data)
    return r.status_code


if __name__ == '__main__':
    main()
