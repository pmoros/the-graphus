"""Module with login endpoint."""
from http import HTTPStatus

from flask import Blueprint

login = Blueprint("login", __name__)


@login.route("/", methods=["POST"])
def login_method():
    return "Login", HTTPStatus.OK
