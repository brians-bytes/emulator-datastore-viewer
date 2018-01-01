import unittest

from tests.test_utils import reset_datastore_emulator
from viewer import app


class BaseAPITest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client(use_cookies=False)

    def tearDown(self):
        reset_datastore_emulator()
