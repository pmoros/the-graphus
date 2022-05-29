from os import getenv
from dotenv import load_dotenv
from unittest import TestCase, skip

from google.auth.exceptions import GoogleAuthError
import app.services.google_auth_service


class TestGoogleAuthService(TestCase):
    @skip("requires a valid user_token")
    def test_should_connect_to_google_api(self):
        load_dotenv()
        google_client_id = getenv("GOOGLE_CLIENT_ID", "")
        user_token = getenv("TEST_GOOGLE_USER_TOKEN", "")
        google_auth_service = app.services.google_auth_service.GoogleAuthService(
            google_client_id
        )
        google_auth_service.validate_token(user_token)
