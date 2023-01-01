# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'floorAdmin_Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from login import gui as G
from floorAdmin import viewReservationsFAN as VR
import updateRoomStatus as UR
import rateResident as RS


def close():
    floorAdmin_Dashboard.close()
    pass

class Ui_floorAdmin_Dashboard(object):
    def logOut(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def back(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def showReservations2(self):
        self.viewReservations = QtWidgets.QMainWindow()
        self.ui = VR.Ui_viewReservations()
        self.ui.setupUi(self.viewReservations)
        self.viewReservations.show()
        # Admin_Dashboard.close()

    def updateRoomStatus(self):
        self.updateRoomStatus = QtWidgets.QMainWindow()
        self.ui = UR.Ui_updateRoomStatus()
        self.ui.setupUi(self.updateRoomStatus)
        self.updateRoomStatus.show()
        # Admin_Dashboard.close()
    def rateResident(self):
        self.rateResident = QtWidgets.QMainWindow()
        self.ui = RS.Ui_rateResident()
        self.ui.setupUi(self.rateResident)
        self.rateResident.show()
        # Admin_Dashboard.close()


    def setupUi(self, floorAdmin_Dashboard):
        floorAdmin_Dashboard.setObjectName("floorAdmin_Dashboard")
        floorAdmin_Dashboard.resize(1200, 600)
        floorAdmin_Dashboard.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(floorAdmin_Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut())
        self.logOutButton.setGeometry(QtCore.QRect(1080, 40, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logOutButton.setFont(font)
        self.logOutButton.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(logout (2).png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.logOutButton.setText("")
        self.logOutButton.setObjectName("logOutButton")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(430, 250, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel_2.setFont(font)
        self.adminDashboardLabel_2.setStyleSheet("color: rgb(41, 84, 125);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel_2.setObjectName("adminDashboardLabel_2")
        self.reservationsButton = QtWidgets.QPushButton(self.centralwidget,  clicked=lambda: self.showReservations2())
        self.reservationsButton.setGeometry(QtCore.QRect(820, 440, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.reservationsButton.setFont(font)
        self.reservationsButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}"
)
        self.reservationsButton.setObjectName("reservationsButton")
        self.rateButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.rateResident())
        self.rateButton.setGeometry(QtCore.QRect(50, 440, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.rateButton.setFont(font)
        self.rateButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}"
)
        self.rateButton.setObjectName("rateButton")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 40, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back())
        self.backButton.setGeometry(QtCore.QRect(960, 40, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(left-arrow-in-circular-button.png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.roomButtom = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.updateRoomStatus())
        self.roomButtom.setGeometry(QtCore.QRect(440, 440, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.roomButtom.setFont(font)
        self.roomButtom.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}"
)
        self.roomButtom.setObjectName("roomButtom")
        self.adminDashboardLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_3.setGeometry(QtCore.QRect(120, 150, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel_3.setFont(font)
        self.adminDashboardLabel_3.setStyleSheet("color: rgb(170, 0, 0);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel_3.setObjectName("adminDashboardLabel_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()



        floorAdmin_Dashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(floorAdmin_Dashboard)
        self.statusbar.setObjectName("statusbar")
        floorAdmin_Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(floorAdmin_Dashboard)
        QtCore.QMetaObject.connectSlotsByName(floorAdmin_Dashboard)

    def retranslateUi(self, floorAdmin_Dashboard):
        _translate = QtCore.QCoreApplication.translate
        floorAdmin_Dashboard.setWindowTitle(_translate("floorAdmin_Dashboard", "Floor Admin Dashboard"))
        self.adminDashboardLabel_2.setText(_translate("floorAdmin_Dashboard", "Mangament"))
        self.reservationsButton.setText(_translate("floorAdmin_Dashboard", "Reservations"))
        self.rateButton.setText(_translate("floorAdmin_Dashboard", "Rate Resident Stay"))
        self.roomButtom.setText(_translate("floorAdmin_Dashboard", "Update Room Status"))
        self.adminDashboardLabel_3.setText(_translate("floorAdmin_Dashboard", "Floor Admin Dashboard"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    floorAdmin_Dashboard = QtWidgets.QMainWindow()
    ui = Ui_floorAdmin_Dashboard()
    ui.setupUi(floorAdmin_Dashboard)
    floorAdmin_Dashboard.show()
    sys.exit(app.exec_())
