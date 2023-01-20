from flask import Flask

app = Flask(__name__)


@app.route("/")
def test():
    return "This is the familytree backend"


if __name__ == "__main__":
    app.run(debug=True)
