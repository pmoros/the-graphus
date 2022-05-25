"""Handle database configuration."""
import os
from threading import Lock
from urllib.parse import urlparse
import pymysql
import base64

from dotenv import load_dotenv

from app.database import logger


load_dotenv()

try:
    db_uri = os.getenv("DB_URI", "")
    # db_uri = base64.b64decode(db_uri).decode("utf-8")
    parsed_uri = urlparse(db_uri)
    host = parsed_uri.hostname
    port = parsed_uri.port
    schema = parsed_uri.path[1:]
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

except Exception as db_e:
    logger.exception("Unable to obtain database credentials.")


class Database:
    def __init__(self):
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
