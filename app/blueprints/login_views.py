"""Module with login endpoint."""
from functools import wraps
from http import HTTPStatus

from flask import Blueprint, jsonify, request
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import app
from app.exceptions.exceptions import InvalidTokenException
from app.log import logger
from app.schemas import google_login_schema
from app.utils.constants import ERROR_RESPONSE_TAG, SUCCESS_RESPONSE_TAG

login = Blueprint("login", __name__)


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
        except Exception as e:
            logger.error(f"{e.__class__.__name__}: {e}")
            return jsonify({ERROR_RESPONSE_TAG: 'Unknown error'}), HTTPStatus.INTERNAL_SERVER_ERROR

    return wrapper


@login.route("/", methods=["POST"])
@error_decorator
def google_login():
    json_data = request.get_json(force=True)
    validate(json_data, google_login_schema)
    login_data = app.login_controller.google_login(json_data)
    return jsonify({SUCCESS_RESPONSE_TAG: login_data}), HTTPStatus.OK
