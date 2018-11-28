import os
import csv
import pygal
lis = []
usecal = 5
def openfile():
    with open('csvfile/skills.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))
def usefile(file1):
    data1 = []
    for i in file1[1:]:
        head = i[0]
        subdata = sum(map(lambda x: int(x.replace(',','')), i[1:]))    
        data1.append([head, subdata])
    chart(data1)
def chart(data):
    #data = data[:10]
    line_chart = pygal.Bar(x_title='General Skill')
    line_chart.title = 'Data Scientist General Skill'
    for i in data:
        line_chart.add(*i)
    line_chart.render_to_file('img/skillall.svg')
openfile()