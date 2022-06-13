class ProgramsController:
    def __init__(self, db):
        self.db = db

    def get_program_info(self, program_code):
        program_info = self.db.get_program_info_by_program_code(program_code)
        return program_info

    def get_curricula(self, curricula_id):
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

        return curricula_courses
