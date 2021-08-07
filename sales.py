# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sales.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 613)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 521, 611))
        self.frame.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.label.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 11pt \"Roboto\";")
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(130, 20, 110, 21))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Roboto\";")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 21, 21))
        self.label_2.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 11pt \"Roboto\";")
        self.label_2.setObjectName("label_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setGeometry(QtCore.QRect(270, 20, 110, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Roboto\";")
        self.dateEdit_2.setWrapping(True)
        self.dateEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_2.setProperty("showGroupSeparator", True)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2021, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(394, 20, 121, 23))
        self.pushButton.setStyleSheet("background-color: rgb(230, 76, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Roboto\";")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 181, 31))
        self.label_3.setStyleSheet("color: rgb(170, 0, 127);\n"
"font: 75 13pt \"Roboto\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 331, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidgetsales = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetsales.setGeometry(QtCore.QRect(10, 110, 501, 351))
        self.tableWidgetsales.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetsales.setObjectName("tableWidgetsales")
        self.tableWidgetsales.setColumnCount(5)
        self.tableWidgetsales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetsales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetsales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetsales.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetsales.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetsales.setHorizontalHeaderItem(4, item)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 490, 181, 21))
        self.label_4.setStyleSheet("font: 75 14pt \"Roboto\";\n"
"color: rgb(170, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 530, 101, 21))
        self.label_5.setStyleSheet("font: 75 14pt \"Roboto\";\n"
"color: rgb(170, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 570, 151, 21))
        self.label_6.setStyleSheet("font: 75 14pt \"Roboto\";\n"
"color: rgb(170, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.pushButtonclose = QtWidgets.QPushButton(self.frame)
        self.pushButtonclose.setGeometry(QtCore.QRect(350, 572, 161, 31))
        self.pushButtonclose.setStyleSheet("font: 75 14pt \"Roboto\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(159, 0, 0);\n"
"border-radius:10px;")
        self.pushButtonclose.setObjectName("pushButtonclose")
        self.labelsalesAmount = QtWidgets.QLabel(self.frame)
        self.labelsalesAmount.setGeometry(QtCore.QRect(200, 490, 91, 31))
        self.labelsalesAmount.setStyleSheet("color: rgb(185, 92, 0);\n"
"font: 75 14pt \"Roboto\";")
        self.labelsalesAmount.setText("")
        self.labelsalesAmount.setObjectName("labelsalesAmount")
        self.labeltotalpaid = QtWidgets.QLabel(self.frame)
        self.labeltotalpaid.setGeometry(QtCore.QRect(120, 530, 81, 31))
        self.labeltotalpaid.setStyleSheet("color: rgb(185, 92, 0);\n"
"font: 75 14pt \"Roboto\";")
        self.labeltotalpaid.setText("")
        self.labeltotalpaid.setObjectName("labeltotalpaid")
        self.labeltotalreceivable = QtWidgets.QLabel(self.frame)
        self.labeltotalreceivable.setGeometry(QtCore.QRect(170, 570, 91, 31))
        self.labeltotalreceivable.setStyleSheet("color: rgb(185, 92, 0);\n"
"font: 75 14pt \"Roboto\";")
        self.labeltotalreceivable.setText("")
        self.labeltotalreceivable.setObjectName("labeltotalreceivable")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Filter sales from:"))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "d/M/yyyy"))
        self.label_2.setText(_translate("Dialog", "to:"))
        self.dateEdit_2.setDisplayFormat(_translate("Dialog", "d/M/yyyy"))
        self.pushButton.setText(_translate("Dialog", "Filter"))
        self.label_3.setText(_translate("Dialog", "Filter by Invoice S/N:"))
        item = self.tableWidgetsales.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Invoice S/N"))
        item = self.tableWidgetsales.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Date"))
        item = self.tableWidgetsales.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Amount"))
        item = self.tableWidgetsales.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Paid"))
        item = self.tableWidgetsales.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Make payment"))
        self.label_4.setText(_translate("Dialog", "Total sales Amount:"))
        self.label_5.setText(_translate("Dialog", "Total paid:"))
        self.label_6.setText(_translate("Dialog", "Total Receivable:"))
        self.pushButtonclose.setText(_translate("Dialog", "XCLOSE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())