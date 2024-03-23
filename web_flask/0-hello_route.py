#!/usr/bin/python3
"""
0. Hello Flask!
"""

from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

app.run(host='0.0.0.0', port=5000)
