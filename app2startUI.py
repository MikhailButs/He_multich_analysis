from dataCore import dataCore
from mainWindowUi import MainWindow
from PyQt5 import QtWidgets
import sys

core = dataCore()
mainWindow = MainWindow()

app = QtWidgets.QApplication(sys.argv)
mainWindow.show()
sys.exit(app.exec_())
