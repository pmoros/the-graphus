from functools import wraps
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.exceptions.exceptions import AcademicHistoryNotFoundException, UserNotFoundException
from app.log import logger
from app.utils.constants import ERROR_RESPONSE_TAG, SUCCESS_RESPONSE_TAG

academic_histories = Blueprint("academic_histories", __name__)


def error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AcademicHistoryNotFoundException as ahnf:
            logger.error(f"{ahnf.__class__.__name__}: {ahnf}")
            return jsonify({ERROR_RESPONSE_TAG: 'Academic History not found'}), HTTPStatus.NOT_FOUND
        except UserNotFoundException as unf:
            logger.error(f"{unf.__class__.__name__}: {unf}")
            return jsonify({ERROR_RESPONSE_TAG: 'User not found'}), HTTPStatus.NOT_FOUND

    return wrapper


@academic_histories.route("/user/<string:user_sub>", methods=["GET"])
@error_decorator
def get_academic_histories_by_user_sub(user_sub):
    """
    Get all academic histories of a user
    """
    res = app.academic_histories_controller.get_academic_histories_by_user_sub(user_sub)
    return jsonify({SUCCESS_RESPONSE_TAG: res}), HTTPStatus.OK
