import os
import csv
import pygal
lis = []
usecal = 5
def openfile():
    with open('csvfile/job.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))
def usefile(file1):
    liscount = []
    for i in range(1, 5):
        head =  file1[0][i]
        summ = sum([int(skill[i].replace(',','')) for skill in file1[1:]])
        liscount.append([head, summ])
    print(liscount)
    chart(liscount)
def chart(data):
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'job want'
    for i in data:
        line_chart.add(*i)
    line_chart.render_to_file('img/Jobwant.svg')
openfile()