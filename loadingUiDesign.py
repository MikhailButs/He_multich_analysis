# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadingUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loadingWidget(object):
    def setupUi(self, loadingWidget):
        loadingWidget.setObjectName("loadingWidget")
        loadingWidget.resize(450, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loadingWidget.sizePolicy().hasHeightForWidth())
        loadingWidget.setSizePolicy(sizePolicy)
        loadingWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.gridLayout = QtWidgets.QGridLayout(loadingWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 2)
        self.fileName_label = QtWidgets.QLabel(loadingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileName_label.sizePolicy().hasHeightForWidth())
        self.fileName_label.setSizePolicy(sizePolicy)
        self.fileName_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fileName_label.setObjectName("fileName_label")
        self.gridLayout.addWidget(self.fileName_label, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(loadingWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.ok_pushButton = QtWidgets.QPushButton(loadingWidget)
        self.ok_pushButton.setEnabled(False)
        self.ok_pushButton.setCheckable(False)
        self.ok_pushButton.setChecked(False)
        self.ok_pushButton.setDefault(False)
        self.ok_pushButton.setFlat(False)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.gridLayout.addWidget(self.ok_pushButton, 5, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(loadingWidget)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.progressBar.setProperty("value", 60)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        self.cancel_pushButton = QtWidgets.QPushButton(loadingWidget)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.gridLayout.addWidget(self.cancel_pushButton, 5, 1, 1, 1)

        self.retranslateUi(loadingWidget)
        QtCore.QMetaObject.connectSlotsByName(loadingWidget)

    def retranslateUi(self, loadingWidget):
        _translate = QtCore.QCoreApplication.translate
        loadingWidget.setWindowTitle(_translate("loadingWidget", "Loading"))
        self.fileName_label.setText(_translate("loadingWidget", "Name"))
        self.label.setText(_translate("loadingWidget", "Loading data from"))
        self.ok_pushButton.setText(_translate("loadingWidget", "OK"))
        self.progressBar.setFormat(_translate("loadingWidget", "%p from 0 made"))
        self.cancel_pushButton.setText(_translate("loadingWidget", "Cancel"))
