import unittest

from tests.test_utils import reset_datastore_emulator
from viewer.models.common import BaseModel
from viewer.models.kind import KindModel

FAKE_ENTITY_DATA = [
    {
        'kind': 'user',
        'id': 'user-id-1',
    }, {
        'kind': 'user',
        'id': 'user-id-2',
    }, {
        'kind': 'user',
        'id': 'user-id-3',
    }, {
        'kind': 'books',
        'id': 'book-id-1',
    }, {
        'kind': 'books',
        'id': 'book-id-2',
    }
]

def create_entities():
    for entity_data in FAKE_ENTITY_DATA:
        print(entity_data)

    assert 1 ==4


class TestKindModel(unittest.TestCase):
    def setUp(self):
        pass # create_entities()

    def tearDown(self):
        reset_datastore_emulator()

    def test_retrieve_all_available_kinds(self):
        pass

    def test_save_entity_to_datastore(self):
        kind = 'user_model'
        fake_id = 'user-id-1'
        instance = KindModel(kind=kind)
        instance.update_attrs(id=fake_id, name='brian')

        instance.put()

        user_rec = KindModel.get(fake_id)
        entity = user_rec.entity()

        self.assertIsNotNone(entity)
        self.assertEqual(fake_id, entity['id'])
        self.assertEqual('brian', entity['name'])
