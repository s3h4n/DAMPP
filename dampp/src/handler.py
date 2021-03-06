from ..packages import Ui_MainWindow
from ..packages import FileHelper
from PyQt5 import QtWidgets
from pathlib import Path
from . import constants
import sys


class Handler:
    """
    Handles the whole application.
    """

    def __init__(self) -> None:
        """
        __init__ initializes the class.
        """
        self.file = FileHelper()
        self.home = Path.home()
        self.main_directory = f"{self.home}/{constants.MAIN_DIR}"

    def handler(self) -> None:
        """
        handler will handle the whole application.
        """
        if self.file.is_this_exists(self.main_directory) != True:
            self.file.create_directory(self.main_directory)

        if self.file.is_this_exists(self.main_directory) == True:
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            app.exec()
