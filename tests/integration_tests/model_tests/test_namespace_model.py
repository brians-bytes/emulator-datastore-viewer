import unittest

from tests.test_utils import reset_datastore_emulator
from viewer.models.kind import KindModel
from viewer.models.name_space import NamespaceModel

FAKE_ENTITY_DATA = [
    {
        'kind': 'user',
        'id': 'user-id-1',
        'namespace': 'test'
    },
    {
        'kind': 'user',
        'id': 'user-id-2',
        'namespace': 'new',
    },
    {
        'kind': 'user',
        'id': 'user-id-2',
        'namespace': None,
    },
]


def create_entities():
    for entity_data in FAKE_ENTITY_DATA:
        instance = KindModel(kind=entity_data['kind'], namespace=entity_data['namespace'])
        instance.update_attrs(id=entity_data['id'])
        instance.put()


class TestNamespaceModel(unittest.TestCase):
    def setUp(self):
        create_entities()

    def tearDown(self):
        reset_datastore_emulator()

    def test_retrieve_all_available_namespaces(self):
        expected_entity_namespace = list(
            set([
                fake_entity_kind['namespace'] if fake_entity_kind['namespace'] else 'default'
                for fake_entity_kind in FAKE_ENTITY_DATA
            ])
        )

        available_entity_namespaces = NamespaceModel.get_all_available_namespaces()
        self.assertCountEqual(expected_entity_namespace, available_entity_namespaces)
