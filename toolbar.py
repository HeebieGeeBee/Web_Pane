from PyQt5.QtWidgets import QToolBar, QAction

#   Class for the toolbar for the main window that will handle all the grid settings, it takes pointer the the main widget as an argument

class GridToolbar(QToolBar):
    def __init__(self, mainWidget):
        super().__init__()
        #   Variables
        self.mainWidget = mainWidget

        #   Grid layouts
        #   Qaction list for each button of the toolbar for different grid layouts
        one_by_one = QAction('1 x 1', self)
        one_by_two = QAction('1 x 2', self)
        one_by_three = QAction('1 x 3', self)
        two_by_one = QAction('2 x 1', self)
        two_by_two = QAction('2 x 2', self)
        two_by_three = QAction('2 x 3', self)
        three_by_one = QAction('3 x 1', self)
        three_by_two = QAction('3 x 2', self)
        three_by_three = QAction('3 x 3', self)

        #   Set status tip for each button
        one_by_one.setStatusTip('Set grid layout to 1 x 1')
        one_by_two.setStatusTip('Set grid layout to 1 x 2')
        one_by_three.setStatusTip('Set grid layout to 1 x 3')
        two_by_one.setStatusTip('Set grid layout to 2 x 1') 
        two_by_two.setStatusTip('Set grid layout to 2 x 2')
        two_by_three.setStatusTip('Set grid layout to 2 x 3')
        three_by_one.setStatusTip('Set grid layout to 3 x 1')
        three_by_two.setStatusTip('Set grid layout to 3 x 2')
        three_by_three.setStatusTip('Set grid layout to 3 x 3')
        
        #   Setting call to the function upon clicking the toolbar button
        one_by_one.triggered.connect(lambda: self.onGridButtonClick(1, 1))
        one_by_two.triggered.connect(lambda: self.onGridButtonClick(1, 2))
        one_by_three.triggered.connect(lambda: self.onGridButtonClick(1, 3))
        two_by_one.triggered.connect(lambda: self.onGridButtonClick(2, 1))
        two_by_two.triggered.connect(lambda: self.onGridButtonClick(2, 2))
        two_by_three.triggered.connect(lambda: self.onGridButtonClick(2, 3))
        three_by_one.triggered.connect(lambda: self.onGridButtonClick(3, 1))
        three_by_two.triggered.connect(lambda: self.onGridButtonClick(3, 2))
        three_by_three.triggered.connect(lambda: self.onGridButtonClick(3, 3))
        
        #   Add each button to the toolbar
        self.addAction(one_by_one)
        self.addAction(one_by_two)
        self.addAction(one_by_three)
        self.addAction(two_by_one)
        self.addAction(two_by_two)
        self.addAction(two_by_three)
        self.addAction(three_by_one)
        self.addAction(three_by_two)
        self.addAction(three_by_three)

    #   Function that will change grid layout
    def onGridButtonClick(self, num1, num2):
        self.mainWidget.populateGrid((num1, num2))
