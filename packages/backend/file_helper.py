from subprocess import run
from os import mkdir, chdir, listdir, access, path


class FileHelper:
    """
    Helper functions for file operations.
    """

    @staticmethod
    def is_this_exists(file_path: str) -> bool:
        """
        is_this_exists checks if a file exists.

        :param file_path: The path to the file.
        :type file_path: str
        :return: True if the file exists, False otherwise.
        :rtype: bool
        """
        return access(file_path, 0)

    @staticmethod
    def open_this(file_path: str) -> bool:
        """
        open_this opens a file.

        :param file_path: The path to the file.
        :type file_path: str
        :return: True if the file exists, False otherwise.
        :rtype: bool
        """
        return run(f"xdg-open {file_path}", shell=True).returncode == 0

    @staticmethod
    def create_directory(file_path: str) -> bool:
        """
        create_directory creates a directory.

        :param file_path: The path to the directory.
        :type file_path: str
        :return: True if the directory was created, False otherwise.
        :rtype: bool
        """
        try:
            mkdir(file_path)
            return True

        except Exception as e:
            print("Error: ", e)
            print("Location:", path.realpath(__file__))
            return False

    @staticmethod
    def change_directory(file_path: str) -> bool:
        """
        change_directory changes the current working directory.

        :param file_path: The path to the directory.
        :type file_path: str
        :return: True if the directory was changed, False otherwise.
        :rtype: bool
        """
        try:
            chdir(file_path)
            return True

        except Exception as e:
            print("Error: ", e)
            print("Location:", path.realpath(__file__))
            return False

    @staticmethod
    def list_directory(file_path: str) -> list or bool:
        """
        list_directory lists the contents of a directory.

        :param file_path: The path to the directory.
        :type file_path: str
        :return: A list of the contents of the directory or False if the directory does not exist.
        :rtype: list or bool
        """
        try:
            dir_list = listdir(file_path)
            for index in range(len(dir_list)):
                dir_list[index] = f"{file_path}/{dir_list[index]}"
            return dir_list

        except Exception as e:
            print("Error: ", e)
            print("Location:", path.realpath(__file__))
            return False

    @staticmethod
    def create_file(file_path: str, data: str) -> bool:
        """
        create_file creates a file.

        :param file_path: The path to the file.
        :type file_path: str
        :param data: Data to be written to the file.
        :type data: str
        :return: True if the file was created, False otherwise.
        :rtype: bool
        """
        try:
            with open(file_path, "w") as file:
                file.write(data)
            return True

        except Exception as e:
            print("Error: ", e)
            print("Location:", path.realpath(__file__))
            return False

    @staticmethod
    def find_ports(file_path: str) -> list or bool:
        """
        find_ports finds the ports of a file.

        :param file_path: The path to the file.
        :type file_path: str
        :return: A list of the ports of the file or False if the file does not exist.
        :rtype: list or bool
        """
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
            print("Location:", path.realpath(__file__))
            return False

    @staticmethod
    def change_ports(file_path: str, port_list: list) -> bool:
        """
        change_ports changes the ports of a file.

        :param file_path: The path to the file.
        :type file_path: str
        :param port_list: A list of the ports to be changed.
        :type port_list: list
        :return: True if the ports were changed, False otherwise.
        :rtype: bool
        """
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
            print("Location:", path.realpath(__file__))
            return False
