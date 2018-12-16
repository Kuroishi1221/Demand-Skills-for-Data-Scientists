""" Demand Skill For Data Scientist
    #Salary
            #MEMBER#
    #61070214 Waruwat   Chaiyadith
    #61070021 Jharinya  Jaipakdee
    #61070093 Terawat   Kanjanapanwong
    #61070182 Ratchanon Chumbunyeanyong """
import os
import csv
import pygal



def openfile():
    """ Open File CSV and set to list"""
    with open('csvfile/income.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))



def usefile(file1):
    """ Set format list to Use"""
    file1.sort(key=lambda x: int(x[1]))
    chart(file1)



def chart(data):
    """ Convert List To Graph """
    line_chart = pygal.Bar()
    line_chart.title = 'Salary for Data Scientists'
    for i, j in data:
        line_chart.add(i, int(j))
    line_chart.render_to_file('img/salary.svg')
openfile()
