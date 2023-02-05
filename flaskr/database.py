from os import getenv
from flaskr import app
from flask_sqlalchemy import SQLAlchemy
from random import randint


app.config["SQLALCHEMY_DATABASE_URI"] = getenv("POSTGRES_URL")
db = SQLAlchemy(app)


def create_db():
    print("Initializing the db...")

    sqllist = [
        "CREATE TABLE IF NOT EXISTS users (id int primary key, name varchar(80), password varchar(80));",
        "CREATE TABLE IF NOT EXISTS games (id int primary key, name varchar(80));",
        "CREATE TABLE IF NOT EXISTS courses (id int primary key, name varchar(80), game_id int references games(id));",
        "CREATE TABLE IF NOT EXISTS standards (id int primary key, name varchar(50), tier varchar(3), points numeric, game_id int references games(id), course_id int references courses(id));",
        "CREATE TABLE IF NOT EXISTS times (id int primary key, game_id int references games(id), course_id int references courses(id), timems varchar(80), date date);",
    ]

    with app.app_context():
        for sql in sqllist:
            db.session.execute(sql)
            db.session.commit()

    print("Db initialization completed.")
    return "Success"


def test_db():
    print("TESTING THE DB ***********************")

    with app.app_context():

        sql = "DROP TABLE IF EXISTS test;"
        db.session.execute(sql)
        db.session.commit()

        sql = "CREATE TABLE IF NOT EXISTS test (id int primary key, greeting text);"
        db.session.execute(sql)
        db.session.commit()

        sql = f"INSERT INTO test (id, greeting) VALUES ({randint(1,100)}, 'hello');"
        db.session.execute(sql)
        db.session.commit()

        result = db.session.execute("SELECT * FROM test;").fetchall()
        print(result)

    return "Working lol"
