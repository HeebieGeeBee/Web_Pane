import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5 import Qt, QtGui
from main_widget import MainWidget
from toolbar import GridToolbar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        #   Styling
        self.setWindowTitle('WebPanes version 0.1')
        self.width = 800
        self.height = 600
        self.top = 200
        self.left = 400
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background: white')

        #   Main widget
        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)

        #   Toolbar
        self.gridToolbar = GridToolbar(self.mainWidget)
        self.addToolBar(self.gridToolbar)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()