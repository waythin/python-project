# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataAnalyzer(object):
    def setupUi(self, DataAnalyzer):
        DataAnalyzer.setObjectName("DataAnalyzer")
        DataAnalyzer.resize(800, 500)
        DataAnalyzer.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtWidgets.QWidget(DataAnalyzer)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 421, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 71, 21))
        self.label.setObjectName("label")
        DataAnalyzer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataAnalyzer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        DataAnalyzer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataAnalyzer)
        self.statusbar.setObjectName("statusbar")
        DataAnalyzer.setStatusBar(self.statusbar)

        self.retranslateUi(DataAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(DataAnalyzer)

    def retranslateUi(self, DataAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        DataAnalyzer.setWindowTitle(_translate("DataAnalyzer", "MainWindow"))
        self.pushButton.setText(_translate("DataAnalyzer", "Select File"))
        self.label.setText(_translate("DataAnalyzer", "Select .csv file"))

    def setDataframeModel(self, model):
        self.tableWidget.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataAnalyzer = QtWidgets.QMainWindow()
    ui = Ui_DataAnalyzer()
    ui.setupUi(DataAnalyzer)
    DataAnalyzer.show()
    sys.exit(app.exec_())

