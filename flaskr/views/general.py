from flask import Blueprint
from flaskr import db

mod = Blueprint("general", __name__)


@mod.route("/")
def test_backend():
    return "This is the working backend"


@mod.route("/db")
def test_db_route():
    return db.test_db()


@mod.route("/login")
def login():
    return "Login to the site"
