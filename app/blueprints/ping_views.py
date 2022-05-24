"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app

ping = Blueprint("ping", __name__)


@ping.route("/", methods=["GET"])
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    response = app.ping_controller.ping_pong()
    return jsonify(response), HTTPStatus.OK
