from PyQt5 import QtCore, QtWidgets
from ...backend import FileHelper
from ....src import constants
from pathlib import Path


class NewProject(object):
    """
    NewProject will create a new project with the given name and ports.

    :param object: self
    :type object: object
    """

    def __init__(self):
        """
        __init__ will initialize the new project dialog.
        """
        self.home = str(Path.home())
        self.file = FileHelper()
        self.main_directory = f"{self.home}/{constants.MAIN_DIR}"
        self.public_directory = constants.PUBLIC_DIR
        self.env_file_name = constants.ENV_FILE_NAME
        self.docker_compose_name = constants.DOCKER_COMPOSE_NAME
        self.docker_file_name = constants.DOCKERFILE_NAME
        self.php_file_name = constants.PHP_FILE_NAME
        self.projects = self.file.list_directory(self.main_directory)
        self.project_keyword = constants.PROJECT_NAME
        self.web_port_keyword = constants.WEB_PORT
        self.db_port_keyword = constants.DB_PORT
        self.pma_port_keyword = constants.PMA_PORT
        self.dockerfile_data = constants.DOCKERFILE
        self.dockercompose_data = constants.DOCKER_COMPOSE
        self.php_file_data = constants.PHP_FILE

    def show(self) -> bool:
        """
        show will show the new project dialog.

        :return: True if the dialog was created successfully.
        :rtype: bool
        """
        self.new_project = QtWidgets.QDialog()
        self.new_project.setObjectName("Dialog")
        self.new_project.setFixedSize(530, 390)

        self.pname_label = QtWidgets.QLabel(self.new_project)
        self.pname_label.setGeometry(QtCore.QRect(20, 10, 120, 50))
        self.pname_label.setObjectName("pname_label")

        self.p_name = QtWidgets.QLineEdit(self.new_project)
        self.p_name.setGeometry(QtCore.QRect(20, 60, 490, 50))
        self.p_name.setObjectName("p_name")
        self.p_name.textChanged.connect(self.name_validate)

        self.port_section_label = QtWidgets.QLabel(self.new_project)
        self.port_section_label.setGeometry(QtCore.QRect(20, 120, 180, 50))
        self.port_section_label.setObjectName("port_section_label")

        self.line = QtWidgets.QFrame(self.new_project)
        self.line.setGeometry(QtCore.QRect(130, 145, 380, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.web_port_label = QtWidgets.QLabel(self.new_project)
        self.web_port_label.setGeometry(QtCore.QRect(20, 170, 140, 50))
        self.web_port_label.setObjectName("web_port_label")

        self.web_port = QtWidgets.QLineEdit(self.new_project)
        self.web_port.setGeometry(QtCore.QRect(20, 220, 150, 50))
        self.web_port.setObjectName("web_port")
        self.web_port.textEdited.connect(self.port_validate)

        self.db_port_label = QtWidgets.QLabel(self.new_project)
        self.db_port_label.setGeometry(QtCore.QRect(190, 170, 150, 50))
        self.db_port_label.setObjectName("db_port")

        self.db_port = QtWidgets.QLineEdit(self.new_project)
        self.db_port.setGeometry(QtCore.QRect(190, 220, 150, 50))
        self.db_port.setObjectName("db_port_label")
        self.db_port.textChanged.connect(self.port_validate)

        self.pma_port_label = QtWidgets.QLabel(self.new_project)
        self.pma_port_label.setGeometry(QtCore.QRect(360, 170, 130, 50))
        self.pma_port_label.setObjectName("pma_port_label")

        self.pma_port = QtWidgets.QLineEdit(self.new_project)
        self.pma_port.setGeometry(QtCore.QRect(360, 220, 150, 50))
        self.pma_port.setObjectName("pma_port")
        self.pma_port.textChanged.connect(self.port_validate)

        self.error_label = QtWidgets.QLabel(self.new_project)
        self.error_label.setGeometry(QtCore.QRect(20, 300, 500, 50))
        self.error_label.setObjectName("error_label")

        self.confirm_btn = QtWidgets.QPushButton(self.new_project)
        self.confirm_btn.setGeometry(QtCore.QRect(399, 320, 108, 34))
        self.confirm_btn.setEnabled(False)
        self.confirm_btn.setObjectName("confirm_btn")
        self.confirm_btn.clicked.connect(self.new_project.accept)
        self.confirm_btn.setText("Confirm")

        self.retranslateUi(self.new_project)
        QtCore.QMetaObject.connectSlotsByName(self.new_project)

        if self.new_project.exec():
            self.new_project.close()
            return self.create_project()

    def retranslateUi(self, dialog: QtWidgets.QDialog) -> None:
        """
        retranslateUi will translate the new project dialog.

        :param dialog: The new project dialog.
        :type dialog: QtWidgets.QDialog
        """
        _translate = QtCore.QCoreApplication.translate

        dialog.setWindowTitle(_translate("Dialog", "New Project"))

        self.web_port_label.setText(_translate("Dialog", "Apache/PHP"))
        self.pname_label.setText(_translate("Dialog", "Project Name"))
        self.db_port_label.setText(_translate("Dialog", "MySQL"))
        self.port_section_label.setText(_translate("Dialog", "Port Details"))
        self.pma_port_label.setText(_translate("Dialog", "PhpMyAdmin"))

    def name_validate(self) -> None:
        """
        name_validate will validate the project name.
        """
        if len(self.p_name.text()) == 0:
            self.error_label.setText(
                "<i style='color:red'>Project Name is required</i>"
            )
            self.confirm_btn.setEnabled(False)
        else:
            self.error_label.setText("")
            self.confirm_btn.setEnabled(True)

        for project in self.projects:
            project = project.split("/")
            for word in project:
                if word == self.p_name.text():
                    self.error_label.setText(
                        "<i style='color:red'>*Project already exists</i>"
                    )
                    self.confirm_btn.setEnabled(False)

    def port_validate(self, input_box: QtWidgets.QLineEdit) -> None:
        """
        port_validate will validate the port number.

        :param input_box: The input box to validate.
        :type input_box: QtWidgets.QLineEdit
        """
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

    def create_project(self) -> bool:
        """
        create_project will create a new project.

        :return: True if the project was created successfully. False otherwise.
        :rtype: bool
        """
        project_dir = f"{self.main_directory}/{self.p_name.text()}"
        public_dir = f"{project_dir}/{self.public_directory}"
        env_file = f"{project_dir}/{self.env_file_name}"
        docker_file = f"{project_dir}/{self.docker_file_name}"
        compose_file = f"{project_dir}/{self.docker_compose_name}"
        php_file = f"{public_dir}/{self.php_file_name}"

        env_file_data = f"{self.project_keyword}={self.p_name.text()}\n{self.web_port_keyword}={ self.web_port.text()}\n{self.db_port_keyword}={self.db_port.text()}\n{self.pma_port_keyword}={ self.pma_port.text()}"

        if self.file.create_directory(project_dir):
            if self.file.create_directory(public_dir):
                if self.file.create_file(env_file, env_file_data):
                    if self.file.create_file(docker_file, self.dockerfile_data):
                        if self.file.create_file(compose_file, self.dockercompose_data):
                            if self.file.create_file(php_file, self.php_file_data):
                                self.new_project.close()
                                return True

        self.new_project.close()
        return False
