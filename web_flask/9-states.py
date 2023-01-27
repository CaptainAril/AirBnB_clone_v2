#!/usr/bin/python3
"""This module starts a flask web app that renders list of states."""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """renders a list of states."""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """renders a list of a state's cities or Not found."""
    states = storage.all('State').values()
    state = None
    for s in states:
        if s.id == id:
            state = s
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    """removes current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
