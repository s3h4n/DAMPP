# Import required modules
from subprocess import run


class DockerHelper:
    def __init__(self) -> None:
        pass

    def is_docker_installed(self) -> bool:
        return run(["docker", "--version"]).returncode == 0

    def is_docker_running(self) -> bool:
        return run(["docker", "info"]).returncode == 0

    def is_compose_installed(self) -> bool:
        return run(["docker-compose", "--version"]).returncode == 0

    def is_compose_running(self) -> bool or int:
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

    def start(self) -> bool:
        return run(["docker-compose", "up", "-d"]).returncode == 0

    def stop(self) -> bool:
        return run(["docker-compose", "stop"]).returncode == 0

    def remove(self) -> bool:
        return run(["docker-compose", "down"]).returncode == 0
