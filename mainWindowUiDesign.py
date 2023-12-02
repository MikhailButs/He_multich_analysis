# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 793)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.settings_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_groupBox.setGeometry(QtCore.QRect(10, 10, 400, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_groupBox.sizePolicy().hasHeightForWidth())
        self.settings_groupBox.setSizePolicy(sizePolicy)
        self.settings_groupBox.setMinimumSize(QtCore.QSize(400, 0))
        self.settings_groupBox.setAutoFillBackground(False)
        self.settings_groupBox.setFlat(False)
        self.settings_groupBox.setObjectName("settings_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settings_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plot_pushButton = QtWidgets.QPushButton(self.settings_groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plot_pushButton.setFont(font)
        self.plot_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plot_pushButton.setAutoExclusive(False)
        self.plot_pushButton.setAutoDefault(True)
        self.plot_pushButton.setObjectName("plot_pushButton")
        self.verticalLayout_2.addWidget(self.plot_pushButton)
        self.pictures_data_groupBox = QtWidgets.QGroupBox(self.settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictures_data_groupBox.sizePolicy().hasHeightForWidth())
        self.pictures_data_groupBox.setSizePolicy(sizePolicy)
        self.pictures_data_groupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.pictures_data_groupBox.setObjectName("pictures_data_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pictures_data_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pictures_scrollArea = QtWidgets.QScrollArea(self.pictures_data_groupBox)
        self.pictures_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pictures_scrollArea.setWidgetResizable(True)
        self.pictures_scrollArea.setObjectName("pictures_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 352, 160))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.pictures_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.pictures_scrollArea, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.pictures_data_groupBox)
        self.sht_data_groupBox = QtWidgets.QGroupBox(self.settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sht_data_groupBox.sizePolicy().hasHeightForWidth())
        self.sht_data_groupBox.setSizePolicy(sizePolicy)
        self.sht_data_groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sht_data_groupBox.setFlat(False)
        self.sht_data_groupBox.setObjectName("sht_data_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sht_data_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sht_scrollArea = QtWidgets.QScrollArea(self.sht_data_groupBox)
        self.sht_scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sht_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.sht_scrollArea.setWidgetResizable(True)
        self.sht_scrollArea.setObjectName("sht_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 352, 199))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sht_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.sht_scrollArea)
        self.verticalLayout_2.addWidget(self.sht_data_groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 26))
        self.menubar.setObjectName("menubar")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        self.menusave = QtWidgets.QMenu(self.menubar)
        self.menusave.setObjectName("menusave")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInput_data = QtWidgets.QAction(MainWindow)
        self.actionInput_data.setObjectName("actionInput_data")
        self.actionPolychromator = QtWidgets.QAction(MainWindow)
        self.actionPolychromator.setObjectName("actionPolychromator")
        self.actionSelect_area = QtWidgets.QAction(MainWindow)
        self.actionSelect_area.setObjectName("actionSelect_area")
        self.action_SHT_settings = QtWidgets.QAction(MainWindow)
        self.action_SHT_settings.setObjectName("action_SHT_settings")
        self.action_CINE_settings = QtWidgets.QAction(MainWindow)
        self.action_CINE_settings.setObjectName("action_CINE_settings")
        self.actionPictures_settings = QtWidgets.QAction(MainWindow)
        self.actionPictures_settings.setObjectName("actionPictures_settings")
        self.actionall_as_txt = QtWidgets.QAction(MainWindow)
        self.actionall_as_txt.setObjectName("actionall_as_txt")
        self.actionpictures = QtWidgets.QAction(MainWindow)
        self.actionpictures.setObjectName("actionpictures")
        self.menusettings.addAction(self.action_SHT_settings)
        self.menusettings.addAction(self.action_CINE_settings)
        self.menusettings.addAction(self.actionPictures_settings)
        self.menusave.addAction(self.actionall_as_txt)
        self.menuView.addAction(self.actionpictures)
        self.menubar.addAction(self.menusettings.menuAction())
        self.menubar.addAction(self.menusave.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ELM"))
        self.settings_groupBox.setTitle(_translate("MainWindow", "Settings"))
        self.plot_pushButton.setText(_translate("MainWindow", "PLOT"))
        self.pictures_data_groupBox.setTitle(_translate("MainWindow", "Pictures data (no data)"))
        self.sht_data_groupBox.setTitle(_translate("MainWindow", ".SHT data (no data)"))
        self.menusettings.setTitle(_translate("MainWindow", "Load"))
        self.menusave.setTitle(_translate("MainWindow", "Save"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionInput_data.setText(_translate("MainWindow", "Input data"))
        self.actionPolychromator.setText(_translate("MainWindow", "Polychromator"))
        self.actionSelect_area.setText(_translate("MainWindow", "Area selection"))
        self.action_SHT_settings.setText(_translate("MainWindow", ".SHT"))
        self.action_CINE_settings.setText(_translate("MainWindow", ".CINE"))
        self.actionPictures_settings.setText(_translate("MainWindow", "pictures"))
        self.actionall_as_txt.setText(_translate("MainWindow", "all as .CSV"))
        self.actionpictures.setText(_translate("MainWindow", "pictures"))
