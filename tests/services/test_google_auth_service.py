import os
from unittest import TestCase
from unittest.mock import patch

from dotenv import load_dotenv

from app.exceptions.exceptions import InvalidTokenException
from app.services.google_auth_service import GoogleAuthService


class TestGoogleAuthService(TestCase):
    def setUp(self) -> None:
        load_dotenv()

        self.google_auth_service = GoogleAuthService("client_id")

    @patch("google.oauth2.id_token.verify_oauth2_token")
    def test_validate_token_ok(self, google_mock):
        google_mock.return_value = {}
        token = "valid_token"
        result = self.google_auth_service.validate_token(token)
        self.assertIsNotNone(result)

    @patch("google.oauth2.id_token.verify_oauth2_token")
    def test_validate_token_fail(self, google_mock):
        google_mock.side_effect = ValueError
        token = "invalid_token"
        self.assertRaises(InvalidTokenException, self.google_auth_service.validate_token, token)
