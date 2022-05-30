import datetime
from google.oauth2 import id_token
from google.auth.transport import requests
import jwt
from flask import current_app

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


class AppAuthService:
    @staticmethod
    def generate_token(user_data):
        user_id = user_data.get("sub")
        token = jwt.encode(
            {
                "sub": user_id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            current_app.config["SECRET_KEY"],
        )

        return token

    @staticmethod
    def extract_token(token):
        return jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])

    @staticmethod
    def parse_token(auth_header):
        PREFIX = "Bearer"
        bearer, _, token = auth_header.partition(" ")
        if bearer != PREFIX:
            raise ValueError("Invalid token")

        return token
