from flask import Blueprint

mod = Blueprint("general", __name__)


@mod.route("/")
def test_backend():
    return "This is the working backend"


@mod.route("/login")
def login():
    return "Login to the site"
