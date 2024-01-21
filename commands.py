from app import db
import click
from flask import Blueprint
from app.user.models import User
import json
from app.avm.models import AVM
from app.avm.schemas import AVMSchema
from app.avm.helper import helper_create_avm

create_userbp = Blueprint('create_user', __name__, cli_group=None)


@create_userbp.cli.command('initial_command')
def initial_command():
    """ Creates data"""
    data = []
    with open('data_initial.json', 'r') as f:
        data = json.load(f)
    for item in data:
        data_ = helper_create_avm(item)
        schema = AVMSchema()
        new_element = AVM(**schema.dump(data_))
        db.session.add(new_element)
        db.session.commit()
    print("---> Create data: Successful <---")


@create_userbp.cli.command('create_user')
@click.argument('username')
@click.argument('password')
def create(username, password):
    """ Creates a user:
        username: <string>
        username: <password>
    """
    new_user = User('admin@nutual.com', username, password, 'ADMIN')
    db.session.add(new_user)
    db.session.commit()
    print("---> Create user: Successful <---")
