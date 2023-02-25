from random import *
from contact import *
import json
global sprav
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
    print('Здравстыуйте, я телефонный справочник. Меня зовут Pavl_Bot и я помогу вам найти,\n\
внести нового контакта, какой-нибудт удалить или изменить уже существующий')
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
    '
    print(tex)

#Метод вывода всего справочника
def show_sprav():
    for(k,v) in sprav.items():
        print(k)
        for (p,g) in v.items():
            print(p, end='')
            print(*g, sep=',')
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
        print('\nДобавлять пользователю номер? 1 - да, 0 - нет')
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
        print('\nДобавлять пользователю номер? 1 - да, 0 - нет')
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
        print('\nДобавлять пользователю Email? 1 - да, 0 - нет')
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

