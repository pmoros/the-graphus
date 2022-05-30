from http import HTTPStatus

from app.exceptions.exceptions import InvalidTokenException, UserNotFoundException
from app.services import auth_service


class UsersController:
    def __init__(self, db, auth_service):
        self.db = db
        self.google_auth_service = auth_service

    def google_login(self, login_data):        
        google_token = login_data.get("tokenId")
        try:
            google_user = self.google_auth_service.validate_token(google_token)
        except InvalidTokenException:
            return None, {"message": "Invalid token"}, HTTPStatus.UNAUTHORIZED

        try:
            self.db.get_user_by_sub(google_user.get("sub"))
            self.db.update_user(google_user)
            status = HTTPStatus.OK
        except UserNotFoundException:
            self.db.create_user(google_user)
            status = HTTPStatus.CREATED

        auth_token = auth_service.AppAuthService.generate_token(google_user)
        return auth_token, self.db.get_user_by_sub(google_user.get("sub")), status

    def get_user_by_sub(self, sub):
        return self.db.get_user_by_sub(sub), HTTPStatus.OK
