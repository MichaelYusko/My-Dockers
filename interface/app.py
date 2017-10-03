"""Main application file"""

from flask import Flask, render_template

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def index():
    """Index route"""
    return render_template('index.html')
