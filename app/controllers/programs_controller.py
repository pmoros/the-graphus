from http import HTTPStatus
from app.log import logger


class ProgramsController:
    def __init__(self, db):
        self.db = db

    def get_curricula(self, curricula_id):
        # Use 1 for testing in local database
        curricula_id = 4  # ! Just for testing in production database
        curricula_courses = self.db.get_courses_by_curricula_id(curricula_id)
        curricula_requirements = self.db.get_requirements_by_curricula_id(curricula_id)
        for course in curricula_courses:
            requirements = list(
                filter(
                    lambda requirement: requirement["course_id"] == course["course_id"],
                    curricula_requirements,
                )
            )
            requirements = [r["identifier"] for r in requirements]
            course["requirements"] = requirements

        return curricula_courses, HTTPStatus.OK
