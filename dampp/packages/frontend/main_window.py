from ...src import constants
from ..backend import DockerHelper
from ..backend import FileHelper
from ..backend import ValidateHelper
from .dialogs import About
from .dialogs import EditPort
from .dialogs import NewProject
from .dialogs import Error
from .dialogs import Confirm
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
from sys import exit
import time


class Ui_MainWindow(object):
    """
    Ui_MainWindow is the main window of the application.

    :param object: self
    :type object: object
    """

    def __init__(self) -> None:
        """
        __init__ initializes the main window of the application.
        """
        self.home = Path.home()
        self.main_directory = constants.MAIN_DIR
        self.env_file_name = constants.ENV_FILE_NAME
        self.public_directory = constants.PUBLIC_DIR
        self.docker = DockerHelper()
        self.file = FileHelper()
        self.validate = ValidateHelper()
        self.error = Error()
        self.confirm = Confirm()
        self.about = About()
        self.edit_port_dialog = EditPort()
        self.new_project = NewProject()

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """
        setupUi sets up the main window of the application.

        :param MainWindow: MainWindow
        :type MainWindow: QMainWindow
        """
        if self.validate.dependancy_check() != True:
            self.error.show(self.validate.dependancy_check())
            exit(0)

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("DAMPP")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plocation_label = QtWidgets.QLabel(self.centralwidget)
        self.plocation_label.setGeometry(QtCore.QRect(20, 10, 180, 50))
        self.plocation_label.setObjectName("plocation_label")

        self.plocation = QtWidgets.QComboBox(self.centralwidget)
        self.plocation.setGeometry(QtCore.QRect(20, 60, 590, 50))
        self.plocation.setObjectName("plocation")
        self.plocation.setPlaceholderText("Please Select a Project")

        self.load_projects()

        self.plocation.currentTextChanged.connect(self.goto_project)

        self.start_stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_btn.setGeometry(QtCore.QRect(630, 60, 150, 50))
        self.start_stop_btn.setCheckable(True)
        self.start_stop_btn.setChecked(False)
        self.start_stop_btn.setEnabled(False)
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.start_stop_btn.clicked.connect(self.service_state)

        self.lhost_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lhost_btn.setGeometry(QtCore.QRect(630, 160, 150, 50))
        self.lhost_btn.setEnabled(False)
        self.lhost_btn.setObjectName("lhost_btn")
        self.lhost_btn.clicked.connect(self.open_localhost)

        self.pma_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pma_btn.setGeometry(QtCore.QRect(630, 230, 150, 50))
        self.pma_btn.setEnabled(False)
        self.pma_btn.setObjectName("pma_btn")
        self.pma_btn.clicked.connect(self.open_pma)

        self.flocation_btn = QtWidgets.QPushButton(self.centralwidget)
        self.flocation_btn.setGeometry(QtCore.QRect(630, 300, 150, 50))
        self.flocation_btn.setEnabled(False)
        self.flocation_btn.setObjectName("flocation_btn")
        self.flocation_btn.clicked.connect(self.open_project)

        self.op_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.op_log.setGeometry(QtCore.QRect(20, 160, 590, 370))

        font = QtGui.QFont()
        font.setFamily("Monospace")

        self.op_log.setFont(font)
        self.op_log.setObjectName("op_log")

        self.op_log_label = QtWidgets.QLabel(self.centralwidget)
        self.op_log_label.setGeometry(QtCore.QRect(20, 110, 100, 50))
        self.op_log_label.setObjectName("op_log_label")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 135, 650, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionNew_Project.triggered.connect(self.create_project)

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.actionEdit_Ports = QtWidgets.QAction(MainWindow)
        self.actionEdit_Ports.setObjectName("actionEdit_Ports")
        self.actionEdit_Ports.setEnabled(False)
        self.actionEdit_Ports.triggered.connect(self.edit_ports)

        self.actionRemove_Services = QtWidgets.QAction(MainWindow)
        self.actionRemove_Services.setObjectName("actionRemove_Services")
        self.actionRemove_Services.setEnabled(False)
        self.actionRemove_Services.triggered.connect(self.remove_services)

        self.actionDAMPP_Help = QtWidgets.QAction(MainWindow)
        self.actionDAMPP_Help.setObjectName("actionDAMPP_Help")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about.show)

        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.menuTools.addAction(self.actionEdit_Ports)
        self.menuTools.addAction(self.actionRemove_Services)

        self.menuHelp.addAction(self.actionDAMPP_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.actionQuit.triggered.connect(self.exit_app)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """
        retranslateUi translates the UI.

        :param MainWindow: The main window.
        :type MainWindow: QMainWindow
        """
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "DAMPP"))

        self.start_stop_btn.setText(_translate("MainWindow", "Start"))
        self.plocation_label.setText(_translate("MainWindow", "Project Location"))
        self.op_log_label.setText(_translate("MainWindow", "Output Log"))
        self.lhost_btn.setText(_translate("MainWindow", "Localhost"))
        self.pma_btn.setText(_translate("MainWindow", "PhpMyAdmin"))
        self.flocation_btn.setText(_translate("MainWindow", "File Location"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_Project.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionEdit_Ports.setText(_translate("MainWindow", "Edit Ports"))
        self.actionEdit_Ports.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionRemove_Services.setText(_translate("MainWindow", "Remove Services"))
        self.actionRemove_Services.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.actionDAMPP_Help.setText(_translate("MainWindow", "DAMPP Help"))
        self.actionDAMPP_Help.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionAbout.setText(_translate("MainWindow", "About "))

    def load_projects(self) -> None:
        """
        load_projects loads the projects from the main directory.
        """
        self.plocation.clear()

        for project in self.file.list_directory(f"{self.home}/{self.main_directory}"):
            self.plocation.addItem(project)

    def goto_project(self) -> None:
        """
        goto_project goes to the selected project.
        """
        self.directory = self.plocation.currentText()

        self.file.change_directory(self.directory)

        if self.validate.requirement_check() != True:
            self.button_state(False)
            self.action_state(False)
            self.create_log(self.validate.requirement_check())
        else:
            self.button_state(True)
            self.action_state(True)
            self.create_log(
                "<span style='color:green;'>All the requirements are met.</span>"
            )
            self.port = self.file.find_ports(self.env_file_name)

    def create_log(self, message: str) -> None:
        """
        create_log creates the log.

        :param message: The message to be displayed.
        :type message: str
        """
        self.current_time = time.localtime()
        self.current_time = time.strftime("%H:%M:%S", self.current_time)

        self.op_log.append(
            "<html><body>"
            + "<b style='color:blue;'>"
            + f"[{self.current_time}]"
            + "</b>"
            + " >>> "
            + message
            + "<br/></body></html>"
        )

    def button_state(self, state: bool) -> None:
        """
        button_state changes the state of the buttons.

        :param state: The state of the buttons.
        :type state: bool
        """
        self.start_stop_btn.setEnabled(state)
        self.lhost_btn.setEnabled(state)
        self.pma_btn.setEnabled(state)
        self.flocation_btn.setEnabled(state)

    def action_state(self, state: bool) -> None:
        """
        action_state changes the state of the actions.

        :param state: The state of the actions.
        :type state: bool
        """
        self.actionEdit_Ports.setEnabled(state)
        self.actionRemove_Services.setEnabled(state)

    def service_state(self) -> None:
        """
        service_state changes the state of the services.
        """
        ready_msg_1 = "Starting..."
        ready_msg_2 = "Stopping..."
        success_msg_1 = "Service started."
        success_msg_2 = "Service stopped."
        error_msg_1 = "Service failed to start."
        error_msg_2 = "Service failed to stop."
        btn_state = self.start_stop_btn.isChecked()

        if btn_state:
            self.create_log(ready_msg_1)
            self.start_stop_btn.setText("Stop")
            if self.docker.start():
                self.create_log(success_msg_1)
            else:
                self.create_log(error_msg_1)
                self.error.show(error_msg_1)
        else:
            self.create_log(ready_msg_2)
            self.start_stop_btn.setText("Start")
            if self.docker.stop():
                self.create_log(success_msg_2)
            else:
                self.create_log(error_msg_2)
                self.error.show(error_msg_2)

    def open_localhost(self) -> None:
        """
        open_localhost opens the localhost.
        """
        ready_msg = "Opening localhost..."
        success_msg = "Opened localhost."
        warning_msg = "Please start the service first."
        error_msg = "Failed to open localhost."
        url = f"http://localhost:{self.port['WEB_PORT']}"

        if self.start_stop_btn.isChecked():
            self.create_log(ready_msg)
            try:
                self.file.open_this(url)
                self.create_log(success_msg)
            except:
                self.create_log(error_msg)
                self.error.show(error_msg)
        else:
            self.create_log(warning_msg)
            self.error.show(warning_msg)

    def open_pma(self) -> None:
        """
        open_pma opens the phpmyadmin.
        """
        ready_msg = "Opening phpmyadmin..."
        success_msg = "Opened phpmyadmin."
        warning_msg = "Please start the service first."
        error_msg = "Failed to open phpmyadmin."
        url = f"http://localhost:{self.port['PMA_PORT']}"

        if self.start_stop_btn.isChecked():
            self.create_log(ready_msg)
            try:
                self.file.open_this(url)
                self.create_log(success_msg)
            except:
                self.create_log(error_msg)
                self.error.show(error_msg)
        else:
            self.create_log(warning_msg)
            self.error.show(warning_msg)

    def open_project(self) -> None:
        """
        open_project opens the project.
        """

        success_msg = "Opened project."
        error_msg = "Failed to open project folder."
        url = f"{self.directory}/{self.public_directory}"

        self.create_log("Opening project...")

        try:
            self.file.open_this(url)
            self.create_log(success_msg)
        except:
            self.create_log(error_msg)
            self.error.show(error_msg)

    def create_project(self) -> None:
        """
        create_project creates the project.
        """
        ready_msg = "Adding new project..."
        success_msg = "Project created."
        error_msg = "Failed to create project."

        self.create_log(ready_msg)

        if self.new_project.show():
            self.create_log(success_msg)
        else:
            self.create_log(error_msg)
            self.error.show(error_msg)

        self.load_projects()

    def exit_app(self) -> None:
        """
        exit_app will exit the application.
        """
        ready_msg = "Stopping services..."
        confirm_msg = "Are you sure you want to quit?"
        success_msg = "Exited."
        cancel_msg = "Exiting canceled."

        if self.confirm.show(confirm_msg):
            self.create_log(ready_msg)
            self.docker.stop()
            self.create_log(success_msg)
            exit()
        else:
            self.create_log(cancel_msg)

    def edit_ports(self) -> None:
        """
        edit_ports will edit the ports.
        """
        ready_msg = "Editing ports..."
        success_msg = "Ports edited."
        warning_msg = "Please start the service first."
        error_msg = "Failed to edit ports."

        self.create_log(ready_msg)

        if not self.start_stop_btn.isChecked():
            result = self.edit_port_dialog.show()
            if result != False:
                self.create_log(success_msg)
            else:
                self.create_log(error_msg)
                self.error.show(error_msg)
        else:
            self.create_log(warning_msg)
            self.error.show(warning_msg)

        self.port = self.file.find_ports(self.env_file_name)

    def remove_services(self) -> None:
        """
        remove_services will remove the services.
        """
        ready_msg = "Removing services..."
        confirm_msg = "Are you sure you want to remove the services?"
        success_msg = "Services removed."
        warning_msg = "Please start the service first."
        error_msg = "Failed to remove services."
        cancel_msg = "Services removal canceled."

        if not self.start_stop_btn.isChecked():
            self.create_log(ready_msg)
            if self.confirm.show(confirm_msg):
                if self.docker.remove():
                    self.create_log(success_msg)
                else:
                    self.create_log(error_msg)
                    self.error.show(error_msg)
            else:
                self.create_log(cancel_msg)
        else:
            self.create_log(warning_msg)
            self.error.show(warning_msg)
