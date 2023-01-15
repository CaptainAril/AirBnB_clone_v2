#!/usr/bin/python3
"""Starts a flask web app."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Displays a HTML page of States."""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes SQLAlchemy session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
