# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shivling.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"background-color: rgb(189, 189, 189);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButtoninventory = QtWidgets.QPushButton(self.page)
        self.pushButtoninventory.setGeometry(QtCore.QRect(10, 40, 211, 41))
        self.pushButtoninventory.setStyleSheet("\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: rgb(200, 100, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtoninventory.setObjectName("pushButtoninventory")
        self.pushButtonsales = QtWidgets.QPushButton(self.page)
        self.pushButtonsales.setGeometry(QtCore.QRect(290, 40, 211, 41))
        self.pushButtonsales.setStyleSheet("\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: rgb(194, 97, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonsales.setObjectName("pushButtonsales")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 90, 51, 20))
        self.label.setStyleSheet("color: rgb(170, 85, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEditfilter = QtWidgets.QLineEdit(self.page)
        self.lineEditfilter.setGeometry(QtCore.QRect(60, 90, 381, 31))
        self.lineEditfilter.setStyleSheet("font: 75 italic 14pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid black;")
        self.lineEditfilter.setMaxLength(40)
        self.lineEditfilter.setClearButtonEnabled(True)
        self.lineEditfilter.setObjectName("lineEditfilter")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, -1, 931, 31))
        self.label_2.setStyleSheet("background-color: rgb(136, 0, 102);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 125, 501, 31))
        self.label_3.setStyleSheet("background-color: rgb(145, 0, 109);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(0, 150, 501, 261))
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButtonrefresh = QtWidgets.QPushButton(self.page)
        self.pushButtonrefresh.setGeometry(QtCore.QRect(20, 430, 371, 41))
        self.pushButtonrefresh.setStyleSheet("border:none;\n"
"background-color: rgb(148, 0, 111);\n"
"border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtonrefresh.setObjectName("pushButtonrefresh")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(650, 50, 71, 31))
        self.label_4.setStyleSheet("color: rgb(139, 0, 104);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(530, 95, 71, 21))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lineEditcustomer = QtWidgets.QLineEdit(self.page)
        self.lineEditcustomer.setGeometry(QtCore.QRect(600, 89, 311, 31))
        self.lineEditcustomer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid grey;")
        self.lineEditcustomer.setClearButtonEnabled(True)
        self.lineEditcustomer.setObjectName("lineEditcustomer")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(530, 130, 381, 41))
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"border:1px solid grey;")
        self.label_6.setObjectName("label_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_2.setGeometry(QtCore.QRect(520, 180, 401, 161))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget_2.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(530, 350, 81, 16))
        self.label_7.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(540, 380, 71, 16))
        self.label_8.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.lineEditpayment = QtWidgets.QLineEdit(self.page)
        self.lineEditpayment.setGeometry(QtCore.QRect(610, 379, 301, 21))
        self.lineEditpayment.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border:1px solid grey;")
        self.lineEditpayment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditpayment.setClearButtonEnabled(True)
        self.lineEditpayment.setObjectName("lineEditpayment")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(550, 415, 91, 21))
        self.label_9.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.labelamountdue = QtWidgets.QLabel(self.page)
        self.labelamountdue.setGeometry(QtCore.QRect(650, 410, 261, 21))
        self.labelamountdue.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.labelamountdue.setText("")
        self.labelamountdue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelamountdue.setObjectName("labelamountdue")
        self.pushButtoncompletesale = QtWidgets.QPushButton(self.page)
        self.pushButtoncompletesale.setGeometry(QtCore.QRect(510, 450, 171, 41))
        self.pushButtoncompletesale.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"background-color: rgb(0, 139, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtoncompletesale.setObjectName("pushButtoncompletesale")
        self.pushButtoncompletesale_2 = QtWidgets.QPushButton(self.page)
        self.pushButtoncompletesale_2.setGeometry(QtCore.QRect(730, 450, 141, 41))
        self.pushButtoncompletesale_2.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(153, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButtoncompletesale_2.setObjectName("pushButtoncompletesale_2")
        self.pushButtonsearch = QtWidgets.QPushButton(self.page)
        self.pushButtonsearch.setGeometry(QtCore.QRect(450, 90, 51, 31))
        self.pushButtonsearch.setStyleSheet("background-color: rgb(147, 0, 110);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButtonsearch.setObjectName("pushButtonsearch")
        self.labeltotal = QtWidgets.QLabel(self.page)
        self.labeltotal.setGeometry(QtCore.QRect(690, 350, 211, 20))
        self.labeltotal.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.labeltotal.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.labeltotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labeltotal.setObjectName("labeltotal")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtoninventory.setText(_translate("MainWindow", "Inventory"))
        self.pushButtonsales.setText(_translate("MainWindow", "sales"))
        self.label.setText(_translate("MainWindow", "Filter:"))
        self.lineEditfilter.setPlaceholderText(_translate("MainWindow", "Filter by item name you want"))
        self.label_2.setText(_translate("MainWindow", "POINT OF SALE"))
        self.label_3.setText(_translate("MainWindow", "Items available in shop"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "unit price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))
        self.pushButtonrefresh.setText(_translate("MainWindow", "Refresh table"))
        self.label_4.setText(_translate("MainWindow", "Invoice"))
        self.label_5.setText(_translate("MainWindow", "customer:"))
        self.label_6.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "item"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "description"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "unit price"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "quantity"))
        self.label_7.setText(_translate("MainWindow", "Grand total:"))
        self.label_8.setText(_translate("MainWindow", "payment:"))
        self.lineEditpayment.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.label_9.setText(_translate("MainWindow", "Amount due:"))
        self.pushButtoncompletesale.setText(_translate("MainWindow", "complete sale"))
        self.pushButtoncompletesale_2.setText(_translate("MainWindow", "clear"))
        self.pushButtonsearch.setText(_translate("MainWindow", "search"))
        self.labeltotal.setText(_translate("MainWindow", "l"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())