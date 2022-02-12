"""
    Name       : DAMPP
    Version    : 1.0
    Description: DAMPP is a program that allows you to create dockerized
                 containers that are able to run simple Apache Php web servers.
    Author     : Sehan Weerasekara (s3h4n)
    Date       : 12-02-2022
    Contact    : https://github.com/s3h4n
"""

from .src import Handler


def main() -> None:
    """
    main is the entry point for the program.
    """
    Handler().handler()


if __name__ == "__main__":
    main()
