from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    from nfl.rushings import bp as api_bp
    app.register_blueprint(api_bp)
    return app
