# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *

from resource.page_welcome_ui import Ui_Form

import sys


class PageWelcomePane(QDialog,Ui_Form):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setupUi(self)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=PageWelcomePane()
    form.show()
    sys.exit(app.exec_())