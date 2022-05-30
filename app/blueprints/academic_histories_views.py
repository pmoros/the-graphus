from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.decorators import error_decorator
from app.decorators import sub_must_match
from app.utils.constants import SUCCESS_RESPONSE_TAG

academic_histories = Blueprint("academic-histories", __name__)


@academic_histories.route("/user/<string:user_sub>", methods=["GET"])
@sub_must_match
@error_decorator
def get_academic_histories_by_user_sub(user_sub):
    """
    Get all academic histories of a user
    """
    res = app.academic_histories_controller.get_academic_histories_by_user_sub(user_sub)
    return jsonify({SUCCESS_RESPONSE_TAG: res}), HTTPStatus.OK
