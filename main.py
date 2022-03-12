import sys
from PyQt5 import QtWidgets, uic
import pandas as pd
from mainWindow import Ui_DataAnalyzer
from Dataframe import Dataframe

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     DataAnalyzer = QtWidgets.QMainWindow()
#     ui = Ui_DataAnalyzer()
#     ui.setupUi(DataAnalyzer)

#     #Dataframe viewing
#     df = pd.read_csv('jm1.csv')
#     dfViewer = Dataframe(df, ui)
#     dfViewer.show()

#     DataAnalyzer.show()
#     sys.exit(app.exec_())


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.dfView = self.findChild(QtWidgets.QTableView, 'tableView') # Find the button

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')
    def initializeDataframe(self, model):
        self.dfView.setModel(model)

app = QtWidgets.QApplication(sys.argv)
window = Ui()

#Dataframe viewing
df = pd.read_csv('test.csv')
dataframe = Dataframe(df, window)
dataframe.show()

app.exec_()

