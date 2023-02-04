import flaskr


def create_db():
    print("Initializing the db...")


def test_db():
    print("TESTING THE DB ***********************")

    with flaskr.app.app_context():

        result = flaskr.db.session.execute("SELECT * FROM test").fetchall()
        print(result)

    return "Working lol"
