import app
from unittest.case import TestCase

from tests.utils.constants import *


class TestViewsCampus(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True

    ''' ping_pong() tests '''

    def test_ping_pong(self):
        result = self.app.get('/campus/ping')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, PING_RESPONSE)
