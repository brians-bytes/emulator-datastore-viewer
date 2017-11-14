import os

import requests

def reset_datastore_emulator():
    datastore_emulator_host = os.environ.get('DATASTORE_EMULATOR_HOST')
    datastore_url = 'http://{}/reset'.format(datastore_emulator_host)
    r = requests.get(datastore_url)

    if r.status_code != 200
        raise RuntimeError('Cannot reset datastore emulator')
