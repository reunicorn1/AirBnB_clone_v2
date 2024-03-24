#!/usr/bin/python3
"""

This script starts a Flask web application listenting
on 0.0.0.0, port 5000

Providing two routes:
    /states: displays a list of states in an HTML page
    /states/<id>: displays the state with the id and its cities

"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    This function returns a web page of all states
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """
    This function returns a webpage accorsing to the id provided
    """
    states = storage.all(State)
    key = "State.{}".format(id)
    state = states.get(key)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(response_or_exc=None):
    """
    This function removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
