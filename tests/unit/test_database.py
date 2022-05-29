from unittest import TestCase
from unittest import mock

from pymysql import IntegrityError
from app import Database
from app.log import logger
from app.exceptions import exceptions


@mock.patch("pymysql.connect")
class TestDatabase(TestCase):
    def setUp(self):
        self.google_user = {
            "sub": "1234567890",
            "email": "sample_email@unal.edu.co",
            "given_name": "sample_given_name",
            "family_name": "sample_family_name",
            "picture": "sample_picture_url",
        }

    def test_should_handle_connection_error(self, mock_conn):
        mock_conn.side_effect = Exception("Connection error")

        with mock.patch("app.log.logger.exception") as mock_logger:
            Database("localhost", 3306, "test", "root", "password")

            mock_logger.assert_called()

    def test_should_get_user_by_sub(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_read_one") as mock_db_read_one:
            mock_db_read_one.return_value = self.google_user
            result = db.get_user_by_sub(self.google_user["sub"])

        self.assertEqual(result, self.google_user)

    def test_should_handle_user_not_found_by_sub(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_read_one") as mock_db_read_one:
            mock_db_read_one.return_value = None
            with self.assertRaises(exceptions.UserNotFoundException):
                db.get_user_by_sub(self.google_user["sub"])

    def test_should_create_user(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_write") as mock_db_write:
            db.create_user(self.google_user)

            mock_db_write.assert_called()

    def test_should_not_create_user_that_exists(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_write") as mock_db_write:
            mock_db_write.side_effect = IntegrityError
            with mock.patch("app.log.logger.exception") as mock_logger:
                db.create_user(self.google_user)

                mock_logger.assert_called()

    def test_should_update_user(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_write") as mock_db_write:
            db.update_user(self.google_user)

            mock_db_write.assert_called()

    def test_should_get_academic_histories_by_user_id(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_read_all") as mock_db_read_all:
            mock_db_read_all.return_value = (1,)
            result = db.get_academic_histories_by_user_id(self.google_user["sub"])

        self.assertIsNotNone(result)

    def test_should_get_curricula_by_curricula_id(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_read_one") as mock_db_read_one:
            mock_db_read_one.return_value = (1,)
            result = db.get_curricula_by_curricula_id(1)

        self.assertIsNotNone(result)

    def test_should_get_courses_by_curricula_id(self, mock_conn):
        db = Database("localhost", 3306, "test", "root", "password")
        with mock.patch.object(Database, "db_read_all") as mock_db_read_all:
            mock_db_read_all.return_value = (1,)
            result = db.get_courses_by_curricula_id(1)

        self.assertIsNotNone(result)
