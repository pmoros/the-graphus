from app.utils.constants import PING_RESPONSE


class PingController:
    def __init__(self, db):
        self.db = db

    def ping_pong(self):
        return PING_RESPONSE
