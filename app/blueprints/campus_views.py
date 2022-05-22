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
def get_all_campuses():
    try:
        res = app.campuses.get_all_campuses()
        return jsonify({SUCCESS_RESPONSE_TAG: res}), 200
    except FileNotFoundError:
        return {ERROR_RESPONSE_TAG: "there are no users in database"}, 404
