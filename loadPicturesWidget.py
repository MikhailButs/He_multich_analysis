from PyQt5 import QtWidgets, QtCore
import sys
import os
import numpy as np
import gc
import time
from numba import njit
from math import ceil
from PIL import Image, ImageFilter
from loadPicturesUiDesign import Ui_picturesWidget
from dataCore import dataCore
from get_data import get_data3
from cine_reader import Cine

# TODO add .cine reading to loadPicturesWidget & delete loadCineWidget


class loadPicturesWidget(QtWidgets.QWidget, Ui_picturesWidget):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=dataCore()):
        super().__init__(parent=parent)
        self.setupUi(self)

        # WIDGETS
        self.data = data
        self.statusbar = QtWidgets.QStatusBar()
        self.verticalLayout_2.addWidget(self.statusbar)
        self.statusbar.show()
        self.filter_size = 0

        # CONNECTIONS
        self.picturesLink_lineEdit.textChanged.connect(self.load_images)
        self.picturesSelect_toolButton.clicked.connect(self.load_images_via_btn)
        self.PicturesLink_pushButton.clicked.connect(self.get_images_data)
        self.interval_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.exposure_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.trigger_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.oneChPic_radioButton.toggled.connect(self.ch_type)
        self.threeChPic_radioButton.toggled.connect(self.ch_type)
        self.filter_spinBox.valueChanged.connect(self.get_settings)
        self.refSelect_pushButton.clicked.connect(self.load_ref_via_btn)
        self.refLoad_pushButton.clicked.connect(self.load_ref)
        self.refClear_pushButton.clicked.connect(self.clear_ref)
        self.source_comboBox.currentTextChanged.connect(self.source_type)

        gc.collect(generation=2)

    def load_images(self, im_dir=None):
        if self.source_comboBox.currentText() == 'directory':
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
        else:
            try:
                self.data.images_dir = os.path.normpath(self.picturesLink_lineEdit.text())
                if not os.path.isfile(self.data.images_dir):
                    raise NameError
                cine = Cine(self.data.images_dir)
                self.data.images_list = [str(i) for i in range(cine.image_count)]
                self.trigger_doubleSpinBox.setValue(cine.get_time_to_trigger(0) * 1e3)
                self.interval_doubleSpinBox.setValue((cine.get_time(1) - cine.get_time(0)) * 1e3)
                self.exposure_doubleSpinBox.setValue(cine.all_exposures[0] * 1e3)
                self.depth_spinBox.setValue(ceil(np.log2(cine.bitmapinfo_dict['bi_clr_important'])))
                self.statusbar.showMessage(f'Got CINE file with {cine.image_count} frames', 3000)
                cine.close()
            except FileNotFoundError:
                self.statusbar.showMessage('Invalid link to file', 3000)
            except NameError:
                self.statusbar.showMessage('Not a file', 3000)
            except:
                self.statusbar.showMessage('Unknown error', 3000)

    def load_images_via_btn(self):
        data_dir = ''
        if self.source_comboBox.currentText() == 'directory':
            data_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать папку измерения", ".")
        elif self.source_comboBox.currentText() == 'CINE file':
            data_dir = QtWidgets.QFileDialog.getOpenFileName(self, 'CINE file', ".", "*.cine; *.CINE")[0]
        self.picturesLink_lineEdit.setText(data_dir)

    def get_images_data(self):
        if self.data.images_dir != '':
            if self.data.got_images_dir != self.data.images_dir:
                self.statusbar.showMessage('Loading...', 1000)
                self.statusbar.repaint()
            else:
                self.statusbar.showMessage('Reloading...', 1000)
                self.statusbar.repaint()
            try:
                self.setDisabled(True)
                self.fileStartTime_label.setText(time.ctime(time.time()))
                self.fileEndTime_label.setText('')
                self.pictures_tableWidget.clear()
                if self.data.ChType == 'three':
                    headers = ['Name', 'Size, px', 'Start time', 'End time', 'Int. 1', 'Int. 2', 'Int. 3']
                elif self.data.ChType == 'one':
                    headers = ['Name', 'Size', 'Start time', 'End time', 'Intensity']
                self.pictures_tableWidget.setColumnCount(len(headers))
                self.pictures_tableWidget.setRowCount(len(self.data.images_list))
                self.pictures_tableWidget.setHorizontalHeaderLabels(headers)

                self.data.images_data = {}
                self.data.intensity_data = {}

                n_images = len(self.data.images_list)

                if self.data.ChType == 'three':
                    self.data.intensity_data['Channel1'] = {}
                    self.data.intensity_data['Channel2'] = {}
                    self.data.intensity_data['Channel3'] = {}
                    self.data.intensity_data['Channel1']['y'] = np.array([])
                    self.data.intensity_data['Channel2']['y'] = np.array([])
                    self.data.intensity_data['Channel3']['y'] = np.array([])
                    times = np.array([step * self.data.interval + self.data.trigger + self.data.exposure / 2
                                       for step in range(len(self.data.images_list))])
                    self.data.intensity_data['Channel1']['x'] = times
                    self.data.intensity_data['Channel2']['x'] = times
                    self.data.intensity_data['Channel3']['x'] = times
                    self.data.images_data['Channel1'] = {}
                    self.data.images_data['Channel2'] = {}
                    self.data.images_data['Channel3'] = {}
                    self.data.images_data['Channel1']['images'] = {}
                    self.data.images_data['Channel2']['images'] = {}
                    self.data.images_data['Channel3']['images'] = {}
                    for num, img in enumerate(self.data.images_list):
                        ch1_data, ch2_data, ch3_data = get_data3(os.path.join(self.data.images_dir, img))
                        self.data.intensity_data['Channel1']['y'] = \
                            np.append(self.data.intensity_data['Channel1']['y'], ch1_data[1])
                        self.data.intensity_data['Channel2']['y'] = \
                            np.append(self.data.intensity_data['Channel2']['y'], ch2_data[1])
                        self.data.intensity_data['Channel3']['y'] = \
                            np.append(self.data.intensity_data['Channel3']['y'], ch3_data[1])
                        self.data.images_data['Channel1']['images'][img] = {}
                        self.data.images_data['Channel2']['images'][img] = {}
                        self.data.images_data['Channel3']['images'][img] = {}
                        self.data.images_data['Channel1']['images'][img]['initial'] = ch1_data[0]
                        self.data.images_data['Channel2']['images'][img]['initial'] = ch2_data[0]
                        self.data.images_data['Channel3']['images'][img]['initial'] = ch3_data[0]
                        start_time = num * self.data.interval + self.data.trigger
                        end_time = num * self.data.interval + self.data.trigger + self.data.exposure
                        self.data.images_data['Channel1']['images'][img]['start_time'] = start_time
                        self.data.images_data['Channel2']['images'][img]['start_time'] = start_time
                        self.data.images_data['Channel3']['images'][img]['start_time'] = start_time
                        self.data.images_data['Channel1']['images'][img]['end_time'] = end_time
                        self.data.images_data['Channel2']['images'][img]['end_time'] = end_time
                        self.data.images_data['Channel3']['images'][img]['end_time'] = end_time
                        self.statusbar.showMessage(f'Image {num + 1} from {n_images} made', 1000)
                        self.statusbar.repaint()
                elif self.data.ChType == 'one':
                    self.data.intensity_data['Pictures'] = {}
                    self.data.intensity_data['Pictures']['y'] = np.array([])
                    times = np.array([step * self.data.interval + self.data.trigger + self.data.exposure / 2
                                      for step in range(len(self.data.images_list))])
                    self.data.intensity_data['Pictures']['x'] = times
                    self.data.images_data['Pictures'] = {}
                    self.data.images_data['Pictures']['images'] = {}
                    if self.source_comboBox.currentText() == 'CINE file':
                        cine = Cine(self.data.images_dir)
                    for num, img in enumerate(self.data.images_list):
                        if self.source_comboBox.currentText() == 'CINE file':
                            pix_matrix = np.array(cine.get_frame(int(img)), dtype=np.int16)
                        else:
                            im = Image.open(os.path.join(self.data.images_dir, img)).convert('L')
                            pix_matrix = np.array(im, dtype=np.int16)
                        self.data.images_data['Pictures']['images'][img] = {}
                        self.data.images_data['Pictures']['images'][img]['initial'] = pix_matrix
                        start_time = num * self.data.interval + self.data.trigger
                        end_time = num * self.data.interval + self.data.trigger + self.data.exposure
                        self.data.images_data['Pictures']['images'][img]['start_time'] = start_time
                        self.data.images_data['Pictures']['images'][img]['end_time'] = end_time
                        intensity = np.sum(pix_matrix) / np.size(pix_matrix)
                        self.data.intensity_data['Pictures']['y'] = \
                            np.append(self.data.intensity_data['Pictures']['y'], intensity)
                        self.statusbar.showMessage(f'Image {num + 1} from {n_images} made', 1000)
                        self.statusbar.repaint()

                self.statusbar.showMessage(f'Making the table', 1000)
                for num, img in enumerate(self.data.images_list):
                    self.pictures_tableWidget.setItem(num, 0, QtWidgets.QTableWidgetItem(img))
                    self.pictures_tableWidget.setItem(num, 1, QtWidgets.QTableWidgetItem(
                        str(self.data.images_data[list(self.data.images_data.keys())[0]]['images'][img]['initial'].shape)))
                    self.pictures_tableWidget.setItem(num, 2, QtWidgets.QTableWidgetItem(
                        str(self.data.images_data[list(self.data.images_data.keys())[0]]['images'][img][
                                'start_time'])))
                    self.pictures_tableWidget.setItem(num, 3, QtWidgets.QTableWidgetItem(
                        str(self.data.images_data[list(self.data.images_data.keys())[0]]['images'][img][
                                'end_time'])))
                    for n, key in enumerate(self.data.images_data.keys()):
                        self.pictures_tableWidget.setItem(num, n+4, QtWidgets.QTableWidgetItem(str(self.data.intensity_data[key]['y'][num])))

                # filtered pic
                self.statusbar.showMessage('Filtering pictures', 1000)
                self.statusbar.repaint()
                self.make_filtered_pic()

                # diff pic
                self.statusbar.showMessage('Making differential pictures', 1000)
                self.statusbar.repaint()
                self.make_diff_pic()

                # final pic
                self.statusbar.showMessage('Making final pictures', 1000)
                self.statusbar.repaint()
                self.make_final_pic()

                self.pictures_tableWidget.resizeColumnsToContents()
                self.data.got_images_dir = self.data.images_dir
                self.fileName_label.setText(self.data.got_images_dir)
                self.fileEndTime_label.setText(time.ctime(time.time()))
                self.refresh_signal.emit()
                self.statusbar.showMessage('Done', 1000)
                self.statusbar.repaint()
                self.setDisabled(False)
            except ValueError:
                self.statusbar.showMessage('Can\'t extract data from images dir', 3000)

    def make_diff_pic(self):
        @njit
        def check_limits(matrix: np.array, depth: int):
            newmatrix = np.zeros_like(matrix)
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    pix = matrix[i][j]
                    if pix > 2**depth-1:
                        newmatrix[i][j] = 2**depth-1
                    elif pix < 0:
                        pass
                    else:
                        newmatrix[i][j] = pix
            return newmatrix

        self.data.depth = self.depth_spinBox.value()
        for key in self.data.images_data.keys():
            prev = self.data.images_data[key]['images'][list(self.data.images_data[key]['images'].keys())[0]]['filtered']
            for img in self.data.images_data[key]['images'].keys():
                diff = np.subtract(self.data.images_data[key]['images'][img]['filtered'], prev)
                diff = check_limits(diff, depth=self.data.depth)
                self.data.images_data[key]['images'][img]['differential'] = diff
                prev = self.data.images_data[key]['images'][img]['filtered']

    def make_filtered_pic(self):
        if self.filter_size > 1:
            for key in self.data.images_data.keys():
                for img in self.data.images_data[key]['images'].keys():
                    self.data.images_data[key]['images'][img]['filtered'] = \
                        np.array(Image.fromarray(self.data.images_data[key]['images'][img]['initial']).filter(ImageFilter.MedianFilter(size=self.filter_size)).convert('L'), dtype=np.float)
        else:
            for key in self.data.images_data.keys():
                for img in self.data.images_data[key]['images'].keys():
                    self.data.images_data[key]['images'][img]['filtered'] = \
                        self.data.images_data[key]['images'][img]['initial']

    def make_final_pic(self):
        for key in self.data.images_data.keys():
            if self.data.reference_picture is not None:
                for img in self.data.images_data[key]['images'].keys():
                    final = self.data.images_data[key]['images'][img]['differential'] * self.alpha_spinBox.value() + self.data.reference_picture
                    self.data.images_data[key]['images'][img]['final'] = final
            else:
                # prev = self.data.images_data[key]['images'][list(self.data.images_data[key]['images'].keys())[0]][
                #     'initial']
                for img in self.data.images_data[key]['images'].keys():
                    final = self.data.images_data[key]['images'][img]['differential'] * self.alpha_spinBox.value() + self.data.images_data[key]['images'][img]['initial']
                    self.data.images_data[key]['images'][img]['final'] = final
                    # prev = self.data.images_data[key]['images'][img]['initial']

    def get_settings(self):
        self.data.interval = self.interval_doubleSpinBox.value()
        self.data.exposure = self.exposure_doubleSpinBox.value()
        self.data.trigger = self.trigger_doubleSpinBox.value()
        self.data.time_list = [step * self.data.interval + self.data.trigger + self.data.exposure / 2
                               for step in range(len(self.data.images_list))]
        filter_size = self.filter_spinBox.value()
        if filter_size % 2 == 0:
            filter_size += 1
        self.filter_spinBox.blockSignals(True)
        self.filter_spinBox.setValue(filter_size)
        self.filter_spinBox.blockSignals(False)
        self.filter_size = filter_size

    def load_ref_via_btn(self):
        data_dir = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать файл фона", '.', "*.npy; *.NPY")[0]
        self.refLink_lineEdit.setText(data_dir)

    def load_ref(self):
        if self.refLink_lineEdit.text() != '' and os.path.isfile(self.refLink_lineEdit.text()):
            self.data.reference_picture = np.load(self.refLink_lineEdit.text())
            self.refName_label.setText(self.refLink_lineEdit.text())
            self.refSize_label.setText(str(self.data.reference_picture.shape))
            self.refIntensity_label.setText(str(np.mean(self.data.reference_picture)))
        else:
            self.statusbar.showMessage('Not a file')

    def clear_ref(self):
        self.refLink_lineEdit.setText('')
        self.refName_label.setText('')
        self.refSize_label.setText('-')
        self.refIntensity_label.setText('-')
        self.data.reference_picture = None

    def ch_type(self):
        if self.oneChPic_radioButton.isChecked() and not self.threeChPic_radioButton.isChecked():
            self.data.ChType = 'one'
        elif self.threeChPic_radioButton.isChecked() and not self.oneChPic_radioButton.isChecked():
            self.data.ChType = 'three'
        else:
            self.statusbar.showMessage('Incorrect channel type')

    def source_type(self):
        if self.source_comboBox.currentText() == 'directory':
            self.threeChPic_radioButton.setDisabled(False)
        elif self.source_comboBox.currentText() == 'CINE file':
            self.oneChPic_radioButton.setChecked(True)
            self.threeChPic_radioButton.setDisabled(True)
        self.load_images()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mv = loadPicturesWidget()
    mv.show()
    sys.exit(app.exec_())
