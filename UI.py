from PyQt5 import QtWidgets, uic
import window
import sys

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('window.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
win = window()
app.exec_()