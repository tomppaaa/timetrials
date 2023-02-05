from flaskr import app
from flaskr.database import db, test_db, create_db


@app.route("/")
def test_backend():
    return "This is the working backend"


@app.route("/db")
def test_db_route():
    return test_db()


@app.route("/login")
def login():
    return "Login to the site"


@app.route("/init")
def initialize_db():
    return create_db()
