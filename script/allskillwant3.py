""" Demand Skill For Data Scientist
    #skill want2
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
    with open('csvfile/job.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))



def usefile(file1):
    """ Set format list to Use"""
    data1 = []
    for i in file1[1:]:
        data1.append([i[0], sum(map(lambda x: int(x.replace(',','')), i[1:5]))])
    chart(data1)



def chart(data):
    """ Convert List To Graph """
    line_chart = pygal.Bar()
    line_chart.title = 'Technology Skill From Job Wanting'
    #line_chart.x_labels = [i[0] for i in data]
    for i, j in data:
        print(i, j)
        line_chart.add(i, j)
    line_chart.render_to_file('img/allskillwant3.svg')
openfile()
