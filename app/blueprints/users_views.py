"""Module with users endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request
from jsonschema import validate

import app
from app.decorators import error_decorator
from app.schemas import google_login_schema
from app.utils.constants import SUCCESS_RESPONSE_TAG

users = Blueprint("users", __name__)


@users.route("/login", methods=["POST"])
@error_decorator
def google_login():
    json_data = request.get_json(force=True)
    validate(json_data, google_login_schema)
    login_data, status_code = app.users_controller.google_login(json_data)
    return jsonify({SUCCESS_RESPONSE_TAG: login_data}), status_code


@users.route("/<string:user_sub>", methods=["GET"])
@error_decorator
def get_user_by_sub(user_sub):
    res = app.users_controller.get_user_by_sub(user_sub)
    return jsonify({SUCCESS_RESPONSE_TAG: res}), HTTPStatus.OK
