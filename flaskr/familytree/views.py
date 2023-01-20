from app import app


@app.route("/familytree")
def familytree():
    return "All of the familytree things"


@app.route("/familytree/add")
def add_member_familytree():
    return "New member to the familytree"
