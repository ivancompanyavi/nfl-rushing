from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)

    app.wsgi_app = ProxyFix(app.wsgi_app)

    from nfl.rushings import bp as api_bp
    app.register_blueprint(api_bp)
    return app
