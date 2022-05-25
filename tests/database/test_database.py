from unittest import TestCase

import app
from app import create_database_conn


class DatabaseTest(TestCase):
    def setUp(self) -> None:
        self.app = app.create_app().test_client()
        self.app.testing = True
        self.database = create_database_conn()

    def test_init(self):
        assert self.database.lock is not None

    def test_should_init_database_connection(self):
        assert self.database.conn is not None
