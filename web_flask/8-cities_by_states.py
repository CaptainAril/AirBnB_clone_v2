#!/usr/bin/python3
""" Starts a flask web app."""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_and_cities():
    """Renders cities and states."""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_db(exception):
    """Removes SQLAlchemy session after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
