""" Demand Skill For Data Scientist
    #General Skill
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
    with open('csvfile/skills.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))



def usefile(file1):
    """ Set format list to Use"""
    data1 = []
    for i in file1[1:]:
        head = i[0]
        subdata = sum(map(lambda x: int(x.replace(',','')), i[1:]))    
        data1.append([head, subdata])
    chart(data1)



def chart(data):
    """ Convert List To Graph """
    line_chart = pygal.Bar(x_title='General Skill')
    line_chart.title = 'Data Scientist General Skill'
    for i in data:
        line_chart.add(*i)
    line_chart.render_to_file('img/skillall.svg')
openfile()
