from unittest import TestCase
from unittest import mock

from flask import Flask

from app.controllers import users_controller
from app.exceptions.exceptions import UserNotFoundException
from app.services import auth_service
from app import Database


class TestUserController(TestCase):
    def setUp(self):
        self.db = mock.create_autospec(Database)
        self.google_auth_service = mock.create_autospec(auth_service.GoogleAuthService)
        self.user_controller = users_controller.UsersController(
            self.db, self.google_auth_service
        )
        self.google_user = {
            "sub": "1234567890",
            "email": "sample_email@unal.edu.co",
            "given_name": "sample_given_name",
            "family_name": "sample_family_name",
            "picture": "sample_picture_url",
        }
        self.app = Flask("test")

    def test_should_not_login_invalid_token(self):
        with self.app.app_context():
            self.user_controller.google_auth_service.validate_token.side_effect = (
                auth_service.InvalidTokenException
            )

            _, _, status = self.user_controller.google_login(
                {"tokenId": "sample_invalid_token"}
            )

            self.assertEqual(status, 401)

    @mock.patch("app.controllers.users_controller.auth_service.AppAuthService")
    def test_should_google_login(self, mock_app_auth_service):
        mock_app_auth_service.return_value.generate_token.return_value = "token_string"
        self.user_controller.google_auth_service.validate_token.return_value = (
            self.google_user
        )

        _, _, status = self.user_controller.google_login({"tokenId": "sample_token"})

        self.assertEqual(status, 200)

    @mock.patch("app.controllers.users_controller.auth_service.AppAuthService")
    def test_should_create_user_when_login(self, mock_app_auth_service):
        self.user_controller.google_auth_service.validate_token.return_value = (
            self.google_user
        )
        self.user_controller.db.get_user_by_sub.side_effect = [
            UserNotFoundException,
            self.google_user,
        ]

        _, _, status = self.user_controller.google_login({"tokenId": "sample_token"})

        self.assertEqual(status, 201)

    def test_should_get_user_by_sub(self):
        self.user_controller.db.get_user_by_sub.return_value = self.google_user

        response, status = self.user_controller.get_user_by_sub("1234567890")

        self.assertEqual(status, 200)
        self.assertEqual(response, self.google_user)
