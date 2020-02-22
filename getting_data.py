import PySimpleGUI as sg
import json
import datetime
from Hackschool_data import data_olymp

file = open('test_data.json', mode='r', encoding='windows-1251')
data = json.load(file)


stage_list = {1:'Школьный', 2:'Муниципальный', 3:'Региональный', 4:'Заключительный'}


def get_data(theme, clas):
    Name = []
    # Probability = []
    WebSite = []
    Date = []
    Stage = []
    Universities = []
    olymp_list = []
    insert_univer = []

    for i in range(len(data)):
        if theme == data[i].get('Theme'):
            if clas in list_up(convert(data[i].get('Class'))):
                #if date(data[i].get('OlympiadDate')):

                    Name.append(data[i].get('Name'))
                    # Probability.append(student(data[i].get('Theme')))
                    WebSite.append(data[i].get('WebSite'))
                    Date.append(data[i].get('OlympiadDate'))
                    Stage.append(stage_list.get(data[i].get('Stage')))

                    for j in range(len(data_olymp)):
                        if data[i].get('Name') == data_olymp[j].get('Name'):
                            insert_univer.append(data_olymp[j].get('University'))
                        else:
                            continue
                    if insert_univer == []:
                        insert_univer = 'Таких ВУЗов нет, либо не найдены'
                    Universities.append(insert_univer)
                    insert_univer = []

    for i in range(len(Name)):
        olymp_list.extend(['Название олимпиады: {}'.format(Name[i]), 'Этап: {}'.format(Stage[i]),
                           'Университеты, в которых она учитывается: {}'.format(Universities[i]),
                           '    Web-site: {}'.format(WebSite[i][0].get('WebSite')), '    Дата проведения: {}'.format(Date[i]), '\n'])

        # Вероятность победы
        # s = '\tВероятность победы: {}'.format(Probability[i])
    return olymp_list


def get_pre_olymp(theme, clas):
    list_pre_olymp = []

    return list_pre_olymp


def convert(c):
    l = []
    if len(c) == 7:
        l.extend([int(c[0:2]), int(c[5:7])])
    elif len(c) == 6:
        l.extend([int(c[0]), int(c[4:6])])
    elif len(c) == 5:
        l.extend([int(c[0]), int(c[4])])
    elif len(c) == 2:
        l.extend([int(c[0:2])])
    elif len(c) == 1:
        l.extend([int(c[0])])
    return l


def list_up(l):
    a = l[0]
    b = l[len(l)-1]
    for i in range(a+1, b):
        l.insert(i-l[0], i)
    return l


def date(date_file):
    now = datetime.datetime.now()
    now_date = []
    now_date.extend([int('%d' % now.day), int('%d' % now.month), int('%d' % now.year)])

    olympiad_date = []
    olympiad_date.extend([int(date_file[0:2]), int(date_file[3:5]), int(date_file[6:10])])
    # print(olympiad_date)
    if olympiad_date[2] > now_date[2]:
        return True
    elif olympiad_date[2] < now_date[2]:
        return False
    elif olympiad_date[2] == now_date[2]:
        if olympiad_date[1] < now_date[1]:
            return False
        elif olympiad_date[1] > now_date[1]:
            return True
        elif olympiad_date[1] == now_date[1]:
            if olympiad_date[0] > now_date[0]:
                return True
            else:
                return False


#with open('test_data.json', mode='r', encoding='windows-1251') as data:
#    json_data = json.load(data)
#    print(get_data(json_data, 'Физика', 10))