#!env/bin/python3
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/user/<username>")
def hello(username):
    return f"Hello, {escape(username)}!"

@app.route("/org/<org_name>")
def hello_from_org(org_name):
    return f"Hello World from {escape(org_name)}!"

@app.route("/org/<org_name>/user/<username>")
def hello_from_org_to_user(org_name, username):
    return f"Hello {escape(username)} from {escape(org_name)}!"
