from PyQt6 import QtCore, QtGui, QtWidgets


class About(object):
    def show(self) -> None:

        self.about = QtWidgets.QDialog()
        self.about.setObjectName("Dialog")
        self.about.setFixedSize(400, 390)
        self.about.setStyleSheet("")

        self.ok_btn = QtWidgets.QDialogButtonBox(self.about)
        self.ok_btn.setGeometry(QtCore.QRect(10, 330, 380, 50))
        self.ok_btn.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.ok_btn.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.ok_btn.setCenterButtons(True)
        self.ok_btn.setObjectName("ok_btn")

        self.details = QtWidgets.QLabel(self.about)
        self.details.setGeometry(QtCore.QRect(10, 10, 380, 320))

        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        self.details.setFont(font)
        self.details.setStyleSheet("")
        self.details.setWordWrap(True)
        self.details.setObjectName("details")

        self.retranslateUi(self.about)

        self.ok_btn.accepted.connect(self.about.accept)
        self.ok_btn.rejected.connect(self.about.reject)

        QtCore.QMetaObject.connectSlotsByName(self.about)

        self.about.exec()

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate

        Dialog.setWindowTitle(_translate("Dialog", "About"))

        self.details.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p align="center"><span style=" color:#ed333b; font-weight:bold;">DAMPP</span></p><p align="center"><span style=" font-size:12pt; color:#000000; font-weight:bold;">Dockerized Apache MySQL PHP</span></p><p align="center"><span style=" font-size:12pt; font-weight:400;">Dampp is a simple tool to create and run simple web servers inside your computer. It will use Docker images to configure and run the service.</span></p><p align="center"><span style=" font-size:12pt; font-weight:400;">Developed by Sehan Weerasekara.</span></p><p align="center"><a href="www.github.com/s3h4n"><span style=" font-size:12pt; font-weight:400; text-decoration: underline; color:#0000ff;">Github</span></a></p></body></html>',
            )
        )
