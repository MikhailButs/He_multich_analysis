from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import os
import numpy as np
import gc
import time
from threading import Thread
from numba import njit
from PIL import Image, ImageFilter
from loadPicturesUiDesign import Ui_picturesWidget
from dataCore import dataCore
from get_data import get_data
from loadingWidget import loadingWidget

# TODO add .cine reading to loadPicturesWidget & delete loadCineWidget


class loadPicturesWidget(QtWidgets.QWidget, Ui_picturesWidget):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=dataCore()):
        super().__init__(parent=parent)
        self.setupUi(self)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        # WIDGETS
        self.data = data
        self.statusbar = QtWidgets.QStatusBar()
        self.verticalLayout_2.addWidget(self.statusbar)
        self.statusbar.show()

        # CONNECTIONS
        self.picturesLink_lineEdit.textChanged.connect(self.load_images)
        self.picturesSelect_toolButton.clicked.connect(self.load_images_via_btn)
        self.PicturesLink_pushButton.clicked.connect(self.get_images_data)
        self.interval_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.exposure_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.trigger_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.oneChPic_radioButton.clicked.connect(self.ch_type)
        self.threeChPic_radioButton.clicked.connect(self.ch_type)

        gc.collect()

    def load_images(self, im_dir=None):
        try:
            if im_dir is None:
                self.data.images_dir = os.path.normpath(self.picturesLink_lineEdit.text())
            else:
                self.data.images_dir = im_dir

            if not os.path.isdir(self.data.images_dir):
                raise NameError
            self.data.images_list = os.listdir(self.data.images_dir)  # ['name1.jpg', 'name2.jpg', ...]
            for im in self.data.images_list:
                if os.path.splitext(im)[-1] != '.jpg':
                    raise TypeError
            self.statusbar.showMessage(f'Got {len(self.data.images_list)} images', 3000)
        except FileNotFoundError:
            self.statusbar.showMessage('Invalid link to images', 3000)
        except TypeError:
            self.statusbar.showMessage('Not only .jpg in dir', 3000)
        except NameError:
            self.statusbar.showMessage('Not a dir', 3000)

    def load_images_via_btn(self):
        data_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать папку измерения", ".")
        self.picturesLink_lineEdit.setText(data_dir)

    def show_loading_widget(self, min_val, max_val, file):
        loading_win = loadingWidget(min_val=min_val, max_val=max_val, file=file)
        win = QtWidgets.QDialog(self)
        win.setModal(True)
        win.setWindowTitle('Loading images')
        win.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        win.verticalLayout = QtWidgets.QVBoxLayout(win)
        win.verticalLayout.addWidget(loading_win)
        win.show()

    def get_images_data(self):
        sht_thread = Thread(target=self.get_images_data_subfunc)
        sht_thread.start()

    def get_images_data_subfunc(self):
        if self.data.got_images_dir != self.data.images_dir and self.data.images_dir != '':
            try:
                # self.show_loading_widget(min_val=0, max_val=len(self.data.images_list), file=self.data.images_dir)

                self.setDisabled(True)
                self.fileStartTime_label.setText(time.ctime(time.time()))
                self.fileEndTime_label.setText('')
                self.pictures_tableWidget.clear()
                headers = ['Name', 'Int1', 'Int3', 'Int3', 'Size']
                self.pictures_tableWidget.setColumnCount(len(headers))
                self.pictures_tableWidget.setRowCount(len(self.data.images_list))
                self.pictures_tableWidget.setHorizontalHeaderLabels(headers)

                # TODO add more np.arrays
                self.data.intensity_list = [[] for i in range(len(self.data.images_list))]
                self.data.init_pic_list = [[] for i in range(len(self.data.images_list))]
                self.data.time_list = [step * self.data.interval + self.data.trigger + self.data.exposure / 2
                                       for step in range(len(self.data.images_list))]

                for img in self.data.images_list:
                    ch1_data, ch2_data, ch3_data = get_data(os.path.join(self.data.images_dir, img))
                    temp_intensity = [ch1_data[1], ch2_data[1], ch3_data[1]]
                    temp_pictures = [ch1_data[0], ch2_data[0], ch3_data[0]]
                    num = self.data.images_list.index(img)
                    self.data.intensity_list[num] = temp_intensity
                    self.data.init_pic_list[num] = np.array(temp_pictures)
                    self.statusbar.showMessage(f'Image {num + 1} from {len(self.data.images_list)} made', 1000)
                    self.statusbar.repaint()

                self.statusbar.showMessage(f'Making the table', 1000)
                for num in range(len(self.data.images_list)):
                    self.pictures_tableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(self.data.images_list[num]))
                    self.pictures_tableWidget.setItem(num, 1, QtWidgets.QTableWidgetItem(str(self.data.intensity_list[num][0])))
                    self.pictures_tableWidget.setItem(num, 2, QtWidgets.QTableWidgetItem(str(self.data.intensity_list[num][1])))
                    self.pictures_tableWidget.setItem(num, 3, QtWidgets.QTableWidgetItem(str(self.data.intensity_list[num][2])))
                    self.pictures_tableWidget.setItem(num, 4, QtWidgets.QTableWidgetItem(str(self.data.init_pic_list[num][0].shape)))

                int1 = []  # np.append(array, item)
                int2 = []
                int3 = []
                for i in range(len(self.data.intensity_list)):
                    int1.append(self.data.intensity_list[i][0])
                    int2.append(self.data.intensity_list[i][1])
                    int3.append(self.data.intensity_list[i][2])
                # for i in range(1, 4):
                #     eval(f'self.int{i} = np.array(self.int{i})')
                #     eval(f'self.int{i} = self.int{i} / np.sum(self.int{i}) * len(self.int{i})')
                self.data.int1 = np.array(int1)
                self.data.int1 = self.data.int1 / np.sum(self.data.int1) * len(self.data.int1)
                self.data.int2 = np.array(int2)
                self.data.int2 = self.data.int2 / np.sum(self.data.int2) * len(self.data.int2)
                self.data.int3 = np.array(int3)
                self.data.int3 = self.data.int3 / np.sum(self.data.int3) * len(self.data.int3)
                # print(self.int1)
                # print(self.int2)
                # print(self.int3)

                # filtered pic
                self.statusbar.showMessage('Filtering pictures', 1000)
                self.make_filtered_pic()

                # diff pic
                self.statusbar.showMessage('Making differential pictures', 1000)
                self.make_diff_pic()

                self.pictures_tableWidget.resizeColumnsToContents()
                self.data.got_images_dir = self.data.images_dir
                self.fileName_label.setText(self.data.got_images_dir)
                self.fileEndTime_label.setText(time.ctime(time.time()))
                self.refresh_signal.emit()
                self.statusbar.showMessage('Done', 1000)
                self.setDisabled(False)
            except ValueError:
                self.statusbar.showMessage('Can\'t extract data from images dir', 3000)

    def make_diff_pic(self):
        @njit
        def check_limits(matrix):
            for i in matrix:
                for j in i:
                    if j < 0.:
                        j = 0.
                    if j > 255.:
                        j = 255.
            return matrix

        self.data.diff_pic_list.append(np.array([np.zeros_like(self.data.init_pic_list[0][0]), np.zeros_like(self.data.init_pic_list[0][1]), np.zeros_like(self.data.init_pic_list[0][2])]))
        for i in range(len(self.data.images_list) - 1):
            # diff_pic3 = self.data.init_pic_list[i+1] - self.data.init_pic_list[i]
            diff_pic3 = self.data.init_flt_pic_list[i + 1] - self.data.init_flt_pic_list[i]  # FILTERING IS HERE!!!
            diff_pic3[0] = check_limits(diff_pic3[0])
            diff_pic3[1] = check_limits(diff_pic3[1])
            diff_pic3[2] = check_limits(diff_pic3[2])
            self.data.diff_pic_list.append(diff_pic3)
        # self.data.diff_pic_list = np.array(self.data.diff_pic_list)

    def make_filtered_pic(self):
        self.data.init_flt_pic_list = []
        for im3 in self.data.init_pic_list:
            self.data.init_flt_pic_list.append(np.array([np.array(Image.fromarray(im).filter(ImageFilter.MedianFilter(size=3)).convert('L'), dtype=np.float) for im in im3]))
        self.data.init_flt_pic_list = np.array(self.data.init_flt_pic_list)

    def get_settings(self):
        self.data.interval = self.interval_doubleSpinBox.value()
        self.data.exposure = self.exposure_doubleSpinBox.value()
        self.data.trigger = self.trigger_doubleSpinBox.value()
        # self.Xtype = self.Xtype_comboBox.currentText()
        self.data.time_list = [step * self.data.interval + self.data.trigger + self.data.exposure / 2
                               for step in range(len(self.data.images_list))]
        # self.time2frames()

    def ch_type(self):
        if self.oneChPic_radioButton.isChecked() and not self.threeChPic_radioButton.isChecked():
            self.data.ChType = 'one'
        elif self.threeChPic_radioButton.isChecked() and not self.oneChPic_radioButton.isChecked():
            self.data.ChType = 'three'
        else:
            self.statusbar.showMessage('Incorrect channel type')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mv = loadPicturesWidget()
    mv.show()
    sys.exit(app.exec_())
