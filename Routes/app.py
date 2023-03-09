from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/hola")
def hola():
    return "Hola."

@app.route("/user/<string:user>")
def user(user):
    return "Hola " + user

@app.route("numero/<int:n>")
def number(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {}, User: {}".format(id, username)

if __name__ == "__main__":
    app.run(debug=True)