# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setMinimumSize(QtCore.QSize(500, 400))
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:#555;")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.submit_report_btn = QtWidgets.QPushButton(Dialog)
        self.submit_report_btn.setEnabled(False)
        self.submit_report_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.submit_report_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.submit_report_btn.setFont(font)
        self.submit_report_btn.setStyleSheet("QPushButton{\n"
"    background-color:#7dc855;\n"
"    color:#fff;\n"
"    border:1px solid rgb(240, 240, 240);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(143, 229, 97);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(105, 168, 71);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color:grey\n"
"}")
        self.submit_report_btn.setObjectName("submit_report_btn")
        self.gridLayout.addWidget(self.submit_report_btn, 3, 0, 1, 2)
        self.problem_te = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.problem_te.setFont(font)
        self.problem_te.setStyleSheet("border-radius:4px;\n"
"border:1px solid rgb(200,200,200);")
        self.problem_te.setObjectName("problem_te")
        self.gridLayout.addWidget(self.problem_te, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "报告问题"))
        self.submit_report_btn.setText(_translate("Dialog", "提交"))
        self.problem_te.setPlaceholderText(_translate("Dialog", "请输入您想反馈的信息..."))
        self.label.setText(_translate("Dialog", "窗口控件"))

import resource_rc
