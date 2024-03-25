#!/usr/bin/python3
"""

This script starts a Flask web application listenting
on 0.0.0.0, port 5000

Providing one route:
    /hbnb_filters: displays a list of states and amenities in
    an HTML page

"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a web page of all states and amenities
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(response_or_exc=None):
    """
    This function removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
