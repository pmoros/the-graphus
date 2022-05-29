from http import HTTPStatus

from app.exceptions.exceptions import UserNotFoundException


class UsersController:
    def __init__(self, db, auth_service):
        self.db = db
        self.auth_service = auth_service

    def google_login(self, login_data):
        google_token = login_data.get("tokenId")
        google_user = self.auth_service.validate_token(google_token)

        try:
            self.get_user_by_sub(google_user.get("sub"))
            self.update_user_info(google_user)
            status = HTTPStatus.OK
        except UserNotFoundException:
            self.db.create_user(google_user)
            status = HTTPStatus.CREATED

        return self.get_user_by_sub(google_user.get("sub")), status

    def get_user_by_sub(self, sub):
        return self.db.get_user_by_sub(sub)

    def update_user_info(self, google_user):
        self.db.update_user(google_user)
