from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/dogs', methods=["POST", "GET",])
def dogs():
    return "dogs"


@app.route('/dogs/<id>', methods=["GET", "POST", "DELETE"])
def createdogs(id):
    request.method
    if request.method == "GET":
        return f"dog:{id}. method was: GET"
    if request.method == "POST":
        return f"dog:{id}. method was: POST"
    if request.method == "DELETE":
        return f"dog:{id}. method was: DELETE"


if __name__ == "__main__":
    app.run(debug=True)