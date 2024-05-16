from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import hometp6,page1tp6,page2tp6

ui= ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow

def hometp6Ui():
    global ui 
    ui = hometp6.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.lesson11.clicked.connect(page1tp6Ui)
    MainWindow.show()
def page1tp6Ui():
    global ui 
    ui = page1tp6.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #ui.lesson11.clicked.connect(page1tp6Ui)
    MainWindow.show()

    hometp6Ui()
    sys.exit(app.exec())