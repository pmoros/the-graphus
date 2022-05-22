from app.controllers.ping_controller import PingController
from app.database.database import Database

try:
    db = Database()
except Exception as e:
    db = None
    print("Database connection error", e)

# TODO: def controllers
# generic_controller = GenericController(db)

ping_controller = PingController(db)
