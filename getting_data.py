import PySimpleGUI as sg
from Hackschool_data import data

def get_data(theme):
    Name = []
    Probability = []
    WebSite = []
    Date = []
    Universities = []
    val = []

    for i in range(len(data)):
        if theme == data[i].get('Theme'):
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
        s = '    Университеты, в которых она учитыается: {} ' .format(Universities[i])
        val.append(s)
        val.append('\n')

        # Вероятность победы
        #s = '\tВероятность победы: {}'.format(Probability[i])
    return val