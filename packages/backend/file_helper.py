from subprocess import run
from os import mkdir, chdir, listdir, access
from pathlib import Path


class FileHelper:
    def __init__(self) -> None:
        self.home = str(Path.home())

    def is_this_exists(self, file_path) -> bool:
        return access(f"{file_path}", 0)

    def open_this(self, file_path) -> bool:
        return run(f"xdg-open {file_path}", shell=True).returncode == 0

    def create_directory(self, file_path) -> bool:
        try:
            mkdir(f"{self.home}/{file_path}")
            return True
        except Exception as e:
            print("Error: ", e)

    def change_directory(self, file_path) -> bool:
        try:
            chdir(f"{file_path}")
            return True
        except:
            return False

    def list_directory(self, file_path: str) -> list:
        try:
            dir_list = listdir(f"{self.home}/{file_path}")
            for index in range(len(dir_list)):
                dir_list[index] = f"{self.home}/{file_path}/{dir_list[index]}"
            return dir_list
        except Exception as e:
            print("Error: ", e)
            return False

    def create_file(self, file_path: str, data: str) -> bool:
        try:
            with open(f"{self.home}/{file_path}", "w") as file:
                file.write(data)
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def find_ports(self, file_path: str) -> list:
        port_list = {}
        keyword = "PORT"

        try:
            with open(file_path, "r") as file:
                for line in file:
                    if keyword in line:
                        port_list[line.split("=")[0]] = line.split("=")[1].strip()
            return port_list
        except Exception as e:
            print("Error: ", e)
            return False

    def change_ports(self, file_path: str, port_list: list) -> bool:
        env_file_data = []
        i = 0

        try:
            with open(file_path, "r") as file:
                env_file_data = file.readlines()
            for index in range(len(env_file_data)):
                if port_list[i][0] in env_file_data[index]:
                    env_file_data[index] = f"{port_list[i][0]}={port_list[i][1]}\n"
                    i += 1
            with open(file_path, "w") as file:
                file.write("".join(env_file_data))
            return True
        except Exception as e:
            print("Error: ", e)
            return False
