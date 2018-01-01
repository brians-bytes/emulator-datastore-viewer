import logging
import os

import requests
from tests.test_factories import KindFactory

logger = logging.getLogger(__name__)


def reset_datastore_emulator():
    """reset internal state for the datastore enmulator"""
    datastore_emulator_host = os.environ.get('DATASTORE_EMULATOR_HOST')
    datastore_url = f'http://{datastore_emulator_host}/reset'
    r = requests.post(datastore_url)

    if r.status_code != 200:
        logger.warn(r.content)
        raise RuntimeError('Cannot reset datastore emulator')


def create_mocked_kinds(batch=10):
    """creates and test entities for API test

    Parameters
    ----------
    batch : int
        number of enities to create, defalut to 10

    Returns
    -------
    list of KindModel
    """
    kind_list = KindFactory.create_batch(batch)
    for kind in kind_list:
        kind.put()

    return kind_list
