import base64
import os
from urllib.parse import urlparse

from dotenv import load_dotenv

from app.controllers.ping_controller import PingController
from app.database.database import Database

load_dotenv()

db_uri = os.getenv("DB_URI", "")
db_uri = base64.b64decode(db_uri).decode("utf-8")
parsed_uri = urlparse(db_uri)
host = parsed_uri.hostname
port = parsed_uri.port
schema = parsed_uri.path[1:]
user = os.getenv("DB_USER", "")
password = os.getenv("DB_PASSWORD", "")

try:
    db = Database(host, port, schema, user, password)
except Exception as e:
    db = None
    print("Database connection error", e)

# TODO: def controllers
# generic_controller = GenericController(db)

ping_controller = PingController(db)
