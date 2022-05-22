from google.oauth2 import id_token
from google.auth.transport import requests

from app.exceptions.exceptions import InvalidTokenException


class GoogleAuthService:
    def __init__(self):
        self.requests = requests.Request()
        pass

    def validate_token(self, token, client_id):
        try:
            id_info = id_token.verify_oauth2_token(token, self.requests, client_id)
            return id_info
        except ValueError:
            raise InvalidTokenException("Invalid token")
