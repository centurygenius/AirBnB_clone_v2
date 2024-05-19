#!/usr/bin/python3
""" Script that starts a flask web application including methods """

from flask import Flask


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
    return 'C {}'.format(text)


@app.route('/python/<text>')
def python_text(text='is cool'):
    """ 
        Replaces variable 'text' with another
        value when different from the default
    """
    text = text.replace('_', ' ')
    if text=='is cool':
        return 'Python is cool'
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

