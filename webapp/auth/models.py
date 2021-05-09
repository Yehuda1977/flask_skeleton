"""
Contains all the database models related to authentication
Classes:
    - User
"""
import flask_login
from werkzeug import security
from sqlalchemy.ext.hybrid import hybrid_property

from . import db, login_manager, ModelMixin

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class User(db.Model, flask_login.UserMixin, ModelMixin): # db.Model is required if you want to create an SQL model
    """
    A class representing a user.

    ...

    Attributes
    ----------
    id : int
        Automatically incremented unique id
    name : str
        Name of the user
    password : str
        Hash of the user's password
    mail : str
        Mail address of the user

    Methods
    ----------
    check_password(pwd):
        Return if <pwd> is the right password for this user
    set_password(pwd):
        Hash the password and set it as this user's password
    """

    name = db.Column(db.String(64))
    password = db.Column(db.String(64)) # TODO: name it password_hash
    mail = db.Column(db.String(254), nullable=True)

    def check_password(self, pwd):
        """
        Check given password against the stored hash

        :param pwd: value to check against the stored password
        :return: True if <pwd> match the stored one else False
        """
        return security.check_password_hash(self.password, pwd)

    def set_password(self, pwd):
        """
        Storing the hash of the password into the database

        :param pwd: new password of the user
        """
        hashed = security.generate_password_hash(pwd)
        self.password = hashed

        self.save()

