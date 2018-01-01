from tests.base_test import BaseAPITest
from tests.test_utils import create_mocked_kinds, extract_json_from_response


class NamespacesEndpointIntegrationTests(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.kinds_list = []

    def test_retrieve_all_available_namespaces(self):
        self.kinds_list = create_mocked_kinds()

        resp = self.client.get('/api/namespaces')
        self.assertEqual(200, resp.status_code)

        resp_json = extract_json_from_response(resp)

        expected_namespaces = set([x.namespace for x in self.kinds_list])
        actual_namespaces = [x['name'] for x in resp_json['items']]
        self.assertCountEqual(expected_namespaces, actual_namespaces)

    def test_get_empty_list_no_namespace(self):

        resp = self.client.get('/api/namespaces')
        self.assertEqual(200, resp.status_code)

        resp_json = resp_json = extract_json_from_response(resp)

        self.assertEqual(len(resp_json['items']), 0)
