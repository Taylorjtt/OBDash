from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from SpekTach.spektach import Ui_SpekTach

# Assuming SpekTach.spektach contains a class Ui_SpekTach for the UI


app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()  # Renamed from SpekTach to main_window for clarity
ui = Ui_SpekTach()
ui.setupUi(main_window)
main_window.show()
sys.exit(app.exec_())