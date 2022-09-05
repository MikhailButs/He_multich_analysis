import gc

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
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


        # for i in ('1', '2', '3'):
        #     eval(f'self.ax_initial{i} = self.static_canvas1.figure.add_subplot(3, 3, 1)')
        # self.ax_initial1 = self.static_canvas.figure.add_subplot(1, 3, 1)
        # self.ax_initial1.set_title('Initial')
        # self.ax_diff1 = self.static_canvas.figure.add_subplot(1, 3, 2)
        # self.ax_diff1.set_title('Differential')
        # self.ax_final1 = self.static_canvas.figure.add_subplot(1, 3, 3)
        # self.ax_final1.set_title('Final')

    def refresh_pictures(self):
        self.picNum_comboBox.blockSignals(True)
        self.picNum_comboBox.clear()
        self.picNum_comboBox.addItems(self.data.images_list)
        self.picNum_comboBox.blockSignals(False)
        self.static_canvas.figure.clear('all')
        self.static_canvas.figure.suptitle('Pictures from camera')

        if self.data.ChType == 'three':
            self.axs = self.static_canvas.figure.subplots(3, 3)
            self.axs[0][0].set(title='Initial')
            self.axs[0][1].set(title='Differential')
            self.axs[0][2].set(title='Final')
            self.axs[0][0].set(ylabel='Channel1')
            self.axs[1][0].set(ylabel='Channel2')
            self.axs[2][0].set(ylabel='Channel3')
        self.show_pictures()

    # def clear_axes(self):
    #     pass

    def show_pictures(self):
        if self.axs is not None:
            self.cur_pic_name = self.picNum_comboBox.currentText()
            cur_pic_num = self.data.images_list.index(self.cur_pic_name)
            if self.data.ChType == 'three':
                self.axs[0][0].clear()
                self.axs[1][0].clear()
                self.axs[2][0].clear()
                self.axs[0][1].clear()
                self.axs[1][1].clear()
                self.axs[2][1].clear()
                self.axs[0][0].imshow(self.data.init_pic_list[cur_pic_num][0], cmap='hot')
                self.axs[1][0].imshow(self.data.init_pic_list[cur_pic_num][1], cmap='hot')
                self.axs[2][0].imshow(self.data.init_pic_list[cur_pic_num][2], cmap='hot')
                self.axs[0][1].imshow(self.data.diff_pic_list[cur_pic_num][0], cmap='hot')
                self.axs[1][1].imshow(self.data.diff_pic_list[cur_pic_num][1], cmap='hot')
                self.axs[2][1].imshow(self.data.diff_pic_list[cur_pic_num][2], cmap='hot')
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
        if event.key() == Qt.Qt.Key_Up:
            self.show_next()
        elif event.key() == Qt.Qt.Key_Down:
            self.show_prev()

    @QtCore.pyqtSlot()
    def refresh_slot(self):
        self.refresh_pictures()


