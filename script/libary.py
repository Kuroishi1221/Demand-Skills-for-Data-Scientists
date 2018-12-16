""" Demand Skill For Data Scientist
    #JOB want
            #MEMBER#
    #61070214 Waruwat   Chaiyadith
    #61070021 Jharinya  Jaipakdee
    #61070093 Terawat   Kanjanapanwong
    #61070182 Ratchanon Chumbunyeanyong """
import pandas as pd 
import pygal



def openfile():
    """ Open File CSV and set to list"""
    data = pd.read_csv("csvfile/freeFormResponses.csv", names=['Q21_OTHER_TEXT'], low_memory=False)
    # Preview the first 5 lines of the loaded data 
    libary = data.Q21_OTHER_TEXT.tolist()
    usefile(libary)
def usefile(file1):
    libary = file1
    """ Set format list to Use"""
    s_libary = set(libary)
    dic_libary = {}
    for i in s_libary:
        each = str(i).split(',')
        for j in each:
            if j == 'nan':
                continue
            if j in dic_libary:
                dic_libary[j] += 1
            else:
                result = libary.count(j)
                dic_libary[j] = result if result > 0 else 1
    ans = dic_libary.items()
    ans = sorted(ans, key=lambda x: x[1], reverse=True)
    print(*ans, sep='\n')
    chart(ans)

def chart(data):
    """ Convert List To Graph """
    gauge = pygal.SolidGauge(half_pie=True, inner_radius=0.70, style=pygal.style.styles['default'](value_font_size=10))
    gauge.title = 'Top data visualization libraries or tools '
    for i in data[:9]:
        gauge.add(*i)
    gauge.render_to_file('img/libary.svg')
openfile()
