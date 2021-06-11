from PyQt5 import QtWidgets, QtGui, Qt
from frmMain import Ui_frmMain


# Class inheriting from QMainWindow and our Ui_frmMain in frmMain.py
class MainForm(QtWidgets.QMainWindow, Ui_frmMain):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())

