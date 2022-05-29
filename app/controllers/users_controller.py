from http import HTTPStatus

from app.exceptions.exceptions import InvalidTokenException, UserNotFoundException


class UsersController:
    def __init__(self, db, auth_service):
        self.db = db
        self.auth_service = auth_service

    def google_login(self, login_data):
        google_token = login_data.get("tokenId")
        try:
            google_user = self.auth_service.validate_token(google_token)
        except InvalidTokenException:
            return {"message": "Invalid token"}, HTTPStatus.UNAUTHORIZED

        try:
            self.db.get_user_by_sub(google_user.get("sub"))
            self.db.update_user(google_user)
            status = HTTPStatus.OK
        except UserNotFoundException:
            self.db.create_user(google_user)
            status = HTTPStatus.CREATED

        return self.db.get_user_by_sub(google_user.get("sub")), status
