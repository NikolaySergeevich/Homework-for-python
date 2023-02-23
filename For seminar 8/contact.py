#метод ввода числа
def enter_num():
    try:
        return int(input('Введите номер задачи: '))
    except:
        return print('\nВведены некоретные данные, попробуйте ещё')
#метод ввода номера телефона
def enter_num_pfone():
    try:
        return int(input('Введите номер телефона: '))
    except:
        return print('\nВведены некоретные данные, попробуйте ещё')
#Метод вывода фио
def enter_fyl_name():
    name = input('\nВведите ФИО: ')
    if any(ch.isdigit() for ch in name):
        print('Введены не коректные данные')
    else:
        return name
        

