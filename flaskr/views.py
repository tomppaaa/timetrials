from flask import render_template, request

from flaskr import app
from flaskr.database import db, test_db, create_db


@app.route("/")
def test_backend():
    return render_template("home.html")


# TODO show 3 games with most times submitted
@app.route("/games")
def get_games():
    return "List of games"


# TODO show 3 courses with most activity
@app.route("/courses")
def get_courses():
    return "List of courses"


# TODO show 3 newest times submitted
@app.route("/times")
def get_times():
    return "List of times"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return "Todo POST request"


@app.route("/init")
def initialize_db():
    return create_db()


@app.route("/db")
def test_db_route():
    return test_db()
