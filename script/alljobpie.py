""" Demand Skill For Data Scientist
    #JOB want_1
            #MEMBER#
    #61070214 Waruwat   Chaiyadith
    #61070021 Jharinya  Jaipakdee
    #61070093 Terawat   Kanjanapanwong
    #61070182 Ratchanon Chumbunyeanyong """
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
    liscount = []
    for i in range(1, 5):
        head =  file1[0][i]
        summ = sum([int(skill[i].replace(',','')) for skill in file1[1:]])
        liscount.append([head, summ])
    print(liscount)
    chart(liscount)



def chart(data):
    """ Convert List To Graph """
    line_chart = pygal.Pie(print_labels=True, print_values=True)
    line_chart.title = 'Data Scientist Job Listing'
    for i in data:
        line_chart.add(i[0], [{'value': i[1], 'label': i[0]}])
    line_chart.render_to_file('img/Jobwant1.svg')
openfile()
