class AcademicHistoriesController:
    def __init__(self, db):
        self.db = db

    def get_academic_histories_by_user_sub(self, user_sub):
        """Get user's academic histories by their user id."""

        user = self.db.get_user_by_sub(user_sub)

        academic_histories = self.db.get_academic_histories_by_user_id(user.get('user_id'))

        return academic_histories


