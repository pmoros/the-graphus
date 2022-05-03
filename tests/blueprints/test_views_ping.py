import app
from unittest.case import TestCase


class TestViewsPing(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True

    ''' ping_pong() tests '''

    def test_ping_pong(self):
        result = self.app.get('/ping')
        self.assertEqual(result.status_code, 200)
