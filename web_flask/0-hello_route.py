#!/usr/bin/python3
"""module"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """basic function"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
