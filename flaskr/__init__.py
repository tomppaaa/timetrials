from flask import Flask

from flaskr.views import general
from flaskr.views import familytree
from flaskr.views import users

app = Flask(__name__)


app.register_blueprint(general.mod)
app.register_blueprint(familytree.mod)
app.register_blueprint(users.mod)
