from PyQt6 import QtCore, QtWidgets
from ....src import constants
from ...backend import FileHelper
from ....src import constants


class EditPort(object):
    def __init__(self) -> None:
        self.file = FileHelper()
        self.env_file_name = constants.ENVFILE_NAME
        self.current_ports = self.file.find_ports(self.env_file_name)
        self.web_port_keyword = constants.WEB_PORT
        self.db_port_keyword = constants.DB_PORT
        self.pma_port_keyword = constants.PMA_PORT

    def show(self):

        self.edit_ports = QtWidgets.QDialog()
        self.edit_ports.setObjectName("Dialog")
        self.edit_ports.setFixedSize(530, 220)

        self.web_port_label = QtWidgets.QLabel(self.edit_ports)
        self.web_port_label.setGeometry(QtCore.QRect(20, 20, 140, 50))
        self.web_port_label.setObjectName("web_port_label")

        self.web_port = QtWidgets.QLineEdit(self.edit_ports)
        self.web_port.setGeometry(QtCore.QRect(20, 70, 150, 50))
        self.web_port.setObjectName("web_port")
        self.web_port.setText(self.current_ports[self.web_port_keyword])
        self.web_port.textChanged.connect(self.port_validate)

        self.db_port_label = QtWidgets.QLabel(self.edit_ports)
        self.db_port_label.setGeometry(QtCore.QRect(190, 20, 150, 50))
        self.db_port_label.setObjectName("db_port")

        self.db_port = QtWidgets.QLineEdit(self.edit_ports)
        self.db_port.setGeometry(QtCore.QRect(190, 70, 150, 50))
        self.db_port.setObjectName("db_port_label")
        self.db_port.setText(self.current_ports[self.db_port_keyword])
        self.db_port.textChanged.connect(self.port_validate)

        self.pma_port_label = QtWidgets.QLabel(self.edit_ports)
        self.pma_port_label.setGeometry(QtCore.QRect(360, 20, 130, 50))
        self.pma_port_label.setObjectName("pma_port_label")

        self.pma_port = QtWidgets.QLineEdit(self.edit_ports)
        self.pma_port.setGeometry(QtCore.QRect(360, 70, 150, 50))
        self.pma_port.setObjectName("pma_port")
        self.pma_port.setText(self.current_ports[self.pma_port_keyword])
        self.pma_port.textChanged.connect(self.port_validate)

        self.error_label = QtWidgets.QLabel(self.edit_ports)
        self.error_label.setGeometry(QtCore.QRect(20, 153, 500, 50))
        self.error_label.setObjectName("error_label")

        self.confirm_btn = QtWidgets.QPushButton(self.edit_ports)
        self.confirm_btn.setGeometry(QtCore.QRect(400, 160, 108, 34))
        self.confirm_btn.setObjectName("confirm_btn")
        self.confirm_btn.clicked.connect(self.edit_ports.accept)
        self.confirm_btn.setText("Confirm")

        self.retranslateUi(self.edit_ports)

        QtCore.QMetaObject.connectSlotsByName(self.edit_ports)

        if self.edit_ports.exec():
            result = [
                [self.web_port_keyword, self.web_port.text()],
                [self.db_port_keyword, self.db_port.text()],
                [self.pma_port_keyword, self.pma_port.text()],
            ]
            return self.edit_ports(result)
        else:
            return False

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "Edit Ports"))

        self.db_port_label.setText(_translate("Dialog", "MySQL"))
        self.pma_port_label.setText(_translate("Dialog", "PhpMyAdmin"))
        self.web_port_label.setText(_translate("Dialog", "Apache/PHP"))

    def port_validate(self, input_box):

        if (
            not input_box.isdigit()
            or input_box == ""
            or int(input_box) < 1024
            or int(input_box) > 65535
        ):
            self.confirm_btn.setEnabled(False)
            self.error_label.setText("<i style='color:red'>*Invalid port number</i>")
        else:
            self.confirm_btn.setEnabled(True)
            self.error_label.setText("")

    def edit_ports(self, new_ports):
        if self.file.change_ports(new_ports):
            self.edit_ports.close()
            return True

        self.edit_ports.close()
        return False
