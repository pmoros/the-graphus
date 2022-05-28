from functools import wraps
from http import HTTPStatus

from flask import jsonify
from jsonschema.exceptions import ValidationError

from app.exceptions.exceptions import *
from app.log import logger
from app.utils.constants import *


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
        except AcademicHistoryNotFoundException as ahnf:
            logger.error(f"{ahnf.__class__.__name__}: {ahnf}")
            return jsonify({ERROR_RESPONSE_TAG: 'Academic History not found'}), HTTPStatus.NOT_FOUND

    return wrapper
