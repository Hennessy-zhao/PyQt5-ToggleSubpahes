# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1242, 861)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: #000000;\n"
"color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#ffffff;")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.identity_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.identity_label.setFont(font)
        self.identity_label.setStyleSheet("color:#ffffff;")
        self.identity_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.identity_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.identity_label.setObjectName("identity_label")
        self.horizontalLayout.addWidget(self.identity_label)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#ffffff;")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.worknumber_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.worknumber_label.setFont(font)
        self.worknumber_label.setStyleSheet("color:#ffffff;")
        self.worknumber_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.worknumber_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.worknumber_label.setObjectName("worknumber_label")
        self.horizontalLayout.addWidget(self.worknumber_label)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setStyleSheet("")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_4.setContentsMargins(0, 2, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.logout_btn = QtWidgets.QPushButton(self.widget_8)
        self.logout_btn.setMinimumSize(QtCore.QSize(22, 22))
        self.logout_btn.setMaximumSize(QtCore.QSize(22, 22))
        self.logout_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout_btn.setStyleSheet("QPushButton{\n"
"    border-image: url(:/icon/images/icon_user_main.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/icon/images/icon_user_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/icon/images/icon_user_pressed.png);\n"
"}\n"
"\n"
"QToolTip{\n"
"    color:#000;\n"
"}")
        self.logout_btn.setText("")
        self.logout_btn.setObjectName("logout_btn")
        self.gridLayout_4.addWidget(self.logout_btn, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_8)
        self.pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(22, 22))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-image: url(:/icon/images/icon_switch_main.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/icon/images/icon_switch_hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/icon/images/icon_switch_pressed.png);\n"
