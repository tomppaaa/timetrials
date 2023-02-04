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

dbname = getenv("POSTGRES_DB")
user = getenv("POSTGRES_USER")
password = getenv("POSTGRES_PASSWORD")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{user}:{password}@db:5432/{dbname}"
db = SQLAlchemy(app)

app.register_blueprint(general.mod)
app.register_blueprint(forum.mod)
app.register_blueprint(users.mod)
