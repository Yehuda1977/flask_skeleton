import flask, flask_login, flask_babel

from . import main_blueprint, db       # . is webmain_blueprint/
from . import forms, news_functions, mail_functions, models

@main_blueprint.route("/set-language/<lang>")
def set_language(lang):
    flask.session["language"] = lang
    flask_babel.refresh()
    return flask.redirect('/')

@main_blueprint.route("/")
def home():
    return flask.render_template("home.html")
