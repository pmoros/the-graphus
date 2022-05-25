from functools import wraps

from app.exceptions.exceptions import UserNotFoundException


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
    def __init__(self, db, auth_service):
        self.db = db
        self.auth_service = auth_service

    @error_decorator
    def google_login(self, login_data):
        google_token = login_data.get('tokenId')
        google_user = self.auth_service.validate_token(google_token)

        try:
            db_user = self.db.get_user_by_sub(google_user.get('sub'))
        except UserNotFoundException:
            db_user = self.db.create_user(google_user)

        return db_user
