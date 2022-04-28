class ControllerPing(object):
    def __init__(self, db):
        self.db = db
        pass

    def ping(self):
        return {"message": "pong"}
