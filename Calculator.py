#-----------------------------------------HEADER FILES---------------------------------------------#
from PyQt5 import QtCore, QtGui, QtWidgets
import math 
from math import*
from math import log10,log

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(451, 388)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/VScode/project/calicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calculator.setWindowIcon(icon)
        Calculator.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Button_ln = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_ln.sizePolicy().hasHeightForWidth())
        self.Button_ln.setSizePolicy(sizePolicy)
        self.Button_ln.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(0,0,0);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_ln.setObjectName("Button_ln")
        self.gridLayout.addWidget(self.Button_ln, 3, 3, 1, 1)
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy)
        self.Button_1.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_1.setObjectName("Button_1")
        self.gridLayout.addWidget(self.Button_1, 7, 0, 1, 1)
        self.Button_cos = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_cos.sizePolicy().hasHeightForWidth())
        self.Button_cos.setSizePolicy(sizePolicy)
        self.Button_cos.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_cos.setObjectName("Button_cos")
        self.gridLayout.addWidget(self.Button_cos, 2, 1, 1, 1)
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy)
        self.Button_6.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_6.setObjectName("Button_6")
        self.gridLayout.addWidget(self.Button_6, 8, 2, 1, 1)
        self.Button_inverse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_inverse.sizePolicy().hasHeightForWidth())
        self.Button_inverse.setSizePolicy(sizePolicy)
        self.Button_inverse.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(0,0,0);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_inverse.setObjectName("Button_inverse")
        self.gridLayout.addWidget(self.Button_inverse, 5, 3, 1, 1)
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy)
        self.Button_3.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_3.setObjectName("Button_3")
        self.gridLayout.addWidget(self.Button_3, 7, 2, 1, 1)
        self.push_sqrt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_sqrt.sizePolicy().hasHeightForWidth())
        self.push_sqrt.setSizePolicy(sizePolicy)
        self.push_sqrt.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 12px;\n"
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
        self.gridLayout.addWidget(self.push_sqrt, 10, 3, 1, 1)
        self.Button_tan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_tan.sizePolicy().hasHeightForWidth())
        self.Button_tan.setSizePolicy(sizePolicy)
        self.Button_tan.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_tan.setObjectName("Button_tan")
        self.gridLayout.addWidget(self.Button_tan, 2, 2, 1, 1)
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy)
        self.Button_5.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_5.setObjectName("Button_5")
        self.gridLayout.addWidget(self.Button_5, 8, 1, 1, 1)
        self.Button_equals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_equals.sizePolicy().hasHeightForWidth())
        self.Button_equals.setSizePolicy(sizePolicy)
        self.Button_equals.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_equals.setObjectName("Button_equals")
        self.gridLayout.addWidget(self.Button_equals, 10, 2, 1, 1)
        self.Button_arctan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_arctan.sizePolicy().hasHeightForWidth())
        self.Button_arctan.setSizePolicy(sizePolicy)
        self.Button_arctan.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_arctan.setObjectName("Button_arctan")
        self.gridLayout.addWidget(self.Button_arctan, 3, 2, 1, 1)
        self.Button_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_plus.sizePolicy().hasHeightForWidth())
        self.Button_plus.setSizePolicy(sizePolicy)
        self.Button_plus.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_plus.setObjectName("Button_plus")
        self.gridLayout.addWidget(self.Button_plus, 6, 3, 1, 1)
        self.textbox1 = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox1.setStyleSheet("font: 75 48pt \"Times New Roman\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textbox1.setText("")
        self.textbox1.setObjectName("textbox1")
        self.gridLayout.addWidget(self.textbox1, 0, 0, 1, 4)
        self.Button_power = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_power.sizePolicy().hasHeightForWidth())
        self.Button_power.setSizePolicy(sizePolicy)
        self.Button_power.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_power.setObjectName("Button_power")
        self.gridLayout.addWidget(self.Button_power, 6, 2, 1, 1)
        self.push_pi = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_pi.sizePolicy().hasHeightForWidth())
        self.push_pi.setSizePolicy(sizePolicy)
        self.push_pi.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_pi.setObjectName("push_pi")
        self.gridLayout.addWidget(self.push_pi, 11, 2, 1, 1)
        self.Button_cube = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_cube.sizePolicy().hasHeightForWidth())
        self.Button_cube.setSizePolicy(sizePolicy)
        self.Button_cube.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_cube.setObjectName("Button_cube")
        self.gridLayout.addWidget(self.Button_cube, 6, 1, 1, 1)
        self.Button_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_mul.sizePolicy().hasHeightForWidth())
        self.Button_mul.setSizePolicy(sizePolicy)
        self.Button_mul.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_mul.setObjectName("Button_mul")
        self.gridLayout.addWidget(self.Button_mul, 8, 3, 1, 1)
        self.push_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_close.sizePolicy().hasHeightForWidth())
        self.push_close.setSizePolicy(sizePolicy)
        self.push_close.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(248, 34, 37);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0,0,0);\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"")
        self.push_close.setObjectName("push_close")
        self.gridLayout.addWidget(self.push_close, 11, 3, 1, 1)
        self.Button_square = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_square.sizePolicy().hasHeightForWidth())
        self.Button_square.setSizePolicy(sizePolicy)
        self.Button_square.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_square.setObjectName("Button_square")
        self.gridLayout.addWidget(self.Button_square, 6, 0, 1, 1)
        self.push_cl = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_cl.sizePolicy().hasHeightForWidth())
        self.push_cl.setSizePolicy(sizePolicy)
        self.push_cl.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_cl.setObjectName("push_cl")
        self.gridLayout.addWidget(self.push_cl, 11, 1, 1, 1)
        self.Button_arcsin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_arcsin.sizePolicy().hasHeightForWidth())
        self.Button_arcsin.setSizePolicy(sizePolicy)
        self.Button_arcsin.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_arcsin.setObjectName("Button_arcsin")
        self.gridLayout.addWidget(self.Button_arcsin, 3, 0, 1, 1)
        self.push_op = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_op.sizePolicy().hasHeightForWidth())
        self.push_op.setSizePolicy(sizePolicy)
        self.push_op.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.push_op.setObjectName("push_op")
        self.gridLayout.addWidget(self.push_op, 11, 0, 1, 1)
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy)
        self.Button_2.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_2.setObjectName("Button_2")
        self.gridLayout.addWidget(self.Button_2, 7, 1, 1, 1)
        self.Button_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_div.sizePolicy().hasHeightForWidth())
        self.Button_div.setSizePolicy(sizePolicy)
        self.Button_div.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_div.setObjectName("Button_div")
        self.gridLayout.addWidget(self.Button_div, 9, 3, 1, 1)
        self.Button_sinh = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_sinh.sizePolicy().hasHeightForWidth())
        self.Button_sinh.setSizePolicy(sizePolicy)
        self.Button_sinh.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_sinh.setObjectName("Button_sinh")
        self.gridLayout.addWidget(self.Button_sinh, 5, 0, 1, 1)
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy)
        self.Button_9.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_9.setObjectName("Button_9")
        self.gridLayout.addWidget(self.Button_9, 9, 2, 1, 1)
        self.Button_arccos = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_arccos.sizePolicy().hasHeightForWidth())
        self.Button_arccos.setSizePolicy(sizePolicy)
        self.Button_arccos.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_arccos.setObjectName("Button_arccos")
        self.gridLayout.addWidget(self.Button_arccos, 3, 1, 1, 1)
        self.Button_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_point.sizePolicy().hasHeightForWidth())
        self.Button_point.setSizePolicy(sizePolicy)
        self.Button_point.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_point.setObjectName("Button_point")
        self.gridLayout.addWidget(self.Button_point, 10, 1, 1, 1)
        self.Button_tanh = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_tanh.sizePolicy().hasHeightForWidth())
        self.Button_tanh.setSizePolicy(sizePolicy)
        self.Button_tanh.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_tanh.setObjectName("Button_tanh")
        self.gridLayout.addWidget(self.Button_tanh, 5, 2, 1, 1)
        self.Button_log = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_log.sizePolicy().hasHeightForWidth())
        self.Button_log.setSizePolicy(sizePolicy)
        self.Button_log.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(0,0,0);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_log.setObjectName("Button_log")
        self.gridLayout.addWidget(self.Button_log, 2, 3, 1, 1)
        self.Button_sin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_sin.sizePolicy().hasHeightForWidth())
        self.Button_sin.setSizePolicy(sizePolicy)
        self.Button_sin.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_sin.setObjectName("Button_sin")
        self.gridLayout.addWidget(self.Button_sin, 2, 0, 1, 1)
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy)
        self.Button_0.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_0.setObjectName("Button_0")
        self.gridLayout.addWidget(self.Button_0, 10, 0, 1, 1)
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy)
        self.Button_4.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_4.setObjectName("Button_4")
        self.gridLayout.addWidget(self.Button_4, 8, 0, 1, 1)
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_minus.sizePolicy().hasHeightForWidth())
        self.Button_minus.setSizePolicy(sizePolicy)
        self.Button_minus.setStyleSheet("QPushButton{\n"
"font: 75 24pt \"Georgia\";\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"border-radius: 12px;\n"
"    \n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(0, 0, 0);\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.Button_minus.setObjectName("Button_minus")
        self.gridLayout.addWidget(self.Button_minus, 7, 3, 1, 1)
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy)
        self.Button_7.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_7.setObjectName("Button_7")
        self.gridLayout.addWidget(self.Button_7, 9, 0, 1, 1)
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy)
        self.Button_8.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_8.setObjectName("Button_8")
        self.gridLayout.addWidget(self.Button_8, 9, 1, 1, 1)
        self.Button_cosh = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_cosh.sizePolicy().hasHeightForWidth())
        self.Button_cosh.setSizePolicy(sizePolicy)
        self.Button_cosh.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.Button_cosh.setObjectName("Button_cosh")
        self.gridLayout.addWidget(self.Button_cosh, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"Georgia\";\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(248, 34, 37);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 255,255);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(191, 191, 191);\n"
"border-radius:12px\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
        self.pushButton.clicked.connect(self.backspace)
        self.pushButton_2.clicked.connect(lambda:self.insert("exp"))
        self.pushButton_3.clicked.connect(self.pm)
        self.pushButton_4.clicked.connect(self.clear)
        self.Button_sin.clicked.connect(lambda:self.insert("sin"))
        self.Button_cos.clicked.connect(lambda:self.insert("cos"))
        self.Button_tan.clicked.connect(lambda:self.insert("tan"))
        self.Button_arcsin.clicked.connect(lambda:self.insert("asin"))
        self.Button_arccos.clicked.connect(lambda:self.insert("acos"))
        self.Button_arctan.clicked.connect(lambda:self.insert("atan"))
        self.Button_sinh.clicked.connect(lambda:self.insert("sinh"))
        self.Button_cosh.clicked.connect(lambda:self.insert("cosh"))
        self.Button_tanh.clicked.connect(lambda:self.insert("tanh"))
        self.Button_square.clicked.connect(lambda:self.insert("^2"))
        self.Button_cube.clicked.connect(lambda:self.insert("^3"))
        self.Button_power.clicked.connect(lambda:self.insert("^"))
        self.Button_plus.clicked.connect(lambda:self.insert("+"))
        self.Button_minus.clicked.connect(lambda:self.insert("-"))
        self.Button_mul.clicked.connect(lambda:self.insert("*"))
        self.Button_div.clicked.connect(lambda:self.insert("/"))
        self.Button_1.clicked.connect(lambda:self.insert("1"))
        self.Button_2.clicked.connect(lambda:self.insert("2"))
        self.Button_3.clicked.connect(lambda:self.insert("3"))
        self.Button_4.clicked.connect(lambda:self.insert("4"))
        self.Button_5.clicked.connect(lambda:self.insert("5"))
        self.Button_6.clicked.connect(lambda:self.insert("6"))
        self.Button_7.clicked.connect(lambda:self.insert("7"))
        self.Button_8.clicked.connect(lambda:self.insert("8"))
        self.Button_9.clicked.connect(lambda:self.insert("9"))
        self.Button_0.clicked.connect(lambda:self.insert("0"))
        self.Button_point.clicked.connect(lambda:self.insert("."))
        self.Button_equals.clicked.connect(self.result)
        self.Button_log.clicked.connect(lambda:self.insert("log"))
        self.Button_ln.clicked.connect(lambda:self.insert("ln"))
        self.Button_inverse.clicked.connect(self.inverse)
        self.push_op.clicked.connect(lambda:self.insert("("))
        self.push_cl.clicked.connect(lambda:self.insert(")"))
        self.push_pi.clicked.connect(lambda:self.insert("π"))
        self.push_sqrt.clicked.connect(lambda:self.insert("√"))
        self.push_close.clicked.connect(lambda:Calculator.close())

    def insert(self,h):
            text=self.textbox1.text()
            self.textbox1.setText(text + h)
    def backspace(self):
            text=self.textbox1.text()
            self.textbox1.setText(text[:len(text)-1])
    def clear(self):
            self.textbox1.setText("")
    def pm(self):
            text=self.textbox1.text()
            self.textbox1.setText((str(-float(text))))
    def inverse(self):
            text=self.textbox1.text()
            self.textbox1.setText("1/"+text)
    def result(self):     
            try:
                    
                    self.s=self.textbox1.text()
                    self.s=self.s.replace("^","**")
                    self.s=self.s.replace('log','log10')
                    self.s=self.s.replace('ln','log')
                    self.s=self.s.replace("√","sqrt")
                    self.s=self.s.replace("π","round(math.pi,8)")
                    self.ans=eval(self.s)
                    self.ans=round(self.ans,8)
                    self.textbox1.setText(str(self.ans))
            except:
                    self.textbox1.setText("Error in input")

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.Button_ln.setText(_translate("Calculator", "ln"))
        self.Button_1.setText(_translate("Calculator", "1"))
        self.Button_1.setShortcut(_translate("Calculator", "1"))
        self.Button_cos.setText(_translate("Calculator", "Cos"))
        self.Button_6.setText(_translate("Calculator", "6"))
        self.Button_6.setShortcut(_translate("Calculator", "6"))
        self.Button_inverse.setText(_translate("Calculator", "1/x"))
        self.Button_3.setText(_translate("Calculator", "3"))
        self.Button_3.setShortcut(_translate("Calculator", "3"))
        self.push_sqrt.setText(_translate("Calculator", "√"))
        self.Button_tan.setText(_translate("Calculator", "Tan"))
        self.Button_5.setText(_translate("Calculator", "5"))
        self.Button_5.setShortcut(_translate("Calculator", "5"))
        self.Button_equals.setText(_translate("Calculator", "="))
        self.Button_equals.setShortcut(_translate("Calculator", "Return"))
        self.Button_arctan.setText(_translate("Calculator", "arc tan"))
        self.Button_plus.setText(_translate("Calculator", "+"))
        self.Button_plus.setShortcut(_translate("Calculator", "+"))
        self.Button_power.setText(_translate("Calculator", "^n"))
        self.Button_power.setShortcut(_translate("Calculator", "^"))
        self.push_pi.setText(_translate("Calculator", "π"))
        self.Button_cube.setText(_translate("Calculator", "^3"))
        self.Button_mul.setText(_translate("Calculator", "×"))
        self.Button_mul.setShortcut(_translate("Calculator", "*"))
        self.push_close.setText(_translate("Calculator", "Close"))
        self.Button_square.setText(_translate("Calculator", "^2"))
        self.Button_square.setShortcut(_translate("Calculator", "S"))
        self.push_cl.setText(_translate("Calculator", ")"))
        self.push_cl.setShortcut(_translate("Calculator",")"))
        self.Button_arcsin.setText(_translate("Calculator", "arc sin"))
        self.push_op.setText(_translate("Calculator", "("))
        self.push_op.setShortcut(_translate("Calculator","("))
        self.Button_2.setText(_translate("Calculator", "2"))
        self.Button_2.setShortcut(_translate("Calculator", "2"))
        self.Button_div.setText(_translate("Calculator", "÷"))
        self.Button_div.setShortcut(_translate("Calculator", "/"))
        self.Button_sinh.setText(_translate("Calculator", "Sin h"))
        self.Button_9.setText(_translate("Calculator", "9"))
        self.Button_9.setShortcut(_translate("Calculator", "9"))
        self.Button_arccos.setText(_translate("Calculator", "arc cos"))
        self.Button_point.setText(_translate("Calculator", "."))
        self.Button_point.setShortcut(_translate("Calculator", "."))
        self.Button_tanh.setText(_translate("Calculator", "Tan h"))
        self.Button_log.setText(_translate("Calculator", "log"))
        self.Button_sin.setText(_translate("Calculator", "Sin"))
        self.Button_0.setText(_translate("Calculator", "0"))
        self.Button_0.setShortcut(_translate("Calculator", "0"))
        self.Button_4.setText(_translate("Calculator", "4"))
        self.Button_4.setShortcut(_translate("Calculator", "4"))
        self.Button_minus.setText(_translate("Calculator", "-"))
        self.Button_minus.setShortcut(_translate("Calculator", "-"))
        self.Button_7.setText(_translate("Calculator", "7"))
        self.Button_7.setShortcut(_translate("Calculator", "7"))
        self.Button_8.setText(_translate("Calculator", "8"))
        self.Button_8.setShortcut(_translate("Calculator", "8"))
        self.Button_cosh.setText(_translate("Calculator", "Cos h"))
        self.pushButton_2.setText(_translate("Calculator", "exp"))
        self.pushButton_3.setText(_translate("Calculator", "±"))
        self.pushButton_4.setText(_translate("Calculator", "clear"))
        self.pushButton_4.setShortcut(_translate("Calculator","Del"))
        self.pushButton.setText(_translate("Calculator", "<-"))
        self.pushButton.setShortcut(_translate("Calculator","Backspace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
