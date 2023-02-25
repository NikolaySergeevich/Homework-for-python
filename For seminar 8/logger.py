from fyncshion import *
from contact import *


def beginning():
    
    try:
        start()
        print('Теперь можем начать рабоать.')
        print('Ознакомтесь с возможностями программы и введите подходящий номер.')
        help()
    except:
        print('У вас нет ещё данных в справочнике. Давайте его заполним!')
        add_contact_in_spravochnik()
        print('Теперь в вашем справочнике есть один контакт.\n\
Ознакомтесь с возможностями программы и введите подходящий номер.')
        help()

def operate():
    while True:
        num = enter_num()
        if num == 1:
            show_sprav()
        elif num == 2:
            find_of_name()
        elif num == 3:
            find_of_number()
        elif num == 4:
            find_of_Email()
        elif num == 5:
            add_contact_in_spravochnik()
        elif num == 6:
            delete_contact()
        elif num == 7:
            help()
        elif num == 8:
            load()
        elif num == 9:
            save()
        elif num == 10:
            add_change()    
        elif num == 0:
            ending()
            break
        else:
            print('Такого функцианала нет. Обратитесь к /help.\n\
Для этого введите число 7')
