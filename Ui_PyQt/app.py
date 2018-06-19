import sys
from PyQt5.QtWidgets import QDialog, QApplication
from login import Ui_Dialog

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()  


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())