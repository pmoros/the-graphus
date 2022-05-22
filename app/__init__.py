"""Flask app creation."""

from flask import Flask
from app.blueprints import *
from app.modules import *
from flask_wtf.csrf import CSRFProtect

# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = [
    {"url": "/ping", "bp": ping},
    {"url": "/login", "bp": login}
]


def create_app():
    """Create Flask app."""
    app = Flask(__name__)

    app.config['WTF_CSRF_CHECK_DEFAULT'] = False

    csrf = CSRFProtect()
    csrf.init_app(app)  # Compliant

    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    for endpoint in ACTIVE_ENDPOINTS:
        app.register_blueprint(endpoint.get("bp"), url_prefix=endpoint.get("url"))

    return app
