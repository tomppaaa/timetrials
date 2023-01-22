from flask import Flask

from flaskr.views import general
from flaskr.views import forum
from flaskr.views import users

app = Flask(__name__)


app.register_blueprint(general.mod)
app.register_blueprint(forum.mod)
app.register_blueprint(users.mod)
