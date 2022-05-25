from http import HTTPStatus
from functools import wraps

from app.exceptions.exceptions import UserNotFoundException


class UsersController:
    def __init__(self, db, auth_service):
        self.db = db
        self.auth_service = auth_service

    def google_login(self, login_data):
        google_token = login_data.get('tokenId')
        google_user = self.auth_service.validate_token(google_token)

        try:
            return self.db.get_user_by_sub(google_user.get('sub')), HTTPStatus.OK
        except UserNotFoundException:
            self.db.create_user(google_user)
            return self.db.get_user_by_sub(google_user.get('sub')), HTTPStatus.CREATED

    def get_user_by_sub(self, sub):
        return self.db.get_user_by_sub(sub)
