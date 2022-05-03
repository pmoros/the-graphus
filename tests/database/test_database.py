import app
from unittest import TestCase

from app.database.database import Database


class DatabaseTest(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True
        self.database = Database()

    def test_init(self):
        assert self.database.lock is not None