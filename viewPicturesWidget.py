import gc
import os
import numpy as np
from PIL import Image
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from viewPicturesUiDesign import Ui_viewWidget
from dataCore import dataCore


class viewPicturesWidget(QtWidgets.QMainWindow, Ui_viewWidget):
    refresh_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=dataCore()):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data = data
        self.statusbar = self.statusBar()
        self.statusbar.show()
        self.add_max_on_diff = 0
        self.add_max_on_init = 0

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        Hlayout = QtWidgets.QHBoxLayout(self._main)
        Vlayout = QtWidgets.QVBoxLayout()
        Hlayout.addLayout(Vlayout)
        Hlayout.addWidget(self.control_groupBox)

        self.static_canvas = FigureCanvasQTAgg(Figure(tight_layout=True))
        self.static_canvas.figure.dpi = 80.0
        self.static_canvas.figure.suptitle('No pictures to show')
        self.addToolBar(NavigationToolbar2QT(self.static_canvas, self))
        Vlayout.addWidget(self.static_canvas)

        self.axs = None
        self.cur_pic_name = ''

        self.picNum_comboBox.currentTextChanged.connect(self.show_pictures)
        self.next_pushButton.clicked.connect(self.show_next)
        self.prev_pushButton.clicked.connect(self.show_prev)
        self.diap_diff_spinBox.valueChanged.connect(self.show_pictures)
        self.diap_init_spinBox.valueChanged.connect(self.show_pictures)
        self.save_pushButton.clicked.connect(self.save_pages)

    def refresh_pictures(self):
        self.picNum_comboBox.blockSignals(True)
        self.picNum_comboBox.clear()
        self.picNum_comboBox.addItems(self.data.images_list)
        self.picNum_comboBox.blockSignals(False)
        self.static_canvas.figure.clear('all')
        self.static_canvas.figure.suptitle('Pictures from camera')

        n_ch = len(list(self.data.intensity_data.keys()))
        self.axs = self.static_canvas.figure.subplots(n_ch, 3)
        self.static_canvas.figure.tight_layout()
        exec(f"self.axs{'' if n_ch==1 else '[0]'}[0].set(title='Initial')")
        exec(f"self.axs{'' if n_ch==1 else '[0]'}[1].set(title='Differential')")
        exec(f"self.axs{'' if n_ch==1 else '[0]'}[2].set(title='Final')")
        for num, key in enumerate(self.data.images_data.keys()):
            exec(f"self.axs{'' if n_ch==1 else '[num]'}[0].set(ylabel=key)")
            exec(f"self.axs{'' if n_ch==1 else '[num]'}[0].set(ylabel=key)")
            exec(f"self.axs{'' if n_ch==1 else '[num]'}[0].set(ylabel=key)")
        self.show_pictures()

    def show_pictures(self):
        if self.axs is not None:
            self.cur_pic_name = self.picNum_comboBox.currentText()
            n_ch = len(list(self.data.intensity_data.keys()))
            self.add_max_on_diff = self.diap_diff_spinBox.value()
            self.add_max_on_init = self.diap_init_spinBox.value()
            self.static_canvas.figure.suptitle(f'Pictures '
                                               f'{self.data.images_data[list(self.data.images_data.keys())[0]]["images"][self.cur_pic_name]["start_time"]}'
                                               f' - '
                                               f'{self.data.images_data[list(self.data.images_data.keys())[0]]["images"][self.cur_pic_name]["end_time"]}'
                                               f' ms')
            for num, key in enumerate(self.data.images_data.keys()):
                exec(f"self.axs{'' if n_ch==1 else '[num]'}[0].clear()")
                exec(f"self.axs{'' if n_ch==1 else '[num]'}[1].clear()")
                exec(f"self.axs{'' if n_ch==1 else '[num]'}[2].clear()")
                initial = self.data.images_data[key]['images'][self.cur_pic_name]['initial']
                differential = self.data.images_data[key]['images'][self.cur_pic_name]['differential']
                final = self.data.images_data[key]['images'][self.cur_pic_name]['final']
                exec(f"self.axs{'' if n_ch==1 else '[num]'}[0].imshow(initial, cmap='magma')")
                exec(f"self.axs{'' if n_ch==1 else '[num]'}[1].imshow(differential, cmap='magma')")
                exec(f"self.axs{'' if n_ch == 1 else '[num]'}[2].imshow(final, cmap='magma')")
            exec(f"self.axs{'' if n_ch == 1 else '[0]'}[0].set(title='Initial')")
            exec(f"self.axs{'' if n_ch == 1 else '[0]'}[1].set(title='Differential')")
            exec(f"self.axs{'' if n_ch == 1 else '[0]'}[2].set(title='Final')")

            self.static_canvas.draw()
        gc.collect(2)

    def show_next(self):
        if self.picNum_comboBox.currentIndex() < self.picNum_comboBox.count()-1:
            self.picNum_comboBox.setCurrentIndex(self.picNum_comboBox.currentIndex()+1)
        else:
            self.statusbar.showMessage('Last picture', 3000)

    def show_prev(self):
        if self.picNum_comboBox.currentIndex() > 0:
            self.picNum_comboBox.setCurrentIndex(self.picNum_comboBox.currentIndex()-1)
        else:
            self.statusbar.showMessage('First picture', 3000)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtCore.Qt.Key_D:
            self.show_next()
        elif event.key() == QtCore.Qt.Key_A:
            self.show_prev()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.static_canvas.figure.tight_layout()

    def save_pages(self):
        data_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбрать папку для сохранения", ".")
        if data_dir is not None and data_dir != '':
            for key in self.data.images_data.keys():
                with open(os.path.join(data_dir, f'{key}_initial.npy'), 'wb') as file:
                    np.save(file, self.data.images_data[key]['images'][self.cur_pic_name]['initial'])
                with open(os.path.join(data_dir, f'{key}_differential.npy'), 'wb') as file:
                    np.save(file, self.data.images_data[key]['images'][self.cur_pic_name]['differential'])
                with open(os.path.join(data_dir, f'{key}_final.npy'), 'wb') as file:
                    np.save(file, self.data.images_data[key]['images'][self.cur_pic_name]['final'])
                Image.fromarray(self.data.images_data[key]['images'][self.cur_pic_name]['initial'], mode='L').save(
                    os.path.join(data_dir, f'{key}_initial.bmp'))
                Image.fromarray(self.data.images_data[key]['images'][self.cur_pic_name]['differential'], mode='L').save(
                    os.path.join(data_dir, f'{key}_differential.bmp'))
                Image.fromarray(self.data.images_data[key]['images'][self.cur_pic_name]['final'], mode='L').save(
                    os.path.join(data_dir, f'{key}_final.bmp'))

            self.statusbar.showMessage(f'Saved to {data_dir}', 3000)
        else:
            self.statusbar.showMessage("Didn't save the pictures", 3000)

    @QtCore.pyqtSlot()
    def refresh_slot(self):
        self.refresh_pictures()
