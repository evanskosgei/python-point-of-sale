from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.Qt import QAbstractItemView
from database import *
#from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import os
import win32print  #pip install pywin32
import win32api
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint, QTimer, QTime,QDate,QDateTime
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtCore import pyqtSlot, QRect
import time

import shivling as shiv
import inventory as inv
import Additem as add
import sales as sl
import print as pr
import load as ld
import sys


class Load(ld.Ui_Dialog, QtWidgets.QDialog): 
    def __init__(self):
        super(Load, self).__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.open)
    def open(self):
        self.label.setText("LOADING...")
        n = 100;
        for i in range(n):
            time.sleep(0.01)
            self.progressBar.setValue(i+1)
        
        self.load()
        self.hide()

    def load(self):
        self.ui = Funct()
        self.ui.show()
    
class Funct(shiv.Ui_MainWindow, QtWidgets.QMainWindow): 
    def __init__(self):
        super(Funct, self).__init__()
        self.setupUi(self)

        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selection)

        self.pushButtoninventory.clicked.connect(self.btn_inventory)
        self.pushButtonrefresh.clicked.connect(self.btn_refresh)
        self.pushButtoncompletesale_2.clicked.connect(self.btn_delete)
        self.pushButtonsales.clicked.connect(self.btn_sales)
        self.pushButtonsearch.clicked.connect(self.btn_search)
        self.pushButtoncompletesale.clicked.connect(self.btn_print)
        self.pushButtoncompletesale.clicked.connect(self.btn_completesale)
    
    def on_selection(self, selected):
        row = 1;
        for ix in selected.indexes():
            #ix =[self.tableWidget.item(row, 0).text() for row in selected(self.tableWidget.rowCount())]
            print(ix)
            print('selected location Row:{0}, column:{1}'.format(ix.row(), ix.column()))
        self.tableWidget_2.setRowCount(0)
        for row_number, row_selected in enumerate(selected):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(selected):
                self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem (str(data)))
        
    def btn_inventory(self):
        self.ui = Inv()
        self.ui.show()
    
    def btn_sales(self):
        self.ui = Sale()
        self.ui.show()
    def btn_refresh(self):

        query = """SELECT *FROM inventory"""
        mycursor.execute(query,)
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem (str(data)))
        

    def btn_delete(self):
        try:

            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "super"
            )
            mycursor = mydb.cursor()
            customer = self.lineEditcustomer.text()
            query= "DELETE FROM sale WHERE customer= %s"
            value = (customer,)
            mycursor.execute(query, value)
            mydb.commit()
            customer = self.lineEditcustomer.clear()
            mycursor.close()
        except mc.Error as e:
            print("User doesnot exist!!!")
    
    def btn_search(self):
        item = self.lineEditfilter.text()
        query = """SELECT item, description, unit_price, quantity from inventory WHERE item=(%s);"""
        mycursor.execute(query, (item,))
        r = tuple(mycursor.fetchall())
        print(r)
        if r !=():
            print("item found")
        else:
            print("item unavailable")
        row = 0
        self.tableWidget.setRowCount(0)
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(r[0][1]))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(r[0][2])) 
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(r[0][3]))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(r[0][4]))
        #self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(r[0][4]))

    def btn_print(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "super"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT unit_price, quantity from sale")
            result = mycursor.fetchall()
            total =0;
            for items in result:
                sum =(int(items[0])* int(items[1]))
                #print(sum)
                total = float(total) + sum;
            #print(total)
            self.labeltotal.setText(str(total))
            try:
                payment = self.lineEditpayment.text();
                #print(payment)
                due = float(payment) - total;
                #print(due)
                self.labelamountdue.setText(str(due))
            except:
                #print("reenter items")
                payment = self.lineEditpayment.clear();

            #insert values to db
            
            #query = """INSERT INTO sales """
            #mycursor.execute(query,values)
        except mc.Error as e:
            self.labeltotal.setText("encountered some problem")

    def btn_completesale(self):
        self.ui = Printing()
        self.ui.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

class Inv (inv.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Inv, self).__init__()
        self.setupUi(self)

        #btn for oppenning add item window
        self.pushButtonadditem.clicked.connect(self.btn_additem)
        #btn show items on the tabel
        self.pushButtontabrefresh.clicked.connect(self.btn_refresh)
        self.pushButtontabrefresh.clicked.connect(self.btn_price)

    def btn_additem(self):
        self.ui = AddI()
        self.ui.show()

    def btn_price(self):

        query = """SELECT unit_price, quantity FROM inventory"""
        mycursor.execute(query,)
        result = mycursor.fetchall()
        #print(result)
        total = 0;
        for items in result:
            sum =int(items[0])* int(items[1])
        #    print(sum)
            total = float(total) + sum;
        #print(total)
        self.labelprice.setText("ksh"+str(total))

    def btn_refresh(self):
            query = """SELECT *FROM inventory"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            self.tableWidgetitemadded.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidgetitemadded.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidgetitemadded.setItem(row_number, column_number, QTableWidgetItem (str(data)))

class AddI (add.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(AddI, self).__init__()
        self.setupUi(self)

        #btn for cancel input
        self.pushButtonsubmit_2.clicked.connect(self.btn_cancel)
        #btn for submitting items to db
        self.pushButtonsubmit.clicked.connect(self.btn_submit)

    def btn_cancel(self):
        self.hide()

    def btn_submit(self):
        item = self.lineEdititem.text()
        description = self.lineEditdescription.text()
        unit_price = self.lineEditunitprice.text()
        quantity = self.lineEditquantity.text()

        query = "INSERT INTO inventory(item,description,unit_price,quantity) VALUE(%s, %s, %s, %s)"
        values = (item,description,unit_price, quantity)
        mycursor.execute(query, values)
        mydb.commit()
        item = self.lineEdititem.clear()
        description = self.lineEditdescription.clear()
        unit_price = self.lineEditunitprice.clear()
        quantity = self.lineEditquantity.clear()
        mycursor.close()

class Sale(sl.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Sale, self).__init__()
        self.setupUi(self)

        self.btn_refresh()
        self.output()

        #btn to close the page
        self.pushButtonclose.clicked.connect(self.btn_close)

    def btn_close(self):
        self.close()

    def output(self):

        query = """SELECT unit_price, quantity, payment, amount_due, total from sale"""
        mycursor.execute(query)
        result = mycursor.fetchall()
        #print(result)
        Amount_received =0;
        total =0;
        for items in result:
            sum =(int(items[0])* int(items[1]))
            #print(sum)
            total = float(total) + sum;
            #print(total)
        self.labelsalesAmount.setText(str(total))
        self.labeltotalpaid.setText(str(items[2]))
        Amount_received = int(items[2]) - total
        self.labeltotalreceivable.setText(str(Amount_received))
    
    def btn_refresh(self):
            query = """SELECT *FROM sale"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            print(result)
            self.tableWidgetsales.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidgetsales.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidgetsales.setItem(row_number, column_number, QTableWidgetItem (str(data)))

class Printing(pr.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Printing, self).__init__()
        self.setupUi(self)

        self.progressBar.setValue(0)
        self.tables()
        self.current_date()
        self.Customer_output()
        self.pushButton.clicked.connect(self.btn_salewithoutprint)
        #self.pushButton_2.clicked.connect(self.progressbar)
        #printing txt
        self.pushButton_2.clicked.connect(self.print_txt)
        self.pushButton_2.clicked.connect(self.print_preview_dialog)
    
    def btn_salewithoutprint(self):
        self.hide()

    def tables(self):

        query = """SELECT id, item, unit_price, total FROM sale"""
        mycursor.execute(query)
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem (str(data)))

    def current_date(self):
        date =QDate.currentDate().toString("dd-MM-yyyy")
        self.labeldate.setText(str(date))

    def Customer_output(self):

        query = """SELECT payment, amount_due, total, customer from sale"""
        mycursor.execute(query)
        result = mycursor.fetchall()
        #print(result)
        for items in result:
            self.labelgrandtotal.setText(str(items[2]))
            self.labelpayment.setText(str(items[0]))
            self.labelAmountdue.setText(str(items[1]))
            self.labelcustomer.setText(str(items[3]))
    def progressbar(self):
        n = 100;
        for i in range(n):
            time.sleep(0.1)
            self.progressBar.setValue(i+1)
        self.hide()
    def print_txt(self):
        DATE = QDate.currentDate().toString("dd-MM-yyyy")

        query = """SELECT *FROM sale"""
        mycursor.execute(query)
        result = mycursor.fetchall()
        #print(result)
        for items in result:
            f = open(str(items[5])+".pdf", "w")
        #f = open(str(items[5])+".txt", "w")
        print("KAMATI SHOPPING CENTER", file=f)
        print("PO. BOX. 193 ELDAMA RAVINE", file=f)
        print("DATE ISSUED"+ DATE, file=f)
        print("items\t" + "prices\t" + "quantity\t"+"description\n", file=f)
        print(str(items[1])+"\t"+""+str(items[3])+"\t"+""+str(items[4]) +"\t"+"\t"+str(items[2]), file=f)
        print("TOTAL AMOUNT:"+str(items[7]), file=f)
        print("AMOUNT RECEIVED:"+ str(items[6]), file=f)
        print("BALANCE:"+str(items[8])+"\n", file=f)
        print("Thank you for your purchase..."+"\n", file=f)
        print("Good once sold can never be returned", file=f)

            #printer box
            #printer = QPrinter(QPrinter.HighResolution)
            #dialog = QPrintDialog(printer, self)

            #if dialog.exec_() == QPrintDialog.Accepted:
            #    painter = QtGui.QPainter(dialog.printer())
            #    f.print_(printer)
        f.close()

    def print_preview_dialog(self): 
        #printer = QPrinter(QPrinter.HighResolution)
        #previewDialog = QPrintPreviewDialog(printer, self)
        #previewDialog.paintRequested.connect(self.print_txt)
        #previewDialog.exec_()
        #printer_name = win32print.GetDefaultPrinter()  #check the type of printer
        #status_bar.config(text=printer_name)

        file_to_print = QFileDialog.getOpenFileName()

        if file_to_print:
            win32api.shellExecute(0, "print", file_to_print, None, ".", 0)

    def print_file(self):
        DATE = QDate.currentDate().toString("dd-MM-yyyy")

        query = """SELECT *FROM sale"""
        mycursor.execute(query)
        result = mycursor.fetchall()


        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            print(result)
            self.print_txt.print_exec(printer)
            
      
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = Load()
    qt_app.show()
    app.exec_()