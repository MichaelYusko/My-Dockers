"""Base file, for all bases classes"""
from docker import APIClient


class BaseDockerInfo:  # pylint: disable=too-few-public-methods
    """Base class for info flow
        Methods:
           ..:: _get_all_containers
               Return all available container names

           ..:: _get_all_containers
                Return all available images names
    """
    def __init__(self):
        self.client = APIClient()

    def _get_all_containers(self):
        """Return all docker containers"""
        return self.client.containers(all=True)

    def _get_all_images(self):
        """Return all docker images"""
        return self.client.images(all=True)
