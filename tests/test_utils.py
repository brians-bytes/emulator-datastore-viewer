import json
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


def extract_json_from_response(resp):
    """gets and decode http jsonrespose to python equivalents
    
    Parameters
    ---------
    resp : URLRespose
        HTTP respomnse from test client
    
    Returns
    -------
    obj
        containing python equivalent of json reponse
    
    Raises
    ------
    json.JSONException
        if the respose cannot be json decode
    """
    resp_data = resp.data.decode(resp.charset)
    return json.loads(resp_data)


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
