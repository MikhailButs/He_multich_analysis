# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadShtUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shtWidget(object):
    def setupUi(self, shtWidget):
        shtWidget.setObjectName("shtWidget")
        shtWidget.resize(600, 483)
        self.verticalLayout = QtWidgets.QVBoxLayout(shtWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(shtWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.shtLink_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.shtLink_lineEdit.setText("")
        self.shtLink_lineEdit.setObjectName("shtLink_lineEdit")
        self.gridLayout.addWidget(self.shtLink_lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.shtLink_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.shtLink_pushButton.setObjectName("shtLink_pushButton")
        self.gridLayout.addWidget(self.shtLink_pushButton, 1, 0, 1, 3)
        self.shtSelect_toolButton = QtWidgets.QToolButton(self.groupBox)
        self.shtSelect_toolButton.setObjectName("shtSelect_toolButton")
        self.gridLayout.addWidget(self.shtSelect_toolButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(shtWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.fileStartTime_label = QtWidgets.QLabel(self.groupBox_2)
        self.fileStartTime_label.setObjectName("fileStartTime_label")
        self.gridLayout_2.addWidget(self.fileStartTime_label, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.fileEndTime_label = QtWidgets.QLabel(self.groupBox_2)
        self.fileEndTime_label.setObjectName("fileEndTime_label")
        self.gridLayout_2.addWidget(self.fileEndTime_label, 1, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setMinimumSize(QtCore.QSize(300, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 4)
        self.sht_tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.sht_tableWidget.setObjectName("sht_tableWidget")
        self.sht_tableWidget.setColumnCount(0)
        self.sht_tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.sht_tableWidget, 4, 0, 1, 4)
        self.fileName_label = QtWidgets.QLabel(self.groupBox_2)
        self.fileName_label.setObjectName("fileName_label")
        self.gridLayout_2.addWidget(self.fileName_label, 0, 1, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(shtWidget)
        QtCore.QMetaObject.connectSlotsByName(shtWidget)

    def retranslateUi(self, shtWidget):
        _translate = QtCore.QCoreApplication.translate
        shtWidget.setWindowTitle(_translate("shtWidget", ".SHT settings"))
        self.groupBox.setTitle(_translate("shtWidget", "Load data"))
        self.shtLink_lineEdit.setPlaceholderText(_translate("shtWidget", "input an absolute link to .SHT file"))
        self.label.setText(_translate("shtWidget", ".SHT abs. link"))
        self.shtLink_pushButton.setText(_translate("shtWidget", "Load"))
        self.shtSelect_toolButton.setText(_translate("shtWidget", "..."))
        self.groupBox_2.setTitle(_translate("shtWidget", "Loaded"))
        self.label_5.setText(_translate("shtWidget", "ended at"))
        self.label_2.setText(_translate("shtWidget", "Current file"))
        self.fileStartTime_label.setText(_translate("shtWidget", "00:00:00"))
        self.label_4.setText(_translate("shtWidget", "Diagnostics"))
        self.label_3.setText(_translate("shtWidget", "Loading started at"))
        self.fileEndTime_label.setText(_translate("shtWidget", "00:00:00"))
        self.fileName_label.setText(_translate("shtWidget", "name"))
