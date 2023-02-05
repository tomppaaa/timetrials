from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import psycopg2

from flaskr.views import general
from flaskr.views import forum
from flaskr.views import users

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = str(getenv("POSTGRES_URL"))
db = SQLAlchemy(app)

app.register_blueprint(general.mod)
app.register_blueprint(forum.mod)
app.register_blueprint(users.mod)
