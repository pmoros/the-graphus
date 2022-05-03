import app
from unittest.case import TestCase
from unittest.mock import patch
from tests.utils.constants import *


class TestViewsPing(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True

    ''' ping_pong() tests '''

    @patch('app.controllers.controller_ping.ControllerPing.ping_pong')
    def test_ping_pong(self, mock_ping_pong):
        mock_ping_pong.return_value = PING_RESPONSE
        result = self.app.get('/ping')
        self.assertEqual(result.status_code, 200)
