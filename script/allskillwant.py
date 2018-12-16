""" Demand Skill For Data Scientist
    #skill want
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
    xlabel = [i[0] for i in file1[1:]]
    for i in range(1, 5):
        head = file1[0][i]
        lisskill = [row[i] for row in file1[1:]]
        summ = list(map(lambda x: int(x.replace(',','')), lisskill))
        data1.append([head, summ])
    chart(data1, xlabel)



def chart(data, label):
    """ Convert List To Graph """
    want = 10
    line_chart = pygal.StackedBar()
    line_chart.title = 'skill want top 10'
    line_chart.x_labels = label[:want]
    for i, j in data:
        line_chart.add(i, j[:want])
    line_chart.render_to_file('img/allskillwant2.svg')
openfile()
