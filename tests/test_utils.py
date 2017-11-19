import logging
import os

import requests

logger = logging.getLogger(__name__)


def reset_datastore_emulator():
    """reset internal state for the datastore enmulator"""
    datastore_emulator_host = os.environ.get('DATASTORE_EMULATOR_HOST')
    datastore_url = f'http://{datastore_emulator_host}/reset'
    r = requests.post(datastore_url)

    if r.status_code != 200:
        logger.warn(r.content)
        raise RuntimeError('Cannot reset datastore emulator')
