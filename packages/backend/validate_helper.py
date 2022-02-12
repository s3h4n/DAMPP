from .docker_helper import DockerHelper
from .file_helper import FileHelper
from ...src import constants
from pathlib import Path


class ValidateHelper:
    """
    Helper functions for validation.
    """

    def __init__(self) -> None:
        """
        __init__ initializes the class.
        """
        self.home = Path.home()
        self.docker = DockerHelper()
        self.file = FileHelper()
        self.main_dir = f"{self.home}/{constants.MAIN_DIR}"
        self.env_file_name = constants.ENV_FILE_NAME
        self.docker_compose_name = constants.DOCKER_COMPOSE_NAME
        self.docker_file_name = constants.DOCKERFILE_NAME

    def dependancy_check(self) -> str or bool:
        """
        dependancy_check checks if the dependancies are installed.

        :return: Error message if the dependancies are not installed, True otherwise.
        :rtype: str or bool
        """
        if not self.docker.is_docker_installed():
            return "Docker is not installed.\nPlease install docker first."
        elif not self.docker.is_docker_running():
            return "Docker is not running.\nPlease start docker first."

        if not self.docker.is_compose_installed():
            return (
                "docker-compose is not installed.\nPlease install docker-compose first."
            )

        if not self.file.is_this_exists(self.main_dir):
            self.file.create_directory(self.main_dir)

        return True

    def requirement_check(self) -> str or bool:
        """
        requirement_check checks if the requirements are met.

        :return: Error message if the requirements are not met, True otherwise.
        :rtype: str
        """
        if not self.file.is_this_exists(self.env_file_name):
            return "<span style='color:red;'>.env environment file is not found. Please create a new project before using DAMPP.</span>"

        if not self.file.is_this_exists(self.docker_compose_name):
            return "<span style='color:red;'>docker-compose.yml file is not found. Please create a new project before using DAMPP.</span>"

        if not self.file.is_this_exists(self.docker_file_name):
            return "<span style='color:red;'>Dockerfile file is not found. Please create a new project before using DAMPP.</span>"

        return True
