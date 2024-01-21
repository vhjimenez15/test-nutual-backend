from flask_jwt_extended import create_access_token


def create_token(user_id: int):
    return create_access_token(identity=user_id)
