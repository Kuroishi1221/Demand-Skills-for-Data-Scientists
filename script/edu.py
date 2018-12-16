""" Demand Skill For Data Scientist
    #Gradulate
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
    with open('csvfile/edu.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))



def usefile(file1):
    """ Set format list to Use"""
    file1 = [[i, int(j)] for i, j in file1]
    count = 0
    for i in file1:
        count += i[1]
    file1 = [[i,float('%.2f' %(j/count * 100))] for i, j in file1]
    print(file1)
    file1.sort()
    chart(file1)



def chart(data):
    """ Convert List To Graph """
    pie_chart = pygal.Pie(inner_radius=.4, value_formatter=lambda x: str(x) + '%')
    pie_chart.title = 'Data Scientist Graduate in? (in %)'
    for i in data:
        pie_chart.add(*i)
    pie_chart.render()
    pie_chart.render_to_file('img/edu.svg')
openfile()
