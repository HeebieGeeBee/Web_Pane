from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QUrl

#   Class for the main widget the will be used by the main menu to display all the web panes in a grid layout

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        #   Variables
        self.panes = []
        self.grid = (3,2)

        #   Layout
        self.gridLayout = QGridLayout()
        #   Call Function to populate the grid layout with web pane widgets
        self.populateGrid(self.grid)
        self.setLayout(self.gridLayout)


    #   Function that populates the grid layout with web panes
    def populateGrid(self, grid):
        #   First clear grid from previous web panes layout
        self.clearGrid()

        index = 0
        #   Nested loops to iterate over the grid dimensions and add web panes to the grid 
        for x in range(grid[1]):
            for y in range(grid[0]):
                #   If statement to determine if there is already existing web pane widgets in the web pane list
                if index < len(self.panes):
                    self.gridLayout.addWidget(self.panes[index], x, y)
                    index = index + 1
                #   If no more web pane widgets exist in the web pane list, create a new and add it the the grid layout
                else:        
                    webPane = QWebView()
                    webPane.load(QUrl('https://www.google.com/'))
                    self.panes.append(webPane)
                    self.gridLayout.addWidget(webPane, x, y)
                    index = index + 1

    #   Function for clearing grid layout of all web pane widgets
    def clearGrid(self):
        #   Loop over the widgets in the grid layout in reverse so no conflict occurs with indexing as widgets are removed from the grid        
        for i in reversed(range(self.gridLayout.count())):
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
    
        

