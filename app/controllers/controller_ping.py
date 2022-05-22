from tests.utils.constants import PING_RESPONSE


class ControllerPing:
    def __init__(self, db):
        self.db = db

    def ping_pong(self):
        return PING_RESPONSE
