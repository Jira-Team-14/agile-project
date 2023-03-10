# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewBuildings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Admin_Dashboardnew as AD
from tkinter import messagebox
from main import main_control
from login import gui as G
import Buildings_Managmentnew as BM



class Ui_addNewBuilding(object):

    def back(self,addNewBuilding):
        self.Buildings_Managment = QtWidgets.QMainWindow()
        self.ui = BM.Ui_Buildings_Managment()
        self.ui.setupUi(self.Buildings_Managment)
        self.Buildings_Managment.show()
        addNewBuilding.close()

    def logOut(self,addNewBuilding):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = G.Ui_LoginWindow()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        addNewBuilding.close()

    def addBuilding(self):
        mc = main_control()
        result = mc.getGuiMsgsControl()
        if (self.idLineEdit.text() == ''):
            messagebox.showwarning('Warning', str(result[3]))
            return
        emptuple = (int(self.idLineEdit.text()), self.locationLineEdit.text(), self.totalFloorsLineEdit.text())
        isacceptable = mc.addBuildingControl(emptuple)
        if str(isacceptable).lower() == "none":
            messagebox.showinfo('information', str(result[4]))

        else:
            ermsg2 = str(result[5])
            ermsg1 = str(isacceptable)
            ermsg = ermsg2 + " " + ermsg1
            messagebox.showerror('Error', ermsg)

    def setupUi(self, addNewBuilding):
        addNewBuilding.setObjectName("addNewBuilding")
        addNewBuilding.resize(1200, 600)
        addNewBuilding.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(addNewBuilding)
        self.centralwidget.setObjectName("centralwidget")
        self.adminDashboardLabel = QtWidgets.QLabel(self.centralwidget)
        self.adminDashboardLabel.setGeometry(QtCore.QRect(30, 100, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.adminDashboardLabel.setFont(font)
        self.adminDashboardLabel.setStyleSheet("color: rgb(41, 84, 125);\n"
"text-align: left;\n"
"")
        self.adminDashboardLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adminDashboardLabel.setObjectName("adminDashboardLabel")
        self.ageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel.setGeometry(QtCore.QRect(130, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")
        self.showNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.showNameLabel.setGeometry(QtCore.QRect(130, 260, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showNameLabel.setFont(font)
        self.showNameLabel.setStyleSheet("color: rgb(122, 122, 122);")
        self.showNameLabel.setObjectName("showNameLabel")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(130, 210, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.idLabel.setFont(font)
        self.idLabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.idLabel.setObjectName("idLabel")
        self.nameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel_2.setGeometry(QtCore.QRect(130, 400, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nameLabel_2.setFont(font)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.ageLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_2.setGeometry(QtCore.QRect(130, 490, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_2.setFont(font)
        self.ageLabel_2.setObjectName("ageLabel_2")
        self.ageLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_3.setGeometry(QtCore.QRect(760, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_3.setFont(font)
        self.ageLabel_3.setObjectName("ageLabel_3")
        self.ageLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_4.setGeometry(QtCore.QRect(760, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_4.setFont(font)
        self.ageLabel_4.setObjectName("ageLabel_4")
        self.ageLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.ageLabel_5.setGeometry(QtCore.QRect(760, 400, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI Semilight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ageLabel_5.setFont(font)
        self.ageLabel_5.setObjectName("ageLabel_5")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.addBuilding())
        self.addButton.setGeometry(QtCore.QRect(710, 510, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)

        self.addButton.setStyleSheet(
                                     "QPushButton {\n"
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
        self.addButton.setObjectName("addButton")
        self.idLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idLineEdit.setGeometry(QtCore.QRect(130, 250, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idLineEdit.setFont(font)
        self.idLineEdit.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"")
        self.idLineEdit.setObjectName("idLineEdit")
        self.locationLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.locationLineEdit.setGeometry(QtCore.QRect(130, 350, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locationLineEdit.setFont(font)
        self.locationLineEdit.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"")
        self.locationLineEdit.setObjectName("locationLineEdit")

        self.totalFloorsLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.totalFloorsLineEdit.setGeometry(QtCore.QRect(760, 250, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalFloorsLineEdit.setFont(font)
        self.totalFloorsLineEdit.setStyleSheet("color: rgb(170, 0, 0);\n"
"border-radius:0px;\n"
"border-bottom: 3px solid #3c79b5;\n"
"padding-bottom:0px;\n"
"")
        self.totalFloorsLineEdit.setObjectName("totalFloorsLineEdit")

        self.showResidentInfoPushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.logOut(addNewBuilding))
        self.showResidentInfoPushButton_2.setGeometry(QtCore.QRect(1100, 30, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.showResidentInfoPushButton_2.setFont(font)
        self.showResidentInfoPushButton_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(logout.png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.showResidentInfoPushButton_2.setText("")
        self.showResidentInfoPushButton_2.setObjectName("showResidentInfoPushButton_2")
        self.showResidentInfoPushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.back(addNewBuilding))
        self.showResidentInfoPushButton_3.setGeometry(QtCore.QRect(980, 30, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.showResidentInfoPushButton_3.setFont(font)
        self.showResidentInfoPushButton_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"image: url(left-arrow-in-circular-button.png);\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"border-radius:6px;\n"
"padding: 10px; \n"
"")
        self.showResidentInfoPushButton_3.setText("")
        self.showResidentInfoPushButton_3.setObjectName("showResidentInfoPushButton_3")
        self.idLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_2.setGeometry(QtCore.QRect(470, 100, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_2.setFont(font)
        self.idLabel_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(home.png);")
        self.idLabel_2.setText("")
        self.idLabel_2.setObjectName("idLabel_2")
        self.idLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_3.setGeometry(QtCore.QRect(160, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_3.setFont(font)
        self.idLabel_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(driver-license.png);")
        self.idLabel_3.setText("")
        self.idLabel_3.setObjectName("idLabel_3")
        self.idLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_4.setGeometry(QtCore.QRect(240, 400, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_4.setFont(font)
        self.idLabel_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(driver-license.png);")
        self.idLabel_4.setText("")
        self.idLabel_4.setObjectName("idLabel_4")
        self.idLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_5.setGeometry(QtCore.QRect(230, 300, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_5.setFont(font)
        self.idLabel_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(location-pin.png);")
        self.idLabel_5.setText("")
        self.idLabel_5.setObjectName("idLabel_5")
        self.idLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_6.setGeometry(QtCore.QRect(250, 490, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_6.setFont(font)
        self.idLabel_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(plan.png);")
        self.idLabel_6.setText("")
        self.idLabel_6.setObjectName("idLabel_6")
        self.idLabel_7 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_7.setGeometry(QtCore.QRect(880, 300, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_7.setFont(font)
        self.idLabel_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(beds.png);")
        self.idLabel_7.setText("")
        self.idLabel_7.setObjectName("idLabel_7")
        self.idLabel_8 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_8.setGeometry(QtCore.QRect(910, 400, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_8.setFont(font)
        self.idLabel_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(gender-fluid.png);")
        self.idLabel_8.setText("")
        self.idLabel_8.setObjectName("idLabel_8")
        self.idLabel_9 = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_9.setGeometry(QtCore.QRect(910, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_9.setFont(font)
        self.idLabel_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"image: url(living-room.png);")
        self.idLabel_9.setText("")
        self.idLabel_9.setObjectName("idLabel_9")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(30, 30, 71, 61))
        self.logoLabel.setStyleSheet("background-image: url(imageedit_2_5347177992.jpg);\n"
"")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        addNewBuilding.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addNewBuilding)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1181, 581))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.lower()

        self.statusbar.setObjectName("statusbar")
        addNewBuilding.setStatusBar(self.statusbar)

        self.retranslateUi(addNewBuilding)
        QtCore.QMetaObject.connectSlotsByName(addNewBuilding)

    def retranslateUi(self, addNewBuilding):
        _translate = QtCore.QCoreApplication.translate
        addNewBuilding.setWindowTitle(_translate("addNewBuilding", "addNewBuilding"))
        self.adminDashboardLabel.setText(_translate("addNewBuilding", "Add New Building"))
        self.ageLabel.setText(_translate("addNewBuilding", "Location"))
        self.showNameLabel.setText(_translate("addNewBuilding", "xx"))
        self.idLabel.setText(_translate("addNewBuilding", "Id"))
        self.ageLabel_3.setText(_translate("addNewBuilding", "Total Floors"))
        self.addButton.setText(_translate("addNewBuilding", "Add"))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     addNewBuilding = QtWidgets.QMainWindow()
#     ui = Ui_addNewBuilding()
#     ui.setupUi(addNewBuilding)
#     addNewBuilding.show()
#     sys.exit(app.exec_())
