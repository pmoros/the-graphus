class InvalidTokenException(Exception):
    """
    Exception raised when the token is invalid.
    """

    def __init__(self, message):
        self.message = message
