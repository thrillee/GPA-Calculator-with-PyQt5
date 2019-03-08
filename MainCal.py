
"""
Created on Mon Sep 17 16:23:48 2018

@author: olutobi
"""

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from resultCal import ResultCalculator

courses = 0

def nextPage():
    clear()
    result.hide()
    ask.hide()
    table.show()
    returnRowCount()
    
def back():
    result.hide()
    ask.show()
    table.hide()
    
def returnRowCount():
    global courses
    courses = int(ask.no_of_courses.text())
    table.tableWidget.setRowCount(courses)


course_titles = []
course_codes = []
units = []
grades = []

def getItems():
    for column in range(4):
        print(courses)
        for row in range(courses):
            value = table.tableWidget.item(row,column).text()
            
            if column==0:
                course_titles.append(value)
            elif column==1:
                course_codes.append(value)
            elif column==2:
                units.append(value)
            elif column==3:
                grades.append(value)


def Main():
    
    getItems()
    ask.hide()
    result.show()
    table.hide()
    lcgpa = float(ask.last_cgpa_box.text())
    lunits = ask.no_of_units.text()

    rc = ResultCalculator(lunits, lcgpa, course_titles, course_codes, units, grades)
    result.GPAlineEdit.setText(str(round(rc.gpa,2)))
    result.CGPAlineEdit.setText(str(round(rc.confirmed_cgpa,2)))
    result.UNITlineEdit.setText(str(rc.unit))
    result.TSlineEdit.setText(str(int(rc.current_cgpa)))
    result.TUTlineEdit.setText(str(rc.total_units))
    result.COlineEdit.setText(str(len(rc.carry_over)))
    del course_titles[:]
    del course_codes[:]
    del units[:]
    del grades[:]

def clear():
    del course_titles[:]
    del course_codes[:]
    del units[:]
    del grades[:]
    for column in range(4):
        for row in range(courses):
            table.tableWidget.setItem(row,column, QTableWidgetItem(""))


def display_back():
    table.show()
    ask.hide()
    result.hide()
    
def display_cont():
    ask.show()
    table.hide()
    result.hide()
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ask = uic.loadUi('firstGpa.ui')
    table = uic.loadUi('resultTable.ui')
    result = uic.loadUi('display.ui')

    ask.calculate_result.clicked.connect(nextPage)
    table.back_btn.clicked.connect(back)
    table.clear_btn.clicked.connect(clear)

    table.get_result.clicked.connect(Main)
    result.back_btn.clicked.connect(display_back)
    result.continue_btn.clicked.connect(display_cont)
    
    ask.show()
    app.exec()
	


