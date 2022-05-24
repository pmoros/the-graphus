import datetime
from functools import wraps

import jwt


def error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise e

    return wrapper


class LoginController:
    @error_decorator
    def __init__(self, auth_service, secret_key):
        self.auth_service = auth_service
        self.secret_key = secret_key

    @error_decorator
    def google_login(self, login_data):
        google_token = login_data.get('tokenId')
        google_user = self.auth_service.validate_token(google_token)

        # TODO Update user DB from google_data

        return google_user


