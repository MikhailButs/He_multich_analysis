# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadPicturesUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_picturesWidget(object):
    def setupUi(self, picturesWidget):
        picturesWidget.setObjectName("picturesWidget")
        picturesWidget.resize(600, 615)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(picturesWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(picturesWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.picturesLink_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.picturesLink_lineEdit.setObjectName("picturesLink_lineEdit")
        self.gridLayout.addWidget(self.picturesLink_lineEdit, 0, 1, 1, 2)
        self.picturesSelect_toolButton = QtWidgets.QToolButton(self.groupBox)
        self.picturesSelect_toolButton.setObjectName("picturesSelect_toolButton")
        self.gridLayout.addWidget(self.picturesSelect_toolButton, 0, 3, 1, 1)
        self.oneChPic_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.oneChPic_radioButton.setObjectName("oneChPic_radioButton")
        self.gridLayout.addWidget(self.oneChPic_radioButton, 1, 2, 1, 2)
        self.PicturesLink_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.PicturesLink_pushButton.setObjectName("PicturesLink_pushButton")
        self.gridLayout.addWidget(self.PicturesLink_pushButton, 2, 0, 1, 4)
        self.threeChPic_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.threeChPic_radioButton.setChecked(True)
        self.threeChPic_radioButton.setObjectName("threeChPic_radioButton")
        self.gridLayout.addWidget(self.threeChPic_radioButton, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(picturesWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.interval_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.interval_doubleSpinBox.setDecimals(5)
        self.interval_doubleSpinBox.setMaximum(999.99)
        self.interval_doubleSpinBox.setSingleStep(1e-05)
        self.interval_doubleSpinBox.setObjectName("interval_doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.interval_doubleSpinBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.exposure_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.exposure_doubleSpinBox.setDecimals(5)
        self.exposure_doubleSpinBox.setMaximum(999.99)
        self.exposure_doubleSpinBox.setSingleStep(1e-05)
        self.exposure_doubleSpinBox.setObjectName("exposure_doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.exposure_doubleSpinBox)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.trigger_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.trigger_doubleSpinBox.setDecimals(5)
        self.trigger_doubleSpinBox.setMinimum(-9999.99)
        self.trigger_doubleSpinBox.setMaximum(9999.99)
        self.trigger_doubleSpinBox.setSingleStep(1e-05)
        self.trigger_doubleSpinBox.setObjectName("trigger_doubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.trigger_doubleSpinBox)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(picturesWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.fileStartTime_label = QtWidgets.QLabel(self.groupBox_2)
        self.fileStartTime_label.setObjectName("fileStartTime_label")
        self.gridLayout_2.addWidget(self.fileStartTime_label, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.fileEndTime_label = QtWidgets.QLabel(self.groupBox_2)
        self.fileEndTime_label.setObjectName("fileEndTime_label")
        self.gridLayout_2.addWidget(self.fileEndTime_label, 1, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 4)
        self.pictures_tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.pictures_tableWidget.setObjectName("pictures_tableWidget")
        self.pictures_tableWidget.setColumnCount(0)
        self.pictures_tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.pictures_tableWidget, 6, 0, 1, 4)
        self.fileName_label = QtWidgets.QLabel(self.groupBox_2)
        self.fileName_label.setObjectName("fileName_label")
        self.gridLayout_2.addWidget(self.fileName_label, 0, 1, 1, 3)
        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.retranslateUi(picturesWidget)
        QtCore.QMetaObject.connectSlotsByName(picturesWidget)

    def retranslateUi(self, picturesWidget):
        _translate = QtCore.QCoreApplication.translate
        picturesWidget.setWindowTitle(_translate("picturesWidget", "Load pictures"))
        self.groupBox.setTitle(_translate("picturesWidget", "Load pictures"))
        self.label.setText(_translate("picturesWidget", "Pictures abs. link"))
        self.picturesLink_lineEdit.setPlaceholderText(_translate("picturesWidget", "input an absolute link to pictures dir"))
        self.picturesSelect_toolButton.setText(_translate("picturesWidget", "..."))
        self.oneChPic_radioButton.setText(_translate("picturesWidget", "one ch picture"))
        self.PicturesLink_pushButton.setText(_translate("picturesWidget", "Load"))
        self.threeChPic_radioButton.setText(_translate("picturesWidget", "three ch picture"))
        self.label_5.setText(_translate("picturesWidget", "Picture type:"))
        self.groupBox_3.setTitle(_translate("picturesWidget", "Settings"))
        self.label_2.setText(_translate("picturesWidget", "Interval, ms"))
        self.label_3.setText(_translate("picturesWidget", "Exposure, ms"))
        self.label_4.setText(_translate("picturesWidget", "Trigger, ms"))
        self.groupBox_2.setTitle(_translate("picturesWidget", "Loaded"))
        self.label_9.setText(_translate("picturesWidget", "ended at"))
        self.label_8.setText(_translate("picturesWidget", "Loading started at"))
        self.label_7.setText(_translate("picturesWidget", "Current directiry"))
        self.fileStartTime_label.setText(_translate("picturesWidget", "00:00:00"))
        self.label_6.setText(_translate("picturesWidget", "Pictures"))
        self.fileEndTime_label.setText(_translate("picturesWidget", "00:00:00"))
        self.fileName_label.setText(_translate("picturesWidget", "name"))
