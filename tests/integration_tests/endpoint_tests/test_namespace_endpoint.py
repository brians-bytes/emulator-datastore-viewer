import json

from tests.base_test import BaseAPITest
from tests.test_utils import create_mocked_kinds


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

    def test_retrieve_all_avaiable_kinds_with_namespace(self):

        namespace = 'namespace_1'

        resp = self.client.get(
            '/api/kinds', query_string={
                'namespace': namespace
            }
        )
        self.assertEqual(200, resp.status_code)

        resp_data = resp.data.decode(resp.charset)
        resp_json = json.loads(resp_data)
        expected_kinds = set(
            [
                (x.kind, x.namespace)
                for x in self.kinds_list if x.namespace == 'namespace_1'
            ]
        )
        actual_kinds = set(
            [(x['name'], x['namespace']) for x in resp_json['items']]
        )
        self.assertCountEqual(expected_kinds, actual_kinds)

    def test_retrieve_no_avaiable_kinds_with_unavailable_namespace(self):

        namespace = 'no-namespace-supported'

        resp = self.client.get(
            '/api/kinds', query_string={
                'namespace': namespace
            }
        )
        self.assertEqual(200, resp.status_code)

        resp_data = resp.data.decode(resp.charset)
        resp_json = json.loads(resp_data)
        self.assertEqual(len(resp_json['items']), 0)
