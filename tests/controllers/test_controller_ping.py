from flask.app import Flask
from unittest import TestCase
from unittest.mock import MagicMock

from app.controllers.controller_ping import ControllerPing
from tests.utils.constants import *


class TestControllerPing(TestCase):
    def setUp(self) -> None:
        self.app = Flask('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.database = MagicMock(return_value='Database')
        self.controller = ControllerPing(self.database)

    def tearDown(self) -> None:
        self.app_context.pop()

    ''' ping_pong() tests '''

    def test_ping_pong(self):
        result = self.controller.ping_pong()
        self.assertEqual(result, PING_RESPONSE)
