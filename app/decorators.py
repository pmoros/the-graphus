from functools import wraps
from http import HTTPStatus

from flask import jsonify, request
from jsonschema.exceptions import ValidationError

from app.exceptions.exceptions import *
from app.log import logger
from app.utils.constants import *

from app.services.auth_service import AppAuthService


def error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidTokenException as ite:
            logger.error(f"{ite.__class__.__name__}: {ite}")
            return (
                jsonify({ERROR_RESPONSE_TAG: "Invalid tokenId"}),
                HTTPStatus.UNAUTHORIZED,
            )
        except ValidationError as ve:
            logger.error(f"{ve.__class__.__name__}: {ve}")
            return (
                jsonify({ERROR_RESPONSE_TAG: "Invalid JSON format"}),
                HTTPStatus.BAD_REQUEST,
            )
        except ResourceNotFoundException as rnfe:
            logger.error(f"{rnfe.__class__.__name__}")
            return (
                jsonify({ERROR_RESPONSE_TAG: f"{rnfe.resource} not found"}),
                HTTPStatus.NOT_FOUND,
            )

    return wrapper


def token_required(func):
    # TODO: refactor errors
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return (
                jsonify({ERROR_RESPONSE_TAG: "Token is missing"}),
                HTTPStatus.UNAUTHORIZED,
            )
        else:
            try:
                token = AppAuthService.parse_token(token)
                AppAuthService.extract_token(token)
            except ValueError:
                return (
                    jsonify({ERROR_RESPONSE_TAG: "Invalid token"}),
                    HTTPStatus.BAD_REQUEST,
                )

        return func(*args, **kwargs)

    return wrapper


def sub_must_match(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return (
                jsonify({ERROR_RESPONSE_TAG: "Token is missing"}),
                HTTPStatus.UNAUTHORIZED,
            )
        else:
            try:
                token = AppAuthService.parse_token(token)
                token_data = AppAuthService.extract_token(token)
                token_sub = token_data.get("sub")
                request_sub = request.view_args.get("user_sub")
                if token_sub != request_sub:
                    return (
                        jsonify({ERROR_RESPONSE_TAG: "Token sub does not match"}),
                        HTTPStatus.UNAUTHORIZED,
                    )
            except ValueError:
                return (
                    jsonify({ERROR_RESPONSE_TAG: "Invalid token"}),
                    HTTPStatus.BAD_REQUEST,
                )

        return func(*args, **kwargs)

    return wrapper
