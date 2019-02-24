from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login.user_loader
def load_user(cid):
    return User.query.get(int(cid))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean)

    # This method is omitted in the tutorial, but is used to solve conflicts caused by PyCharm.
    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_admin_privileges(self, level):
        self.admin = level

    def is_admin(self):
        return self.admin


class Potion(db.Model):
    """
    This is a temporary class used for development on the flask-backend branch of the project.
    It uses the simplified view that will be in use when this branch merges with master.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    cost = db.Column(db.String(120), index=True, unique=False)
    rarity = db.Column(db.Integer)
    description = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # This method is omitted in the tutorial, but is used to solve conflicts caused by PyCharm.
    def __init__(self, name=None, cost=None, rarity=None, description=None):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.description = description

    def __repr__(self):
        return '<Potion {}>'.format(self.username)
