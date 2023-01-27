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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns `Python` + text."""
    str = 'Python ' + text.replace('_', ' ')
    return str


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Displays `<n> is a number`."""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
