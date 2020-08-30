from PyQt5.QtWidgets import QWidget, QGridLayout, QSplitter
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

#   Class for the main widget the will be used by the main menu to display all the web panes in a grid layout

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        #   Variables
        self.panes = []
        self.grid = (3,2)
        self.splitters = []

        #   Layout
        self.gridLayout = QGridLayout()
        #   Call Function to populate the splitters for the layout with web pane widgets
        self.populateSplitters(self.grid)

        self.setLayout(self.gridLayout)

        
    #   Function that populates the grid layout with web panes
    def populateSplitters(self, grid):
        #   First clear grid from previous web panes layout
        self.clearSplitters()
        #   function variables
        vertSplitters = QSplitter(Qt.Vertical)
        horiSplitters = QSplitter(Qt.Horizontal)
        index = 0
        #   Nested loops to iterate over the grid dimensions and add web panes to the splitter
        for x in range(grid[1]):            
            for y in range(grid[0]):
                #   If statement to determine if there is already existing web pane widgets in the web pane list
                if index < len(self.panes):
                    #self.gridLayout.addWidget(self.panes[index], x, y)
                    #   Add web pane widgets to horizontal splitter
                    horiSplitters.addWidget(self.panes[index])
                    index = index + 1
                #   If no more web pane widgets exist in the web pane list, create a new and add it the the grid layout
                else:        
                    webPane = QWebEngineView()
                    webPane.load(QUrl('https://www.tradingview.com/chart/'))
                    self.panes.append(webPane)
                    #self.gridLayout.addWidget(webPane, x, y)
                    #   Add web pane widget to horizontal splitters
                    horiSplitters.addWidget(self.panes[index])
                    index = index + 1
            #   Add horizontal splitters to vertical splitters
            vertSplitters.addWidget(horiSplitters)
            #   Create new horizontal splitter for next horizontal loop
            horiSplitters = QSplitter(Qt.Horizontal)
    
        #   Add vertical splitter to grid layout first insert new splitter widget to the from of the splitters list then add the widget to the grid layout
        self.splitters.insert(0, vertSplitters)
        self.gridLayout.addWidget(self.splitters[0])
        
#        del self.splitters[1:]

    #   Function for clearing grid layout of all web pane widgets
    def clearSplitters(self):
        #   Loop over the widgets in the grid layout in reverse so no conflict occurs with indexing as widgets are removed from the grid        
        for i in reversed(range(self.gridLayout.count())):
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        
        

