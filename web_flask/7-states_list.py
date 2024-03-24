#!/usr/bin/python3
"""
This script starts a Flask web application listenting
on 0.0.0.0, port 5000

Providing only one route:
    /states_list: displays a list of states in an HTML page
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(response_or_exc):
    """
    This function removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """
    This function returns a web page of all states
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html',
                           states=sorted(states, key=lambda x:x.name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
