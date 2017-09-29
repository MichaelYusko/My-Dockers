"""File for all info classes"""
from .base import BaseDockerInfo
from .utils import get_all_fields_by


class DockerInfo(BaseDockerInfo):
    """Docker info class

        ..:: all_containers
            Return an array with container names

        ..:: all_images
            Return an array with image names
    """
    def all_containers(self):
        """Return all container names"""
        fields = get_all_fields_by('Names', self._get_all_containers())
        return fields

    def all_images(self):
        """Return all images names"""
        pass
