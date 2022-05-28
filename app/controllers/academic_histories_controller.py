from app.utils.constants import *


def get_weighted_mean(courses, pa=False):
    """Get weighted mean from courses, can be used for PAPA or PAPPI."""
    grade_times_credits = 0.0
    total_credits = 0
    for course in courses:
        if pa:
            if course.get('last_time_seen') != TRUE:
                continue
        if course.get('grade') and course.get('taking_course') != TRUE:
            grade_times_credits += course.get('grade') * course.get('credits')
            total_credits += course.get('credits')

    if total_credits == 0:
        return 0
    return grade_times_credits / total_credits


class AcademicHistoriesController:
    def __init__(self, db):
        self.db = db

    def get_academic_histories_by_user_sub(self, user_sub):
        """Get user's academic histories by their user id."""

        user = self.db.get_user_by_sub(user_sub)
        academic_histories = self.db.get_academic_histories_by_user_id(user.get('user_id'))

        for academic_history in academic_histories:
            curricula = self.db.get_curricula_by_curricula_id(academic_history.pop('curricula_curricula_id', None))
            academic_history['curricula'] = curricula

            courses = self.db.get_courses_by_curricula_id(curricula.get('curricula_id'))

            semesters_history = {}
            for course in courses:
                semester_id = course.pop('semester', 'unknown')

                semester = semesters_history.get(semester_id, {})

                semester['courses'] = semester.get('courses', []) + [course]
                semester['credits'] = semester.get('credits', 0) + course.get('credits', 0)
                if course.get('passed') == TRUE:
                    academic_history['credits_seen'] = academic_history.get('credits_seen', 0) + course.get('credits', 0)
                semester[PAPPI] = get_weighted_mean(semester.get('courses'))

                semesters_history[semester_id] = semester

            academic_history['semesters'] = semesters_history
            academic_history[PAPA] = get_weighted_mean(courses)
            academic_history[PA] = get_weighted_mean(courses, pa=True)

        return academic_histories
