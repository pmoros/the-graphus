"""Handle database configuration."""
from threading import Lock

import pymysql
from pymysql import IntegrityError

from app.exceptions.exceptions import UserNotFoundException
from app.log import logger

GET_USER_BY_SUB_QUERY = "SELECT * FROM user WHERE sub = %s"
CREATE_USER = "INSERT INTO user (sub, email, given_name, family_name, picture) VALUES (%s, %s, %s, %s, %s)"


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
            logger.exception(f"Unable to connect to the database. {e}")

    def get_user_by_sub(self, sub):
        """Get user by sub."""

        with self.lock:
            self.conn.ping()
            cur = self.conn.cursor()
            cur.execute(GET_USER_BY_SUB_QUERY, [sub])
            row = cur.fetchone()
            cur.close()
            self.conn.commit()
            self.conn.close()
        if row:
            return row
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
                self.conn.ping()
                cur = self.conn.cursor()
                cur.execute(CREATE_USER, [sub, email, given_name, family_name, picture])
                cur.close()
                self.conn.commit()
                self.conn.close()
            except IntegrityError:
                logger.exception(f"User {sub} already exists.")

