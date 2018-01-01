import json

from tests.base_test import BaseAPITest
from tests.test_utils import create_mocked_kinds


class NamespaceEnpointIntegrationTests(BaseAPITest):
    def setUp(self):
        super().setUp()
        self.kinds_list = create_mocked_kinds()
