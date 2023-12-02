from PyQt5 import QtWidgets
from signalWindowUiDesign import Ui_sig_check


class signalWindowWidget(QtWidgets.QWidget, Ui_sig_check):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_name(self, name):
        self.show_checkBox.setText(name)

    def is_checked(self):
        return self.show_checkBox.isChecked()

    def mult_coef(self):
        return self.mult_doubleSpinBox.value()

    def zero_signal(self):
        return self.zero_signal_doubleSpinBox.value()

    def set_zero_signal(self, zero: float):
        self.zero_signal_doubleSpinBox.setValue(zero)

    def zero_time(self):
        return self.zero_time_doubleSpinBox.value()

    def set_zero_time(self, zero: float):
        self.zero_time_doubleSpinBox.setValue(zero)

