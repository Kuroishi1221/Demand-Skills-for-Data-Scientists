import os
import csv
import pygal
lis = []
def openfile():
    with open('csvfile/job.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))
def usefile(file1):
    data1 = []
    for i in file1[1:]:
        data1.append([i[0], sum(map(lambda x: int(x.replace(',','')), i[1:5]))])
    chart(data1)
def chart(data):
    want = 10
    line_chart = pygal.Bar()
    line_chart.title = 'Technology Skill From Job Wanting'
    #line_chart.x_labels = [i[0] for i in data]
    for i, j in data:
        print(i, j)
        line_chart.add(i, j)
    line_chart.render_to_file('img/allskillwant3.svg')
openfile()