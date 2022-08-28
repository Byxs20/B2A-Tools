# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\GUI\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 614)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 301, 561))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit = MyQPlanTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(130, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_8.setReadOnly(True)
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.horizontalLayout_7.addWidget(self.plainTextEdit_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(330, 21, 301, 561))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout.addWidget(self.plainTextEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.horizontalLayout_3.addWidget(self.plainTextEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.horizontalLayout_4.addWidget(self.plainTextEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.horizontalLayout_5.addWidget(self.plainTextEdit_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.widget1)
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.horizontalLayout_6.addWidget(self.plainTextEdit_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binary转换Ascii工具   作者:Byxs20"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "输入二进制字符串。"))
        self.checkBox.setText(_translate("MainWindow", "是否进行0和1互换"))
        self.pushButton.setText(_translate("MainWindow", "转换"))
        self.label_7.setText(_translate("MainWindow", "          正常情况:"))
        self.label.setText(_translate("MainWindow", "[7Bit]:"))
        self.label_2.setText(_translate("MainWindow", "[8Bit]:"))
        self.label_8.setText(_translate("MainWindow", "          全部字节倒序后转换Ascii码:"))
        self.label_4.setText(_translate("MainWindow", "[7Bit]:"))
        self.label_3.setText(_translate("MainWindow", "[8Bit]:"))
        self.label_9.setText(_translate("MainWindow", "          每个字节依次倒序后转换Ascii码:"))
        self.label_6.setText(_translate("MainWindow", "[7Bit]:"))
        self.label_5.setText(_translate("MainWindow", "[8Bit]:"))
from src.GUI.myqplantextedit import MyQPlanTextEdit