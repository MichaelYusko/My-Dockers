"""Main application file"""

from flask import Flask, render_template

from dockers.docker_info import DockerInfo

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def index():
    """Index route"""
    dockers = DockerInfo().all_container_names()
    return render_template('index.html', dockers=dockers)
