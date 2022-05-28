"""Module with users endpoint."""
from functools import wraps
from http import HTTPStatus

from flask import Blueprint, jsonify, request
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import app
from app.exceptions.exceptions import InvalidTokenException, UserNotFoundException
from app.log import logger
from app.schemas import google_login_schema
from app.utils.constants import ERROR_RESPONSE_TAG, SUCCESS_RESPONSE_TAG

users = Blueprint("users", __name__)


def error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidTokenException as ite:
            logger.error(f"{ite.__class__.__name__}: {ite}")
            return jsonify({ERROR_RESPONSE_TAG: 'Invalid tokenId'}), HTTPStatus.UNAUTHORIZED
        except ValidationError as ve:
            logger.error(f"{ve.__class__.__name__}: {ve}")
            return jsonify({ERROR_RESPONSE_TAG: 'Invalid JSON format'}), HTTPStatus.BAD_REQUEST
        except UserNotFoundException as unf:
            logger.error(f"{unf.__class__.__name__}: {unf}")
            return jsonify({ERROR_RESPONSE_TAG: 'User not found'}), HTTPStatus.NOT_FOUND

    return wrapper


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
