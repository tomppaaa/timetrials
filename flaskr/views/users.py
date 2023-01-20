from flask import Blueprint

mod = Blueprint("users", __name__)


@mod.route("/users/<id>")
def user(_id):
    return "Account information"


@mod.route("/users/create")
def create_user():
    return "New user"
