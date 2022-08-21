# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUiDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.settings_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_groupBox.setGeometry(QtCore.QRect(11, 11, 238, 606))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_groupBox.sizePolicy().hasHeightForWidth())
        self.settings_groupBox.setSizePolicy(sizePolicy)
        self.settings_groupBox.setObjectName("settings_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settings_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plot_pushButton = QtWidgets.QPushButton(self.settings_groupBox)
        self.plot_pushButton.setObjectName("plot_pushButton")
        self.verticalLayout_2.addWidget(self.plot_pushButton)
        self.data_groupBox = QtWidgets.QGroupBox(self.settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_groupBox.sizePolicy().hasHeightForWidth())
        self.data_groupBox.setSizePolicy(sizePolicy)
        self.data_groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.data_groupBox.setObjectName("data_groupBox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.data_groupBox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.data_groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.data_groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.He_checkBox = QtWidgets.QCheckBox(self.data_groupBox)
        self.He_checkBox.setObjectName("He_checkBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.He_checkBox)
        self.He_norm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.data_groupBox)
        self.He_norm_doubleSpinBox.setDecimals(5)
        self.He_norm_doubleSpinBox.setMinimum(1e-05)
        self.He_norm_doubleSpinBox.setSingleStep(0.01)
        self.He_norm_doubleSpinBox.setProperty("value", 1.0)
        self.He_norm_doubleSpinBox.setObjectName("He_norm_doubleSpinBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.He_norm_doubleSpinBox)
        self.NII_checkBox = QtWidgets.QCheckBox(self.data_groupBox)
        self.NII_checkBox.setObjectName("NII_checkBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.NII_checkBox)
        self.NII_norm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.data_groupBox)
        self.NII_norm_doubleSpinBox.setDecimals(5)
        self.NII_norm_doubleSpinBox.setMinimum(1e-05)
        self.NII_norm_doubleSpinBox.setSingleStep(0.01)
        self.NII_norm_doubleSpinBox.setProperty("value", 1.0)
        self.NII_norm_doubleSpinBox.setObjectName("NII_norm_doubleSpinBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.NII_norm_doubleSpinBox)
        self.Dalpha_checkBox = QtWidgets.QCheckBox(self.data_groupBox)
        self.Dalpha_checkBox.setObjectName("Dalpha_checkBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Dalpha_checkBox)
        self.Dalpha_norm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.data_groupBox)
        self.Dalpha_norm_doubleSpinBox.setDecimals(5)
        self.Dalpha_norm_doubleSpinBox.setMinimum(1e-05)
        self.Dalpha_norm_doubleSpinBox.setSingleStep(0.01)
        self.Dalpha_norm_doubleSpinBox.setProperty("value", 1.0)
        self.Dalpha_norm_doubleSpinBox.setObjectName("Dalpha_norm_doubleSpinBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Dalpha_norm_doubleSpinBox)
        self.int3_checkBox = QtWidgets.QCheckBox(self.data_groupBox)
        self.int3_checkBox.setObjectName("int3_checkBox")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.int3_checkBox)
        self.int3_norm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.data_groupBox)
        self.int3_norm_doubleSpinBox.setDecimals(5)
        self.int3_norm_doubleSpinBox.setMinimum(1e-05)
        self.int3_norm_doubleSpinBox.setSingleStep(0.01)
        self.int3_norm_doubleSpinBox.setProperty("value", 1.0)
        self.int3_norm_doubleSpinBox.setObjectName("int3_norm_doubleSpinBox")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.int3_norm_doubleSpinBox)
        self.int2_checkBox = QtWidgets.QCheckBox(self.data_groupBox)
        self.int2_checkBox.setObjectName("int2_checkBox")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.int2_checkBox)
        self.int2_norm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.data_groupBox)
        self.int2_norm_doubleSpinBox.setDecimals(5)
        self.int2_norm_doubleSpinBox.setMinimum(1e-05)
        self.int2_norm_doubleSpinBox.setSingleStep(0.01)
        self.int2_norm_doubleSpinBox.setProperty("value", 1.0)
        self.int2_norm_doubleSpinBox.setObjectName("int2_norm_doubleSpinBox")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.int2_norm_doubleSpinBox)
        self.int1_norm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.data_groupBox)
        self.int1_norm_doubleSpinBox.setDecimals(5)
        self.int1_norm_doubleSpinBox.setMinimum(1e-05)
        self.int1_norm_doubleSpinBox.setSingleStep(0.01)
        self.int1_norm_doubleSpinBox.setProperty("value", 1.0)
        self.int1_norm_doubleSpinBox.setObjectName("int1_norm_doubleSpinBox")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.int1_norm_doubleSpinBox)
        self.int1_checkBox = QtWidgets.QCheckBox(self.data_groupBox)
        self.int1_checkBox.setObjectName("int1_checkBox")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.int1_checkBox)
        self.verticalLayout_2.addWidget(self.data_groupBox)
        self.polychromator_groupBox = QtWidgets.QGroupBox(self.settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polychromator_groupBox.sizePolicy().hasHeightForWidth())
        self.polychromator_groupBox.setSizePolicy(sizePolicy)
        self.polychromator_groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.polychromator_groupBox.setObjectName("polychromator_groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.polychromator_groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.polychromator_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_3 = QtWidgets.QLabel(self.polychromator_groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.polychromator_groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.trigger_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.polychromator_groupBox)
        self.trigger_doubleSpinBox.setDecimals(5)
        self.trigger_doubleSpinBox.setMinimum(-99.99)
        self.trigger_doubleSpinBox.setObjectName("trigger_doubleSpinBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.trigger_doubleSpinBox)
        self.Xtype_comboBox = QtWidgets.QComboBox(self.polychromator_groupBox)
        self.Xtype_comboBox.setObjectName("Xtype_comboBox")
        self.Xtype_comboBox.addItem("")
        self.Xtype_comboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Xtype_comboBox)
        self.interval_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.polychromator_groupBox)
        self.interval_doubleSpinBox.setDecimals(5)
        self.interval_doubleSpinBox.setObjectName("interval_doubleSpinBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interval_doubleSpinBox)
        self.label_4 = QtWidgets.QLabel(self.polychromator_groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.exposure_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.polychromator_groupBox)
        self.exposure_doubleSpinBox.setDecimals(5)
        self.exposure_doubleSpinBox.setObjectName("exposure_doubleSpinBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.exposure_doubleSpinBox)
        self.verticalLayout_2.addWidget(self.polychromator_groupBox)
        self.link_groupBox = QtWidgets.QGroupBox(self.settings_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_groupBox.sizePolicy().hasHeightForWidth())
        self.link_groupBox.setSizePolicy(sizePolicy)
        self.link_groupBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.link_groupBox.setObjectName("link_groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.link_groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.link_groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.images_lineEdit = QtWidgets.QLineEdit(self.link_groupBox)
        self.images_lineEdit.setObjectName("images_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.images_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.link_groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.sht_lineEdit = QtWidgets.QLineEdit(self.link_groupBox)
        self.sht_lineEdit.setObjectName("sht_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sht_lineEdit)
        self.verticalLayout_2.addWidget(self.link_groupBox)
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
        self.data_groupBox.setTitle(_translate("MainWindow", "data"))
        self.label_7.setText(_translate("MainWindow", "graph"))
        self.label_8.setText(_translate("MainWindow", "norm"))
        self.He_checkBox.setText(_translate("MainWindow", "He"))
        self.NII_checkBox.setText(_translate("MainWindow", "N II"))
        self.Dalpha_checkBox.setText(_translate("MainWindow", "D alpha"))
        self.int3_checkBox.setText(_translate("MainWindow", "intensity 3"))
        self.int2_checkBox.setText(_translate("MainWindow", "intensity 2"))
        self.int1_checkBox.setText(_translate("MainWindow", "intensity 1"))
        self.polychromator_groupBox.setTitle(_translate("MainWindow", "polychromator"))
        self.label_6.setText(_translate("MainWindow", "X-type"))
        self.label_3.setText(_translate("MainWindow", "interval, ms"))
        self.label_5.setText(_translate("MainWindow", "trigger, ms"))
        self.Xtype_comboBox.setItemText(0, _translate("MainWindow", "frames"))
        self.Xtype_comboBox.setItemText(1, _translate("MainWindow", "time"))
        self.label_4.setText(_translate("MainWindow", "exposure, ms"))
        self.link_groupBox.setTitle(_translate("MainWindow", "links"))
        self.label.setText(_translate("MainWindow", "images:"))
        self.images_lineEdit.setPlaceholderText(_translate("MainWindow", "directory with images"))
        self.label_2.setText(_translate("MainWindow", ".sht:"))
        self.sht_lineEdit.setPlaceholderText(_translate("MainWindow", ".sht file"))
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
