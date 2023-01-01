# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewReservations.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import gui as G
from main import main_control
from tkinter import messagebox
import Reservations_Managmentnew as R

def close():
    viewReservations.close()
    pass

class Ui_viewReservations(object):
    def logOut(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def back(self):
        self.Reservations_Managment = QtWidgets.QMainWindow()
        self.ui = R.Ui_Reservations_Managment()
        self.ui.setupUi(self.Reservations_Managment)
        self.Reservations_Managment.show()
        close()

    def deleteData(self):
        return

    def showData(self):
        _translate = QtCore.QCoreApplication.translate

        mc = main_control()
        result = mc.getGuiMsgsControl()
        if (self.idLineEdit.text() == ''):
            messagebox.showwarning('Warning', str(result[6]))
            return
        result = mc.getBuildingInfoControl(int(self.idLineEdit.text()))

        if (not result):
            result = mc.getGuiMsgsControl()
            messagebox.showerror('Error', result[8])
            return
        # self.locationLineEdit.insert(_translate("modifyEmployee", str(result[0][1])))
        # self.totalFloorsLineEdit.insert(_translate("modifyEmployee", str(result[0][2])))
        self.reservationIdLabel.insert(_translate("modifyEmployee", str(result[0][1])))
        self.dateOfReservationLabel.insert(_translate("modifyEmployee", str(result[0][2])))
        self.receptionistIdLabel.insert(_translate("modifyEmployee", str(result[0][3])))
        self.buildingIdLabel.insert(_translate("modifyEmployee", str(result[0][4])))
        self.residentIdLabel.insert(_translate("modifyEmployee", str(result[0][5])))
        self.floorIdLabel.insert(_translate("modifyEmployee", str(result[0][6])))
        self.roomLabel.insert(_translate("modifyEmployee", str(result[0][7])))

        return



    def setupUi(self, viewReservations):
        viewReservations.setObjectName("viewReservations")
        viewReservations.resize(1200, 600)
        viewReservations.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(viewReservations)
        self.centralwidget.setObjectName("centralwidget")
        self.ageLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_3.setGeometry(QtCore.QRect(470, 190, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_3.setFont(font)
        self.ageLabel_3.setObjectName("ageLabel_3")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(130, 200, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.nameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel_2.setGeometry(QtCore.QRect(130, 390, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_2.setFont(font)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.ageLabel_8 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_8.setGeometry(QtCore.QRect(850, 190, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_8.setFont(font)
        self.ageLabel_8.setObjectName("ageLabel_8")
        self.ageLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_4.setGeometry(QtCore.QRect(470, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_4.setFont(font)
        self.ageLabel_4.setObjectName("ageLabel_4")
        self.showNameLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.showNameLabel_3.setGeometry(QtCore.QRect(130, 330, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showNameLabel_3.setFont(font)
        self.showNameLabel_3.setStyleSheet("color: rgb(122, 122, 122);")
        self.showNameLabel_3.setText("")
        self.showNameLabel_3.setObjectName("showNameLabel_3")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(130, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.roomLabel = QtWidgets.QLabel(self.centralwidget)
        self.roomLabel.setGeometry(QtCore.QRect(130, 340, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roomLabel.setFont(font)
        self.roomLabel.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.roomLabel.setText("")
        self.roomLabel.setObjectName("roomLabel")
        self.buildingIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.buildingIdLabel.setGeometry(QtCore.QRect(130, 440, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buildingIdLabel.setFont(font)
        self.buildingIdLabel.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.buildingIdLabel.setText("")
        self.buildingIdLabel.setObjectName("buildingIdLabel")
        self.receptionistIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.receptionistIdLabel.setGeometry(QtCore.QRect(470, 240, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.receptionistIdLabel.setFont(font)
        self.receptionistIdLabel.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.receptionistIdLabel.setText("")
        self.receptionistIdLabel.setObjectName("receptionistIdLabel")
        self.floorIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.floorIdLabel.setGeometry(QtCore.QRect(470, 340, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.floorIdLabel.setFont(font)
        self.floorIdLabel.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.floorIdLabel.setText("")
        self.floorIdLabel.setObjectName("floorIdLabel")
        self.dateOfReservationLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateOfReservationLabel.setGeometry(QtCore.QRect(850, 240, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateOfReservationLabel.setFont(font)
        self.dateOfReservationLabel.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.dateOfReservationLabel.setText("")
        self.dateOfReservationLabel.setObjectName("dateOfReservationLabel")
        self.residentIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.residentIdLabel.setGeometry(QtCore.QRect(850, 340, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.residentIdLabel.setFont(font)
        self.residentIdLabel.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.residentIdLabel.setText("")
        self.residentIdLabel.setObjectName("residentIdLabel")
        self.ageLabel_9 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_9.setGeometry(QtCore.QRect(850, 290, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_9.setFont(font)
        self.ageLabel_9.setObjectName("ageLabel_9")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(120, 100, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel_2.setFont(font)
        self.adminDashboardLabel_2.setStyleSheet("color: rgb(41, 84, 125);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel_2.setObjectName("adminDashboardLabel_2")
        self.idLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_2.setGeometry(QtCore.QRect(400, 110, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_2.setFont(font)
        self.idLabel_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(bill.png);")
        self.idLabel_2.setText("")
        self.idLabel_2.setObjectName("idLabel_2")
        self.idLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_4.setGeometry(QtCore.QRect(950, 290, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_4.setFont(font)
        self.idLabel_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(driver-license.png);")
        self.idLabel_4.setText("")
        self.idLabel_4.setObjectName("idLabel_4")
        self.idLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_6.setGeometry(QtCore.QRect(620, 190, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_6.setFont(font)
        self.idLabel_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(driver-license.png);")
        self.idLabel_6.setText("")
        self.idLabel_6.setObjectName("idLabel_6")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.deleteData())
        self.deleteButton.setGeometry(QtCore.QRect(590, 440, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(0,100,150);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}")
        self.deleteButton.setObjectName("deleteButton")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut())
        self.logOutButton.setGeometry(QtCore.QRect(1090, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logOutButton.setFont(font)
        self.logOutButton.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(logout.png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.logOutButton.setText("")
        self.logOutButton.setObjectName("logOutButton")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 20, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back())
        self.backButton.setGeometry(QtCore.QRect(970, 20, 101, 61))
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
        self.idLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idLineEdit.setGeometry(QtCore.QRect(130, 240, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idLineEdit.setFont(font)
        self.idLineEdit.setStyleSheet("color: rgb(122, 122, 122);\n"
                                      "border-radius:0px;\n"
                                      "border-bottom: 3px solid #3c79b5;\n"
                                      "padding-bottom:0px;\n"
                                      "color: rgb(170, 0, 0);")
        self.idLineEdit.setObjectName("idLineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.ageLabel_3.raise_()
        self.idLabel.raise_()
        self.nameLabel_2.raise_()
        self.ageLabel_8.raise_()
        self.ageLabel_4.raise_()
        self.showNameLabel_3.raise_()
        self.nameLabel.raise_()
        self.roomLabel.raise_()
        self.buildingIdLabel.raise_()
        self.receptionistIdLabel.raise_()
        self.floorIdLabel.raise_()
        self.dateOfReservationLabel.raise_()
        self.residentIdLabel.raise_()
        self.ageLabel_9.raise_()
        self.adminDashboardLabel_2.raise_()
        self.idLabel_2.raise_()
        self.idLabel_4.raise_()
        self.idLabel_6.raise_()
        self.deleteButton.raise_()
        self.logOutButton.raise_()
        self.logoLabel.raise_()
        self.backButton.raise_()
        self.idLineEdit.raise_()
        viewReservations.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(viewReservations)
        self.statusbar.setObjectName("statusbar")
        viewReservations.setStatusBar(self.statusbar)

        self.showPushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showData())
        self.showPushButton.setGeometry(QtCore.QRect(270, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.showPushButton.setFont(font)
        self.showPushButton.setStyleSheet("QPushButton {\n"
                                     "background-color: rgb(140,140,140);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}\n"
                                     "QPushButton:hover\n"
                                     "{\n"
                                     "background-color: rgb(170,0,0);\n"
                                     "border-radius: 13px;\n"
                                     "color: white;\n"
                                     "}")
        self.showPushButton.setObjectName("showPushButton")

        self.retranslateUi(viewReservations)
        QtCore.QMetaObject.connectSlotsByName(viewReservations)

    def retranslateUi(self, viewReservations):
        _translate = QtCore.QCoreApplication.translate
        viewReservations.setWindowTitle(_translate("viewReservations", "viewReservations"))
        self.ageLabel_3.setText(_translate("viewReservations", "Receptionist Id"))
        self.idLabel.setText(_translate("viewReservations", "Reservation Id"))
        self.nameLabel_2.setText(_translate("viewReservations", "Building Id"))
        self.ageLabel_8.setText(_translate("viewReservations", "Date of Reservation"))
        self.ageLabel_4.setText(_translate("viewReservations", "Floor Id "))
        self.nameLabel.setText(_translate("viewReservations", "Room Id"))
        self.ageLabel_9.setText(_translate("viewReservations", "Resident Id"))
        self.adminDashboardLabel_2.setText(_translate("viewReservations", "Reservation"))
        self.deleteButton.setText(_translate("viewReservations", "Delete"))
        self.showPushButton.setText(_translate("modifyEmployee", "Show "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewReservations = QtWidgets.QMainWindow()
    ui = Ui_viewReservations()
    ui.setupUi(viewReservations)
    viewReservations.show()
    sys.exit(app.exec_())
