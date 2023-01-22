from flask import Blueprint

mod = Blueprint("forum", __name__)


@mod.route("/forum")
def show_forum():
    return "All of the forum things"


@mod.route("/forum/add")
def add_new_post():
    return "New member to the familytree"
