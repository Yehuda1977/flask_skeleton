import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))


# https://flask.palletsprojects.com/en/1.1.x/config/
class Config:

    BASEDIR = basedir
    UPLOADS_DIR = os.path.join(basedir, 'webapp/uploads')


class DevConfig(Config):
    """
    Development config
    """

    DEBUG = True
    SECRET_KEY = "my-very-secret-key"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


    MAIL_SERVER  = "smtp.gmail.com" # mail.yahoo.fr
    MAIL_PORT    = 587 # 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME       = 'yehuda1977@gmail.com'
    MAIL_DEFAULT_SENDER = 'yehuda1977@gmail.com'

    # Somewhere you need to do (probably in ~/.bash_profile):
    # export MAIL_PASSWORD="mypassword"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    """
    Production config
    """
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    MAIL_SERVER  = "smtp.gmail.com" # mail.yahoo.fr
    MAIL_PORT    = 587 # 465
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME       = 'yehuda1977@gmail.com'
    MAIL_DEFAULT_SENDER = 'yehuda1977@gmail.com'



    # Somewhere you need to do (probably in ~/.bash_profile):
    # export MAIL_PASSWORD="mypassword"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')



configs = {
    "dev": DevConfig,
    "prod": ProdConfig,
}

mode = os.environ.get("FLASK_ENV")
if not mode or mode.lower() not in configs.keys():
    valid = False
    while not valid:
        print("No config mode has been specified as an environment variable, please select one manually:")
        print("0) exit")
        keys_ix = {}
        for ix, key in enumerate(configs.keys()):
            print(f"{ix+1}) {key}")
            keys_ix[ix+1] = key

        try:
            choice = int(input("> "))
            if choice == 0:
                sys.exit(0)
            mode = keys_ix[choice]
        except Exception as e:
            print(f"Something went wrong ({str(e)})")
            valid = False
        else:
            valid = True

current_config = configs[mode]
