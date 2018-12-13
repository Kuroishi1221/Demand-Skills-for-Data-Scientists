import os
import csv
import pygal
lis = []
usecal = 5
def openfile():
    with open('csvfile/income.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))
def usefile(file1):
    file1.sort(key=lambda x: int(x[1]))
    chart(file1)
def chart(data):
    line_chart = pygal.Bar()
    line_chart.title = 'Salary for Data Scientists'
    for i, j in data:
        line_chart.add(i, int(j))
    line_chart.render_to_file('img/salary.svg')
openfile()
