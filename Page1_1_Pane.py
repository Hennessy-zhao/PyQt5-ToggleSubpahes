# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *

from resource.page1_1_ui import Ui_Form

import sys


class PageOneOnePane(QDialog,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setupUi(self)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=PageOneOnePane()
    form.show()
    sys.exit(app.exec_())