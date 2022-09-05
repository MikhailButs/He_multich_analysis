from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os
import numpy as np
import gc
import time
from threading import Thread
from multiprocessing import Process
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
        sht_thread = Thread(target=self.get_sht_data_subfunc)
        sht_thread.start()
        # sht_process = Process(target=self.get_sht_data_subfunc)
        # sht_process.start()

    def get_sht_data_subfunc(self):
        if self.data.got_sht_file != self.data.sht_file and self.data.sht_file != '':
            try:
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

                # data, link = rp.extract(self.data.sht_file,
                #                         ['D-alfa верхний купол', 'Газонапуск He капиляр', 'N II'])
                # Dalpha_x, Dalpha_y = rp.x_y(data[link['D-alfa верхний купол'][0]])
                # Dalpha_y = np.array(Dalpha_y)
                # self.data.Dalpha_y = Dalpha_y / np.sum(np.abs(Dalpha_y)) * len(Dalpha_y)
                # self.data.Dalpha_x = np.array(Dalpha_x) * 1000 - 100
                #
                # NII_x, NII_y = rp.x_y(data[link['N II'][0]])
                # NII_y = np.array(NII_y)
                # self.data.NII_y = NII_y / np.sum(np.abs(NII_y)) * len(NII_y)
                # self.data.NII_x = np.array(NII_x) * 1000 - 100
                #
                # He_x, He_y = rp.x_y(data[link['Газонапуск He капиляр'][0]])
                # He_y = np.array(He_y)
                # self.data.He_y = He_y / np.sum(np.abs(He_y)) * len(He_y)
                # self.data.He_x = np.array(He_x)
                #
                # # self.change_norm()

                # self.data.plots.pop()

                self.data.sht_data = rp.extract(self.data.sht_file, self.statusbar)[0]

                keys = list(self.data.sht_data.keys())
                self.sht_tableWidget.setRowCount(len(keys))
                for num in range(len(keys)):
                    item = self.data.sht_data[keys[num]]
                    self.sht_tableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(item['name']))
                    self.sht_tableWidget.setItem(num, 1, QtWidgets.QTableWidgetItem(item['comm']))
                    sht_time = item['time']
                    time2set = f'{sht_time["monthDay"]}.{sht_time["month"]}.{sht_time["year"]} {sht_time["hour"]}:{sht_time["minute"]}:{sht_time["second"]}.{sht_time["mSecond"]}'
                    self.sht_tableWidget.setItem(num, 2, QtWidgets.QTableWidgetItem(time2set))
                    self.sht_tableWidget.setItem(num, 3, QtWidgets.QTableWidgetItem(str(item['#ch'])))
                    rate = round(len(item['data']) / (item['tMax'] - item['tMin']) / 1000)  # kHz
                    self.sht_tableWidget.setItem(num, 4, QtWidgets.QTableWidgetItem(f'{rate} kHz'))
                self.sht_tableWidget.resizeColumnsToContents()

                self.data.got_sht_file = self.data.sht_file
                self.fileEndTime_label.setText(time.ctime(time.time()))
                self.refresh_signal.emit()
                self.setDisabled(False)

            except ValueError:
                self.statusbar.showMessage('Can\'t extract data from .sht', 3000)


