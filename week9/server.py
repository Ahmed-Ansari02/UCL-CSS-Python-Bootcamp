from flask import Flask, render_template

server = Flask(__name__)

@server.route("/")
def helloworld():
    return "Hello world"

@server.route("/congratulate")
def hello():
    return render_template("index.html")

@server.route("/user/<name>")
def userName(name):
    return f"Hi there {name}"


if __name__ == "__main__":
    server.run()