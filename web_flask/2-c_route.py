#!/usr/bin/python3
""" Script to start a Flask web application including routes """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Returns 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Returns 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ Replaces variable 'text' with value. """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

