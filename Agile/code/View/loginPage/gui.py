
import os
import sys
sys.path.append(os.path.join('D:/', 'Projects', 'Agile','Agile','code','Control'))
from main import checkloginControl
from PyQt5 import QtCore, QtGui, QtWidgets
import admingui as ag
import BAgui as bg
import FAgui as fg
import receptionistgui as rg


# This is the Gui class of the login page
class Ui_LoginWindow(object):
    type=0

# functions to switch windows after login authentication
    def showAD(self):
        self.ADgui = QtWidgets.QMainWindow()
        self.ui = ag.Ui_MainWindow()
        self.ui.setupUi(self.ADgui)
        self.ADgui.show()

    def showBA(self):
        self.BAgui = QtWidgets.QMainWindow()
        self.ui = bg.Ui_MainWindow()
        self.ui.setupUi(self.BAgui)
        self.BAgui.show()

    def showFA(self):
        self.FAgui = QtWidgets.QMainWindow()
        self.ui = fg.Ui_MainWindow()
        self.ui.setupUi(self.FAgui)
        self.FAgui.show()

    def showRE(self):
        self.REgui = QtWidgets.QMainWindow()
        self.ui = rg.Ui_MainWindow()
        self.ui.setupUi(self.REgui)
        self.REgui.show()

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(908, 518)
        LoginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 461))
        self.label.setStyleSheet("background-color: rgb(2, 114, 141);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 361, 461))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background-image: url(logintransparentimage.png);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 211, 111))
        self.label_3.setStyleSheet("background-image: url(70447380_2355764128087080_2304351109373755392_n.jpg.jpg);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("70447380_2355764128087080_2304351109373755392_n.jpg.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(360, 0, 841, 641))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet("background-image: url(d1668ee13fec4635d7f8d2a65c89d1b2.jpg);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("d1668ee13fec4635d7f8d2a65c89d1b2.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.adminButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.usertypechoice(1) )
        self.adminButton.setGeometry(QtCore.QRect(380, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.adminButton.setFont(font)
        self.adminButton.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid grey;\n"
"color:rgb(104,112,137);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(137,147,179);\n"
"border: 1px solid grey;\n"
"color:white;\n"
"}\n"
"")
        self.adminButton.setObjectName("adminButton")
        self.buildingAButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.usertypechoice(2))
        self.buildingAButton.setGeometry(QtCore.QRect(510, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.buildingAButton.setFont(font)
        self.buildingAButton.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid grey;\n"
"color:rgb(104,112,137);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(137,147,179);\n"
"border: 1px solid grey;\n"
"color:white;\n"
"}")
        self.buildingAButton.setObjectName("buildingAButton")
        self.floorAButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.usertypechoice(3))
        self.floorAButton.setGeometry(QtCore.QRect(630, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.floorAButton.setFont(font)
        self.floorAButton.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid grey;\n"
"color:rgb(104,112,137);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(137,147,179);\n"
"border: 1px solid grey;\n"
"color:white;\n"
"}")
        self.floorAButton.setObjectName("floorAButton")
        self.receptionistButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.usertypechoice(4))
        self.receptionistButton.setGeometry(QtCore.QRect(750, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.receptionistButton.setFont(font)
        self.receptionistButton.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid grey;\n"
"color:rgb(104,112,137);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(137,147,179);\n"
"border: 1px solid grey;\n"
"color:white;\n"
"}")
        self.receptionistButton.setObjectName("receptionistButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 60, 31, 31))
        self.label_5.setStyleSheet("background-image: url(fa5b1aaf768ac5d000823c335d161813.png);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("fa5b1aaf768ac5d000823c335d161813.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(461, 206, 31, 31))
        self.label_6.setStyleSheet("background-image: url(Sample_User_Icon.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Sample_User_Icon.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(104,112,137);")
        self.label_7.setObjectName("label_7")
        self.usernameBox = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameBox.setGeometry(QtCore.QRect(500, 216, 251, 21))
        self.usernameBox.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 0);\n"
" border: 0px solid grey")
        self.usernameBox.setInputMask("")
        self.usernameBox.setPlaceholderText("")
        self.usernameBox.setObjectName("usernameBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 226, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(2,114,141);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(500, 296, 251, 20))
        self.label_9.setStyleSheet("color:rgb(2,114,141);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(463, 283, 21, 21))
        self.label_10.setStyleSheet("background-image: url(Sample_User_Icon.png);")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("png-transparent-computer-icons-padlock-lock-technic-computer-icons-symbol-thumbnail.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(500, 261, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(104,112,137);")
        self.label_11.setObjectName("label_11")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget , clicked=lambda: self.checklogin())
        self.loginButton.setEnabled(True)
        self.loginButton.setGeometry(QtCore.QRect(440, 359, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.loginButton.setMouseTracking(False)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(104,112,137);\n"
"border-radius: 13px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(137,147,179);\n"
"border-radius: 13px;\n"
"color: white;\n"
"}")
        self.loginButton.setCheckable(False)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.passwordBox = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordBox.setGeometry(QtCore.QRect(499, 286, 251, 21))
        self.passwordBox.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 0);\n"
" border: 0px solid grey")
        self.passwordBox.setInputMask("")
        self.passwordBox.setPlaceholderText("")
        self.passwordBox.setObjectName("passwordBox")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 26))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.adminButton.setText(_translate("LoginWindow", "Admin"))
        self.buildingAButton.setText(_translate("LoginWindow", "Building Admin"))
        self.floorAButton.setText(_translate("LoginWindow", "Floor Admin"))
        self.receptionistButton.setText(_translate("LoginWindow", "Receptionist"))
        self.label_7.setText(_translate("LoginWindow", "Username"))
        self.label_8.setText(_translate("LoginWindow", "____________________________________"))
        self.label_9.setText(_translate("LoginWindow", "____________________________________"))
        self.label_11.setText(_translate("LoginWindow", "Password"))
        self.loginButton.setText(_translate("LoginWindow", "Login"))
        self.menuLogin.setTitle(_translate("LoginWindow", "Login"))

