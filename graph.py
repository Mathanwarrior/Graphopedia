#-----------------------------------------HEADER FILES---------------------------------------------#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import matplotlib.pyplot as plt
from math import *
import math


class Ui_MainWindow1(object):  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 377)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/VScode/project/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(16, 16, 16);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_1.sizePolicy().hasHeightForWidth())
        self.push_1.setSizePolicy(sizePolicy)
        self.push_1.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_1.setObjectName("push_1")
        self.gridLayout.addWidget(self.push_1, 4, 0, 1, 1)
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_6.sizePolicy().hasHeightForWidth())
        self.push_6.setSizePolicy(sizePolicy)
        self.push_6.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_6.setObjectName("push_6")
        self.gridLayout.addWidget(self.push_6, 5, 2, 1, 1)
        self.push_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_div.sizePolicy().hasHeightForWidth())
        self.push_div.setSizePolicy(sizePolicy)
        self.push_div.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Rockwell\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.push_div.setObjectName("push_div")
        self.gridLayout.addWidget(self.push_div, 5, 3, 1, 1)
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_4.sizePolicy().hasHeightForWidth())
        self.push_4.setSizePolicy(sizePolicy)
        self.push_4.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_4.setObjectName("push_4")
        self.gridLayout.addWidget(self.push_4, 5, 0, 1, 1)
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_2.sizePolicy().hasHeightForWidth())
        self.push_2.setSizePolicy(sizePolicy)
        self.push_2.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_2.setObjectName("push_2")
        self.gridLayout.addWidget(self.push_2, 4, 1, 1, 1)
        self.push_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_0.sizePolicy().hasHeightForWidth())
        self.push_0.setSizePolicy(sizePolicy)
        self.push_0.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_0.setObjectName("push_0")
        self.gridLayout.addWidget(self.push_0, 7, 0, 1, 1)
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_8.sizePolicy().hasHeightForWidth())
        self.push_8.setSizePolicy(sizePolicy)
        self.push_8.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_8.setObjectName("push_8")
        self.gridLayout.addWidget(self.push_8, 6, 1, 1, 1)
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_9.sizePolicy().hasHeightForWidth())
        self.push_9.setSizePolicy(sizePolicy)
        self.push_9.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_9.setObjectName("push_9")
        self.gridLayout.addWidget(self.push_9, 6, 2, 1, 1)
        self.push_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_sqrt.sizePolicy().hasHeightForWidth())
        self.push_sqrt.setSizePolicy(sizePolicy)
        self.push_sqrt.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Rockwell\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.push_sqrt.setObjectName("push_sqrt")
        self.gridLayout.addWidget(self.push_sqrt, 6, 3, 1, 1)
        self.push_plot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_plot.sizePolicy().hasHeightForWidth())
        self.push_plot.setSizePolicy(sizePolicy)
        self.push_plot.setStyleSheet("QPushButton{\n"
"font: 75 22pt \"stencil\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"")
        self.push_plot.setObjectName("push_plot")
        self.gridLayout.addWidget(self.push_plot, 7, 3, 1, 1)
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_7.sizePolicy().hasHeightForWidth())
        self.push_7.setSizePolicy(sizePolicy)
        self.push_7.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_7.setObjectName("push_7")
        self.gridLayout.addWidget(self.push_7, 6, 0, 1, 1)
        self.push_log = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_log.sizePolicy().hasHeightForWidth())
        self.push_log.setSizePolicy(sizePolicy)
        self.push_log.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_log.setObjectName("push_log")
        self.gridLayout.addWidget(self.push_log, 7, 2, 1, 1)
        self.push_opbracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_opbracket.sizePolicy().hasHeightForWidth())
        self.push_opbracket.setSizePolicy(sizePolicy)
        self.push_opbracket.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_opbracket.setObjectName("push_opbracket")
        self.gridLayout.addWidget(self.push_opbracket, 8, 0, 1, 1)
        self.push_inverse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_inverse.sizePolicy().hasHeightForWidth())
        self.push_inverse.setSizePolicy(sizePolicy)
        self.push_inverse.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_inverse.setObjectName("push_inverse")
        self.gridLayout.addWidget(self.push_inverse, 8, 2, 1, 1)
        self.push_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_point.sizePolicy().hasHeightForWidth())
        self.push_point.setSizePolicy(sizePolicy)
        self.push_point.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_point.setObjectName("push_point")
        self.gridLayout.addWidget(self.push_point, 7, 1, 1, 1)
        self.push_clobracket = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_clobracket.sizePolicy().hasHeightForWidth())
        self.push_clobracket.setSizePolicy(sizePolicy)
        self.push_clobracket.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_clobracket.setObjectName("push_clobracket")
        self.gridLayout.addWidget(self.push_clobracket, 8, 1, 1, 1)
        self.push_backspace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_backspace.sizePolicy().hasHeightForWidth())
        self.push_backspace.setSizePolicy(sizePolicy)
        self.push_backspace.setStyleSheet("QPushButton{\n"
"font: 75 14pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_backspace.setObjectName("push_backspace")
        self.gridLayout.addWidget(self.push_backspace, 1, 0, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    background-color: rgb(248, 34, 37);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 8, 3, 1, 1)
        self.push_cube = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_cube.sizePolicy().hasHeightForWidth())
        self.push_cube.setSizePolicy(sizePolicy)
        self.push_cube.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_cube.setObjectName("push_cube")
        self.gridLayout.addWidget(self.push_cube, 2, 1, 1, 1)
        self.push_power = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_power.sizePolicy().hasHeightForWidth())
        self.push_power.setSizePolicy(sizePolicy)
        self.push_power.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_power.setObjectName("push_power")
        self.gridLayout.addWidget(self.push_power, 2, 2, 1, 1)
        self.push_ln = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_ln.sizePolicy().hasHeightForWidth())
        self.push_ln.setSizePolicy(sizePolicy)
        self.push_ln.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_ln.setObjectName("push_ln")
        self.gridLayout.addWidget(self.push_ln, 1, 2, 1, 1)
        self.push_x = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_x.sizePolicy().hasHeightForWidth())
        self.push_x.setSizePolicy(sizePolicy)
        self.push_x.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_x.setObjectName("push_x")
        self.gridLayout.addWidget(self.push_x, 1, 1, 1, 1)
        self.push_square = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_square.sizePolicy().hasHeightForWidth())
        self.push_square.setSizePolicy(sizePolicy)
        self.push_square.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_square.setObjectName("push_square")
        self.gridLayout.addWidget(self.push_square, 2, 0, 1, 1)
        self.push_sin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_sin.sizePolicy().hasHeightForWidth())
        self.push_sin.setSizePolicy(sizePolicy)
        self.push_sin.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_sin.setObjectName("push_sin")
        self.gridLayout.addWidget(self.push_sin, 3, 0, 1, 1)
        self.push_cos = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_cos.sizePolicy().hasHeightForWidth())
        self.push_cos.setSizePolicy(sizePolicy)
        self.push_cos.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_cos.setObjectName("push_cos")
        self.gridLayout.addWidget(self.push_cos, 3, 1, 1, 1)
        self.push_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_plus.sizePolicy().hasHeightForWidth())
        self.push_plus.setSizePolicy(sizePolicy)
        self.push_plus.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Rockwell\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.push_plus.setObjectName("push_plus")
        self.gridLayout.addWidget(self.push_plus, 2, 3, 1, 1)
        self.push_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_minus.sizePolicy().hasHeightForWidth())
        self.push_minus.setSizePolicy(sizePolicy)
        self.push_minus.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Rockwell\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.push_minus.setObjectName("push_minus")
        self.gridLayout.addWidget(self.push_minus, 3, 3, 1, 1)
        self.push_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_mul.sizePolicy().hasHeightForWidth())
        self.push_mul.setSizePolicy(sizePolicy)
        self.push_mul.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Rockwell\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.push_mul.setObjectName("push_mul")
        self.gridLayout.addWidget(self.push_mul, 4, 3, 1, 1)
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_3.sizePolicy().hasHeightForWidth())
        self.push_3.setSizePolicy(sizePolicy)
        self.push_3.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_3.setObjectName("push_3")
        self.gridLayout.addWidget(self.push_3, 4, 2, 1, 1)
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_5.sizePolicy().hasHeightForWidth())
        self.push_5.setSizePolicy(sizePolicy)
        self.push_5.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_5.setObjectName("push_5")
        self.gridLayout.addWidget(self.push_5, 5, 1, 1, 1)
        self.push_tan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_tan.sizePolicy().hasHeightForWidth())
        self.push_tan.setSizePolicy(sizePolicy)
        self.push_tan.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_tan.setObjectName("push_tan")
        self.gridLayout.addWidget(self.push_tan, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 48pt \"Georgia\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.push_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        self.push_clear.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 15px;\n"
"    \n"
"    background-color: rgb(248, 34, 37);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 3, 1, 1)
        self.textbox = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox.sizePolicy().hasHeightForWidth())
        self.textbox.setSizePolicy(sizePolicy)
        self.textbox.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 75 60pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.textbox.setText("")
        self.textbox.setObjectName("textbox")
        self.gridLayout.addWidget(self.textbox, 0, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.push_backspace.clicked.connect(self.backspace)
        self.push_x.clicked.connect(lambda:self.display("X"))
        self.push_ln.clicked.connect(lambda:self.display("ln"))
        self.push_clear.clicked.connect(lambda:self.clear())
        self.push_square.clicked.connect(lambda:self.display("^2"))
        self.push_cube.clicked.connect(lambda:self.display("^3"))
        self.push_power.clicked.connect(lambda:self.display("^"))
        self.push_sin.clicked.connect(lambda:self.display("sin"))
        self.push_cos.clicked.connect(lambda:self.display("cos"))
        self.push_tan.clicked.connect(lambda:self.display("tan"))
        self.push_1.clicked.connect(lambda:self.display("1"))
        self.push_2.clicked.connect(lambda:self.display("2"))
        self.push_3.clicked.connect(lambda:self.display("3"))
        self.push_4.clicked.connect(lambda:self.display("4"))
        self.push_5.clicked.connect(lambda:self.display("5"))
        self.push_6.clicked.connect(lambda:self.display("6"))
        self.push_7.clicked.connect(lambda:self.display("7"))
        self.push_8.clicked.connect(lambda:self.display("8"))
        self.push_9.clicked.connect(lambda:self.display("9"))
        self.push_0.clicked.connect(lambda:self.display("0"))
        self.push_point.clicked.connect(lambda:self.display("."))
        self.push_log.clicked.connect(lambda:self.display("log"))
        self.push_opbracket.clicked.connect(lambda:self.display("("))
        self.push_clobracket.clicked.connect(lambda:self.display(")"))
        self.push_plus.clicked.connect(lambda:self.display("+"))
        self.push_minus.clicked.connect(lambda:self.display("-"))
        self.push_mul.clicked.connect(lambda:self.display("*"))
        self.push_div.clicked.connect(lambda:self.display("/"))
        self.push_sqrt.clicked.connect(lambda:self.display("√"))
        self.push_inverse.clicked.connect(lambda:self.display("π"))
        self.pushButton_32.clicked.connect(lambda: MainWindow.close())
        self.push_plot.clicked.connect(lambda:self.plot())
        

    def display(self,h):
            text=self.textbox.text()
            self.textbox.setText(text + h)
       
    def clear(self):
            self.textbox.setText("")
    def backspace(self):
            text=self.textbox.text()
            self.textbox.setText(text[:len(text)-1])
    def plot(self):
        self.add=0
        self.s=self.textbox.text()
        self.s=self.s.lower()
        self.temp=self.s
        self.s=self.s.replace('√','sqrt')
        self.s=self.s.replace('log','log10')
        self.s=self.s.replace('ln','log')
        self.s=self.s.replace('x','(x)')
        self.s=self.s.replace('^','**')
        self.s=self.s.replace("π","round(math.pi,8)")
        var, x, y = 10, [], []
        while var>=-10:
                     self.s1=''
                     self.add=0
                     self.s1=self.s.replace('x',str(var))
                     try:
                                self.add=eval(self.s1)
                                y.append(self.add)
                                x.append(var)
                     except:
                                pass
                     var-=0.1
        plt.figure(figsize=(10,8),num ='Graphopedia')
        plt.title("Graphical demonstration of "+"Y="+self.temp)
        plt.plot(x,y,label = 'y = '+self.temp,color = 'red')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        ax = plt.gca()
        plt.grid(True)
        plt.legend(bbox_to_anchor=(1.1,1.1))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data',0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))
        plt.show()

    
       
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Demonstrator"))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_1.setShortcut(_translate("MainWindow", "1"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_6.setShortcut(_translate("MainWindow", "6"))
        self.push_div.setText(_translate("MainWindow", "÷"))
        self.push_div.setShortcut(_translate("MainWindow", "/"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_4.setShortcut(_translate("MainWindow", "4"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_2.setShortcut(_translate("MainWindow", "2"))
        self.push_0.setText(_translate("MainWindow", "0"))
        self.push_0.setShortcut(_translate("MainWindow", "0"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_8.setShortcut(_translate("MainWindow", "8"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_9.setShortcut(_translate("MainWindow", "9"))
        self.push_sqrt.setText(_translate("MainWindow", "√ "))
        self.push_sqrt.setShortcut(_translate("MainWindow", "Shift+R"))
        self.push_plot.setText(_translate("MainWindow", "PLOT"))
        self.push_plot.setShortcut(_translate("MainWindow", "Return"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_7.setShortcut(_translate("MainWindow", "7"))
        self.push_log.setText(_translate("MainWindow", "log"))
        self.push_opbracket.setText(_translate("MainWindow", "("))
        self.push_opbracket.setShortcut(_translate("MainWindow", "("))
        self.push_inverse.setText(_translate("MainWindow", "π"))
        self.push_point.setText(_translate("MainWindow", "."))
        self.push_point.setShortcut(_translate("MainWindow", "."))
        self.push_clobracket.setText(_translate("MainWindow", ")"))
        self.push_clobracket.setShortcut(_translate("MainWindow", ")"))
        self.push_backspace.setText(_translate("MainWindow", "Backspace"))
        self.push_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.pushButton_32.setText(_translate("MainWindow", "Close"))
        self.push_cube.setText(_translate("MainWindow", "^3"))
        self.push_cube.setShortcut(_translate("MainWindow", "Shift+C"))
        self.push_power.setText(_translate("MainWindow", "^n"))
        self.push_power.setShortcut(_translate("MainWindow", "^"))
        self.push_ln.setText(_translate("MainWindow", "ln"))
        self.push_x.setText(_translate("MainWindow", "X"))
        self.push_x.setShortcut(_translate("MainWindow", "X"))
        self.push_square.setText(_translate("MainWindow", "^2"))
        self.push_square.setShortcut(_translate("MainWindow", "Shift+S"))
        self.push_sin.setText(_translate("MainWindow", "Sin"))
        self.push_sin.setShortcut(_translate("MainWindow", "S"))
        self.push_cos.setText(_translate("MainWindow", "Cos"))
        self.push_cos.setShortcut(_translate("MainWindow", "C"))
        self.push_plus.setText(_translate("MainWindow", "+"))
        self.push_plus.setShortcut(_translate("MainWindow", "+"))
        self.push_minus.setText(_translate("MainWindow", "-"))
        self.push_minus.setShortcut(_translate("MainWindow", "-"))
        self.push_mul.setText(_translate("MainWindow", "×"))
        self.push_mul.setShortcut(_translate("MainWindow", "*"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_3.setShortcut(_translate("MainWindow", "3"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_5.setShortcut(_translate("MainWindow", "5"))
        self.push_tan.setText(_translate("MainWindow", "Tan"))
        self.push_tan.setShortcut(_translate("MainWindow", "T"))
        self.label.setText(_translate("MainWindow", " Y="))
        self.push_clear.setText(_translate("MainWindow", "Clear"))
        self.push_clear.setShortcut(_translate("MainWindow", "Del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
