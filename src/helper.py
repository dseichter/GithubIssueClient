import urllib3
import json
import logging

VERSION = "1.0.0"
URL = 'https://api.github.com/repos/dseichter/GithubIssueClient/releases/latest'


def check_for_new_release():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', URL)
        data = json.loads(r.data.decode('utf-8'))
        latest_version = data['tag_name']
        return latest_version != VERSION
    except Exception as e:
        logging.error(f"Error checking for new release: {e}")
        return False
