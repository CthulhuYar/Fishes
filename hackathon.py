import PySimpleGUI as sg
from getting_data import get_data

sg.theme('GreenTan')
win2_active, win3_active = False, False

layout = [
    [sg.Text('Индивидуальный поиск олимпиад', size=(30, 1), font=("Helvetica", 15))],
    [sg.Text('Выберете ваш класс'), sg.Spin(values=(8, 9, 10, 11))],
    [sg.Text('Выберете предмет'), sg.Spin(values=('Физика', 'Математика'))],
    [sg.Button('Выход'), sg.Button('Вывод', bind_return_key=True)]
        ]

# Первое окно
main_win = sg.Window('Хакатон', layout)
while True:
    event1, values1 = main_win.read()
    if event1 is None or event1=='Выход':
        break
    elif event1 == 'Вывод' and not win2_active:
        win2_active = True
        main_win.Hide()
        layout2 = [
            [sg.Text('Вы выбрали предмет - {0}, для класса - {1}'.format(values1[1], values1[0]))],
            [sg.Button('Выход'), sg.Button('Сохранить файл')]]

        # Второе окно
        # Выбор заслуг и оценка сложности *в разработке*
        win2 = sg.Window('Список олимпиад', layout2)
        while True:
            event2, values2 = win2.Read()
            if event2 is None or event2 == 'Выход':
                win2.Close()
                win2_active = False
                main_win.UnHide()
                break

            elif event2 == 'Сохранить файл' and not win3_active:
                win2_active, win3_active = False, True
                win2.Hide()

                layout3 = [
                    [sg.Text('Индивидуальный подбор олимпиад по вашим ответам', size=(90, 1), font=("Helvetica", 9))],
                    [sg.Listbox(values=get_data(values1[1]), size=(90, 20))],
                    [sg.Button('Выход')]]

                # Третье окно
                win3 = sg.Window('Подборка олимпиад', layout3)
                while True:
                    event3, values3 = win3.read()
                    if event1 is None or event3 =='Выход':
                        win3.Close()
                        win3_active = False
                        win2.UnHide()

                        break


main_win.close()
