# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topic6lesson12.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1291, 881)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1291, 881))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0.398091, y1:0.358, x2:0.806818, y2:0.778, stop:0.153409 rgba(255, 147, 206, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.widget.setObjectName("widget")
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setGeometry(QtCore.QRect(50, 50, 141, 91))
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 85, 255);\n"
"font: 25pt \"MV Boli\";\n"
"border-radius:10px;\n"
"border: 2px solid pink;\n"
"")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 161, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 24pt \"MV Boli\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(510, 60, 561, 71))
        self.label_3.setStyleSheet("font: 24pt \"MV Boli\";\n"
"text-decoration: underline;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 521, 111))
        self.label_4.setStyleSheet("font: 24pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid #ffffff;\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 410, 751, 301))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 751, 301))
        self.label_5.setStyleSheet("\n"
"border-image: url(:/congthuc/topic6ls12a.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(-4, -8, 751, 311))
        self.label_6.setStyleSheet("border-image: url(:/congthuc/topic6ls12b.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 751, 301))
        self.label_7.setStyleSheet("border-image: url(:/congthuc/topic6ls12c.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 751, 301))
        self.label_8.setStyleSheet("border-image: url(:/congthuc/topic6ls12d.jpg);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page_4)
        self.Button_1 = QtWidgets.QPushButton(self.widget)
        self.Button_1.setGeometry(QtCore.QRect(1010, 420, 151, 41))
        self.Button_1.setStyleSheet("color: rgb(255, 29, 169);\n"
"\n"
"font: 18pt \"MV Boli\";")
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.widget)
        self.Button_2.setGeometry(QtCore.QRect(1010, 500, 151, 41))
        self.Button_2.setStyleSheet("font: 18pt \"MV Boli\";\n"
"color: rgb(255, 29, 169);")
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.widget)
        self.Button_3.setGeometry(QtCore.QRect(1010, 580, 151, 41))
        self.Button_3.setStyleSheet("font: 18pt \"MV Boli\";\n"
"color: rgb(255, 29, 169);")
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.widget)
        self.Button_4.setGeometry(QtCore.QRect(1010, 660, 151, 41))
        self.Button_4.setStyleSheet("color: rgb(255, 29, 169);\n"
"font: 18pt \"MV Boli\";")
        self.Button_4.setObjectName("Button_4")
        self.back2 = QtWidgets.QPushButton(self.widget)
        self.back2.setGeometry(QtCore.QRect(1180, 790, 75, 39))
        self.back2.setStyleSheet("color: rgb(255, 29, 169);\n"
"\n"
"font: 18pt \"MV Boli\";")
        self.back2.setObjectName("back2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "page2tp6"))
        self.label_1.setText(_translate("MainWindow", "Topic 6"))
        self.label_2.setText(_translate("MainWindow", "やすみのひ"))
        self.label_3.setText(_translate("MainWindow", "Yasumi no hi 1 / Holidays and Days off 1"))
        self.label_4.setText(_translate("MainWindow", "Lesson 12:  Shall we go together?"))
        self.Button_1.setText(_translate("MainWindow", "Structure 1"))
        self.Button_2.setText(_translate("MainWindow", "Structure 2"))
        self.Button_3.setText(_translate("MainWindow", "Structure 3"))
        self.Button_4.setText(_translate("MainWindow", "Structure 4"))
        self.back2.setText(_translate("MainWindow", "Back"))
        self.Button_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Button_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.Button_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.Button_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
import topic6_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
