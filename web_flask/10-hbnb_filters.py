#!/usr/bin/python3
"""This module starts a flask web app that renders list of states."""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    return render_template('6-index.html', storage=storage)

@app.teardown_appcontext
def teardown(exception):
    """removes current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
