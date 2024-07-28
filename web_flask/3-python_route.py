#!/usr/bin/python3
"""module"""
from flask import Flask
from flask import render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/")
def hello_world():
    """basic function"""
    return "Hello HBNB!"


@app.route("/hbnb")
def h():
    """another function"""
    return "HBNB"


@app.route("/c/<text>")
def i(text):
    """"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/")
@app.route("/python/<text>")
def j(text=None):
    """"""
    if not text:
        return "Python is cool"
    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
