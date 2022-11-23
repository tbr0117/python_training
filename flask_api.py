from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/overview")
def show_description():
    return "your at location on of overview page"

@app.route("/details/<name>")
def show_details(name):
    return f"your at location on details page of user {escape(name)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)