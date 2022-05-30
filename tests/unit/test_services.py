from unittest import TestCase
from unittest import mock

from flask import Flask

from app.__main__ import app
import app.services.auth_service


@mock.patch("app.services.auth_service.id_token", autospec=True)
class TestGoogleAuthService(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client_id = "client_id"
        cls.sample_user_info = {
            "sub": "1234567890",
            "email": "sample_email@unal.edu.co",
            "given_name": "sample_given_name",
            "family_name": "sample_family_name",
            "picture": "sample_picture_url",
        }

        with mock.patch("app.services.auth_service.requests.Request", autospec=True):
            cls.auth_service = app.services.auth_service.GoogleAuthService(
                cls.client_id
            )

    def test_should_validate_token_when_token_is_valid(self, mock_id_token):
        mock_id_token.verify_oauth2_token.return_value = self.sample_user_info

        result_validation = self.auth_service.validate_token("valid_token")

        self.assertEqual(result_validation, self.sample_user_info)

    def test_should_raise_exception_when_token_is_invalid(self, mock_id_token):
        mock_id_token.verify_oauth2_token.side_effect = ValueError

        with self.assertRaises(app.services.auth_service.InvalidTokenException):
            self.auth_service.validate_token("invalid_token")

    # TODO: Test GoogleAuthError when token is expired


class TestAppAuthService(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client_id = "client_id"
        cls.sample_user_info = {
            "sub": "1234567890",
            "email": "sample_email@unal.edu.co",
            "given_name": "sample_given_name",
            "family_name": "sample_family_name",
            "picture": "sample_picture_url",
        }
        cls.app = Flask("test")

    @mock.patch("app.services.auth_service.jwt.encode", autospec=True)
    def test_should_generate_token(self, mock_jwt_encode):
        with self.app.app_context():
            mock_jwt_encode.return_value = "token_string_utf8"
            token = app.services.auth_service.AppAuthService.generate_token(
                self.sample_user_info
            )

        self.assertIsNotNone(token)

    def test_should_parse_token(self):
        token = app.services.auth_service.AppAuthService.parse_token("Bearer token_string_utf8")

        self.assertEqual(token, "token_string_utf8")