# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewPicturesUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewWidget(object):
    def setupUi(self, viewWidget):
        viewWidget.setObjectName("viewWidget")
        viewWidget.resize(720, 751)
        self.control_groupBox = QtWidgets.QGroupBox(viewWidget)
        self.control_groupBox.setGeometry(QtCore.QRect(20, 90, 200, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_groupBox.sizePolicy().hasHeightForWidth())
        self.control_groupBox.setSizePolicy(sizePolicy)
        self.control_groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.control_groupBox.setObjectName("control_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.control_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_pushButton = QtWidgets.QPushButton(self.control_groupBox)
        self.save_pushButton.setObjectName("save_pushButton")
        self.verticalLayout.addWidget(self.save_pushButton)
        self.line = QtWidgets.QFrame(self.control_groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.next_pushButton = QtWidgets.QPushButton(self.control_groupBox)
        self.next_pushButton.setObjectName("next_pushButton")
        self.verticalLayout.addWidget(self.next_pushButton)
        self.prev_pushButton = QtWidgets.QPushButton(self.control_groupBox)
        self.prev_pushButton.setObjectName("prev_pushButton")
        self.verticalLayout.addWidget(self.prev_pushButton)
        self.picNum_comboBox = QtWidgets.QComboBox(self.control_groupBox)
        self.picNum_comboBox.setObjectName("picNum_comboBox")
        self.verticalLayout.addWidget(self.picNum_comboBox)
        self.line_2 = QtWidgets.QFrame(self.control_groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.control_groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.diap_init_label = QtWidgets.QLabel(self.control_groupBox)
        self.diap_init_label.setObjectName("diap_init_label")
        self.verticalLayout.addWidget(self.diap_init_label)
        self.diap_init_spinBox = QtWidgets.QSpinBox(self.control_groupBox)
        self.diap_init_spinBox.setMaximum(255)
        self.diap_init_spinBox.setObjectName("diap_init_spinBox")
        self.verticalLayout.addWidget(self.diap_init_spinBox)
        self.diap_diff_label = QtWidgets.QLabel(self.control_groupBox)
        self.diap_diff_label.setObjectName("diap_diff_label")
        self.verticalLayout.addWidget(self.diap_diff_label)
        self.diap_diff_spinBox = QtWidgets.QSpinBox(self.control_groupBox)
        self.diap_diff_spinBox.setMaximum(255)
        self.diap_diff_spinBox.setObjectName("diap_diff_spinBox")
        self.verticalLayout.addWidget(self.diap_diff_spinBox)
        self.line_4 = QtWidgets.QFrame(self.control_groupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(viewWidget)
        QtCore.QMetaObject.connectSlotsByName(viewWidget)

    def retranslateUi(self, viewWidget):
        _translate = QtCore.QCoreApplication.translate
        viewWidget.setWindowTitle(_translate("viewWidget", "View pictures"))
        self.control_groupBox.setTitle(_translate("viewWidget", "Control"))
        self.save_pushButton.setText(_translate("viewWidget", "Save page"))
        self.next_pushButton.setText(_translate("viewWidget", "Next -->"))
        self.prev_pushButton.setText(_translate("viewWidget", "<-- Previous"))
        self.diap_init_label.setText(_translate("viewWidget", "Поднять диапазон изнач.:"))
        self.diap_diff_label.setText(_translate("viewWidget", "Поднять диапазон дифф.:"))
