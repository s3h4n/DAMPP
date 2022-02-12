from ..packages import Ui_MainWindow
from ..packages import FileHelper
from PyQt6 import QtWidgets
from pathlib import Path
from . import constants
import sys


class Handler:
    def __init__(self) -> None:
        self.file = FileHelper()
        self.home = str(Path.home())
        self.main_directory = constants.MAIN_DIR

    def handler(self) -> None:

        if self.file.is_this_exists(f"{self.home}/{self.main_directory}") != True:
            self.file.create_directory(self.main_directory)

        if self.file.is_this_exists(f"{self.home}/{self.main_directory}") == True:
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            app.exec()
