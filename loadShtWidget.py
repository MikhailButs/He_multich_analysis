from PyQt5 import QtWidgets, QtCore
import os
import numpy as np
import gc
import time
from loadShtUiDesign import Ui_shtWidget
from dataCore import dataCore
import app2rip.ripper as rp


class loadShtWidget(QtWidgets.QWidget, Ui_shtWidget):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=dataCore()):
        super().__init__(parent=parent)
        self.setupUi(self)

        # WIDGETS
        self.data = data
        self.statusbar = QtWidgets.QStatusBar()
        self.verticalLayout.addWidget(self.statusbar)
        self.statusbar.show()

        # CONNECTIONS
        self.shtLink_lineEdit.textChanged.connect(self.load_sht)
        self.shtSelect_toolButton.clicked.connect(self.load_sht_via_btn)
        self.shtLink_pushButton.clicked.connect(self.get_sht_data)

        gc.collect()

    def load_sht(self):
        try:
            self.data.sht_file = os.path.normpath(self.shtLink_lineEdit.text())
            if not os.path.exists(self.data.sht_file):
                raise ValueError
            elif os.path.splitext(self.data.sht_file)[-1] not in ('.sht', '.SHT'):
                raise ValueError
            self.data.sht_file = os.path.normpath(self.shtLink_lineEdit.text())
            self.data.sht_dir, sht_tail = os.path.split(self.data.sht_file)
            # TODO try except
            self.data.sht_num = int(sht_tail[3:-4])
            self.statusbar.showMessage(f'Got {self.data.sht_num} shot', 3000)
        except ValueError:
            self.statusbar.showMessage('Invalid link .sht', 3000)

    def load_sht_via_btn(self):
        data_dir = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл измерения",
                                                         ".",
                                                         "Файл выстрела (*.sht *.SHT)")[0]
        self.shtLink_lineEdit.setText(data_dir)

    def get_sht_data(self):
        if self.data.got_sht_file != self.data.sht_file and self.data.sht_file != '':
            try:
                self.statusbar.showMessage('analysing...', 3000)
                self.setDisabled(True)
                self.fileStartTime_label.setText(time.ctime(time.time()))
                self.fileEndTime_label.setText('')
                self.fileName_label.setText(self.data.sht_file)
                self.sht_tableWidget.clear()
                headers = ['Name', 'Comment', 'Time', '#CH', 'Rate']
                self.sht_tableWidget.setColumnCount(len(headers))
                # self.sht_tableWidget.setRowCount(len(self.data.images_list))
                self.sht_tableWidget.setHorizontalHeaderLabels(headers)
                self.repaint()

                self.data.sht_data = {}
                temp_sht_data = rp.extract(self.data.sht_file, self.statusbar)[0]
                for num in temp_sht_data.keys():
                    x_data, y_data = rp.x_y(temp_sht_data[num])
                    sht_time = temp_sht_data[num]['time']
                    time2set = f'{sht_time["monthDay"]}.{sht_time["month"]}.{sht_time["year"]} {sht_time["hour"]}:{sht_time["minute"]}:{sht_time["second"]}.{sht_time["mSecond"]}'
                    rate = round(len(temp_sht_data[num]['data']) / (temp_sht_data[num]['tMax'] - temp_sht_data[num]['tMin']) / 1000)  # kHz
                    comment = temp_sht_data[num]['comm']
                    ch = temp_sht_data[num]['#ch']
                    temp_dict = {'x': np.array(x_data)*1e3, 'y': np.array(y_data), 'time': time2set, 'ratekhz': rate, 'comm': comment, '#ch': ch}
                    self.data.sht_data[temp_sht_data[num]['name']] = temp_dict

                self.sht_tableWidget.setRowCount(len(self.data.sht_data))
                for num, key in enumerate(self.data.sht_data.keys()):
                    item = self.data.sht_data[key]
                    self.sht_tableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(key))  # name
                    self.sht_tableWidget.setItem(num, 1, QtWidgets.QTableWidgetItem(item['comm']))
                    self.sht_tableWidget.setItem(num, 2, QtWidgets.QTableWidgetItem(item['time']))
                    self.sht_tableWidget.setItem(num, 3, QtWidgets.QTableWidgetItem(str(item['#ch'])))
                    self.sht_tableWidget.setItem(num, 4, QtWidgets.QTableWidgetItem(f'{item["ratekhz"]} kHz'))
                self.sht_tableWidget.resizeColumnsToContents()

                self.data.got_sht_file = self.data.sht_file
                self.fileEndTime_label.setText(time.ctime(time.time()))
                self.refresh_signal.emit()  # need to remake
                self.statusbar.showMessage('Done!', 3000)
                self.setDisabled(False)

            except ValueError:
                self.statusbar.showMessage('Can\'t extract data from .sht', 3000)


