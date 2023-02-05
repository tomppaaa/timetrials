import flaskr


def create_db():
    print("Initializing the db...")


def test_db():
    print("TESTING THE DB ***********************")

    with flaskr.app.app_context():

        sql = "DROP TABLE IF EXISTS test"
        flaskr.db.session.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS test (id int primary key, greeting text)"
        flaskr.db.session.execute(sql)

        sql = "INSERT INTO test (id, greeting) VALUES (1, 'hello')"
        flaskr.db.session.execute(sql)

        result = flaskr.db.session.execute("SELECT * FROM test").fetchall()
        print(result)

    return "Working lol"
