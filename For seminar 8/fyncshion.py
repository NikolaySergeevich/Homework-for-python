from random import *
from contact import *
import json
global sprav

# sprav = {"Пельмешов Руслан Викторович": {"рабочий:": [674756, 54321], "личный:": [88888, 76584], "почта:": ["nion@mail.ru"]},\
# "Гурман Николай Сергеевич": {"рабочий:": [99999], "личный:": [232323], "почта:": ["napoleon@gmail.com"]},\
# "Поттер Гарри Иванович": {"рабочий:": [666, 365987, 90890], "личный:": [343434], "почта:": ["hogvarz@tyt.by"]},\
# "Вупкина Эльвира Максимовна": {"рабочий:": [8786], "личный:": [], "почта:": []}}
sprav = {}
spravochnik_about_client = {}
lst_work_numbers = []
lst_home_numbers = []
lst_email = []
# lst_for_delete = []

def save():
    with open("D:/Учёба в GB/Python/Homeworks/For seminar 8/sprav.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(sprav,ensure_ascii=False))
    print("Ваш справочник был успешно сохранён в файле sprav.json")

def load():
    global sprav
    with open("D:/Учёба в GB/Python/Homeworks/For seminar 8/sprav.json","r",encoding="utf-8") as fh:
        sprav=json.load(fh)
    print("Справочник был успешна загружен!")

def start():
    print('Здравстыуйте, вы открыли телефонный справочник. Меня зовут Pavl_Bot и я помогу вам найти,\n\
внести нового контакта, удалить необходимый или изменить уже существующий')
    print()
    load()

def ending():
    save()
    print('\nБот закончил свою работу')

def help():
    tex = '\n\
1 - просмотреть все контакты справочника\n\
2 - найти контакт по его фамилии, имени, отчетству или по всему и сразу\n\
3 - найти контакт по его одному из номеров телефона\n\
4 - найти контакт по его Email\n\
5 - добавить контак\n\
6 - удалить контакт\n\
7 - help\n\
8 - Загрузить справочник с хронилища\n\
9 - Сохранить справочник в хронилище\n\
0 - Закончить работу со справочником\n\
10 - Внесение изменений\n\
    '
    print(tex)

#Метод вывода всего справочника
def show_sprav():
    for(k,v) in sprav.items():
        print(k)
        for (p,g) in v.items():
            print(p, end='')
            print(*g, sep=', ')
        print()

#Метод поиска по фио(раздельно по фио и нет. в любом регистре)
def find_of_name():
    try:
        control = 0
        count = 0
        print('Введите ФИО: ', end=' ')
        name = enter_text().lower().split()
        lst_persone = list(map(lambda x: x, sprav))
        global lst_for_delete
        lst_for_delete = []
        for i in lst_persone:
            global h
            h = i
            i = i.lower().split()
            if len(name) <= len(i):
                for j in name:
                    if j in i:
                        count += 1
                if count == len(name):
                    lst_for_delete.append(h)
                    control += 1
                    print('\n', h)
                    for (p,g) in sprav[h].items():
                        print(p, end=' ')
                        print(*g, sep=',')
                    print()
                count = 0
        if control == 0:
            print('\nДанных по такому человеку нет. Попробуйте ещё раз.\n\
Введите 2 или 7 и выберите другой функционал.')
    except:
        print('\nЧто-то пошло не так.')


# Метод поиска контакта по номеру
def find_of_number():
    try:
        num = enter_num_pfone()
        count = 0
        for i in sprav:
            for j in sprav[i]:
                if num in sprav[i][j]:
                    count += 1
                    print('\n',i)
                    for (p,g) in sprav[i].items():
                        print(p, end=' ')
                        print(*g, sep=',')
                    print()
        if count == 0:
            print('\nТаких нет в базе справочника')
    except:
        print('Введены не коректные данные.')  


# Метод поиска контакта по Email
def find_of_Email():
    email = enter_email()
    count = 0
    for i in sprav:
        for j in sprav[i]:
            if email in sprav[i][j]:
                count += 1
                print('\n', i)
                for (p,g) in sprav[i].items():
                    print(p, end=' ')
                    print(*g, sep=',')
                print()
    if count == 0:
        print('\nТаких нет в базе справочника')  
# ------------------------------------------------------------------------------------------------------------
# Метод создания ключа - ФИО
def creat_caes_contact():
    print('\nВведите Фамилию', end=' ')
    first_name = enter_text()
    print('\nВведите Имя', end=' ')
    last_name = enter_text()
    print('\nВведите Отчетство', end=' ')
    otch = enter_text()
    ful_name = first_name + ' ' + last_name + ' ' + otch
    return ful_name


#Метод создания списаа номеров телефонов
def add_phon_num():
    lst = []
    try:
        print('\nДобавлять контакту номер? 1 - да, 0 - нет')
        pol = int(input('Введите число '))
        if pol == 1:
            lst.append(enter_num_pfone())
            print('\nНомер был успешно добавлен')
            return lst
        elif pol == 0:
            print()
            return lst
    except:
        print('Нужно вводить цифры.')


#Метод создания списаа номеров телефонов ичных
def add_hom_num():
    lst = []
    try:
        print('\nДобавлять контакту номер? 1 - да, 0 - нет')
        pol = int(input('Введите число '))
        if pol == 1:
            lst.append(enter_num_pfone())
            print('\nНомер был успешно добавлен')
            return lst
        elif pol == 0:
            print()
            return lst
    except:
        print('Нужно вводить цифры.')


#Метод создания списаа email
def add_email():
    lst = []
    try:
        print('\nДобавлять контакту Email? 1 - да, 0 - нет')
        pol = int(input('Введите номер '))
        if pol == 1:
            lst.append(enter_email())
            print('\Email был успешно добавлен')
            return lst
        elif pol == 0:
            print()
            return lst
    except:
        print('Ошибка')

#Метод добавления нового контакта в справочник.
def add_contact_in_spravochnik():
    try:
        lst_work_numbers = []
        lst_home_numbers = []
        lst_email = []
        index_name = creat_caes_contact()
        print('\nТеперь добавим рабочий номер телефона')
        lst_work_numbers = add_phon_num()
        if len(lst_work_numbers) == 1 or len(lst_work_numbers) == 0:
            True
        else: False
        print('\nТеперь добавим личный номер телефона')
        lst_home_numbers = add_hom_num()
        if len(lst_home_numbers) == 1 or len(lst_home_numbers) == 0:
            True
        else: False
        print('\nТеперь добавим почту')
        lst_email = add_email()
        if len(lst_email) == 1 or len(lst_email) == 0:
            True
        else: False
        spravochnik_about_client = {'рабочий:':lst_work_numbers, 'личный:':lst_home_numbers, 'почта:':lst_email}
        sprav[index_name] = spravochnik_about_client
        print('\n',index_name)
        for (k,v) in spravochnik_about_client.items():
            print(k,v)
    except:
        print('Что-то пошло не так. Введите 5, что бы попробовать ещё.\n\
Или 7, что бы вызвать help')
        
# Метод удаления контакта

def delete_contact():
    find_of_name()
    if len(lst_for_delete) == 1:
        print('\nВы действительно хотите удалить контакт?\
\nДА - 1\
\nНЕТ - 0')
        pod = enter_num()
        if pod == 1:
            del sprav[lst_for_delete[0]]
            print('Контак удалён')
        elif pod == 0:
            print('Контак не удалён')
        else:
            print('Пробуйте ещё')
    elif len(lst_for_delete) > 1:
        print('С такими данными есть несколько контактов')
        print(*lst_for_delete, sep=', ')
        print('Попробуйте ещё, но уточните Данные(через пробел)')














# -------------------блок для внесения изменений-------------------



# Метод внесений изменений
def add_change():
    try:
        dopysk()
        concretika()
        if numb == 1:
            chench_name()
        elif numb == 2:
            chench_phon(text='рабочий:')
        elif numb == 3:
            chench_phon(text='личный:')
        elif numb == 4:
            chench_email(text='почта:')
    except:
        print('Пробуйте ещё')
    
    



#метод допуска к изменению
def dopysk():
    print('Укажите данные контакта, который хотите изменить')
    find_of_name()
    if len(lst_for_delete) == 1:
        True
    elif len(lst_for_delete) > 1:
        print('С такими данными есть несколько контактов')
        print(*lst_for_delete, sep=', ')
        print('Попробуйте ещё, но уточните Данные(через пробел)')
# Метод выбора что именно нужно изменить
def concretika():
    print('Выберете, что именно хотите изменить:\
\n1 - ФИО\
\n2 - Номер рабочего телефона\
\n3 - Номер личного телефона\
\n4 - Email\
    ')
    global numb
    numb = enter_num()
    if numb == 1 or numb == 2 or numb == 3 or numb == 4:
        print('Идём дальше')

# Метод изменения ФИО
def chench_name():
    new_name = creat_caes_contact()
    sprav[new_name] = sprav[lst_for_delete[0]]
    del sprav[lst_for_delete[0]]

#Метод редактирования рабочего телефона
def chench_phon(text = ''):
    inform_of_case = sprav[lst_for_delete[0]]
    lst_num = inform_of_case[text]
    print('\nВот текущие номера телефонов:')
    print(inform_of_case[text])
    print('\nВыберете действие\
\n1 - добавление\
\n2 - изменение\
\n3 - удаление\
    ')
    pod = enter_num()
    if pod == 1:
        lst_num.append(enter_num_pfone())
        inform_of_case[text] = lst_num
        print('Номер добавлен')


    elif pod == 2:
        if len(lst_num) == 0:
            print('Номеров нет, поэтому просто дбавим.')
            lst_num.append(enter_num_pfone())
            inform_of_case[text] = lst_num
            print('Номер добавлен')
        elif len(lst_num) == 1:
            lst_num[0] = enter_num_pfone()
            inform_of_case[text] = lst_num
            print('Номер изменён')
        elif len(lst_num) > 1:
            for i in range(len(lst_num)):
                print(f'{lst_num[i]} Этот номер нужно изменять?\
\n1 - да\
\n0 - нет')
                j = enter_num_pfone()
                if j == 1:
                    lst_num[i] = enter_num_pfone()
                    print('Номер изменён')
                elif j == 0:
                    print('Идём дальше')
            inform_of_case[text] = lst_num
            print('Изменения внесены')


    elif pod == 3:
        if len(lst_num) == 0:
            print('Номеров нет, поэтому удалить ничего не получится.')
        elif len(lst_num) > 1:
            print('Все номера нужно удалять?\
\n1 - да\
\n0 - нет')
            j = enter_num_pfone()
            if j == 1:
                lst_num.clear()
                inform_of_case[text] = lst_num
                print('Номера все удалены')
            elif j == 0:
                for i in range(len(lst_num)):
                    print(f'{lst_num[i]} Этот номер нужно удалять?\
\n1 - да\
\n0 - нет')
                    j = enter_num_pfone()
                    if j == 1:
                        lst_num.remove(lst_num[i])
                        print('Номер удалён')
                    elif j == 0:
                        print('Идём дальше')
                inform_of_case[text] = lst_num
                print('Изменения внесены')
        elif len(lst_num) == 1:
            print('Удалять номер?\
\n1 - да\
\n0 - нет')
            j = enter_num_pfone()
            if j == 1:
                lst_num.clear()
                inform_of_case[text] = lst_num
                print('Номер удалён')
            elif j == 0:
                print('Номер удалён не будет')





#Метод редактирования email
def chench_email(text = ''):
    inform_of_case = sprav[lst_for_delete[0]]
    lst_em = inform_of_case[text]
    print('\nВот текущие Email:')
    print(inform_of_case[text])
    print('\nВыберете действие\
\n1 - добавление\
\n2 - изменение\
\n3 - удаление\
    ')
    pod = enter_num()
    if pod == 1:
        lst_em.append(enter_email())
        inform_of_case[text] = lst_em
        print('Email добавлен')


    elif pod == 2:
        if len(lst_em) == 0:
            print('Email нет, поэтому просто дбавим.')
            lst_em.append(enter_email())
            inform_of_case[text] = lst_em
            print('Email добавлен')
        elif len(lst_em) == 1:
            lst_em[0] = enter_email()
            inform_of_case[text] = lst_em
            print('Email изменён')
        elif len(lst_em) > 1:
            for i in range(len(lst_em)):
                print(f'{lst_em[i]} Этот Email нужно изменять?\
\n1 - да\
\n0 - нет')
                j = enter_num()
                if j == 1:
                    lst_em[i] = enter_email()
                    print('Email изменён')
                elif j == 0:
                    print('Идём дальше')
            inform_of_case[text] = lst_em
            print('Изменения внесены')


    elif pod == 3:
        if len(lst_em) == 0:
            print('Email нет, поэтому удалить ничего не получится.')
        elif len(lst_em) > 1:
            print('Все Email нужно удалять?\
\n1 - да\
\n0 - нет')
            j = enter_num()
            if j == 1:
                lst_em.clear()
                inform_of_case[text] = lst_em
                print('Email все удалены')
            elif j == 0:
                for i in range(len(lst_em)):
                    print(f'{lst_em[i]} Этот Email нужно удалять?\
\n1 - да\
\n0 - нет')
                    j = enter_num()
                    if j == 1:
                        lst_em.remove(lst_em[i])
                        print('Email удалён')
                    elif j == 0:
                        print('Идём дальше')
                inform_of_case[text] = lst_em
                print('Изменения внесены')
        elif len(lst_em) == 1:
            print('Удалять Email?\
\n1 - да\
\n0 - нет')
            j = enter_num()
            if j == 1:
                lst_em.clear()
                inform_of_case[text] = lst_em
                print('Email удалён')
            elif j == 0:
                print('Email удалён не будет')

