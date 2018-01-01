import json
import unittest

from tests.base_test import BaseAPITest
from tests.test_factories import KindFactory


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


class KindEnpointIntegrationTests(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.kinds_list = create_mocked_kinds()

    def test_retrieve_all_avaiable_kinds_no_namespace(self):

        resp = self.client.get('/api/kinds')
        self.assertEqual(200, resp.status_code)

        resp_data = resp.data.decode(resp.charset)
        resp_json = json.loads(resp_data)
        expected_kinds = set(
            [
                (x.kind, x.namespace)
                for x in self.kinds_list if x.namespace == 'default'
            ]
        )
        actual_kinds = set(
            [(x['name'], x['namespace']) for x in resp_json['items']]
        )
        self.assertCountEqual(expected_kinds, actual_kinds)