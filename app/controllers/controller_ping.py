class ControllerPing:
    def __init__(self, db):
        self.db = db

    def ping(self):
        return {"message": "pong"}
