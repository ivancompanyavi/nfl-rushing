
from . import routes
from flask import Blueprint

bp = Blueprint('rushings', __name__, url_prefix="/rushings")

routes.init(bp)
