# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *

from resource.page2_2_ui import Ui_Form

import sys


class PageTwoTwoPane(QDialog,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setupUi(self)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=PageTwoTwoPane()
    form.show()
    sys.exit(app.exec_())