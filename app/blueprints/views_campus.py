"""Module with campus endpoint."""
from flask import Blueprint

from tests.utils.constants import PING_RESPONSE

campus = Blueprint("campus", __name__)


@campus.route("/ping")
def ping():
    """Ping endpoint."""
    return PING_RESPONSE
