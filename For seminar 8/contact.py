#метод ввода числа
def enter_num():
    try:
        return int(input('Введите число: '))
    except:
        print('Введены некоретные данные, попробуйте ещё')

#Метод вывода фио
def enter_fyl_name():
    name = input('\nВведите ФИО: ')
    if any(ch.isdigit() for ch in name):
        print('Введены не коректные данные')
    else:
        return name
        

