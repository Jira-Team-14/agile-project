# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rateResident.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from login import gui as G
import floorAdmin_Dashboardnew as FD
from main import main_control
from datetime import datetime

def close():
    rateResident.close()
    pass

class Ui_rateResident(object):

    def logOut(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        close()

    def back(self):
                self.floorAdmin_Dashboard = QtWidgets.QMainWindow()
                self.ui = FD.Ui_floorAdmin_Dashboard()
                self.ui.setupUi(self.floorAdmin_Dashboard)
                self.floorAdmin_Dashboard.show()
                close()

    def rate(self):
        mc = main_control
        result = mc.getGuiMsgsControl()
        if (self.idLineEdit.text() == '' or  self.reservationIdLineEdit.text() == '' or  self.rateLineEdit.text() == ''):
            messagebox.showwarning('Warning', str(result[3]))
            return
        dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        infotuple = (self.rateLineEdit, dateTime, self.reservationIdLineEdit,self.idLineEdit)
        isacceptable = mc.rateStayControl(infotuple)
        if str(isacceptable).lower() == "none":
            messagebox.showinfo('information', str(result[4]))
        else:
            ermsg2 = str(result[5])
            ermsg1 = str(isacceptable)
            ermsg = ermsg2 + " " + ermsg1
            messagebox.showerror('Error', ermsg)
        return

    def setupUi(self, rateResident):
        rateResident.setObjectName("rateResident")
        rateResident.resize(1200, 600)
        rateResident.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(rateResident)
        self.centralwidget.setObjectName("centralwidget")
        self.showNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.showNameLabel.setGeometry(QtCore.QRect(130, 280, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showNameLabel.setFont(font)
        self.showNameLabel.setStyleSheet("color: rgb(122, 122, 122);")
        self.showNameLabel.setObjectName("showNameLabel")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(130, 230, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.ageLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_3.setGeometry(QtCore.QRect(470, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_3.setFont(font)
        self.ageLabel_3.setObjectName("ageLabel_3")
        self.idLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idLineEdit.setGeometry(QtCore.QRect(130, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idLineEdit.setFont(font)
        self.idLineEdit.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.idLineEdit.setObjectName("idLineEdit")
        self.ageLabel_8 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_8.setGeometry(QtCore.QRect(850, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_8.setFont(font)
        self.ageLabel_8.setObjectName("ageLabel_8")
        self.dateOfBirthLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateOfBirthLabel.setGeometry(QtCore.QRect(130, 530, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateOfBirthLabel.setFont(font)
        self.dateOfBirthLabel.setStyleSheet("color: rgb(122, 122, 122);")
        self.dateOfBirthLabel.setText("")
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.reservationIdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.reservationIdLineEdit.setGeometry(QtCore.QRect(470, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reservationIdLineEdit.setFont(font)
        self.reservationIdLineEdit.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.reservationIdLineEdit.setObjectName("reservationIdLineEdit")
        self.rateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rateLineEdit.setGeometry(QtCore.QRect(850, 270, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rateLineEdit.setFont(font)
        self.rateLineEdit.setStyleSheet("color: rgb(122, 122, 122);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"color: rgb(170, 0, 0);")
        self.rateLineEdit.setObjectName("rateLineEdit")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.rate())
        self.saveButton.setGeometry(QtCore.QRect(410, 480, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton {\n"
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
        self.saveButton.setObjectName("saveButton")
        self.adminDashboardLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel_2.setGeometry(QtCore.QRect(40, 120, 481, 71))
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
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back())
        self.backButton.setGeometry(QtCore.QRect(970, 30, 101, 61))
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
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut())
        self.logOutButton.setGeometry(QtCore.QRect(1090, 30, 91, 61))
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
        self.logoLabel.setGeometry(QtCore.QRect(20, 30, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.idLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_3.setGeometry(QtCore.QRect(280, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_3.setFont(font)
        self.idLabel_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(driver-license.png);\n"
)
        self.idLabel_3.setText("")
        self.idLabel_3.setObjectName("idLabel_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()


        rateResident.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(rateResident)
        self.statusbar.setObjectName("statusbar")
        rateResident.setStatusBar(self.statusbar)

        self.retranslateUi(rateResident)
        QtCore.QMetaObject.connectSlotsByName(rateResident)

    def retranslateUi(self, rateResident):
        _translate = QtCore.QCoreApplication.translate
        rateResident.setWindowTitle(_translate("rateResident", "rateResident"))
        self.showNameLabel.setText(_translate("rateResident", "xx"))
        self.idLabel.setText(_translate("rateResident", "Enter Resident Id"))
        self.ageLabel_3.setText(_translate("rateResident", "Enter Reservation Id"))
        self.ageLabel_8.setText(_translate("rateResident", "Enter Rate "))
        self.saveButton.setText(_translate("rateResident", "Save"))
        self.adminDashboardLabel_2.setText(_translate("rateResident", "Rate Resident Stay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rateResident = QtWidgets.QMainWindow()
    ui = Ui_rateResident()
    ui.setupUi(rateResident)
    rateResident.show()
    sys.exit(app.exec_())
