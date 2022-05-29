from unittest import TestCase
from unittest import mock

import app.services.google_auth_service


@mock.patch("app.services.google_auth_service.id_token", autospec=True)
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

        with mock.patch(
            "app.services.google_auth_service.requests.Request", autospec=True
        ):
            cls.google_auth_service = (
                app.services.google_auth_service.GoogleAuthService(cls.client_id)
            )

    def test_should_validate_token_when_token_is_valid(self, mock_id_token):
        mock_id_token.verify_oauth2_token.return_value = self.sample_user_info

        result_validation = self.google_auth_service.validate_token("valid_token")

        self.assertEqual(result_validation, self.sample_user_info)

    def test_should_raise_exception_when_token_is_invalid(self, mock_id_token):
        mock_id_token.verify_oauth2_token.side_effect = ValueError

        with self.assertRaises(app.services.google_auth_service.InvalidTokenException):
            self.google_auth_service.validate_token("invalid_token")

    # TODO: Test GoogleAuthError when token is expired
