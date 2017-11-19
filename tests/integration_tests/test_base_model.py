import unittest

from unittest.mock import patch

from tests.test_utils import reset_datastore_emulator
from viewer.models.common import BaseModel

FAKE_KIND = 'test_models'


class FakeEntityModel(BaseModel):
    def __init__(self, kind=FAKE_KIND):
        super(FakeEntityModel, self).__init__(kind=kind)


class TestBaseModelIntegration(unittest.TestCase):
    def tearDown(self):
        reset_datastore_emulator()

    def test_create_new_entity_kind(self):
        entity = FakeEntityModel()
        self.assertEqual(entity.__kind__, FAKE_KIND)

    def test_update_entity_kinds_attributes(self):
        name = 'brian'
        state = 'Kenya'
        instance = FakeEntityModel()

        instance.update_attrs(name=name, state=state)
        entity = instance.entity()

        self.assertIsNotNone(entity)
        from_entity = FakeEntityModel.from_entity(entity)
        self.assertIn('name', from_entity)
        self.assertEqual(from_entity['name'], name)
        self.assertIn('state', from_entity)
        self.assertEqual(entity['state'], state)

    def test_save_new_entity(self):
        entity_id = 'fake-id-entity'
        name = 'fake name'
        instance = FakeEntityModel()
        instance.update_attrs(id=entity_id, name=name)
        instance.put()

        instance = FakeEntityModel.get(FAKE_KIND, entity_id)

        self.assertIsNotNone(instance)
        self.assertEqual(entity_id, instance.id())
        self.assertEqual(name, instance.entity()['name'])
