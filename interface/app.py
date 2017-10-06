"""Main application file"""

from flask import Flask, render_template

from dockers.docker_info import DockerInfo

app = Flask(__name__)  # pylint: disable=invalid-name

docker_client = DockerInfo()  # pylint: disable=invalid-name


@app.route('/')
def index():
    """Index route"""
    container_names = docker_client.all_container_names()
    image_names = docker_client.all_image_names()
    containers = docker_client.all_container_objects()

    return render_template('index.html',
                           container_names=container_names,
                           image_names=image_names,
                           containers=containers)
