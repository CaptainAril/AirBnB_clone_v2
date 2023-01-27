#!/usr/bin/python3
"""Starts a simple flask web app."""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns `Hello HBNB!`"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns `HBNB`."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    """Returns `C` plus <text>"""
    str = 'C ' + text.replace('_', ' ')
    return str


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
