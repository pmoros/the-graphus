class InvalidTokenException(Exception):
    pass


class ResourceNotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class UserNotFoundException(ResourceNotFoundException):
    def __init__(self):
        self.resource = "User"


class AcademicHistoryNotFoundException(ResourceNotFoundException):
    def __init__(self):
        self.resource = "Academic History"


class CurriculaNotFoundException(ResourceNotFoundException):
    def __init__(self):
        self.resource = "Curricula"


class CourseNotFoundException(ResourceNotFoundException):
    def __init__(self):
        self.resource = "Course"
