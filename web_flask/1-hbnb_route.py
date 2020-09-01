#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def default_route():
    """ default_route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """hbnb_route """
    return "HBNB"


if __name__ == "__main__":
    app.run()
