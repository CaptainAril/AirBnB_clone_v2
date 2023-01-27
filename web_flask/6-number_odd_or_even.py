#!/usr/bin/python3
"""Starts a simple flask web app."""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def render(n):
    """Renders a html template."""
    if isinstance(n, int):
        text = "Number: {}".format(n)
        return render_template('5-number.html', text=text)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Number is odd or even."""
    if n % 2 == 0:
        text = "Number: {} is even".format(n)
    else:
        text = "Number: {} is odd".format(n)
    return render_template('6-number_odd_or_even.html', text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
