#метод ввода числа
def enter_num():
    try:
        print()
        return int(input('Введите номер задачи: '))
    except:
        return print('\nВведены некоретные данные')
#метод ввода номера телефона
def enter_num_pfone():
        return int(input('Введите номер телефона: '))
#Метод вывода текстовой информации(непредусматривающей наличие цифр)
def enter_text():
    name = input('')
    if any(ch.isdigit() for ch in name):
        print('Введены не коректные данные')
    else:
        return name
    
#Метод ввода email
def enter_email():
    em = input('\nВведите Email: ')
    return em
        