# function to change UI as user chooses role (AD , BA , FA , RE)
    def usertypechoice(self,type):
        self.adminButton.setStyleSheet("QPushButton {\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "border: 1px solid grey;\n"
                                           "color:rgb(104,112,137);\n"
                                           "}\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "background-color: rgb(137,147,179);\n"
                                           "border: 1px solid grey;\n"
                                           "color:white;\n"
                                           "}")
        self.buildingAButton.setStyleSheet("QPushButton {\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "border: 1px solid grey;\n"
                                           "color:rgb(104,112,137);\n"
                                           "}\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "background-color: rgb(137,147,179);\n"
                                           "border: 1px solid grey;\n"
                                           "color:white;\n"
                                           "}")
        self.floorAButton.setStyleSheet("QPushButton {\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "border: 1px solid grey;\n"
                                           "color:rgb(104,112,137);\n"
                                           "}\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "background-color: rgb(137,147,179);\n"
                                           "border: 1px solid grey;\n"
                                           "color:white;\n"
                                           "}")
        self.receptionistButton.setStyleSheet("QPushButton {\n"
                                           "background-color: rgba(255, 255, 255, 0);\n"
                                           "border: 1px solid grey;\n"
                                           "color:rgb(104,112,137);\n"
                                           "}\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           "background-color: rgb(137,147,179);\n"
                                           "border: 1px solid grey;\n"
                                           "color:white;\n"
                                           "}")
        if type == 1:
            self.adminButton.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}")

        elif type == 2:
            self.buildingAButton.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}")

        elif type == 3:
            self.floorAButton.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}")

        else:
            self.receptionistButton.setStyleSheet("QPushButton {\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "background-color: rgb(137,147,179);\n"
                                               "border: 1px solid grey;\n"
                                               "color:white;\n"
                                               "}")
        self.type=type
        print(self.type)

#collect login info and send to CONTROL to authenticate login info
    def checklogin(self):
        usertuple=(int(self.usernameBox.text()),int(self.passwordBox.text()))
        isacceptable = checkloginControl(self.type,usertuple)
        print(isacceptable)
        if isacceptable:
            if (self.type == 1):
                self.showAD()
                LoginWindow.close()
            elif(self.type == 2):
                self.showBA()
                LoginWindow.close()
            elif(self.type == 3):
                self.showFA()
                LoginWindow.close()
            elif(self.type == 4):
                self.showRE()
                LoginWindow.close()
        else:
            print ("invalid login")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
