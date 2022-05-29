"""Handle database configuration."""
from threading import Lock

import pymysql
from pymysql import IntegrityError
from app.database import with_connection

from app.exceptions.exceptions import *
from app.log import logger

GET_USER_BY_SUB_QUERY = "SELECT * FROM user WHERE sub = %s"
CREATE_USER = "INSERT INTO user (sub, email, given_name, family_name, picture) VALUES (%s, %s, %s, %s, %s)"
UPDATE_USER = "UPDATE user SET email = %s, given_name = %s, family_name = %s, picture = %s WHERE sub = %s"

GET_ACADEMIC_HISTORIES_BY_USER_ID_QUERY = (
    "SELECT * FROM academic_history WHERE user_id = %s"
)
GET_CURRICULA_BY_CURRICULA_ID_QUERY = "SELECT * FROM curricula WHERE curricula_id = %s"
GET_COURSES_BY_CURRICULA_ID_QUERY = "SELECT * FROM course WHERE course_id IN (SELECT course_id FROM curricula_has_course WHERE curricula_id = %s)"


class Database:
    def __init__(self, host, port, schema, user, password):
        self.lock = Lock()
        try:
            self.conn = pymysql.connect(
                host=host,
                port=port,
                db=schema,
                user=user,
                password=password,
                cursorclass=pymysql.cursors.DictCursor,
            )
        except Exception as e:
            self.conn = None
            logger.exception("Unable to connect to the database. %s", e)

    def get_user_by_sub(self, sub):
        """Get user by sub."""
        with self.lock:
            user = self.db_read_one(GET_USER_BY_SUB_QUERY, [sub])
        if user:
            return user
        else:
            raise UserNotFoundException

    def create_user(self, google_user):
        """Create user by google info."""

        sub = str(google_user.get("sub"))
        email = str(google_user.get("email"))
        given_name = str(google_user.get("given_name"))
        family_name = str(google_user.get("family_name"))
        picture = str(google_user.get("picture"))

        with self.lock:
            try:
                self.db_write(
                    CREATE_USER, [sub, email, given_name, family_name, picture]
                )
            except IntegrityError:
                logger.exception("User %s already exists.", sub)

    def update_user(self, google_user):
        """Update user by google info."""

        email = str(google_user.get("email"))
        given_name = str(google_user.get("given_name"))
        family_name = str(google_user.get("family_name"))
        picture = str(google_user.get("picture"))
        sub = str(google_user.get("sub"))

        with self.lock:
            self.db_write(UPDATE_USER, [email, given_name, family_name, picture, sub])

    def get_academic_histories_by_user_id(self, user_id):
        """Get user by user id."""

        with self.lock:
            academic_histories = self.db_read_all(
                GET_ACADEMIC_HISTORIES_BY_USER_ID_QUERY, [user_id]
            )
        if academic_histories:
            return academic_histories
        else:
            raise AcademicHistoryNotFoundException

    def get_curricula_by_curricula_id(self, curricula_id):
        """Get curricula by curricula id."""

        with self.lock:
            curricula = self.db_read_one(
                GET_CURRICULA_BY_CURRICULA_ID_QUERY, [curricula_id]
            )
        if curricula:
            return curricula
        else:
            raise CurriculaNotFoundException

    def get_courses_by_curricula_id(self, curricula_id):
        """Get courses by curricula id."""

        with self.lock:
            courses = self.db_read_all(
                GET_COURSES_BY_CURRICULA_ID_QUERY, [curricula_id]
            )
        if courses:
            return courses
        else:
            raise CourseNotFoundException

    @with_connection
    def db_read_one(self, query, params):
        """Read one row from the database."""
        cur = self.conn.cursor()
        cur.execute(query, params)
        row = cur.fetchone()
        cur.close()

        return row

    @with_connection
    def db_read_many(self, query, params):
        "Read many rows from the database."
        cur = self.conn.cursor()
        cur.execute(query, params)
        row = cur.fetchone()
        cur.close()

        return row

    @with_connection
    def db_read_all(self, query, params):
        "Read all rows from the database."
        cur = self.conn.cursor()
        cur.execute(query, params)
        row = cur.fetchall()
        cur.close()

        return row

    @with_connection
    def db_write(self, query, params):
        """Write to the database."""
        cur = self.conn.cursor()
        cur.execute(query, params)
        cur.close()
