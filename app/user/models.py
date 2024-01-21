from app import db
from app import bcrypt


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(400))
    name = db.Column(db.String(100))

    def __init__(self, email, username, password, name):
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.name = name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "name": self.name,
        }


def check_password(user_password, login_password):
    return bcrypt.check_password_hash(user_password, login_password)
