# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *

from resource.report_ui import Ui_Dialog

import sys


class ReportDialog(QDialog,Ui_Dialog):

    def __init__(self,parent=None):
        super().__init__(parent)

        self.setupUi(self)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ReportDialog()
    form.show()
    sys.exit(app.exec_())