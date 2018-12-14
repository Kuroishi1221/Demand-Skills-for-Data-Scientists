import os
import csv
import pygal
lis = []
usecal = 5
def openfile():
    with open('csvfile/edu.csv') as csvfile:
        file1 = csv.reader(csvfile)
        print('open Success')
        usefile(list(file1))
def usefile(file1):
    file1 = [[i, int(j)] for i, j in file1]
    count = 0
    for i in file1:
        count += i[1]
    file1 = [[i,float('%.2f' %(j/count * 100))] for i, j in file1]
    print(file1)
    file1.sort(key=lambda x: int(x[1]))
    chart(file1)
def chart(data):
    pie_chart = pygal.Pie(inner_radius=.4, value_formatter=lambda x: str(x) + '%')
    pie_chart.title = 'Data Scientist Graduate in? (in %)'
    for i in data:
        pie_chart.add(*i)
    pie_chart.render()
    pie_chart.render_to_file('img/edu.svg')
openfile()
