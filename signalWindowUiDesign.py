# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signalWindowUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sig_check(object):
    def setupUi(self, sig_check):
        sig_check.setObjectName("sig_check")
        sig_check.resize(300, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sig_check.sizePolicy().hasHeightForWidth())
        sig_check.setSizePolicy(sizePolicy)
        sig_check.setMinimumSize(QtCore.QSize(300, 150))
        self.frame = QtWidgets.QFrame(sig_check)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 130))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.zero_signal_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.zero_signal_doubleSpinBox.setDecimals(4)
        self.zero_signal_doubleSpinBox.setMinimum(-9999.9999)
        self.zero_signal_doubleSpinBox.setMaximum(9999.9999)
        self.zero_signal_doubleSpinBox.setObjectName("zero_signal_doubleSpinBox")
        self.gridLayout.addWidget(self.zero_signal_doubleSpinBox, 2, 1, 1, 1)
        self.show_checkBox = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_checkBox.sizePolicy().hasHeightForWidth())
        self.show_checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.show_checkBox.setFont(font)
        self.show_checkBox.setObjectName("show_checkBox")
        self.gridLayout.addWidget(self.show_checkBox, 0, 0, 1, 2)
        self.mult_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.mult_doubleSpinBox.setDecimals(4)
        self.mult_doubleSpinBox.setMinimum(-999.0)
        self.mult_doubleSpinBox.setMaximum(999.99)
        self.mult_doubleSpinBox.setProperty("value", 1.0)
        self.mult_doubleSpinBox.setObjectName("mult_doubleSpinBox")
        self.gridLayout.addWidget(self.mult_doubleSpinBox, 1, 1, 1, 1)
        self.mult_label = QtWidgets.QLabel(self.frame)
        self.mult_label.setObjectName("mult_label")
        self.gridLayout.addWidget(self.mult_label, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.zero_time_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.zero_time_doubleSpinBox.setDecimals(4)
        self.zero_time_doubleSpinBox.setMinimum(-9999.9999)
        self.zero_time_doubleSpinBox.setMaximum(9999.9999)
        self.zero_time_doubleSpinBox.setObjectName("zero_time_doubleSpinBox")
        self.gridLayout.addWidget(self.zero_time_doubleSpinBox, 3, 1, 1, 1)

        self.retranslateUi(sig_check)
        QtCore.QMetaObject.connectSlotsByName(sig_check)

    def retranslateUi(self, sig_check):
        _translate = QtCore.QCoreApplication.translate
        sig_check.setWindowTitle(_translate("sig_check", "Signal"))
        self.show_checkBox.setText(_translate("sig_check", "Name"))
        self.mult_label.setText(_translate("sig_check", "Множитель"))
        self.label.setText(_translate("sig_check", "Ноль сигнала"))
        self.label_2.setText(_translate("sig_check", "Ноль времени"))