# MODELS.py
import flask_login

from . import db, login_manager, ModelMixin

class MyModel(db.Model, ModelMixin):
    pass
