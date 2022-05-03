class ControllerPing:
    def __init__(self, db):
        self.db = db

    def ping_pong(self):
        return {"message": "pong"}
