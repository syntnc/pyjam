# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 368)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 50, 671, 311))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/unmute.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 3)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 3)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.horizontal_3 = QtWidgets.QHBoxLayout()
        self.horizontal_3.setObjectName("horizontal_3")
        self.label_37 = QtWidgets.QLabel(self.widget)
        self.label_37.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.horizontal_3.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.widget)
        self.label_38.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.horizontal_3.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.widget)
        self.label_39.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.horizontal_3.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.widget)
        self.label_40.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.horizontal_3.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.widget)
        self.label_41.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.horizontal_3.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.widget)
        self.label_42.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.horizontal_3.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.widget)
        self.label_43.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.horizontal_3.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.widget)
        self.label_44.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.horizontal_3.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.widget)
        self.label_45.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.horizontal_3.addWidget(self.label_45)
        self.label_46 = QtWidgets.QLabel(self.widget)
        self.label_46.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.horizontal_3.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.widget)
        self.label_47.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.horizontal_3.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(self.widget)
        self.label_48.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.horizontal_3.addWidget(self.label_48)
        self.label_49 = QtWidgets.QLabel(self.widget)
        self.label_49.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.horizontal_3.addWidget(self.label_49)
        self.label_50 = QtWidgets.QLabel(self.widget)
        self.label_50.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.horizontal_3.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(self.widget)
        self.label_51.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.horizontal_3.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.widget)
        self.label_52.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.horizontal_3.addWidget(self.label_52)
        self.gridLayout_4.addLayout(self.horizontal_3, 3, 1, 1, 1)
        self.horizontal_2 = QtWidgets.QHBoxLayout()
        self.horizontal_2.setObjectName("horizontal_2")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontal_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontal_2.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.horizontal_2.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.horizontal_2.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.horizontal_2.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.horizontal_2.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.horizontal_2.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.horizontal_2.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.widget)
        self.label_27.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.horizontal_2.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.horizontal_2.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.horizontal_2.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.horizontal_2.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.widget)
        self.label_31.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.horizontal_2.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.horizontal_2.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.widget)
        self.label_33.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.horizontal_2.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.widget)
        self.label_34.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.horizontal_2.addWidget(self.label_34)
        self.gridLayout_4.addLayout(self.horizontal_2, 2, 1, 1, 1)
        self.horizontal_1 = QtWidgets.QHBoxLayout()
        self.horizontal_1.setObjectName("horizontal_1")
        self.label_0_0 = QtWidgets.QLabel(self.widget)
        self.label_0_0.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_0_0.setText("")
        self.label_0_0.setObjectName("label_0_0")
        self.horizontal_1.addWidget(self.label_0_0)
        self.label_0_1 = QtWidgets.QLabel(self.widget)
        self.label_0_1.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_0_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_0_1.setText("")
        self.label_0_1.setObjectName("label_0_1")
        self.horizontal_1.addWidget(self.label_0_1)
        self.label_0_2 = QtWidgets.QLabel(self.widget)
        self.label_0_2.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_0_2.setText("")
        self.label_0_2.setObjectName("label_0_2")
        self.horizontal_1.addWidget(self.label_0_2)
        self.label2_4 = QtWidgets.QLabel(self.widget)
        self.label2_4.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label2_4.setText("")
        self.label2_4.setObjectName("label2_4")
        self.horizontal_1.addWidget(self.label2_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontal_1.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontal_1.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontal_1.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontal_1.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontal_1.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontal_1.addWidget(self.label_7)
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.horizontal_1.addWidget(self.label_1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontal_1.addWidget(self.label_9)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontal_1.addWidget(self.label_12)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontal_1.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setStyleSheet("background-color: #40464d;\n"
"border: 1px solid white;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontal_1.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setStyleSheet("background-color: #1790BB;\n"
"border: 1px solid white;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontal_1.addWidget(self.label_13)
        self.gridLayout_4.addLayout(self.horizontal_1, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_86 = QtWidgets.QLabel(self.widget)
        self.label_86.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_86.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_86.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_86.setText("")
        self.label_86.setObjectName("label_86")
        self.horizontalLayout_6.addWidget(self.label_86)
        self.label_85 = QtWidgets.QLabel(self.widget)
        self.label_85.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_85.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_85.setText("")
        self.label_85.setObjectName("label_85")
        self.horizontalLayout_6.addWidget(self.label_85)
        self.label_89 = QtWidgets.QLabel(self.widget)
        self.label_89.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_89.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_89.setText("")
        self.label_89.setObjectName("label_89")
        self.horizontalLayout_6.addWidget(self.label_89)
        self.label_92 = QtWidgets.QLabel(self.widget)
        self.label_92.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_92.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_92.setText("")
        self.label_92.setObjectName("label_92")
        self.horizontalLayout_6.addWidget(self.label_92)
        self.label_94 = QtWidgets.QLabel(self.widget)
        self.label_94.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_94.setStyleSheet("background-color: rgb(27, 184, 90);\n"
"border: 1px solid grey;")
        self.label_94.setText("")
        self.label_94.setObjectName("label_94")
        self.horizontalLayout_6.addWidget(self.label_94)
        self.label_96 = QtWidgets.QLabel(self.widget)
        self.label_96.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_96.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_96.setText("")
        self.label_96.setObjectName("label_96")
        self.horizontalLayout_6.addWidget(self.label_96)
        self.label_97 = QtWidgets.QLabel(self.widget)
        self.label_97.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_97.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_97.setText("")
        self.label_97.setObjectName("label_97")
        self.horizontalLayout_6.addWidget(self.label_97)
        self.label_99 = QtWidgets.QLabel(self.widget)
        self.label_99.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_99.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_99.setText("")
        self.label_99.setObjectName("label_99")
        self.horizontalLayout_6.addWidget(self.label_99)
        self.label_101 = QtWidgets.QLabel(self.widget)
        self.label_101.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_101.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_101.setText("")
        self.label_101.setObjectName("label_101")
        self.horizontalLayout_6.addWidget(self.label_101)
        self.label_102 = QtWidgets.QLabel(self.widget)
        self.label_102.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_102.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_102.setText("")
        self.label_102.setObjectName("label_102")
        self.horizontalLayout_6.addWidget(self.label_102)
        self.label_100 = QtWidgets.QLabel(self.widget)
        self.label_100.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_100.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_100.setText("")
        self.label_100.setObjectName("label_100")
        self.horizontalLayout_6.addWidget(self.label_100)
        self.label_98 = QtWidgets.QLabel(self.widget)
        self.label_98.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_98.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_98.setText("")
        self.label_98.setObjectName("label_98")
        self.horizontalLayout_6.addWidget(self.label_98)
        self.label_95 = QtWidgets.QLabel(self.widget)
        self.label_95.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_95.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_95.setText("")
        self.label_95.setObjectName("label_95")
        self.horizontalLayout_6.addWidget(self.label_95)
        self.label_93 = QtWidgets.QLabel(self.widget)
        self.label_93.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_93.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_93.setText("")
        self.label_93.setObjectName("label_93")
        self.horizontalLayout_6.addWidget(self.label_93)
        self.label_91 = QtWidgets.QLabel(self.widget)
        self.label_91.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_91.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_91.setText("")
        self.label_91.setObjectName("label_91")
        self.horizontalLayout_6.addWidget(self.label_91)
        self.label_90 = QtWidgets.QLabel(self.widget)
        self.label_90.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_90.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_90.setText("")
        self.label_90.setObjectName("label_90")
        self.horizontalLayout_6.addWidget(self.label_90)
        self.label_88 = QtWidgets.QLabel(self.widget)
        self.label_88.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_88.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_88.setText("")
        self.label_88.setObjectName("label_88")
        self.horizontalLayout_6.addWidget(self.label_88)
        self.label_87 = QtWidgets.QLabel(self.widget)
        self.label_87.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_87.setStyleSheet("background-color: white;\n"
"border: 1px solid grey;")
        self.label_87.setText("")
        self.label_87.setObjectName("label_87")
        self.horizontalLayout_6.addWidget(self.label_87)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 12)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 4)
        self.gridLayout_4.setRowStretch(2, 4)
        self.gridLayout_4.setRowStretch(3, 4)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 671, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/paused.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images/paused.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images/paused.svg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images/play.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("images/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.setAutoRepeat(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_55 = QtWidgets.QLabel(self.widget1)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_4.addWidget(self.label_55)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label_0_0.raise_()
        self.label_0_1.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_1.raise_()
        self.label_15.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.pushButton_7.raise_()
        self.label_55.raise_()
        self.label_85.raise_()
        self.label_86.raise_()
        self.label_87.raise_()
        self.label_88.raise_()
        self.label_89.raise_()
        self.label_90.raise_()
        self.label_91.raise_()
        self.label_92.raise_()
        self.label_93.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_8.setToolTip(_translate("Form", "<html><head/><body><p>Select file</p></body></html>"))
        self.pushButton_3.setToolTip(_translate("Form", "<html><head/><body><p>Set audio source</p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "hat.wav"))
        self.pushButton_5.setToolTip(_translate("Form", "<html><head/><body><p>Set audio source</p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "hat.wav"))
        self.pushButton_9.setToolTip(_translate("Form", "<html><head/><body><p>Select file</p></body></html>"))
        self.pushButton.setToolTip(_translate("Form", "<html><head/><body><p>Set audio source</p></body></html>"))
        self.pushButton.setText(_translate("Form", "hat.wav"))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p>Select file</p></body></html>"))
        self.label_55.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">PyMixerj</span></p></body></html>"))



import sys
from PyQt5.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
