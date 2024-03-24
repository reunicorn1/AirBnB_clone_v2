#!/usr/bin/python3
"""

This script starts a Flask web application listenting
on 0.0.0.0, port 5000

Providing only one route:
    /cities_by_states: displays a list of states and their respective
    cities in an HTML page

"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """
    This function returns a web page of all states
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(response_or_exc=None):
    """
    This function removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
