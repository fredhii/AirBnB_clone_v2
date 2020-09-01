#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """ states_list_route """
    res = []
    storage.reload()

    for v in storage.all("State").values():
        res.append([v.id, v.name])

    return render_template("7-states_list.html", states=res)


@app.teardown_appcontext
def teardown_db(exception):
    """ Close session to database """
    storage.close()


if __name__ == "__main__":
    app.run()
