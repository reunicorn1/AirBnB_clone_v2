#!/usr/bin/python3
"""
This script starts a web application listening on
0.0.0.0, port 5000

with six routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value text
    /python/<text>: display “Python ”, followed by the value of text
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display a HTML page if n is an integer
    """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    This function dispays a web page of "Hello HBNB!”
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function displays "HBNB" web page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    This function displays "C ” followed by the value of the text
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text=None):
    """
    This function displays "Python ” followed by the value of the text
    """
    if not text:
        text = "is_cool"
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This function displays “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This function displays an HTML page with the number
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """
    This function displays an HTML page with the number
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
