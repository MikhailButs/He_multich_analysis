import sys
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np
from mainWindowUiDesign import Ui_MainWindow
import os
import gc
from loadPicturesWidget import loadPicturesWidget
from loadShtWidget import loadShtWidget
from viewPicturesWidget import viewPicturesWidget
from dataCore import dataCore
from signalWindowUi import signalWindowWidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

        self.refresh_signal.connect(self.refresh_slot)

        self.statusbar = self.statusBar()
        self.statusbar.show()

        self.signals_dict = {}
        self.intensity_dict = {}

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        Hlayout = QtWidgets.QHBoxLayout(self._main)

        self.static_canvas = FigureCanvasQTAgg(Figure(tight_layout=True))
        self.static_canvas.figure.dpi = 80.0
        self.addToolBar(NavigationToolbar2QT(self.static_canvas, self))

        Hlayout.addWidget(self.static_canvas)
        Hlayout.addWidget(self.settings_groupBox)

        self.sig_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.intensity_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)

        self.data = dataCore()

        self.loadPicturesWidget = loadPicturesWidget(data=self.data)
        self.actionPictures_settings.triggered.connect(self.show_loadPicturesWidget)
        self.loadPicturesWidget.refresh_signal.connect(self.refresh_signal)

        self.loadShtWidget = loadShtWidget(data=self.data)
        self.action_SHT_settings.triggered.connect(self.show_loadShtWidget)
        self.loadShtWidget.refresh_signal.connect(self.refresh_signal)

        self.viewPicturesWidget = viewPicturesWidget(data=self.data)
        self.actionpictures.triggered.connect(self.show_viewPicturesWidget)
        self.refresh_signal.connect(self.viewPicturesWidget.refresh_slot)

        self.plot_pushButton.clicked.connect(self.make_plot)
        self.plot_pushButton.click()

    def show_loadPicturesWidget(self):
        self.loadPicturesWidget.show()

    def show_loadShtWidget(self):
        self.loadShtWidget.show()

    def show_viewPicturesWidget(self):
        self.viewPicturesWidget.show()

    def make_plot(self):
        self.static_canvas.figure.clear('all')
        ax1 = self.static_canvas.figure.add_subplot(1, 1, 1)
        ax1.set_title("Data from diagnostics on Globus-M2 tokamak")

        if self.data.sht_data is not None and len(self.data.sht_data.keys()) != 0:
            for key in self.data.sht_data.keys():
                if self.signals_dict[key].is_checked():
                    k = self.signals_dict[key].mult_coef()
                    signal_shift = self.signals_dict[key].zero_signal()
                    time_shift = self.signals_dict[key].zero_time()
                    ax1.plot(self.data.sht_data[key]['x'] + time_shift, self.data.sht_data[key]['y'] * k + signal_shift, label=key)
        if self.data.intensity_data is not None and len(self.data.intensity_data.keys()) != 0:
            for key in self.data.intensity_data.keys():
                if self.intensity_dict[key].is_checked():
                    k = self.intensity_dict[key].mult_coef()
                    signal_shift = self.intensity_dict[key].zero_signal()
                    time_shift = self.intensity_dict[key].zero_time()
                    ax1.plot(self.data.intensity_data[key]['x'] + time_shift, self.data.intensity_data[key]['y'] * k + signal_shift,
                             label=key)
        ax1.legend()
        ax1.grid()
        ax1.set_xlabel('Time, ms')
        ax1.set_ylabel('Arbitrary units')
        self.static_canvas.draw()
        self.statusbar.showMessage('Plotted', 3000)
        gc.collect(generation=2)

    def refresh_slot(self):
        self.static_canvas.figure.clear('all')
        gc.collect(generation=2)

        self.clear_sht_box()
        self.fill_sht_box()
        self.clear_pictures_box()
        self.fill_pictures_box()

    def clear_sht_box(self):
        children = self.scrollAreaWidgetContents.children()
        for i in children:
            if isinstance(i, signalWindowWidget):
                self.scrollAreaWidgetContents.layout().removeWidget(i)
                i.deleteLater()
                i = None
        self.signals_dict = {}
        gc.collect()

    def clear_pictures_box(self):
        children = self.scrollAreaWidgetContents_2.children()
        for i in children:
            if isinstance(i, signalWindowWidget):
                self.scrollAreaWidgetContents_2.layout().removeWidget(i)
                i.deleteLater()
                i = None
        self.intensity_dict_dict = {}
        gc.collect()

    def fill_sht_box(self):
        if self.data.sht_data is not None and len(self.data.sht_data.keys()) > 0:
            for num, key in enumerate(self.data.sht_data.keys()):
                exec(f'win{num} = signalWindowWidget()')
                exec(f'self.signals_dict[key] = win{num}')
                exec(f'win{num}.set_name(key)')
                zero_signal = np.mean(self.data.sht_data[key]['y'][0:100])
                exec(f'win{num}.set_zero_signal(-zero_signal)')
                exec(f'self.sig_layout.addWidget(win{num})')
            self.sht_data_groupBox.setTitle(f'.SHT data from {os.path.split(self.data.got_sht_file)[1]}')

    def fill_pictures_box(self):
        if self.data.intensity_data is not None and len(self.data.intensity_data.keys()) > 0:
            for num, key in enumerate(self.data.intensity_data.keys()):
                exec(f'pic_win{num} = signalWindowWidget()')
                exec(f'self.intensity_dict[key] = pic_win{num}')
                exec(f'pic_win{num}.set_name(key)')
                zero_signal = np.mean(self.data.intensity_data[key]['y'][0:10])
                exec(f'pic_win{num}.set_zero_signal(-zero_signal)')
                exec(f'pic_win{num}.set_zero_time(100.0)')
                exec(f'self.intensity_layout.addWidget(pic_win{num})')
            self.pictures_data_groupBox.setTitle(f'Pictures data from {os.path.split(self.data.got_images_dir)[1]}')


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mv = MainWindow()
    mv.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
