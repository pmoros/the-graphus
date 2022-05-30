"""Flask app creation."""
import os
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS

from app.blueprints import *
from app.modules import *
from flask_wtf.csrf import CSRFProtect

# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = [
    {"url": "/ping", "bp": ping},
    {"url": "/users", "bp": users},
    {"url": "/academic-histories", "bp": academic_histories},
]


def create_app():
    """Create Flask app."""
    load_dotenv()
    app = Flask(__name__)
    CORS(app)

    app.config["WTF_CSRF_CHECK_DEFAULT"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "")

    csrf = CSRFProtect()
    csrf.init_app(app)  # Compliant

    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    for endpoint in ACTIVE_ENDPOINTS:
        app.register_blueprint(endpoint.get("bp"), url_prefix=endpoint.get("url"))

    return app
