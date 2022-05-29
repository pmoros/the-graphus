from google.oauth2 import id_token
from google.auth.transport import requests

from app.exceptions.exceptions import InvalidTokenException


class GoogleAuthService:
    def __init__(self, app_client_id):
        self.requests = requests.Request()
        self.app_client_id = app_client_id

    def validate_token(self, token):
        try:
            id_info = id_token.verify_oauth2_token(
                token, self.requests, self.app_client_id
            )
            return id_info
        except ValueError as invalid_token:
            raise InvalidTokenException from invalid_token

    # TODO: Handle GoogleAuthError when token is expired
