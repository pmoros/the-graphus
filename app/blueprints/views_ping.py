"""Module with ping endpoint."""
from flask import Blueprint

import app

ping = Blueprint("ping", __name__)


@ping.route("/", methods=["GET"])
def ping_pong():
    """Ping endpoint, used to know if the app is up and running."""
    return app.controller_ping.ping()
