import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from matplotlib import pyplot as plt
import numpy as np
from appUiDesign import Ui_MainWindow
import os
import gc
import app2rip.ripper as rp
from get_data import get_data
import mplcursors
from blittedCursor import BlittedCursor
from numba import njit


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        self.statusbar = self.statusBar()
        self.statusbar.show()

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        Hlayout = QtWidgets.QHBoxLayout(self._main)

        self.static_canvas = FigureCanvasQTAgg(Figure(tight_layout=True))
        self.static_canvas.figure.dpi = 80.0
        self.addToolBar(NavigationToolbar2QT(self.static_canvas, self))

        Hlayout.addWidget(self.static_canvas)
        Hlayout.addWidget(self.settings_groupBox)

        self.images_lineEdit.textChanged.connect(self.load_images)
        self.sht_lineEdit.textChanged.connect(self.load_sht)
        self.interval_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.exposure_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.trigger_doubleSpinBox.valueChanged.connect(self.get_settings)
        self.Xtype_comboBox.currentTextChanged.connect(self.change_type)
        self.plot_pushButton.clicked.connect(self.make_plot)
        self.He_checkBox.clicked.connect(self.check2show)
        self.NII_checkBox.clicked.connect(self.check2show)
        self.Dalpha_checkBox.clicked.connect(self.check2show)
        self.int1_checkBox.clicked.connect(self.check2show)
        self.int2_checkBox.clicked.connect(self.check2show)
        self.int3_checkBox.clicked.connect(self.check2show)
        self.Dalpha_norm_doubleSpinBox.valueChanged.connect(self.check2show)
        self.NII_norm_doubleSpinBox.valueChanged.connect(self.check2show)
        self.He_norm_doubleSpinBox.valueChanged.connect(self.check2show)
        self.int1_norm_doubleSpinBox.valueChanged.connect(self.check2show)
        self.int2_norm_doubleSpinBox.valueChanged.connect(self.check2show)
        self.int3_norm_doubleSpinBox.valueChanged.connect(self.check2show)

        # images
        self.images_dir = ''
        self.got_images_dir = ''
        self.images_list = []
        self.exposure = 0
        self.interval = 0
        self.trigger = 0
        self.Xtype = 'time'
        self.intensity_list = []
        self.time_list = []
        self.frames_list = []
        self.int1 = np.array([])
        self.int1_scaled = np.array([])
        self.int2 = np.array([])
        self.int2_scaled = np.array([])
        self.int3 = np.array([])
        self.int3_scaled = np.array([])

        # sht
        self.sht_dir = ''
        self.sht_num = ''
        self.sht_file = ''
        self.got_sht_file = ''
        self.Dalpha_x = np.array([])
        self.Dalpha_x_frames = []
        self.Dalpha_y = np.array([])
        self.Dalpha_y_scaled = np.array([])
        self.NII_x = np.array([])
        self.NII_x_frames = []
        self.NII_y = np.array([])
        self.NII_y_scaled = np.array([])
        self.He_x = np.array([])
        self.He_x_frames = []
        self.He_y = np.array([])
        self.He_y_scaled = np.array([])

        # common
        self.to_show = {'Dalpha': 0, 'NII': 0, 'He': 0, 'int1': 0, 'int2': 0, 'int3': 0}
        self.norms = {'Dalpha': 1., 'NII': 1., 'He': 1., 'int1': 1., 'int2': 1., 'int3': 1.}

        self.change_type()
        self.check2show()

    def check2show(self):
        for graph in self.to_show:
            self.to_show[graph] = eval(f'self.{graph}_checkBox.checkState()')
        for graph in self.norms:
            self.norms[graph] = eval(f'self.{graph}_norm_doubleSpinBox.value()')
        self.change_norm()

    def load_images(self):
        try:
            self.images_dir = os.path.normpath(self.images_lineEdit.text())
            if not os.path.isdir(self.images_dir):
                raise NameError
            self.images_list = os.listdir(self.images_dir)  # ['name1.jpg', 'name2.jpg', ...]
            for im in self.images_list:
                if os.path.splitext(im)[-1] != '.jpg':
                    raise TypeError
            self.statusbar.showMessage(f'Got {len(self.images_list)} images', 3000)
        except FileNotFoundError:
            self.statusbar.showMessage('Invalid link to images', 3000)
        except TypeError:
            self.statusbar.showMessage('Not only .jpg in dir', 3000)
        except NameError:
            self.statusbar.showMessage('Not a dir', 3000)

    def load_sht(self):
        try:
            self.sht_file = os.path.normpath(self.sht_lineEdit.text())
            if not os.path.exists(self.sht_file):
                raise ValueError
            elif os.path.splitext(self.sht_file)[-1] not in ('.sht', '.SHT'):
                raise ValueError
            self.sht_file = os.path.normpath(self.sht_lineEdit.text())
            self.sht_dir, sht_tail = os.path.split(self.sht_file)
            self.sht_num = int(sht_tail[3:-4])
            self.statusbar.showMessage(f'Got {self.sht_num} shot', 3000)
        except ValueError:
            self.statusbar.showMessage('Invalid link .sht', 3000)

    def time2frames(self):
        if len(self.time_list) > 1 and len(self.images_list) > 1:
            self.frames_list = np.linspace(1, len(self.images_list), len(self.images_list))
            shift = self.frames_list[0] - self.time_list[0]
            extension = (self.frames_list[-1] - self.frames_list[0]) / (self.time_list[-1] - self.time_list[0])
            if len(self.Dalpha_x) > 0:
                # l = self.Dalpha_x[-1] - self.Dalpha_x[0]
                # start = self.Dalpha_x[0] + shift
                # end = start + l * extension
                # self.Dalpha_x_frames = np.linspace(start, end, len(self.Dalpha_x))
                self.Dalpha_x_frames = self.Dalpha_x * extension + shift
                # TODO check frame-scale
            if len(self.NII_x) > 0:
                self.NII_x_frames = self.NII_x * extension + shift
            if len(self.He_x) > 0:
                self.He_x_frames = self.He_x * extension + shift

    def change_norm(self):
        self.Dalpha_y_scaled = self.Dalpha_y * self.norms['Dalpha']
        self.NII_y_scaled = self.NII_y * self.norms['NII']
        self.He_y_scaled = self.He_y * self.norms['He']
        self.int1_scaled = self.int1 * self.norms['int1']
        self.int2_scaled = self.int2 * self.norms['int2']
        self.int3_scaled = self.int3 * self.norms['int3']

    def get_settings(self):
        self.interval = self.interval_doubleSpinBox.value()
        self.exposure = self.exposure_doubleSpinBox.value()
        self.trigger = self.trigger_doubleSpinBox.value()
        # self.Xtype = self.Xtype_comboBox.currentText()
        self.time_list = [step * self.interval + self.trigger + self.exposure / 2
                          for step in range(len(self.images_list))]
        self.time2frames()

    def change_type(self):
        if len(self.images_list) > 0:
            self.Xtype = self.Xtype_comboBox.currentText()
        else:
            self.Xtype = 'time'
            self.statusbar.showMessage('Set images link')
            self.Xtype_comboBox.blockSignals(True)
            self.Xtype_comboBox.setCurrentIndex(1)
            self.Xtype_comboBox.blockSignals(False)

    def get_sht_data(self):
        if self.got_sht_file != self.sht_file and self.sht_file != '':
            try:
                data, link = rp.extract(self.sht_dir, self.sht_num,
                                        ['D-alfa верхний купол', 'Газонапуск He капиляр', 'N II'])
                Dalpha_x, Dalpha_y = rp.x_y(data[link['D-alfa верхний купол'][0]])
                Dalpha_y = np.array(Dalpha_y)
                self.Dalpha_y = Dalpha_y / np.sum(np.abs(Dalpha_y)) * len(Dalpha_y)
                self.Dalpha_x = np.array(Dalpha_x) * 1000 - 100

                NII_x, NII_y = rp.x_y(data[link['N II'][0]])
                NII_y = np.array(NII_y)
                self.NII_y = NII_y / np.sum(np.abs(NII_y)) * len(NII_y)
                self.NII_x = np.array(NII_x) * 1000 - 100

                He_x, He_y = rp.x_y(data[link['Газонапуск He капиляр'][0]])
                He_y = np.array(He_y)
                self.He_y = He_y / np.sum(np.abs(He_y)) * len(He_y)
                self.He_x = np.array(He_x)

                self.change_norm()

                self.got_sht_file = self.sht_file
            except ValueError:
                self.statusbar.showMessage('Can\'t extract data from .sht', 3000)

    def get_images_data(self):
        if self.got_images_dir != self.images_dir and self.images_dir != '':
            try:
                self.intensity_list = [[] for i in range(len(self.images_list))]
                self.time_list = [step * self.interval + self.trigger + self.exposure / 2
                                  for step in range(len(self.images_list))]
                self.time2frames()
                for img in self.images_list:
                    ch1_data, ch2_data, ch3_data = get_data(os.path.join(self.images_dir, img))
                    temp_intensity = [ch1_data[1], ch2_data[1], ch3_data[1]]
                    self.intensity_list[self.images_list.index(img)] = temp_intensity
                    print(f'Image {self.images_list.index(img) + 1} from {len(self.images_list)} made')
                int1 = []
                int2 = []
                int3 = []
                for i in range(len(self.intensity_list)):
                    int1.append(self.intensity_list[i][0])
                    int2.append(self.intensity_list[i][1])
                    int3.append(self.intensity_list[i][2])
                # for i in range(1, 4):
                #     eval(f'self.int{i} = np.array(self.int{i})')
                #     eval(f'self.int{i} = self.int{i} / np.sum(self.int{i}) * len(self.int{i})')
                self.int1 = np.array(int1)
                self.int1 = self.int1 / np.sum(self.int1) * len(self.int1)
                self.int2 = np.array(int2)
                self.int2 = self.int2 / np.sum(self.int2) * len(self.int2)
                self.int3 = np.array(int3)
                self.int3 = self.int3 / np.sum(self.int3) * len(self.int3)
                # print(self.int1)
                # print(self.int2)
                # print(self.int3)

                self.change_norm()

                self.got_images_dir = self.images_dir
            except ValueError:
                self.statusbar.showMessage('Can\'t extract data from images dir', 3000)

    def make_plot(self):
        self.get_sht_data()
        self.get_images_data()

        self.static_canvas.figure.clear('all')
        ax1 = self.static_canvas.figure.add_subplot(1, 1, 1)
        ax1.set_title("Data from diagnostics on Globus-M2 tokamak")
        if self.to_show['Dalpha']:
            ax1.plot(self.Dalpha_x_frames if self.Xtype == 'frames' else self.Dalpha_x, self.Dalpha_y_scaled, label='D_alpha')
        if self.to_show['NII']:
            ax1.plot(self.NII_x_frames if self.Xtype == 'frames' else self.NII_x, self.NII_y_scaled, label='N_II')
        if self.to_show['He']:
            ax1.plot(self.He_x_frames if self.Xtype == 'frames' else self.He_x, self.He_y_scaled, label='He')
        if self.to_show['int1']:
            ax1.plot(self.frames_list if self.Xtype == 'frames' else self.time_list, self.int1_scaled, label='CH1 int 728 nm')
        if self.to_show['int2']:
            ax1.plot(self.frames_list if self.Xtype == 'frames' else self.time_list, self.int2_scaled, label='CH2 int 706 nm')
        if self.to_show['int3']:
            ax1.plot(self.frames_list if self.Xtype == 'frames' else self.time_list, self.int3_scaled, label='CH3 int 667 nm')
        ax1.legend()
        ax1.grid()
        ax1.set_xlabel('Time, ms')
        ax1.set_ylabel('Arbitrary units')
        self.static_canvas.draw()
        self.statusbar.showMessage('Plotted', 3000)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mv = MainWindow()
    mv.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
