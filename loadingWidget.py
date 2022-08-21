from PyQt5 import QtWidgets, QtGui, QtCore
from loadingUiDesign import Ui_loadingWidget


class loadingWidget(QtWidgets.QWidget, Ui_loadingWidget):
    def __init__(self, parent=None, min_val=0, max_val=100, cur_val=0, file='-'):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.min = min_val
        self.max = max_val
        self.cur = cur_val
        self.file = file

        self.fileName_label.setText(str(self.file))
        self.progressBar.setMinimum(self.min)
        self.progressBar.setMaximum(self.max)
        self.progressBar.setValue(self.cur)

    def change_cur(self, cur_val):
        self.cur = cur_val
        self.progressBar.setValue(self.cur)
        if self.cur == self.max:
            self.ok_pushButton.setEnabled(True)
