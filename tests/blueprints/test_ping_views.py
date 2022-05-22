import app
from unittest.case import TestCase
from unittest.mock import patch

from app.utils.constants import PING_RESPONSE


class TestPingViews(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True

    ''' ping_pong() tests '''

    @patch('app.controllers.ping_controller.PingController.ping_pong')
    def test_ping_pong(self, mock_ping_pong):
        mock_ping_pong.return_value = PING_RESPONSE
        result = self.app.get('/ping')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, PING_RESPONSE)
