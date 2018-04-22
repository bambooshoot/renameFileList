# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\RenameFileList.ui'
#
# Created: Sun Apr 22 16:53:21 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_Source = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Source.setGeometry(QtCore.QRect(10, 70, 441, 481))
        self.listWidget_Source.setObjectName("listWidget_Source")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_NewName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_NewName.setObjectName("lineEdit_NewName")
        self.gridLayout.addWidget(self.lineEdit_NewName, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.listWidget_Target = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Target.setGeometry(QtCore.QRect(470, 70, 431, 481))
        self.listWidget_Target.setObjectName("listWidget_Target")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(470, 10, 431, 54))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.btn_Rename = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_Rename.setObjectName("btn_Rename")
        self.gridLayout_2.addWidget(self.btn_Rename, 0, 1, 1, 1)
        self.btn_Preview = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_Preview.setObjectName("btn_Preview")
        self.gridLayout_2.addWidget(self.btn_Preview, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.spinBox_StartFrame = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_StartFrame.setMaximum(9999)
        self.spinBox_StartFrame.setProperty("value", 1)
        self.spinBox_StartFrame.setObjectName("spinBox_StartFrame")
        self.horizontalLayout.addWidget(self.spinBox_StartFrame)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Rename FileList", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "NewName", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "把文件往下面列表拽", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "新文件名列表预览", None, -1))
        self.btn_Rename.setText(QtWidgets.QApplication.translate("MainWindow", "改名", None, -1))
        self.btn_Preview.setText(QtWidgets.QApplication.translate("MainWindow", "预览", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "%04d代表数字部分", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "开头数字", None, -1))

