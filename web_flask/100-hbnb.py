#!/usr/bin/python3
"""This module starts a flask web app."""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Loads and renders storage"""
    return render_template('100-hbnb.html', storage=storage)

@app.teardown_appcontext
def teardown(exception):
    """removes current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
