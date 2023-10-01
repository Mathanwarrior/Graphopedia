#-----------------------------------------HEADER FILES---------------------------------------------#
from Calculator import Ui_Calculator
from graph import Ui_MainWindow1
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def openwindow(self):
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow1()
            self.ui.setupUi(self.window)
            self.window.show()
    def openwindow1(self):
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_Calculator()
            self.ui.setupUi(self.window)
            self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 310)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/VScode/project/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_cal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_cal.sizePolicy().hasHeightForWidth())
        self.push_cal.setSizePolicy(sizePolicy)
        self.push_cal.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(0,0,111);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"")
        self.push_cal.setObjectName("push_cal")
        self.gridLayout.addWidget(self.push_cal, 4, 0, 1, 1)
        self.push_graph = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_graph.sizePolicy().hasHeightForWidth())
        self.push_graph.setSizePolicy(sizePolicy)
        self.push_graph.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(0,0,111);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"\n"
"")
        self.push_graph.setObjectName("push_graph")
        self.gridLayout.addWidget(self.push_graph, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("font: 40pt \"Niagara Engraved\";\n"
"color: rgb(0, 0, 111);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 40pt \"Niagara Engraved\";\n"
"color: rgb(0, 0, 111);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.push_graph.clicked.connect(self.openwindow)
        self.push_cal.clicked.connect(self.openwindow1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graphopedia"))
        self.push_cal.setText(_translate("MainWindow", "Scientific Calculator"))
        self.push_graph.setText(_translate("MainWindow", "Graph Demonstrator"))
        self.label_2.setText(_translate("MainWindow", "                 App Using Python"))
        self.label.setText(_translate("MainWindow", "              Graph Demonstration "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedHeight(600)
    MainWindow.setFixedWidth(760)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
