import json

CONFIGFILE = 'config.json'


def create_config():
    # create the config file if it does not exist
    try:
        with open(CONFIGFILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(CONFIGFILE, 'w') as f:
            f.write('{}')

    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)

    if 'username' not in data:
        data['username'] = ''
    if 'personal_access_token' not in data:
        data['personal_access_token'] = ''
    if 'use_github' not in data:
        data['use_github'] = True
    if 'use_ghe' not in data:
        data['use_ghe'] = False
    if 'ghe_url' not in data:
        data['ghe_url'] = ''

    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def read_config():
    with open(CONFIGFILE, 'r') as f:
        return json.load(f)


def save_config(key, value):
    with open(CONFIGFILE, 'r') as f:
        data = json.load(f)
        data[key] = value
    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
