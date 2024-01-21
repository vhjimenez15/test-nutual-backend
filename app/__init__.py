from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import config
from flask_cors import CORS

# type enviroment
enviroment = config['development']

# Create FLask app
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
cors = CORS(app)


# Initialize db
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# vistas
from app.avm.controllers import avmBp
from app.user.controllers import userBp
from commands import create_userbp

app.register_blueprint(avmBp)
app.register_blueprint(userBp)
app.register_blueprint(create_userbp)
