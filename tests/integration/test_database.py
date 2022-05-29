from os import getenv
from unittest import TestCase
from urllib.parse import urlparse

from dotenv import load_dotenv
from app import Database


class TestDatabase(TestCase):
    """All tables keys for the tests will have as value 1."""

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.db_uri = getenv("DB_URI", "")
        cls.parsed_uri = urlparse(cls.db_uri)

        host = cls.parsed_uri.hostname
        port = cls.parsed_uri.port
        schema = cls.parsed_uri.path[1:]
        users = getenv("DB_USER", "")
        password = getenv("DB_PASSWORD", "")
        cls.db = Database(host, port, schema, users, password)

    def setUp(self) -> None:
        self.google_user = {
            "sub": "1234567890",
            "email": "sample_email@unal.edu.co",
            "given_name": "sample_given_name",
            "family_name": "sample_family_name",
            "picture": "sample_picture_url",
        }

        self.truncate_database()

    def tearDown(self) -> None:
        self.truncate_database()

    def test_should_create_user(self):
        self.db.create_user(self.google_user)

        result = self.read_test_user_by_sub()

        self.assertIsNotNone(result)

    def test_should_get_user_by_sub(self):
        self.insert_test_user()

        result = self.db.get_user_by_sub(self.google_user.get("sub"))

        self.assertEqual(result.get("sub"), self.google_user.get("sub"))

    def test_should_update_user(self):
        self.insert_test_user()

        previous_name = self.google_user.get("given_name")
        self.google_user["given_name"] = "new_given_name"
        self.db.update_user(self.google_user)

        result = self.read_test_user_by_sub()

        self.assertEqual(result.get("sub"), self.google_user.get("sub"))
        self.assertNotEqual(previous_name, result.get("given_name"))

    def test_should_get_academic_histories_by_id(self):
        self.insert_test_user()
        self.insert_test_curricula()
        self.insert_test_academic_histories()

        result = self.db.get_academic_histories_by_user_id(1)

        self.assertIsNotNone(result)

    def test_should_get_curricula_by_curricula_id(self):
        self.insert_test_curricula()

        result = self.db.get_curricula_by_curricula_id(1)

        self.assertEqual(result.get("curricula_id"), 1)
        self.assertEqual(result.get("name"), "test_curricula")

    def test_should_get_courses_by_curricula_id(self):
        self.insert_test_curricula()
        self.insert_test_program_components()
        self.insert_test_training_expertise()
        self.insert_test_program_component_has_training_expertise()
        self.insert_test_courses()
        self.insert_test_curricula_has_course()

        result = self.db.get_courses_by_curricula_id(1)

        self.assertIsNotNone(result)

    # Auxiliary methods for filling the database with test data.

    def truncate_database(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute("SET FOREIGN_KEY_CHECKS = 0", [])
            cur.execute("TRUNCATE user", [])
            cur.execute("TRUNCATE curricula", [])
            cur.execute("TRUNCATE academic_history", [])
            cur.execute("TRUNCATE program_component", [])
            cur.execute("TRUNCATE training_expertise", [])
            cur.execute("TRUNCATE program_component_has_training_expertise", [])
            cur.execute("TRUNCATE course", [])
            cur.execute("TRUNCATE curricula_has_course", [])
            cur.execute("SET FOREIGN_KEY_CHECKS = 1", [])

    def insert_test_user(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO user (sub, email, given_name, family_name, picture) VALUES (%s, %s, %s, %s, %s)",
                [
                    self.google_user.get("sub"),
                    self.google_user.get("email"),
                    self.google_user.get("given_name"),
                    self.google_user.get("family_name"),
                    self.google_user.get("picture"),
                ],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_curricula(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute("INSERT INTO curricula (name) VALUES (%s)", ["test_curricula"])
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_academic_histories(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO academic_history (code, user_id, curricula_id) VALUES (%s, %s, %s)",
                [1, 1, 1],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_program_components(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO program_component (name) VALUES (%s)",
                ["test_program_component"],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_training_expertise(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO training_expertise (name) VALUES (%s)",
                ["test_training_expertise"],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_program_component_has_training_expertise(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO program_component_has_training_expertise (program_component_id, training_expertise_id) VALUES (%s, %s)",
                [1, 1],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_courses(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO course (code, name, credits, program_component_id, training_expertise_id) VALUES (%s, %s, %s, %s, %s)",
                [1, "test_course", 3, 1, 1],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def insert_test_curricula_has_course(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "INSERT INTO curricula_has_course (curricula_id, course_id) VALUES (%s, %s)",
                [1, 1],
            )
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

    def read_test_user_by_sub(self):
        with self.db.conn.cursor() as cur:
            self.db.conn.ping()
            cur.execute(
                "SELECT * FROM user WHERE sub = %s", [self.google_user.get("sub")]
            )
            row = cur.fetchone()
            cur.close()
            self.db.conn.commit()
            self.db.conn.close()

        return row
