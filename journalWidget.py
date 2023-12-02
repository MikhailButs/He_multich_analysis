import os
import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from journalUiDesign import Ui_journalWidget


class journalWidget(QtWidgets.QWidget, Ui_journalWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.paths = {'day': None, 'cine': None, 'sht': None}
        self.cine_dir_list = None
        self.sht_dir_list = None
        self.sync_table_flag = False

        self.dayPath_toolButton.clicked.connect(self._select_day_dir)
        self.dayDir_lineEdit.textChanged.connect(self._validate_day_dir)
        self.cineDir_lineEdit.textChanged.connect(self._validate_cine_dir)
        self.shtDir_lineEdit.textChanged.connect(self._validate_sht_dir)
        self.dayComment_plainTextEdit.textChanged.connect(self._save_day_comment)
        self.onSync_pushButton.clicked.connect(self.start_sync)
        self.offSync_pushButton.clicked.connect(self.stop_sync)

        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        # self.timer.timeout.connect(self._cine_listdir)
        # self.timer.timeout.connect(self._sht_listdir)
        self.timer.timeout.connect(self.check_dirs)

        self.offSync_pushButton.hide()

    def _select_day_dir(self):
        day_dir = QtWidgets.QFileDialog.getExistingDirectory(self, ".")
        if day_dir != '':
            self.dayDir_lineEdit.setText(day_dir)

    def _select_cine_dir(self):
        cine_dir = QtWidgets.QFileDialog.getExistingDirectory(self, ".")
        if cine_dir != '':
            self.cineDir_lineEdit.setText(cine_dir)

    def _select_sht_dir(self):
        sht_dir = QtWidgets.QFileDialog.getExistingDirectory(self, ".")
        if sht_dir != '':
            self.dayDir_lineEdit.setText(sht_dir)

    def _validate_day_dir(self):
        dir = self.dayDir_lineEdit.text()
        if os.path.exists(dir) and os.path.isdir(dir):
            self.paths['day'] = dir
            font = self.label_4.font()
            self.dayDir_lineEdit.setStyleSheet('colour : black')
            self.dayDir_lineEdit.setFont(font)
            if 'cine' in os.listdir(dir):
                self.cineDir_lineEdit.setText(os.path.normpath(os.path.join(dir, 'cine')))
            if 'sht' in os.listdir(dir):
                self.shtDir_lineEdit.setText(os.path.normpath(os.path.join(dir, 'sht')))
            if 'DayDescription.txt' in os.listdir(self.paths['day']):
                with open(os.path.join(self.paths['day'], 'DayDescription.txt'), 'r') as f:
                    self.dayComment_plainTextEdit.setPlainText(f.read())
        else:
            font = self.label_4.font()
            self.dayDir_lineEdit.setStyleSheet('colour : red')
            self.dayDir_lineEdit.setFont(font)

    def _validate_cine_dir(self):
        dir = self.cineDir_lineEdit.text()
        if os.path.exists(dir) and os.path.isdir(dir):
            self.paths['cine'] = dir
            font = self.label_4.font()
            self.dayDir_lineEdit.setStyleSheet('colour : black')
            self.dayDir_lineEdit.setFont(font)
        else:
            font = self.label_4.font()
            self.cineDir_lineEdit.setStyleSheet('colour : red')
            self.cineDir_lineEdit.setFont(font)

    def _validate_sht_dir(self):
        dir = self.shtDir_lineEdit.text()
        if os.path.exists(dir) and os.path.isdir(dir):
            self.paths['sht'] = dir
            font = self.label_4.font()
            self.dayDir_lineEdit.setStyleSheet('colour : black')
            self.dayDir_lineEdit.setFont(font)
        else:
            font = self.label_4.font()
            self.shtDir_lineEdit.setStyleSheet('colour : red')
            self.shtDir_lineEdit.setFont(font)

    def _save_day_comment(self):
        if self.paths['day'] is not None:
            with open(os.path.join(self.paths['day'], 'DayDescription.txt'), 'w') as f:
                f.write(self.dayComment_plainTextEdit.toPlainText())

    def _cine_listdir(self):
        if self.paths['cine'] is not None:
            # stat = os.stat(self.paths['cine'])
            self.cineDir_treeWidget.clear()
            n = 0
            v = 0
            for file in os.scandir(self.paths['cine']):
                stat = file.stat()
                v += stat.st_size
                item = QtWidgets.QTreeWidgetItem([file.name, str(round(stat.st_size / 1048576, 1)),
                                                  time.strftime('%X %d.%m.%y', time.gmtime(stat.st_ctime))])
                if file.name[-5:] == '.cine':
                    item.setIcon(0, QtGui.QIcon(
                        os.path.join(os.curdir, 'icons', 'cinefile.png')))
                    n += 1
                self.cineDir_treeWidget.addTopLevelItem(item)
            self.cineDir_treeWidget.resizeColumnToContents(0)
            self.cineDir_treeWidget.resizeColumnToContents(1)
            self.cineDir_treeWidget.scrollToBottom()
            self.cineDirInfo_label.setText(f'В папке {n} файлов ({round(v / 1048576, 1)} Мб):')

    def _sht_listdir(self):
        if self.paths['sht'] is not None:
            # stat = os.stat(self.paths['sht'])
            self.shtDir_treeWidget.clear()
            n = 0
            v = 0
            for file in sorted(os.scandir(self.paths['sht']), key=lambda x: x.name[3:-4]):
                stat = file.stat()
                v += stat.st_size
                item = QtWidgets.QTreeWidgetItem([file.name, str(round(stat.st_size / 1048576, 1)),
                                                  time.strftime('%X %d.%m.%y', time.gmtime(stat.st_ctime))])
                if file.name[-4:] == '.SHT':
                    item.setIcon(0, QtGui.QIcon(
                        os.path.join(os.curdir, 'icons', 'shtfile.png')))
                    n += 1
                self.shtDir_treeWidget.addTopLevelItem(item)
            self.shtDir_treeWidget.resizeColumnToContents(0)
            self.shtDir_treeWidget.resizeColumnToContents(1)
            self.shtDir_treeWidget.scrollToBottom()
            self.shtDirInfo_label.setText(f'В папке {n} файлов ({round(v / 1048576, 1)} Мб):')

    def update_table(self):
        for n, name in enumerate(os.listdir(self.paths['cine'])):
            print(n, name)

    def check_dirs(self):
        flag = 0
        if self.paths['cine'] is not None and self.cine_dir_list != os.listdir(self.paths['cine']):
            self.cine_dir_list = os.listdir(self.paths['cine'])
            self._cine_listdir()
            flag += 1
        if self.paths['sht'] is not None and self.sht_dir_list != os.listdir(self.paths['sht']):
            self.sht_dir_list = os.listdir(self.paths['sht'])
            self._sht_listdir()
            flag += 1
        if self.sync_table_flag and flag:
            self.update_table()

    def start_sync(self):
        self.onSync_pushButton.hide()
        self.offSync_pushButton.show()
        self.sync_table_flag = True
        self.update_table()

    def stop_sync(self):
        self.offSync_pushButton.hide()
        self.onSync_pushButton.show()
        self.sync_table_flag = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mv = journalWidget()
    mv.show()
    sys.exit(app.exec_())
