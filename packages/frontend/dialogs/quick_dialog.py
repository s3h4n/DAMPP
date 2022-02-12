from PyQt6 import QtWidgets


class Error(object):
    def show(self, message: str) -> None:
        QtWidgets.QMessageBox().critical(None, "Error", message)


class Confirm(object):
    def show(self, message: str) -> None:
        result = QtWidgets.QMessageBox.question(
            None,
            "Confirm",
            message,
            QtWidgets.QMessageBox.StandardButton.Yes,
            QtWidgets.QMessageBox.StandardButton.No,
        )
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
