from flask import Blueprint, jsonify, request
from app.user.uitls import create_token

from app.user.models import User, check_password

userBp = Blueprint('user', __name__)


@userBp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Query your database for username and password
    user = User.query.filter_by(username=username).first()
    if user is None or not check_password(user.password, password):
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_token(user.id)
    return jsonify(
        {
            "token": access_token,
            "user": {"user_id": user.id, "username": user.username}
        }
    )
