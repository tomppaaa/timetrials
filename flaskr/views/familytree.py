from flask import Blueprint

mod = Blueprint("familytree", __name__)


@mod.route("/familytree")
def show_familytree():
    return "All of the familytree things"


@mod.route("/familytree/add")
def add_member_familytree():
    return "New member to the familytree"
