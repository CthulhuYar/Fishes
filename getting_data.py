import PySimpleGUI as sg
import json
import datetime


def get_data(data, theme, clas):
    Name = []
    Probability = []
    WebSite = []
    Date = []
    Universities = []
    val = []

    for i in range(len(data)):
        if theme == data[i].get('Theme'):
            if clas in list_up(convert(data[i].get('Class'))):
                if date(data[i].get('OlympiadDate')):

                    Name.append(data[i].get('Name'))
                    # Probability.append(student(data[i].get('Theme')))
                    WebSite.append(data[i].get('WebSite'))
                    Date.append(data[i].get('OlympiadDate'))
                    Universities.append(data[i].get('University'))

    for i in range(len(Name)):
        s = 'Название олимпиады: {}'.format(Name[i])
        val.append(s)
        s = '    Web-site: {}'.format(WebSite[i])
        val.append(s)
        s = '    Дата проведения: {}'.format(Date[i])
        val.append(s)
        s = '    Университеты, в которых она учитывается: {} ' .format(Universities[i])
        val.append(s)
        val.append('\n')

        # Вероятность победы
        # s = '\tВероятность победы: {}'.format(Probability[i])
    return val


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


with open('test_data.json', mode='r', encoding='windows-1251') as data:
    json_data = json.load(data)
    print(get_data(json_data, 'Физика', 10))
