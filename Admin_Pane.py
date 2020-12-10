# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *

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
        self.content_tabW.addTab(PageWelcomePane(), '欢迎使用')  # 添加欢迎子页面
        self.content_tabW.tabBar().setTabButton(0, self.content_tabW.tabBar().RightSide, None)  # 设置欢迎子页面的关闭按钮不可点击


    # 关闭界面触发函数
    def closeEvent(self, QCloseEvent):
        for tab_widget in self.tab_list_widget:         #遍历子页面控件列表
            if tab_widget[1]:                           #如果子页面被创建
                tab_widget[1].deleteLater()             #销毁子页面


    # 定义变量函数
    def define_variate(self):
        '''
        选项卡对应子页面控件的列表
        初始每一项设置为[False,False],第一个False表示该子页面未被添加至界面，
        第二个False为该子页面未被创建，创建后存放子页面对象
        '''
        self.tab_list_widget = [[False,False] for i in range(5)]        #选项卡对应子页面控件的列表

        self.report_dialog = ReportDialog(self)             # 创建报告问题模块


    # 选项卡触发函数       选项卡被点击
    def change_tab(self):
        sender = self.sender()                  # 获取事件发送者-QPushButton
        filter_list = list(filter(str.isdigit, sender.objectName()))  # 获取控件的objname的数字项
        tab_index = int(filter_list[0])

        tab_widget = self.tab_list_widget[tab_index]            #获取选项卡对应的子页面数据
        page_widget=tab_widget[1]                               #获取子页面对象
        if not tab_widget[0]:                                   #子页面未被添加至界面
            if not page_widget:                                 #子页面对象未被创建
                page_widget=self.add_tab_page(tab_index)        #创建并获取子页面对象
                self.tab_list_widget[tab_index][1]=page_widget  #修改选项卡列表对应子页面对象数据

            #子页面对象已创建
            tab_text = sender.text()                            #获取当前按钮text内容
            self.content_tabW.addTab(tab_widget[1], tab_text)   #添加子页面
            self.tab_list_widget[tab_index][0]=True             #修改选项卡列表对应子页面是否添加数据

        self.content_tabW.setCurrentWidget(page_widget)      # 将该子页面显示在最顶层

        # 添加页面函数
    def add_tab_page(self, tab_index=-1):
        if tab_index==0:                                    #选项卡1_1被点击
            child_window=PageOneOnePane()                   #创建子页面对象
        elif tab_index==1:                                  #选项卡1_2被点击
            child_window = PageOneTwoPane()                 #创建子页面对象
        elif tab_index==2:                                  #选项卡2_1被点击
            child_window = PageTwoOnePane()                 #创建子页面对象
        elif tab_index==3:                                  #选项卡2_2被点击
            child_window = PageTwoTwoPane()                 #创建子页面对象
        else:                                               #选项卡3_1被点击
            child_window = PageThreeOnePane()               #创建子页面对象

        return child_window                                 #返回添加的子页面对象


    # 删除page点击触发函数/删除page函数
    def close_tab_page(self, page_index):
        page_widget = self.content_tabW.widget(page_index)  # 获取子页面Qwidget
        self.content_tabW.removeTab(page_index)             # 移除该子页面

        for tab_widget in self.tab_list_widget:             #遍历子页面控件列表
            if tab_widget[1]==page_widget:                  #找到当前子页面对应的数据项
                tab_widget[0]=False                         #修改选项卡列表对应子页面是否添加数据


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