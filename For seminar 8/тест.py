from random import *
from contact import *
import json

spravochnik = {"Павловский Николай Сергеевич": {"рабочий:": ["15625", "9876"], "домашний:": ["3542"], "почта:": ["nik.pav@mail.ru"]},
          "Павловский Максим Николаевич": {"рабочий:": ["748382"], "домашний:": ["7658"], "почта:": []}} 


def save():
    with open("D:/Учёба в GB/Python/Homeworks/For seminar 8/spravochnik.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(spravochnik,ensure_ascii=False))
    print("Ваш справочник был успешно сохранён в файле spravochnik.json")

def load():
    global spravochnik
    with open("D:/Учёба в GB/Python/Homeworks/For seminar 8/spravochnik.json","r",encoding="utf-8") as fh:
        spravochnik=json.load(fh)
    print("Справочник был успешна загружен!")

def start():
    print('Здравстыуйте, меня зовут Pavl_Bot и я помогу вам найти,\n\
внести нового контакта, какой-нибудт удалить или изменить уже существующий')
    print()
    load()

def help():
    tex = '\n\
1 - просмотреть все контакты справочника\n\
2 - найти контакт по его фамилии, имени, отчетству или по всему и сразу\n\
3 - найти контакт по его одному из номеров телефона\n\
4 - найти контакт по его Email\n\
5 - добавить контак\n\
6 - удалить контакт\n\
7 - help\n\
    '
    print(tex)

#Метод вывода всего справочника
def show_sprav():
    for(k,v) in spravochnik.items():
        print(k)
        for (p,g) in v.items():
            print(p, end=' ')
            print(*g, sep=',')
        print()

def find_of_name():
    count = 0
    name = enter_fyl_name().lower().split()
    lst_persone = list(map(lambda x: x, spravochnik))
    print(lst_persone)
    print(name)

    for i in lst_persone:
        h = i
        i = i.lower().split()
        if len(name) <= len(i):
            for j in name:
                if j in i:
                    count += 1
            if count == len(name):
                print(h)
                for (p,g) in spravochnik[h].items():
                    print(p, end=' ')
                    print(*g, sep=',')
                print()
            count = 0







find_of_name()













# name ="Павловский Николай Сергеевич"
# pol = "Николай Павлвский"
# count = 0
# name = name.split()
# pol = pol.split()
# print(name, pol)
# print(name >= pol)
# for i in pol:
#     if i in name:
#         count += 1 
# if count == len(pol):
#     print("ok")
# else:
#     print("no")