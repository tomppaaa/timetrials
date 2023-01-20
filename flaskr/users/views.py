from app import app


@app.route("/login")
def login():
    return "Login to the site"


@app.route("/user")
def user():
    return "Account information"


@app.route("/users/create")
def create_user():
    return "New user"
