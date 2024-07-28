#!/usr/bin/python3
"""module"""
from flask import Flask, abort, render_template
from markupsafe import escape
# from ..models.engine import storage
# from ..models.state import State
from models import storage
from models.state import State
from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def hay(error=None):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def hello_world():
    """basic function"""
    dict = {}
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        for state in states:
            s = f"{state.id}.{state.name}"
            dict[s] = sorted(list(state.cities), key=lambda x: x.name)
    else:
        for state in states:
            s = f"{state.id}.{state.name}"
            dict[s] = sorted(state.cities(), key=lambda x: x.name)
    return render_template("8-cities_by_states.html", dict=dict)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
