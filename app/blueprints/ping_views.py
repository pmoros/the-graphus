"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint

import app

ping = Blueprint("ping", __name__)


@ping.route("/", methods=["GET"])
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return app.controller_ping.ping_pong(), HTTPStatus.OK
