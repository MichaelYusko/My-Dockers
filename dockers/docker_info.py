"""File for all info classes"""
from .base import BaseDockerInfo
from .utils import get_all_fields_by, get_field_by


class DockerInfo(BaseDockerInfo):
    """Docker info class

        ..:: all_containers
            Return an array with container names

        ..:: all_images
            Return an array with image names
    """
    def all_container_names(self):
        """Return all container names"""
        names = get_all_fields_by('Names', self._get_all_containers())
        return names

    def all_image_names(self):
        """Return all images names"""
        images = get_field_by('Image', self._get_all_containers())
        return images

    def all_container_objects(self):
        """Return container objects"""
        return self._get_all_containers()
