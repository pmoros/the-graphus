import os
from urllib.parse import urlparse

from dotenv import load_dotenv

from app.controllers.academic_histories_controller import AcademicHistoriesController
from app.controllers.ping_controller import PingController
from app.controllers.users_controller import UsersController
from app.database.database import Database
from app.services.auth_service import GoogleAuthService


def create_database_conn():
    load_dotenv()

    db_uri = os.getenv("DB_URI", "")
    parsed_uri = urlparse(db_uri)

    host = parsed_uri.hostname
    port = parsed_uri.port
    schema = parsed_uri.path[1:]
    users = os.getenv("DB_USER", "")
    password = os.getenv("DB_PASSWORD", "")

    try:
        return Database(host, port, schema, users, password)
    except Exception as e:
        print("Database connection error", e)
        return None


db = create_database_conn()

load_dotenv()
google_client_id = os.getenv("GOOGLE_CLIENT_ID", "")

google_auth_service = GoogleAuthService(google_client_id)

ping_controller = PingController(db)
users_controller = UsersController(db, google_auth_service)
academic_histories_controller = AcademicHistoriesController(db)
