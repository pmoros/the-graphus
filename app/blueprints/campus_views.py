"""Module with campus endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.utils.constants import PING_RESPONSE, SUCCESS_RESPONSE_TAG, ERROR_RESPONSE_TAG

campus = Blueprint("campus", __name__)


@campus.route("/ping", methods=["GET"])
def ping():
    """Ping endpoint."""
    return PING_RESPONSE, HTTPStatus.OK


@campus.route("/", methods=["GET"])
def get_all():
    """
    Return all campuses.
    ---
    tags:
        - campus
    responses:
        200:
            description: Returns all campuses.
        404:
            description: No campuses found
    """
    try:
        res = app.campus_controller.get_all()
        return jsonify({SUCCESS_RESPONSE_TAG: res}), HTTPStatus.OK
    except FileNotFoundError:
        return {ERROR_RESPONSE_TAG: "there are no campuses in database"}, HTTPStatus.NOT_FOUND
