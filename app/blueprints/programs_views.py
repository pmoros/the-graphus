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
    program_code = "2879"  # ! Just for testing
    # Use 1 for testing in local database
    curricula_id = 4  # ! Just for testing in production database

    program_curricula = {}
    program_curricula["code"] = program_code
    program_curricula["name"] = app.programs_controller.get_program_info(program_code)[
        "name"
    ]
    curricula_courses = app.programs_controller.get_curricula(curricula_id)
    program_curricula["courses"] = curricula_courses

    status_code = HTTPStatus.OK
    return jsonify({SUCCESS_RESPONSE_TAG: program_curricula}), status_code
