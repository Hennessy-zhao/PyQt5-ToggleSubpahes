# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Page_Welcome_Pane import PageWelcomePane
from Report_Dialog import ReportDialog
from Page1_1_Pane import PageOneOnePane
from Page1_2_Pane import PageOneTwoPane
from Page2_1_Pane import PageTwoOnePane
from Page2_2_Pane import PageTwoTwoPane
from Page3_1_Pane import PageThreeOnePane

from resource.admin_ui import Ui_Form
import sys

class AdminPane(QWidget,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.list_widget.resize(130, 0)     #设置选项卡控件初始显示宽度
        self.define_variate()               # 定义变量


    # 设置初始显示内容
    def showEvent(self, QShowEvent):
        self.select_tBox.setCurrentIndex(0)     # 设置左侧选项卡选项1展开

        # 添加欢迎子页面
        self.add_tab_page(tab_text='欢迎使用')  # 添加欢迎子页免
        self.content_tabW.tabBar().setTabButton(0, self.content_tabW.tabBar().RightSide, None)  # 设置欢迎子页面的关闭按钮不可点击




    # 关闭界面触发函数
    def closeEvent(self, QCloseEvent):
        for page_widget in self.tab_list_widget:    #遍历子页面列表
            if page_widget:                         #如果子页面存在
                page_widget.deleteLater()           #销毁子页面


    # 定义变量函数
    def define_variate(self):
        self.tab_list_widget = [False for i in range(5)]    # 选项卡对应子页面控件的列表,初始设置为False,即不存在。存放子页面的Qwidget

        self.report_dialog = ReportDialog(self)             # 创建报告问题模块


    # 选项卡触发函数       选项卡被点击
    def change_tab(self):
        sender = self.sender()                  # 获取事件发送者-QPushButton
        filter_list = list(filter(str.isdigit, sender.objectName()))  # 获取控件的objname的数字项
        tab_index = int(filter_list[0])

        tab_widget = self.tab_list_widget[tab_index]        #获取当前要显示的子页面对象
        if not tab_widget:                                  #判断该子页面是否被添加
            # 添加子页面
            tab_text = sender.text()                        # 获取当前按钮text内容
            tab_widget = self.add_tab_page(tab_index=tab_index, tab_text=tab_text)      #添加子页面
            self.tab_list_widget[tab_index] = tab_widget    # 将QWidget添加至tab_list_widget中对应列表项

        self.content_tabW.setCurrentWidget(tab_widget)      # 将子页面显示在最顶层

        # 添加页面函数
    def add_tab_page(self, tab_index=-1, tab_text=''):
        if tab_index==0:                                    #选项卡1_1被点击
            child_window=PageOneOnePane()                   #创建子页面对象
        elif tab_index==1:                                  #选项卡1_2被点击
            child_window = PageOneTwoPane()                 #创建子页面对象
        elif tab_index==2:                                  #选项卡2_1被点击
            child_window = PageTwoOnePane()                 #创建子页面对象
        elif tab_index==3:                                  #选项卡2_2被点击
            child_window = PageTwoTwoPane()                 #创建子页面对象
        elif tab_index==4:                                  #选项卡3_1被点击
            child_window = PageThreeOnePane()               #创建子页面对象
        else:
            child_window = PageWelcomePane()                #创建子页面对象

        self.content_tabW.addTab(child_window, tab_text)    # 将子窗口添加至子页面

        return child_window                                 #返回添加的子页面对象

    # 删除page点击触发函数/删除page函数
    def close_tab_page(self, page_index):
        page_widget = self.content_tabW.widget(page_index)  # 获取子页面Qwidget
        self.content_tabW.removeTab(page_index)             # 移除该子页面

        self.tab_list_widget[self.tab_list_widget.index(page_widget)]=False     #将被移除的子页面对应的tab_list项设为False
        page_widget.deleteLater()

    # 显示报告窗口
    def show_report_Pane(self):
        self.report_dialog.show()       #显示报告窗口

    # 切换系统按钮被点击
    def change_system(self):
        QMessageBox.about(self, "切换系统", "切换系统啦啦啦啦啦啦啦")      #弹出提示框

    # 切换用户按钮被点击
    def change_user(self):
        reply = QMessageBox.question(self, "是否切换账号", "您确定切换当前账号吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)   #弹出提示框
        if reply == 16384:                                                   #弹出的提示框点击确定
            QMessageBox.about(self,"切换账号","切换账号啦啦啦啦啦啦啦")        #弹出提示框






if __name__=='__main__':
    app=QApplication(sys.argv)
    form=AdminPane()
    form.show()
    sys.exit(app.exec_())