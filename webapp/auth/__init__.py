import flask
from .. import db, login_manager
from .. import mail_functions
from ..mixins import ModelMixin

auth_blueprint = flask.Blueprint('auth', __name__, template_folder="templates")

from . import routes, models

