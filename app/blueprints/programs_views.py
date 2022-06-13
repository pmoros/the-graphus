"""Module with users endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.decorators import error_decorator, token_required
from app.utils.constants import SUCCESS_RESPONSE_TAG

programs = Blueprint("programs", __name__)


@programs.route("/<program_code>/curriculas/<curricula_id>", methods=["GET"])
@error_decorator
@token_required
def get_program_curricula(program_code, curricula_id):

    curricula, status_code = app.programs_controller.get_curricula(curricula_id=None)
    status_code = HTTPStatus.OK
    return jsonify({SUCCESS_RESPONSE_TAG: curricula}), status_code
