from app.controllers.controller_ping import ControllerPing
from app.database.database import Database

try:
    db = Database()
except Exception as e:
    db = None
    print("Database connection error", e)

# TODO: def controllers
# generic_controller = GenericController(db)

controller_ping = ControllerPing(db)

