from unittest import TestCase

import app
from app.database.database import Database


class DatabaseTest(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True
        self.database = Database()

    def test_should_init_database_connection(self):
        assert self.database.conn is not None
