from unittest import TestCase
from unittest import mock

from app.controllers import users_controller
from app.exceptions.exceptions import UserNotFoundException
from app.services import google_auth_service
from app import Database


class TestUserController(TestCase):
    def setUp(self):
        self.db = mock.create_autospec(Database)
        self.auth_service = mock.create_autospec(google_auth_service.GoogleAuthService)
        self.user_controller = users_controller.UsersController(
            self.db, self.auth_service
        )
        self.google_user = {
            "sub": "1234567890",
            "email": "sample_email@unal.edu.co",
            "given_name": "sample_given_name",
            "family_name": "sample_family_name",
            "picture": "sample_picture_url",
        }

    def test_should_not_login_invalid_token(self):
        self.user_controller.auth_service.validate_token.side_effect = (
            google_auth_service.InvalidTokenException
        )

        response, status = self.user_controller.google_login(
            {"tokenId": "sample_invalid_token"}
        )

        self.assertEqual(status, 401)

    def test_should_google_login(self):
        self.user_controller.auth_service.validate_token.return_value = self.google_user

        _, status = self.user_controller.google_login({"tokenId": "sample_token"})

        self.assertEqual(status, 200)

    def test_should_create_user_when_login(self):
        self.user_controller.auth_service.validate_token.return_value = self.google_user
        self.user_controller.db.get_user_by_sub.side_effect = [
            UserNotFoundException,
            self.google_user,
        ]

        _, status = self.user_controller.google_login({"tokenId": "sample_token"})

        self.assertEqual(status, 201)
