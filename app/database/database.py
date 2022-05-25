"""Handle database configuration."""
from threading import Lock

import pymysql

from app.log import logger


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
            logger.exception("Unable to connect to the database.")
