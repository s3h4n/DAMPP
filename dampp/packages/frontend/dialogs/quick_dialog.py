from PyQt5 import QtWidgets


class Error(object):
    """
    Error will show an error message.

    :param object: self
    :type object: object
    """

    def show(self, message: str) -> None:
        """
        show will show an error message.

        :param message: The message to show.
        :type message: str
        """
        QtWidgets.QMessageBox().critical(None, "Error", message)


class Confirm(object):
    """
    Confirm will show a confirmation message.

    :param object: self
    :type object: object
    """

    def show(self, message: str) -> bool:
        """
        show will show a confirmation message.

        :param message: The message to show.
        :type message: str
        :return: True if the user confirms. False otherwise.
        :rtype: bool
        """
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
