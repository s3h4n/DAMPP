from subprocess import run


class DockerHelper:
    """
    Helper functions for docker-compose.
    """

    @staticmethod
    def is_docker_installed() -> bool:
        """
        is_docker_installed checks if docker is installed on the system.

        :return: True if docker is installed, False otherwise.
        :rtype: bool
        """
        return run(["docker", "--version"]).returncode == 0

    @staticmethod
    def is_docker_running() -> bool:
        """
        is_docker_running checks if docker is running on the system.

        :return: True if docker is running, False otherwise.
        :rtype: bool
        """
        return run(["docker", "info"]).returncode == 0

    @staticmethod
    def is_compose_installed() -> bool:
        """
        is_compose_installed checks if docker-compose is installed on the system.

        :return: True if docker-compose is installed, False otherwise.
        :rtype: bool
        """
        return run(["docker-compose", "--version"]).returncode == 0

    @staticmethod
    def is_compose_running() -> bool or int:
        """
        is_compose_running checks if docker-compose is running on the system.

        :return: True if docker-compose is running, False otherwise. -1 if containers are removed.
        :rtype: bool or int
        """
        result = (
            run(["docker-compose", "ps"], text=True, capture_output=True)
            .stdout.strip()
            .split("\n")
        )

        for line in result:
            if "Up" in line:
                return True
            if "Exit" in line:
                return False

        return -1

    @staticmethod
    def start() -> bool:
        """
        start starts the docker containers.

        :return: True if docker-compose is started, False otherwise.
        :rtype: bool
        """
        return run(["docker-compose", "up", "-d"]).returncode == 0

    @staticmethod
    def stop() -> bool:
        """
        stop stops the docker containers.

        :return: True if docker-compose is stopped, False otherwise.
        :rtype: bool
        """
        return run(["docker-compose", "stop"]).returncode == 0

    @staticmethod
    def remove() -> bool:
        """
        remove removes the docker containers.

        :return: True if docker-compose is removed, False otherwise.
        :rtype: bool
        """
        return run(["docker-compose", "down"]).returncode == 0
