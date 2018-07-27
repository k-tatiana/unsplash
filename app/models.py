from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    image_id = db.Column(db.String(255), index=True, default='NULL')
    image_url = db.Column(db.String(255), default='NULL')
    image_desc = db.Column(db.String(255), default='NULL')
    image_full = db.Column(db.String(255), default='NULL')

    def __init__(self, image_id, image_url, image_desc, image_full):
        self.image_id = image_id
        self.image_url = image_url
        self.image_desc = image_desc
        self.image_full = image_full

    def __repr__(self):
        return '<Image {}>'.format(self.image_desc)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.filter_by(int(id))

