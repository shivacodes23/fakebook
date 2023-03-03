from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self):
        self.generate_password(self.password)
        #self.password = generate_password_hash(self.password)

    def check_password(self, password_to_check):
        return check_password_hash(self.password, password_to_check)

    def generate_password(self,password_create_salt_from):
        self.password = generate_password_hash(password_create_salt_from)

    def to_dict(self):
        from app.blueprints.authentication.models import User
        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
        return data

    def __repr__(self):
        return f'<User: {self.email}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)