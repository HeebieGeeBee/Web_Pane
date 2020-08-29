from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.panes = []
        self.grid = (3,2)

        #   Layout
        self.gridLayout = QGridLayout()
        self.populateGrid(self.grid)

        self.setLayout(self.gridLayout)

        self.show()


    def populateGrid(self, grid):

        self.clearGrid()

        index = 0

        for x in range(grid[1]):
            for y in range(grid[0]):
                if index < len(self.panes):
                    self.gridLayout.addWidget(self.panes[index], x, y)
                    index = index + 1
                else:        
                    webPane = QWebView()
                    webPane.load(QUrl('https://www.google.com/'))
                    self.panes.append(webPane)
                    self.gridLayout.addWidget(webPane, x, y)
                    index = index + 1
        print(self.panes)

    def clearGrid(self):
        
        for i in reversed(range(self.gridLayout.count())):
            #self.itemAt(i).widget().deleteLater()
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
    
        

