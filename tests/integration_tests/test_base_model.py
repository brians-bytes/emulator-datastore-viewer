import unittest

from tests.test_utils import reset_datastore_emulator
from viewer.models.common import BaseModel

FAKE_KIND = 'test_models'


class FakeEntityModel(BaseModel):
    __kind__ = FAKE_KIND


class TestBaseModelIntegration(unittest.TestCase):
    def tearDown(self):
        reset_datastore_emulator()

    def test_create_new_entity_kind(self):
        entity = FakeEntityModel()

        self.assertEqual(entity.__kind__, FAKE_KIND)
        self.assertIsNotNone(entity.id())

    def test_update_entity_kinds_attributes(self):
        name = 'brian'
        state = 'Kenya'
        instance = FakeEntityModel()

        instance.update_attrs(name=name, state=state)
        entity = instance.entity()

        self.assertIsNotNone(entity)
        self.assertIn('name', entity)
        self.assertEqual(entity['name'], name)
        self.assertIn('state', entity)
        self.assertEqual(entity['state'], state)
