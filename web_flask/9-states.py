#!/usr/bin/python3
"""module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def hay(error=None):
    """teardown app context"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def hello_world2(id=None):
    """basic function"""
    if id is not None:
        name = ''
        states = storage.all(State).values()
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            for state in states:
                if state.id == id:
                    name = state.name
                    li = sorted(list(state.cities), key=lambda x: x.name)
                    break
        else:
            for state in states:
                if state.id == id:
                    name = state.name
                    li = sorted(state.cities(), key=lambda x: x.name)
                    break
        if name == '':
            return render_template("9-states.html", name=None, li=None,
                                   states=None)
        return render_template("9-states.html", name=name, li=li, states=None)
    else:
        states = sorted(storage.all(State).values(), key=lambda x: x.name)
        if len(states) == 0:
            pass
        return render_template("9-states.html", name=None, li=None,
                               states=states)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