"}\n"
"\n"
"QToolTip{\n"
"    color:#000;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_8)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_5.addWidget(self.widget)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.list_widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_widget.sizePolicy().hasHeightForWidth())
        self.list_widget.setSizePolicy(sizePolicy)
        self.list_widget.setMinimumSize(QtCore.QSize(50, 0))
        self.list_widget.setBaseSize(QtCore.QSize(180, 0))
        self.list_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_widget.setStyleSheet("background-color: rgb(52,58,64);\n"
"")
        self.list_widget.setObjectName("list_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.list_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.custom_label = QtWidgets.QLabel(self.list_widget)
        self.custom_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.custom_label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.custom_label.setFont(font)
        self.custom_label.setStyleSheet("color:#ffffff;\n"
"background-color: rgb(75, 137, 253);\n"
"padding-top:10px;\n"
"padding-bottom:10px;")
        self.custom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.custom_label.setWordWrap(False)
        self.custom_label.setIndent(-1)
        self.custom_label.setObjectName("custom_label")
        self.verticalLayout_2.addWidget(self.custom_label)
        self.widget_6 = QtWidgets.QWidget(self.list_widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-bottom:1px solid rgb(255,255,255);\n"
"padding-top:10px;\n"
"padding-bottom:10px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.select_tBox = QtWidgets.QToolBox(self.widget_6)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.select_tBox.setFont(font)
        self.select_tBox.setStyleSheet("QToolBox::tab {\n"
"         border:none;\n"
"        color:#ffffff;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:#ffffff;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,255,255,50);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgba(255,255,255,80);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"")
        self.select_tBox.setObjectName("select_tBox")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 69, 551))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tab_list_0 = QtWidgets.QPushButton(self.page_2)
        self.tab_list_0.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.tab_list_0.setFont(font)
        self.tab_list_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_list_0.setObjectName("tab_list_0")
        self.verticalLayout_6.addWidget(self.tab_list_0)
        self.tab_list_1 = QtWidgets.QPushButton(self.page_2)
        self.tab_list_1.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.tab_list_1.setFont(font)
        self.tab_list_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_list_1.setObjectName("tab_list_1")
        self.verticalLayout_6.addWidget(self.tab_list_1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 462, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/icon_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_tBox.addItem(self.page_2, icon, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 69, 551))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.page_3.setFont(font)
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tab_list_2 = QtWidgets.QPushButton(self.page_3)
        self.tab_list_2.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.tab_list_2.setFont(font)
        self.tab_list_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_list_2.setObjectName("tab_list_2")
        self.verticalLayout_7.addWidget(self.tab_list_2)
        self.tab_list_3 = QtWidgets.QPushButton(self.page_3)
        self.tab_list_3.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.tab_list_3.setFont(font)
        self.tab_list_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_list_3.setObjectName("tab_list_3")
        self.verticalLayout_7.addWidget(self.tab_list_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.select_tBox.addItem(self.page_3, icon, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 69, 551))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tab_list_4 = QtWidgets.QPushButton(self.page_4)
        self.tab_list_4.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.tab_list_4.setFont(font)
        self.tab_list_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_list_4.setObjectName("tab_list_4")
        self.verticalLayout_8.addWidget(self.tab_list_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 502, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.select_tBox.addItem(self.page_4, icon, "")
        self.verticalLayout.addWidget(self.select_tBox)
        self.report_problem_btn = QtWidgets.QPushButton(self.widget_6)
        self.report_problem_btn.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.report_problem_btn.setFont(font)
        self.report_problem_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report_problem_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border:none;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,255,255,0.15);\n"
"    color:rgb(255,255,255);\n"
"}\n"
"")
        self.report_problem_btn.setFlat(False)
        self.report_problem_btn.setObjectName("report_problem_btn")
        self.verticalLayout.addWidget(self.report_problem_btn)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.content_widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content_widget.sizePolicy().hasHeightForWidth())
        self.content_widget.setSizePolicy(sizePolicy)
        self.content_widget.setStyleSheet("background-color:rgb(255,255,255);\n"
"")
        self.content_widget.setObjectName("content_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content_widget)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.content_tabW = QtWidgets.QTabWidget(self.content_widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.content_tabW.setFont(font)
        self.content_tabW.setStyleSheet("QWidget.tab_page{\n"
"    background-color: #ffffff;\n"
"    border-top:1px solid rgb(230,230,230);\n"
"}\n"
"QTabWidget#content_tabW::pane{\n"
"    \n"
"}\n"
" QTabWidget#content_tabW::tab-bar {\n"
" border:1px solid black;\n"
"}\n"
"\n"
" QTabWidget#content_tabW > QTabBar::tab {\n"
"    background-color: #ffffff;\n"
"    color: #555555;\n"
"    padding:5% 8% 3% 8%;\n"
"    border-bottom:2px solid rgb(75, 137, 253);\n"
"}\n"
"\n"
"QTabWidget#content_tabW > QTabBar::tab:!selected {\n"
"    background-color: #F5F5F5;\n"
"    color:rgb(102,102,102);\n"
"    border:1px solid rgb(230,230,230);\n"
"    border-left:none;\n"
" }\n"
"\n"
"QTabWidget#content_tabW > QTabBar::tab:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    color:rgb(102,102,102);\n"
" }\n"
"\n"
"\n"
"")
        self.content_tabW.setTabPosition(QtWidgets.QTabWidget.North)
        self.content_tabW.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.content_tabW.setElideMode(QtCore.Qt.ElideLeft)
        self.content_tabW.setUsesScrollButtons(True)
        self.content_tabW.setDocumentMode(False)
        self.content_tabW.setTabsClosable(True)
        self.content_tabW.setMovable(True)
        self.content_tabW.setTabBarAutoHide(False)
        self.content_tabW.setObjectName("content_tabW")
        self.horizontalLayout_2.addWidget(self.content_tabW)
        self.verticalLayout_5.addWidget(self.splitter)
        self.verticalLayout_5.setStretch(1, 1)

        self.retranslateUi(Form)
        self.select_tBox.setCurrentIndex(2)
        self.content_tabW.setCurrentIndex(-1)
        self.pushButton.clicked.connect(Form.change_system)
        self.logout_btn.clicked.connect(Form.change_user)
        self.tab_list_0.clicked.connect(Form.change_tab)
        self.tab_list_1.clicked.connect(Form.change_tab)
        self.tab_list_2.clicked.connect(Form.change_tab)
        self.tab_list_3.clicked.connect(Form.change_tab)
        self.tab_list_4.clicked.connect(Form.change_tab)
        self.content_tabW.tabCloseRequested['int'].connect(Form.close_tab_page)
        self.report_problem_btn.clicked.connect(Form.show_report_Pane)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "系统名称-系统名称-系统名称"))
        self.label_2.setText(_translate("Form", "系统名称-系统名称-系统名称-系统名称"))
        self.label_3.setText(_translate("Form", "信息1："))
        self.identity_label.setText(_translate("Form", "信息1"))
        self.label_5.setText(_translate("Form", "信息2："))
        self.worknumber_label.setText(_translate("Form", "信息2"))
        self.logout_btn.setToolTip(_translate("Form", "切换用户"))
        self.pushButton.setToolTip(_translate("Form", "切换系统"))
        self.custom_label.setText(_translate("Form", "数据信息"))
        self.label_9.setText(_translate("Form", "选项卡"))
        self.tab_list_0.setText(_translate("Form", "页面1_1"))
        self.tab_list_1.setText(_translate("Form", "页面1_2"))
        self.select_tBox.setItemText(self.select_tBox.indexOf(self.page_2), _translate("Form", "选项1"))
        self.tab_list_2.setText(_translate("Form", "页面2_1"))
        self.tab_list_3.setText(_translate("Form", "页面2_2"))
        self.select_tBox.setItemText(self.select_tBox.indexOf(self.page_3), _translate("Form", "选项2"))
        self.tab_list_4.setText(_translate("Form", "页面3_1"))
        self.select_tBox.setItemText(self.select_tBox.indexOf(self.page_4), _translate("Form", "选项3"))
        self.report_problem_btn.setText(_translate("Form", "子窗口"))

import resource_rc
