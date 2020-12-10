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
        self.select_tBox.setCurrentIndex(0)                 # 设置左侧选项卡选项1展开

        # 添加欢迎子页面
        self.content_tabW.addTab(PageWelcomePane(), '欢迎使用')     # 添加欢迎子页面
        self.content_tabW.tabBar().setTabButton(0, self.content_tabW.tabBar().RightSide, None)  # 设置欢迎子页面的关闭按钮不可点击



    # 关闭界面触发函数
    def closeEvent(self, QCloseEvent):
        for page_widget in self.page_widget_list:       #遍历子页面列表
            page_widget.close()                         #关闭子页面
            page_widget.deleteLater()                   #销毁子页面


    # 定义变量函数
    def define_variate(self):
        self.page_widget_list=[PageOneOnePane(),PageOneTwoPane(),PageTwoOnePane(),PageTwoTwoPane(),PageThreeOnePane()]  #定义并初始化子页面界面
        self.report_dialog = ReportDialog(self)             # 创建报告问题模块


    # 选项卡触发函数       选项卡被点击
    def change_tab(self):
        sender = self.sender()          # 获取事件发送者-QPushButton
        filter_list = list(filter(str.isdigit, sender.objectName()))  # 获取控件的objname的数字项
        tab_index = int(filter_list[0])

        tabW=self.content_tabW.children()               #获取显示子页面控件QtabWidget的子控件
        page_widget_exist=tabW[0].children()            #获取已显示的所有子页面控件列表

        tab_widget=self.page_widget_list[tab_index]     #获取当前要显示的子页面对象
        if tab_index not in page_widget_exist:          #判断该子页面是否被添加
            # 添加子页面
            tab_text = sender.text()                            # 获取当前按钮text内容
            self.content_tabW.addTab(tab_widget, tab_text)      #添加子页面

        self.content_tabW.setCurrentWidget(tab_widget)          # 将子页面显示在最顶层


    # 删除page点击触发函数/删除page函数
    def close_tab_page(self, page_index):
        self.content_tabW.removeTab(page_index)                 # 移除该子页面

    #显示报告窗口
    def show_report_Pane(self):
        self.report_dialog.show()                               #显示报告窗口

    #切换系统按钮被点击
    def change_system(self):
        QMessageBox.about(self, "切换系统", "切换系统啦啦啦啦啦啦啦")      #弹出提示框

    # 切换用户按钮被点击
    def change_user(self):
        reply = QMessageBox.question(self, "是否切换账号", "您确定切换当前账号吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)       #弹出提示框
        if reply == 16384:                                                  #弹出的提示框点击确定
            QMessageBox.about(self,"切换账号","切换账号啦啦啦啦啦啦啦")       #弹出提示框




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=AdminPane()
    form.show()
    sys.exit(app.exec_())